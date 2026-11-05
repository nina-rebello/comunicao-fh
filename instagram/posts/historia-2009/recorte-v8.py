"""Foto da v8: a copa (fotos/capa-b.jpg, foto da Nina de 04/11), recortada no formato da moldura de foto-v8.html
(936 x 828, em 2x) e levemente esfriada. Saída: fotos/v8-copa.jpg.
Uso: python3 instagram/posts/historia-2009/recorte-v8.py"""
from pathlib import Path
import numpy as np
from PIL import Image
AQUI = Path(__file__).parent / 'fotos'
im = Image.open(AQUI / 'capa-b.jpg').convert('RGB')
W, H = 936 * 2, 828 * 2
esc = W / im.width
im = im.resize((W, round(im.height * esc)), Image.LANCZOS)
y0 = round((im.height - H) * 0.55)
im = im.crop((0, y0, W, y0 + H))
a = np.asarray(im).astype(np.float32) / 255
lum = (a @ np.array([0.299, 0.587, 0.114], dtype=np.float32))[..., None]
a = lum + (a - lum) * 0.85
a *= np.array([0.96, 1.0, 1.04], dtype=np.float32)
a = np.clip(a * 1.06, 0, 1)
Image.fromarray((a * 255).astype(np.uint8)).save(AQUI / 'v8-copa.jpg', quality=90)
print('ok v8-copa.jpg')
