"""Monta a entrega final: o MP4 para postar (volume em -14 LUFS) e as peças soltas para o CapCut.

entrega.py <video> <versao_da_previa>

Parte da prévia aprovada (Vídeos Prontos/<video>/vNN/). Escreve Vídeos Prontos/<video>/final_vNN/:
<video>_final_vNN.mp4 (H.264, AAC 48 kHz, voz + efeitos normalizados em dois passes, pico real ≤ -1 dBTP),
apresentadora_vNN.mp4, sfx_vNN.wav, as camadas no formato de validacao.md (se já validado) e LEIA.txt.
Confere resolução, fps, número de quadros e loudness.
"""
import json, os, re, subprocess, sys
from comum import carregar, pasta_prontos, pasta_trabalho, salvar

ALVO_I, ALVO_TP = -14.0, -1.0


def ff(*a, **k):
    return subprocess.run(["ffmpeg", "-hide_banner", "-y", *a], check=True, capture_output=True, text=True, **k)


def quadros(arq):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v", "-count_packets", "-show_entries",
                          "stream=width,height,r_frame_rate,nb_read_packets", "-of", "csv=p=0", arq],
                         capture_output=True, text=True).stdout.strip()
    return out


def main(video, versao):
    e = carregar(video)
    vv = f"v{int(versao):02}"
    origem = os.path.join(pasta_prontos(), video, vv)
    destino = os.path.join(pasta_prontos(), video, f"final_{vv}")
    if os.path.exists(destino):
        sys.exit(f"{destino} já existe: use uma versão nova")
    os.makedirs(destino)
    previa = os.path.join(origem, f"{video}_previa_{vv}.mp4")
    final = os.path.join(destino, f"{video}_final_{vv}.mp4")
    # passo 1: medir
    err = ff("-i", previa, "-af", f"loudnorm=I={ALVO_I}:TP={ALVO_TP}:LRA=11:print_format=json", "-f", "null", "-").stderr
    m = json.loads(err[err.rindex("{"):err.rindex("}") + 1])
    # passo 2: aplicar com o que foi medido
    af = (f"loudnorm=I={ALVO_I}:TP={ALVO_TP}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']},aresample=48000")
    ff("-i", previa, "-c:v", "copy", "-af", af, "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-movflags", "+faststart", final)
    err = ff("-i", final, "-af", "ebur128=peak=true", "-f", "null", "-").stderr
    i_final = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", err)[-1])
    tp_final = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", err)[-1])
    pecas = []
    for nome in (f"apresentadora_{vv}.mp4", f"sfx_{vv}.wav", f"animacoes_{vv}.mov", f"legendas_{vv}.mov",
                 f"animacoes_{vv}.mp4", f"legendas_{vv}.mp4"):
        src = os.path.join(origem, nome)
        if os.path.exists(src):
            ff("-i", src, "-c", "copy", os.path.join(destino, nome))
            pecas.append(nome)
    camadas = [p for p in pecas if p.startswith(("animacoes", "legendas"))]
    leia = f"""{video} · entrega final {vv} · gerada pelo fluxo de edição (edit-entrega)

PARA POSTAR
  {video}_final_{vv}.mp4  1080x1920, 30 fps, voz + efeitos em {i_final:.1f} LUFS (pico {tp_final:.1f} dBTP). Sem música:
  a música de fundo fica com você, no CapCut ou no Instagram.

PEÇAS PARA AJUSTAR NO CAPCUT (todas com a duração do vídeo e começando em 0:00: arraste cada uma para uma
faixa no começo da linha do tempo)
  apresentadora_{vv}.mp4  a Marília com a câmera aplicada, com a voz original (mais baixa: use "Normalizar
                          volume" do CapCut ou suba uns 15 dB)
  sfx_{vv}.wav            os efeitos sonoros, já no tempo certo
  {"  ".join(camadas) if camadas else "animações e legendas: chegam depois do teste do CapCut (fundo verde ou transparente),"}
  {"" if camadas else "                          que está em teste_capcut/. O vídeo final acima já tem tudo."}
Ordem das faixas: apresentadora embaixo, animações, recorte da Marília (só no trecho do cartão; vem junto
com as camadas), legendas em cima.
"""
    open(os.path.join(destino, "LEIA.txt"), "w").write(leia)
    conf = {p: quadros(os.path.join(destino, p)) for p in [os.path.basename(final)] + [p for p in pecas if p.endswith((".mp4", ".mov"))]}
    e["entrega"] = {"versao": vv, "pasta": destino, "loudness_lufs": i_final, "pico_dbtp": tp_final, "pecas": pecas,
                    "conferencia": conf}
    salvar(video, e)
    print(f"entrega em {destino}\n  loudness {i_final:.1f} LUFS, pico {tp_final:.1f} dBTP")
    for k, v in conf.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
