"""Gera o fundo do post de depoimentos (19/11): Tiffany com grade fina branca, brilho creme no canto de baixo e
granulado leve, como imagem (o Canva não aceita a grade e o brilho em CSS).
Uso: python3 instagram/posts/depoimentos/gerar.py
"""
from pathlib import Path

import numpy as np
from PIL import Image

FOTOS = Path(__file__).resolve().parent / 'fotos'
W, H = 2160, 2700  # 2x de 1080x1350

rng = np.random.default_rng(5)
img = np.ones((H, W, 3)) * np.array((159, 197, 189), float)
# brilho creme embaixo à direita e um pouco de luz no alto à esquerda
yy, xx = np.mgrid[0:H, 0:W]
for cx, cy, r, cor, forca in [(2100, 2750, 1500, (240, 240, 233), .85), (0, 0, 1300, (191, 224, 217), .5)]:
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    a = np.clip(1 - d, 0, 1) ** 1.6 * forca
    img = img * (1 - a[..., None]) + np.array(cor, float) * a[..., None]
# grade: linhas brancas finas a cada 72 px (144 em 2x)
grade = np.zeros((H, W))
passo = 144
grade[:, (np.arange(W) % passo) < 2] = 1
grade[(np.arange(H) % passo) < 2, :] = 1
img = img * (1 - grade[..., None] * .16) + 255 * grade[..., None] * .16
img += rng.normal(0, 3.5, (H, W, 1))
Image.fromarray(np.clip(img, 0, 255).astype('uint8')).save(FOTOS / 'fundo-grade.jpg', quality=90)
print('ok fundo-grade.jpg')
