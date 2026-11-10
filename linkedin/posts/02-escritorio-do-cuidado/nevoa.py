"""Foto da versão LinkedIn (quadrada, 1080 x 1080) do post do Escritório do Cuidado (Instagram de 06/11).
Mesmo efeito da arte aprovada (instagram/posts/historia-2009/nevoa-v13.py baixo): desfoque e névoa branca no
alto, granulado fino; só que recortado em quadrado e com a névoa medida para o texto do quadrado.
Entrada: instagram/posts/historia-2009/fotos/capa-fria.jpg. Saída: fundo.jpg.
Uso: python3 linkedin/posts/02-escritorio-do-cuidado/nevoa.py"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
AQUI = Path(__file__).parent
foto = Image.open(AQUI.parent.parent.parent / 'instagram/posts/historia-2009/fotos/capa-fria.jpg').convert('RGB')
foto = foto.crop((0, 200, 1080, 1280))
W, H = foto.size
y = np.linspace(0, 1, H, dtype=np.float32)[:, None]
def suave(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)
raios = [0, 4, 9, 16, 26]
camadas = [np.asarray(foto if r == 0 else foto.filter(ImageFilter.GaussianBlur(r)), np.float32) for r in raios]
nivel = suave((0.66 - y) / 0.56) * (len(raios) - 1)
a = np.zeros_like(camadas[0])
for i in range(len(raios)):
    a += camadas[i] * np.clip(1 - np.abs(nivel - i), 0, 1)[..., None]
nevoa = np.array([0xF1, 0xF5, 0xF3], np.float32)
forca = (0.88 * suave((0.60 - y) / 0.54))[..., None]
a = a * (1 - forca) + nevoa * forca
a += np.random.default_rng(13).normal(0, 4.5, (H, W, 1)).astype(np.float32)
Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(AQUI / 'fundo.jpg', quality=92)
print('ok fundo.jpg')
