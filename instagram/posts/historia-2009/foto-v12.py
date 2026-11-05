"""Foto da v12 (05/11). A Nina mandou uma arte pronta ("faça exatamente como esse, só use as nossas tipografias"),
com a foto do espaço em tons frios e o tapete e as poltronas saindo da moldura. Aqui recortamos a parte da foto
dessa arte (fotos/referencia-nina-v12.jpg), sem o título nem o texto, e trocamos o fundo por um tom liso
(#EAE5E1) para casar com o fundo da página em foto-v12.html. O que fica fora da moldura (tapete, pés das poltronas,
sombra) é separado do fundo pela diferença de cor. Saída: fotos/v12-foto.jpg (1080 x 691, em 2x).
Uso: python3 instagram/posts/historia-2009/foto-v12.py"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
AQUI = Path(__file__).parent / 'fotos'
ref = Image.open(AQUI / 'referencia-nina-v12.jpg').convert('RGB')
Y0, Y1 = 522, 1240                       # do topo da moldura (sem as pontas das letras da arte) até o fim da sombra do tapete
MOLD = (36, 522, 1086, 1106)             # a moldura da foto, em px da referência
corte = np.asarray(ref.crop((0, Y0, ref.width, Y1))).astype(np.float32)
fundo = np.array([0xEA, 0xE5, 0xE1], np.float32)
dif = np.abs(corte - fundo).sum(2)
alfa = np.clip((dif - 18) / 30, 0, 1)
x0, y0, x1, y1 = MOLD
alfa[y0 - Y0:y1 - Y0, x0:x1] = 1
alfa = np.asarray(Image.fromarray((alfa * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8)), np.float32) / 255
saida = corte * alfa[..., None] + fundo * (1 - alfa[..., None])
im = Image.fromarray(np.clip(saida, 0, 255).astype(np.uint8))
im = im.resize((1080 * 2, round(im.height * 1080 / ref.width) * 2), Image.LANCZOS)
im.save(AQUI / 'v12-foto.jpg', quality=92)
print('ok v12-foto.jpg', im.size)
