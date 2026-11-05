"""Fotos da v9 (v8 com o texto de volta): recorta a copa (fotos/capa-b.jpg) e as poltronas azuis
(fotos/espaco-nina-original.jpg) no formato da moldura de foto-v9.html (936 x 710, em 2x) e esfria de leve.
Saída: fotos/v9-copa.jpg e fotos/v9-poltronas.jpg.
Uso: python3 instagram/posts/historia-2009/recorte-v9.py"""
from pathlib import Path
import numpy as np
from PIL import Image
AQUI = Path(__file__).parent / 'fotos'
W, H = 936 * 2, 710 * 2

def recorta(arq, fx, fy, sat, frio):
    im = Image.open(AQUI / arq).convert('RGB')
    esc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
    x = min(max(round(im.width * fx - W / 2), 0), im.width - W)
    y = min(max(round(im.height * fy - H / 2), 0), im.height - H)
    a = np.asarray(im.crop((x, y, x + W, y + H))).astype(np.float32) / 255
    lum = (a @ np.array([0.299, 0.587, 0.114], dtype=np.float32))[..., None]
    a = lum + (a - lum) * sat
    a *= np.array([1 - frio, 1.0, 1 + frio], dtype=np.float32)
    return Image.fromarray((np.clip(a * 1.05, 0, 1) * 255).astype(np.uint8))

recorta('capa-b.jpg', 0.5, 0.6, 0.85, 0.04).save(AQUI / 'v9-copa.jpg', quality=90)
recorta('espaco-nina-original.jpg', 1.0, 0.55, 0.78, 0.06).save(AQUI / 'v9-poltronas.jpg', quality=90)
print('ok v9-copa.jpg v9-poltronas.jpg')
