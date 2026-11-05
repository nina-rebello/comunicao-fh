"""Foto da moldura (v6, referência da Nina de 05/11: foto emoldurada sobre fundo de cor). Recorta a foto do espaço
(fotos/espaco-nina-original.jpg) no formato da moldura de foto-v6.html (888 x 640, em 2x quando possível) e esfria a
luz como em esfriar.py, sem véu. Saída: fotos/moldura.jpg.
Uso: python3 instagram/posts/historia-2009/moldura.py"""
from pathlib import Path
import numpy as np
from PIL import Image
AQUI = Path(__file__).parent / 'fotos'
im = Image.open(AQUI / 'espaco-nina-original.jpg').convert('RGB')
W, H = 888, 640
y0 = 60                                # tira a faixa do forro
h = im.height - y0
w = round(h * W / H)
x0 = im.width - w                      # encostado à direita: do vidro com folhagem até a costela-de-adão
im = im.crop((x0, y0, x0 + w, y0 + h)).resize((W * 2, H * 2), Image.LANCZOS)
a = np.asarray(im).astype(np.float32) / 255
lum = (a @ np.array([0.299, 0.587, 0.114], dtype=np.float32))[..., None]
a = lum + (a - lum) * 0.74
a *= np.array([0.94, 1.0, 1.06], dtype=np.float32)
tom = np.array([0.18, 0.42, 0.39], dtype=np.float32)
peso = (1 - lum) * 0.12
a = np.clip((a * (1 - peso) + tom * peso) * 1.04, 0, 1)
Image.fromarray((a * 255).astype(np.uint8)).save(AQUI / 'moldura.jpg', quality=90)
print('ok moldura.jpg', w, h)
