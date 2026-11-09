"""Aplica a câmera (aproximações e punch) no vídeo da apresentadora, sem tremer.

camera.py <video> <versao>

Lê o bloco `camera.movimentos` do estado: [{"id", "inicio", "fim", "de", "para", "curva"}] (escala, 1.0 = quadro
inteiro) e `camera.ancora` [x, y] (o ponto que fica parado na tela, em 1080x1920; o rosto). Entre os
movimentos a escala fica parada no último valor. Nunca mostra borda: escala ≥ 1 e a âncora dentro do quadro.

Base: o bruto aparado e escalado para 1080x1920 (lanczos), igual ao usado nos recortes; com escala 1.0 o
quadro sai idêntico a ele, então o recorte continua alinhado. O zoom usa o filtro `perspective` com
interpolação cúbica (subpixel), porque `crop` arredonda para pixels inteiros e o zoom lento treme.
Escreve _CLAUDE/<video>/renders/apresentadora_vNN.mp4.
"""
import os, subprocess, sys
from comum import carregar, pasta_trabalho, salvar

W, H = 1080, 1920
CURVAS = {  # p de 0 a 1 → progresso
    "linear": "{p}",
    "power2.out": "(1-pow(1-{p},2))",
    "power2.inOut": "if(lt({p},0.5),2*pow({p},2),1-pow(-2*{p}+2,2)/2)",
    "sine.inOut": "(-(cos(PI*{p})-1)/2)",
    "expo.out": "(1-pow(2,-10*{p}))",
}


def expr_escala(movs, fps):
    """Escala como soma de trechos: cada movimento soma o seu delta, com o progresso preso entre 0 e 1.
    (if aninhado estoura o analisador de expressões do FFmpeg.)"""
    t = f"(in/{fps})"  # no perspective o número do quadro é `in`
    z = str(movs[0]["de"])
    for m in movs:
        p = f"clip(({t}-{m['inicio']})/{m['fim'] - m['inicio']:.4f},0,1)"
        z += f"+({m['para'] - m['de']:.4f})*{CURVAS[m['curva']].format(p=p)}"
    return z


def main(video, versao):
    e, pasta = carregar(video), pasta_trabalho(video)
    c, cam = e["cortes"], e["camera"]
    fps = c["fps"]
    movs = sorted(cam["movimentos"], key=lambda m: m["inicio"])
    for a, b in zip(movs, movs[1:]):
        if b["inicio"] < a["fim"] or abs(b["de"] - a["para"]) > 1e-6:
            sys.exit(f"{a['id']} → {b['id']}: movimentos sobrepostos ou que não partem de onde a câmera está")
    if min(min(m["de"], m["para"]) for m in movs) < 1.0:
        sys.exit("escala abaixo de 1.0 mostraria a borda")
    ax, ay = cam["ancora"]
    z = expr_escala(movs, fps)
    # cantos do recorte na imagem de origem (sense=source): ficam nos cantos da saída
    x0, y0 = f"{ax}*(1-1/({z}))", f"{ay}*(1-1/({z}))"
    x1, y1 = f"({x0})+{W}/({z})", f"({y0})+{H}/({z})"
    persp = (f"perspective=x0='{x0}':y0='{y0}':x1='{x1}':y1='{y0}':x2='{x0}':y2='{y1}':x3='{x1}':y3='{y1}'"
             ":interpolation=cubic:sense=source:eval=frame")
    out = os.path.join(pasta, "renders", f"apresentadora_v{int(versao):02}.mp4")
    if os.path.exists(out):
        sys.exit(f"{out} já existe: use uma versão nova")
    roteiro = os.path.join(pasta, "renders", f"camera_v{int(versao):02}.filtro")
    open(roteiro, "w").write(f"scale={W}:{H}:flags=lanczos,fps={fps},{persp},format=yuv420p")
    tmp = out.replace(".mp4", "_parcial.mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(c["inicio"]), "-i", e["midia"]["arquivo"], "-t", str(c["duracao"]),
                    "-/vf", roteiro, "-c:v", "libx264", "-crf", "16",
                    "-preset", "slow", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", tmp], check=True)
    os.replace(tmp, out)
    cam["render"] = out
    salvar(video, e)
    print("câmera aplicada:", out)
    for m in movs:
        print(f"  {m['id']} {m['inicio']:6.2f}–{m['fim']:6.2f}  {m['de']:.2f} → {m['para']:.2f}  {m['curva']}  {m.get('nota', '')}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
