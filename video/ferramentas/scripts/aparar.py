"""Apara o começo e o fim do vídeo com a folga do perfil (estilo-cortes.md). Não corta o meio.

aparar.py <video> [folga_inicio=0.15] [folga_fim=0.4]
"""
import json, os, sys
from comum import carregar, frame, pasta_trabalho, salvar


def main(video, fi=0.15, ff=0.4):
    e = carregar(video)
    ws = json.load(open(os.path.join(pasta_trabalho(video), "transcricao_palavras.json")))
    fps, dur = e["midia"]["fps"], e["midia"]["duracao"]
    ini_f = max(0, frame(ws[0]["inicio"] - fi, fps))
    fim_f = min(frame(dur, fps), frame(ws[-1]["fim"] + ff, fps))
    e["cortes"] = {"versao": 1, "inicio_frame": ini_f, "fim_frame": fim_f, "inicio": round(ini_f / fps, 3),
                   "fim": round(fim_f / fps, 3), "duracao": round((fim_f - ini_f) / fps, 3), "fps": fps}
    salvar(video, e)
    c = e["cortes"]
    print(f"bruto {dur:.2f} s → aparado {c['duracao']:.2f} s (de {c['inicio']:.2f} a {c['fim']:.2f} s; frames {ini_f}–{fim_f})")


if __name__ == "__main__":
    main(sys.argv[1], *map(float, sys.argv[2:]))
