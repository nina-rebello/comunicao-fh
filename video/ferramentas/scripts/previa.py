"""Monta a prévia e as peças para o CapCut a partir das camadas renderizadas.

previa.py <video> <versao> [--teste-capcut INICIO FIM]

Lê: o bruto (aparado pelo bloco `cortes`), _CLAUDE/<video>/renders/{animacoes,legendas}_vNN.mov (ProRes 4444
com transparência) e, se existir, renders/apresentadora_vNN.mp4 (com a câmera aplicada).
Escreve em Vídeos Prontos/<video>/vNN/: <video>_previa_vNN.mp4 e apresentadora_vNN.mp4; as camadas no formato
validado em validacao.md (verde: MP4 sobre #00FF00; transparencia: MOV ProRes 4444).
--teste-capcut gera só o teste curto dos dois formatos (camadas juntas), em Vídeos Prontos/<video>/teste_capcut/.
"""
import os, subprocess, sys
from comum import FERR, carregar, pasta_prontos, pasta_trabalho, salvar

W, H = 1080, 1920


def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def formato_validado():
    txt = open(os.path.join(FERR, "validacao.md")).read().lower()
    for linha in txt.splitlines():
        if linha.startswith("|") and "camadas" in linha and "aprovado" in linha:
            return "verde" if "verde" in linha else "transparencia"
    return None


def main(video, versao, teste=None):
    e, pasta = carregar(video), pasta_trabalho(video)
    c, fps = e["cortes"], e["cortes"]["fps"]
    vv = f"v{int(versao):02}"
    anim = os.path.join(pasta, "renders", f"animacoes_{vv}.mov")
    leg = os.path.join(pasta, "renders", f"legendas_{vv}.mov")
    apres = os.path.join(pasta, "renders", f"apresentadora_{vv}.mp4")
    if not os.path.exists(apres):  # sem câmera ainda: só apara e escala (um reescalonamento só)
        ff("-ss", str(c["inicio"]), "-i", e["midia"]["arquivo"], "-t", str(c["duracao"]),
           "-vf", f"scale={W}:{H}:flags=lanczos,fps={fps},format=yuv420p", "-c:v", "libx264", "-crf", "16",
           "-preset", "slow", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", apres)
    if teste:
        ini, fim = teste
        out = os.path.join(pasta_prontos(), video, "teste_capcut")
        os.makedirs(out, exist_ok=True)
        junta = "[0:v][1:v]overlay=0:0:format=auto"
        ff("-ss", str(ini), "-t", str(fim - ini), "-i", anim, "-ss", str(ini), "-t", str(fim - ini), "-i", leg,
           "-filter_complex", f"{junta},format=yuva444p10le", "-c:v", "prores_ks", "-profile:v", "4444",
           "-pix_fmt", "yuva444p10le", os.path.join(out, "teste_A_transparente.mov"))
        ff("-f", "lavfi", "-i", f"color=c=0x00FF00:s={W}x{H}:r={fps}:d={fim - ini}",
           "-ss", str(ini), "-t", str(fim - ini), "-i", anim, "-ss", str(ini), "-t", str(fim - ini), "-i", leg,
           "-filter_complex", "[0:v][1:v]overlay=0:0[a];[a][2:v]overlay=0:0,format=yuv420p", "-c:v", "libx264",
           "-crf", "14", os.path.join(out, "teste_B_fundo_verde.mp4"))
        ff("-ss", str(ini), "-t", str(fim - ini), "-i", apres, "-c", "copy", os.path.join(out, "teste_fundo_apresentadora.mp4"))
        print("teste em", out)
        return
    out = os.path.join(pasta_prontos(), video, vv)
    os.makedirs(out, exist_ok=True)
    previa = os.path.join(out, f"{video}_previa_{vv}.mp4")
    if os.path.exists(previa):
        sys.exit(f"{previa} já existe: use uma versão nova")
    ff("-i", apres, "-i", anim, "-i", leg, "-filter_complex",
       "[0:v][1:v]overlay=0:0[a];[a][2:v]overlay=0:0,format=yuv420p", "-c:v", "libx264", "-crf", "17",
       "-preset", "slow", "-c:a", "copy", "-movflags", "+faststart", previa)
    ff("-i", apres, "-c", "copy", os.path.join(out, f"apresentadora_{vv}.mp4"))
    fmt = formato_validado()
    for nome, src in (("animacoes", anim), ("legendas", leg)):
        if fmt == "transparencia":
            ff("-i", src, "-c", "copy", os.path.join(out, f"{nome}_{vv}.mov"))
        elif fmt == "verde":
            ff("-f", "lavfi", "-i", f"color=c=0x00FF00:s={W}x{H}:r={fps}:d={c['duracao']}", "-i", src,
               "-filter_complex", "[0:v][1:v]overlay=0:0:shortest=1,format=yuv420p", "-c:v", "libx264", "-crf", "14",
               os.path.join(out, f"{nome}_{vv}.mp4"))
    e.setdefault("entregas", []).append({"versao": vv, "pasta": out, "camadas": fmt or "aguardando teste do CapCut"})
    salvar(video, e)
    print("entrega em", out, "| camadas:", fmt or "aguardando o teste do CapCut")


if __name__ == "__main__":
    a = sys.argv[1:]
    teste = (float(a[3]), float(a[4])) if "--teste-capcut" in a else None
    main(a[0], a[1], teste)
