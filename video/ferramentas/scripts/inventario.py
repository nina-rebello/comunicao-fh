"""Cria o estado do vídeo (se não existir) e grava o inventário do bruto no bloco `midia`.

inventario.py <video>
"""
import os, sys
from fractions import Fraction
from comum import bruto, carregar, ffprobe, pasta_trabalho, salvar
from estado import ETAPAS


def main(video):
    os.makedirs(pasta_trabalho(video), exist_ok=True)
    if os.path.exists(os.path.join(pasta_trabalho(video), "projeto.json")):
        e = carregar(video)
    else:
        e = {"projeto": video, "perfil": "fairhealth", "etapas": {et: "pendente" for et in ETAPAS},
             "pendencias": [], "marcadores": [], "alertas": []}
        open(os.path.join(pasta_trabalho(video), "aprendizados.md"), "a").close()
    arq = bruto(video)
    info = ffprobe(arq)
    v = next(s for s in info["streams"] if s["codec_type"] == "video")
    au = [s for s in info["streams"] if s["codec_type"] == "audio"]
    r, avg = Fraction(v["r_frame_rate"]), Fraction(v["avg_frame_rate"])
    rot = next((sd.get("rotation") for sd in v.get("side_data_list", []) if "rotation" in sd), 0)
    m = {"arquivo": arq, "duracao": float(info["format"]["duration"]), "largura": v["width"], "altura": v["height"],
         "rotacao": rot, "fps": float(r), "fps_texto": v["r_frame_rate"], "fps_medio": round(float(avg), 3),
         "codec": v["codec_name"], "audio": {"codec": au[0]["codec_name"], "taxa": int(au[0]["sample_rate"]),
                                             "canais": au[0]["channels"]} if au else None}
    alertas = []
    if not au:
        alertas.append("bruto sem áudio")
    if abs(float(r) - float(avg)) > 0.01:
        alertas.append(f"fps variável ({float(r)} × média {float(avg):.3f})")
    w, h = (v["height"], v["width"]) if abs(rot) == 90 else (v["width"], v["height"])
    if w < 1080 or h < 1920:
        alertas.append(f"resolução {w}x{h}, abaixo de 1080x1920: zoom da câmera limitado (perfil)")
    e["midia"], e["alertas"] = m, alertas
    if e["etapas"]["preparar"] == "pendente":
        e["etapas"]["preparar"] = "em_andamento"
    salvar(video, e)
    print(f"{video}: {m['duracao']:.2f} s, {w}x{h}, {m['fps']} fps (médio {m['fps_medio']}), {m['codec']}, áudio {m['audio']}")
    for a in alertas:
        print("ALERTA:", a)


if __name__ == "__main__":
    main(sys.argv[1])
