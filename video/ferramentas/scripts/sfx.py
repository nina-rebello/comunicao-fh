"""Gera os efeitos sonoros (sintetizados no FFmpeg, sem licença de terceiros) e mixa a faixa de sons do vídeo.

sfx.py <video> <versao>

Lê o bloco `sfx.itens` do estado: [{"id", "tempo", "som", "alinhar": "inicio"|"pico", "db"}]. `db` é relativo ao
nível base (pico do efeito ~14 dB abaixo do pico da voz, perfil estilo-som.md). Os sons ficam em
video/ferramentas/sons/ (gerados na primeira vez; fora do git). Escreve _CLAUDE/<video>/renders/sfx_vNN.wav
(48 kHz estéreo, com a duração do vídeo, começando em 0:00).
"""
import json, os, re, subprocess, sys
from comum import FERR, carregar, pasta_trabalho, salvar

SONS = os.path.join(FERR, "sons")
# nome: (expressão aevalsrc ou None para ruído, duração, tempo até o pico)
RECEITAS = {
    "pop": ("0.8*sin(2*PI*(420+520*exp(-t*45))*t)*exp(-t*30)", 0.2, 0.0),
    "tique": ("0.6*sin(2*PI*2200*t)*exp(-t*160)", 0.05, 0.0),
    "sino": ("0.45*(sin(2*PI*880*t)+0.6*sin(2*PI*1320*t)+0.25*sin(2*PI*1760*t))*exp(-t*6)", 0.9, 0.0),
    "whoosh": (None, 0.55, 0.32),
}


def ff(*a):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *a], check=True)


def gerar_sons():
    os.makedirs(SONS, exist_ok=True)
    for nome, (ex, dur, _) in RECEITAS.items():
        arq = os.path.join(SONS, f"{nome}.wav")
        if os.path.exists(arq):
            continue
        if ex:
            ff("-f", "lavfi", "-i", f"aevalsrc='{ex}':s=48000:d={dur}", "-af", "afade=t=out:st=" + str(dur - 0.02) + ":d=0.02",
               "-ac", "2", arq)
        else:  # ruído rosa filtrado que cresce até o pico e some
            ff("-f", "lavfi", "-i", f"anoisesrc=color=pink:d={dur}:a=0.5:r=48000:seed=7", "-af",
               f"highpass=f=500,lowpass=f=5000,afade=t=in:d=0.32:curve=exp,afade=t=out:st=0.32:d=0.23:curve=qsin",
               "-ac", "2", arq)


def pico_db(arq, inicio=None, dur=None):
    a = ["-i", arq] if inicio is None else ["-ss", str(inicio), "-t", str(dur), "-i", arq]
    err = subprocess.run(["ffmpeg", "-hide_banner", *a, "-af", "astats=metadata=0", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    vals = [float(x) for x in re.findall(r"Peak level dB: (-?[\d.]+)", err)]
    return max(vals) if vals else -99


def main(video, versao):
    e, pasta = carregar(video), pasta_trabalho(video)
    gerar_sons()
    dur = e["cortes"]["duracao"]
    voz = pico_db(e["midia"]["arquivo"], e["cortes"]["inicio"], dur)
    base = voz - 14
    itens = sorted(e["sfx"]["itens"], key=lambda i: i["tempo"])
    entradas, filtros = [], []
    for k, it in enumerate(itens):
        arq = os.path.join(SONS, f"{it['som']}.wav")
        ini = it["tempo"] - (RECEITAS[it["som"]][2] if it.get("alinhar") == "pico" else 0)
        ganho = base + it.get("db", 0) - pico_db(arq)
        entradas += ["-i", arq]
        ms = max(0, int(round(ini * 1000)))
        filtros.append(f"[{k}:a]volume={ganho:.2f}dB,adelay={ms}|{ms}[s{k}]")
        it["inicio_real"], it["ganho_db"] = round(ini, 3), round(ganho, 2)
    mix = "".join(f"[s{k}]" for k in range(len(itens)))
    filtros.append(f"{mix}amix=inputs={len(itens)}:normalize=0,apad,atrim=0:{dur},aresample=48000[out]")
    out = os.path.join(pasta, "renders", f"sfx_v{int(versao):02}.wav")
    ff(*entradas, "-filter_complex", ";".join(filtros), "-map", "[out]", "-ac", "2", "-ar", "48000", out)
    e["sfx"]["render"], e["sfx"]["voz_pico_db"] = out, voz
    salvar(video, e)
    print(f"voz: pico {voz:.1f} dB; efeitos ~{base:.1f} dB → {out}")
    for it in itens:
        print(f"  {it['id']} {it['tempo']:6.2f}  {it['som']:7} {it.get('db', 0):+d} dB  {it.get('nota', '')}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
