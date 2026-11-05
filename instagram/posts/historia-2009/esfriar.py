"""Recorta a foto do espaço (fotos/espaco-nina-original.jpg, enviada pela Nina em 05/11) em 4:5 e esfria a luz
âmbar para perto dos tons da marca (Tiffany e verde). Saída: fotos/capa-fria.jpg (1080 x 1350).
Uso: python3 instagram/posts/historia-2009/esfriar.py"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
AQUI = Path(__file__).parent / 'fotos'
im = Image.open(AQUI / 'espaco-nina-original.jpg').convert('RGB')
x0, w = 700, 753                      # as duas poltronas, a mesinha e o abajur
im = im.crop((x0, 0, x0 + w, im.height)).resize((1080, 1350), Image.LANCZOS)
im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
a = np.asarray(im).astype(np.float32) / 255
lum = a @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
# 1) menos laranja: tira saturação dos tons quentes
cinza = lum[..., None]
a = cinza + (a - cinza) * 0.72
# 2) balanço de branco mais frio
a *= np.array([0.93, 1.0, 1.07], dtype=np.float32)
# 3) sombras e meios-tons puxados para o verde-água da marca (#2F6B64 / #96C3BA)
tom = np.array([0.18, 0.42, 0.39], dtype=np.float32)
peso = (1 - lum)[..., None] * 0.16
a = a * (1 - peso) + tom * peso
a = np.clip(a * 1.03, 0, 1)
Image.fromarray((a * 255).astype(np.uint8)).save(AQUI / 'capa-fria.jpg', quality=90)
print('ok capa-fria.jpg')
