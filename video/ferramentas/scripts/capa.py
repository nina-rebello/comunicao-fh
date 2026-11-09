"""Gera a capa (texto de título inicial) de um reel no modelo padrão: PNG 1080x1920 com topo transparente.

capa.py <video> "<título com a [palavra-chave] entre colchetes>" "<subtítulo com o trecho em **negrito**>" [@arroba]

Usa video/ferramentas/modelos/capa-reel.html. Escreve em Vídeos Prontos/<video>/: capa_titulo.png (para pôr por
cima do vídeo no CapCut) e capa_previa.png (sobre o primeiro quadro, para conferir).
"""
import glob, html, os, re, subprocess, sys
from comum import FERR, carregar, pasta_prontos, pasta_trabalho

BASE_PX = 368  # distância do fim do subtítulo até a base do quadro (modelo: subtítulo termina em y 1552)


def main(video, titulo, sub, arroba="@FAIRHEALTH.BR"):
    e, pasta = carregar(video), pasta_trabalho(video)
    t = html.escape(titulo)
    # a palavra-chave vira pílula e fica presa à pontuação que vem depois (o "?" não cai sozinho na linha)
    t = re.sub(r"\[(.+?)\]([?!.,:]*)", r'<span class="nw"><span class="k">\1</span>\2</span>', t).replace("\n", "<br>")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", html.escape(sub))
    doc = open(os.path.join(FERR, "modelos", "capa-reel.html")).read()
    doc = doc.replace("__TITULO__", t).replace("__SUB__", s).replace("__ARROBA__", html.escape(arroba)).replace("__BASE__", str(BASE_PX))
    proj = os.path.join(pasta, "motion", "capa")
    os.makedirs(proj, exist_ok=True)
    open(os.path.join(proj, "index.html"), "w").write(doc)
    snap = os.path.join(pasta, "snapshots", "capa")
    subprocess.run(["npx", "--yes", f"hyperframes@{e['ferramentas']['hyperframes']}", "snapshot", proj, "--at", "0.5",
                    "--no-end", "-o", snap], check=True, capture_output=True)
    png = sorted(glob.glob(os.path.join(snap, "frame-*.png")))[-1]
    out = os.path.join(pasta_prontos(), video)
    os.makedirs(out, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", png, "-c:v", "png", os.path.join(out, "capa_titulo.png")], check=True)
    base = e.get("camera", {}).get("render") or e["midia"]["arquivo"]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", base, "-i", png, "-filter_complex",
                    "[0:v]scale=1080:1920[b];[b][1:v]overlay", "-frames:v", "1", os.path.join(out, "capa_previa.png")], check=True)
    print("capa em", out)


if __name__ == "__main__":
    main(*sys.argv[1:])
