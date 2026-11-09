"""Transcreve o bruto com tempo por palavra e prepara a leitura por frase.

transcrever.py <video>

Gera em _CLAUDE/<video>/: audio.wav, transcricao_palavras.json, transcricao_frases.txt, e o bloco
`transcricao` no estado. Passos: mlx-whisper sem initial_prompt; bordas das palavras ajustadas às pausas
(silencedetect); trechos com som e sem palavra retranscritos sozinhos; termos de termos.md aplicados.
"""
import json, os, re, subprocess, sys, unicodedata
import mlx_whisper
from comum import FERR, carregar, pasta_trabalho, salvar, silencios

MODELO = "mlx-community/whisper-large-v3-turbo"
FIM_FRASE = (".", "?", "!")


def whisper(wav, deslocamento=0.0):
    r = mlx_whisper.transcribe(wav, path_or_hf_repo=MODELO, language="pt", word_timestamps=True,
                               condition_on_previous_text=False)
    return [{"palavra": w["word"].strip(), "inicio": round(w["start"] + deslocamento, 3),
             "fim": round(w["end"] + deslocamento, 3), "prob": round(w["probability"], 2)}
            for s in r["segments"] for w in s["words"]]


def ajustar_bordas(ws, sil):
    """Puxa as bordas das palavras para fora das pausas medidas."""
    ajustes = 0
    for i, w in enumerate(ws):
        for a, b in sil:
            if not (w["inicio"] < b and w["fim"] > a):
                continue
            antes, depois = a - w["inicio"], w["fim"] - b
            if w["inicio"] >= a:                      # começa dentro da pausa
                w["inicio"] = b
            elif w["fim"] <= b:                       # termina dentro da pausa
                w["fim"] = a
            else:                                     # atravessa a pausa inteira: de que lado ela fica?
                ant = ws[i - 1]["palavra"] if i else "."
                if ant.endswith(FIM_FRASE + (",",)):
                    w["inicio"] = b
                elif w["palavra"].endswith(FIM_FRASE + (",",)):
                    w["fim"] = a
                elif antes >= depois:
                    w["fim"] = a
                else:
                    w["inicio"] = b
            ajustes += 1
    for w in ws:
        w["inicio"], w["fim"] = round(w["inicio"], 3), round(max(w["fim"], w["inicio"] + 0.04), 3)
    return ajustes


def buracos(ws, sil, duracao, minimo=0.5):
    """Intervalos sem palavra que não são pausa: som que a transcrição pode ter engolido."""
    marcos = [(0.0, 0.0)] + [(w["inicio"], w["fim"]) for w in ws] + [(duracao, duracao)]
    res = []
    for (_, f1), (i2, _) in zip(marcos, marcos[1:]):
        if i2 - f1 < minimo:
            continue
        coberto = sum(max(0, min(b, i2) - max(a, f1)) for a, b in sil)
        if (i2 - f1) - coberto >= minimo:
            res.append([round(f1, 3), round(i2, 3)])
    return res


def termos():
    t, p = [], os.path.join(FERR, "termos.md")
    for linha in open(p):
        cols = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(cols) == 2 and cols[0] and not cols[0].startswith(("Sai", "---")):
            for variante in cols[0].split(","):
                t.append((variante.strip().lower().split(), cols[1]))
    return sorted(t, key=lambda x: -len(x[0]))


def aplicar_termos(ws):
    trocas, i = [], 0
    def limpo(x): return re.sub(r"[^\w]", "", x.lower())
    while i < len(ws):
        for var, certo in termos():
            n = len(var)
            if [limpo(w["palavra"]) for w in ws[i:i + n]] == [limpo(v) for v in var]:
                pont = re.sub(r"[\w]", "", ws[i + n - 1]["palavra"].split()[-1])[-1:] if ws[i + n - 1]["palavra"][-1:] in ".,?!" else ""
                antigo = " ".join(w["palavra"] for w in ws[i:i + n])
                ws[i:i + n] = [{"palavra": certo + pont, "inicio": ws[i]["inicio"], "fim": ws[i + n - 1]["fim"], "prob": 1.0}]
                trocas.append(f"{antigo} → {certo + pont} ({ws[i]['inicio']:.2f} s)")
                break
        i += 1
    return trocas


def frases(ws):
    res, atual = [], []
    for w in ws:
        atual.append(w)
        if w["palavra"].endswith(FIM_FRASE):
            res.append(atual); atual = []
    if atual:
        res.append(atual)
    return [{"inicio": f[0]["inicio"], "fim": f[-1]["fim"], "texto": " ".join(w["palavra"] for w in f)} for f in res]


def mmss(t): return f"{int(t // 60):02}:{t % 60:05.2f}"


def main(video):
    e, pasta = carregar(video), pasta_trabalho(video)
    wav = os.path.join(pasta, "audio.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", e["midia"]["arquivo"], "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
    sil = silencios(wav)
    ws = whisper(wav)
    ajustes = ajustar_bordas(ws, sil)
    marcadores = []
    for a, b in buracos(ws, sil, e["midia"]["duracao"]):
        trecho = os.path.join(pasta, f"trecho_{a:.2f}.wav")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(a), "-to", str(b), "-i", wav, trecho], check=True)
        novas = whisper(trecho, a)
        os.remove(trecho)
        if novas:
            ws = sorted(ws + novas, key=lambda w: w["inicio"])
            marcadores.append({"tipo": "retranscrito", "inicio": a, "fim": b, "texto": " ".join(w["palavra"] for w in novas)})
        else:
            marcadores.append({"tipo": "som_sem_palavra", "inicio": a, "fim": b, "texto": "som sem palavra transcrita"})
    trocas = aplicar_termos(ws)
    fr = frases(ws)
    json.dump(ws, open(os.path.join(pasta, "transcricao_palavras.json"), "w"), ensure_ascii=False, indent=0)
    with open(os.path.join(pasta, "transcricao_frases.txt"), "w") as f:
        for i, x in enumerate(fr):
            pausa = f"   [pausa {fr[i + 1]['inicio'] - x['fim']:.2f} s]" if i + 1 < len(fr) else ""
            f.write(f"{mmss(x['inicio'])}–{mmss(x['fim'])}  {x['texto']}{pausa}\n")
    e["transcricao"] = {"modelo": MODELO, "palavras": len(ws), "frases": len(fr), "pausas": sil,
                        "bordas_ajustadas": ajustes, "termos_trocados": trocas, "baixa_confianca":
                        [f"{w['palavra']} ({w['inicio']:.2f} s, {w['prob']})" for w in ws if w["prob"] < 0.5]}
    for m in marcadores:
        m["id"] = f"mk{len(e['marcadores']) + 1:02}"
        e["marcadores"].append(m)
    salvar(video, e)
    print(open(os.path.join(pasta, "transcricao_frases.txt")).read())
    print(f"{len(ws)} palavras, {ajustes} bordas ajustadas, termos: {trocas or 'nenhum'}")
    print("baixa confiança:", e["transcricao"]["baixa_confianca"] or "nenhuma")
    for m in marcadores:
        print(f"{m['id']} {m['tipo']} {m['inicio']:.2f}–{m['fim']:.2f}: {m['texto']}")


if __name__ == "__main__":
    main(sys.argv[1])
