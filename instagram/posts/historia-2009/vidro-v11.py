"""Vidro fosco da v11 (retorno da Nina sobre a v10a: "caixa de vidro mais bonita, tá muito tosca").
Tudo assado na foto, para o Canva receber uma imagem só: sombra suave por baixo do vidro, desfoque forte com a cor
um pouco mais viva, véu verde-escuro leve para o texto branco ler, brilho diagonal (mais claro no alto à esquerda),
granulado fino e borda de luz com degradê (forte no alto, quase some embaixo).
Entrada: fotos/capa-fria.jpg. Saída: fotos/v11-fundo.jpg. Uso: python3 instagram/posts/historia-2009/vidro-v11.py"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
AQUI = Path(__file__).parent / 'fotos'
S = 4                                                   # supersample das máscaras, para bordas lisas

CAIXAS = [                                              # (x0, y0, x1, y1, raio), em px do slide
    (-80, 744, 700, 1290, 44),                          # cartão do texto, sai pela esquerda
    (628, 88, 1160, 240, 38),                           # selo do alto, sai pela direita
]

def mascara(tam, caixa, encolhe=0):
    x0, y0, x1, y1, r = caixa
    m = Image.new('L', (tam[0] * S, tam[1] * S), 0)
    ImageDraw.Draw(m).rounded_rectangle(((x0 + encolhe) * S, (y0 + encolhe) * S, (x1 - encolhe) * S, (y1 - encolhe) * S),
                                        (r - encolhe) * S, fill=255)
    return m.resize(tam, Image.LANCZOS)

foto = Image.open(AQUI / 'capa-fria.jpg').convert('RGB')
W, H = foto.size
f = np.asarray(foto).astype(np.float32)

# 1) sombra suave por baixo de cada vidro
sombra = np.zeros((H, W), np.float32)
for c in CAIXAS:
    x0, y0, x1, y1, r = c
    m = mascara((W, H), (x0, y0 + 22, x1, y1 + 22, r))
    sombra = np.maximum(sombra, np.asarray(m.filter(ImageFilter.GaussianBlur(38)), np.float32) / 255)
f *= (1 - 0.30 * sombra)[..., None]

# 2) o vidro: desfoque, cor mais viva, véu verde-escuro, brilho diagonal e granulado
borr = Image.fromarray(np.clip(f, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(20))
borr = ImageEnhance.Color(borr).enhance(1.2)
v = np.asarray(borr).astype(np.float32) * np.array([0.90, 0.99, 1.06], np.float32)   # vidro um pouco mais frio
verde = np.array([14, 30, 32], np.float32)
v = v * 0.66 + verde * 0.34
rng = np.random.default_rng(11)
grao = rng.normal(0, 3.2, (H, W)).astype(np.float32)[..., None]

for c in CAIXAS:
    x0, y0, x1, y1, r = c
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    t = np.clip(((xx - max(x0, 0)) / (x1 - max(x0, 0)) * 0.45 + (yy - y0) / (y1 - y0) * 0.55), 0, 1)
    brilho = (0.13 * (1 - t) ** 1.4)[..., None]          # luz branca no alto à esquerda
    vidro = v * (1 - brilho) + 255 * brilho + grao
    m = np.asarray(mascara((W, H), c), np.float32)[..., None] / 255
    f = f * (1 - m) + vidro * m
    # 3) borda de luz: anel de 1,5 px, forte no alto e fraco embaixo
    anel = (np.asarray(mascara((W, H), c), np.float32) - np.asarray(mascara((W, H), c, encolhe=1.6), np.float32)) / 255
    forca = (0.80 * (1 - t) ** 0.8 + 0.14)[..., None] * anel[..., None]
    f = f * (1 - forca) + 255 * forca
    # brilho interno fino logo abaixo da borda de cima
    topo = np.asarray(mascara((W, H), c, encolhe=1.6), np.float32) - np.asarray(mascara((W, H), (x0, y0 + 5, x1, y1, r), encolhe=1.6), np.float32)
    topo = np.clip(topo / 255, 0, 1)[..., None] * 0.10
    f = f * (1 - topo) + 255 * topo

Image.fromarray(np.clip(f, 0, 255).astype(np.uint8)).save(AQUI / 'v11-fundo.jpg', quality=92)
print('ok v11-fundo.jpg')
