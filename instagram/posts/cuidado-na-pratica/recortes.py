"""Recorta as fotos de fotos/ no tamanho exato de cada moldura do slides.html.

O Canva importa <img> melhor que background-image e ignora object-fit, então
cada foto sai já no formato da moldura (em 2x, para ficar nítida).
Uso: python3 instagram/posts/cuidado-na-pratica/recortes.py
"""
from pathlib import Path

from PIL import Image

PASTA = Path(__file__).parent / 'fotos'
# saída: (original, largura, altura da moldura em px, foco x, foco y)
# O foco é o ponto da foto (0 a 1) que fica o mais perto possível do centro do recorte.
MOLDURAS = {
    'c-03': ('maos.jpg', 1080, 480, 0.50, 0.55),
    'c-04': ('industria2.jpg', 368, 520, 0.24, 0.40),
    'c-05': ('comida.jpg', 448, 360, 0.70, 0.45),
}

for nome, (orig, w, h, fx, fy) in MOLDURAS.items():
    im = Image.open(PASTA / orig).convert('RGB')
    escala = max(2 * w / im.width, 2 * h / im.height)
    im = im.resize((round(im.width * escala), round(im.height * escala)), Image.LANCZOS)
    x = min(max(round(im.width * fx - w), 0), im.width - 2 * w)
    y = min(max(round(im.height * fy - h), 0), im.height - 2 * h)
    im.crop((x, y, x + 2 * w, y + 2 * h)).save(PASTA / f'{nome}.jpg', quality=88)
    print(nome, orig, f'{2 * w}x{2 * h}')
