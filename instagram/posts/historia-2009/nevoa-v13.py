"""Foto da v13 (referência da Nina de 05/11: a imagem vai ficando desfocada e clara, como névoa, com granulado).
Aqui o efeito fica no alto, de leve, para o texto entrar por cima: o desfoque cresce de baixo para cima a partir
de ~62% da altura, e a névoa (off-white da marca) clareia o alto. Granulado fino na foto inteira.
Entrada: fotos/capa-fria.jpg (poltronas azuis, já esfriada). Saída: fotos/v13-nevoa.jpg.
Com "tiffany" (v14, pedido da Nina: "use mais o nosso Tiffany"): a névoa passa a ser Tiffany #9FC5BD, mais forte
no alto. Saída: fotos/v14-nevoa-tiffany.jpg.
Uso: python3 instagram/posts/historia-2009/nevoa-v13.py [tiffany]"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
AQUI = Path(__file__).parent / 'fotos'
foto = Image.open(AQUI / 'capa-fria.jpg').convert('RGB')
W, H = foto.size
y = np.linspace(0, 1, H, dtype=np.float32)[:, None]

def suave(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)

# desfoque progressivo: mistura de camadas cada vez mais desfocadas
raios = [0, 4, 9, 16, 26]
camadas = [np.asarray(foto if r == 0 else foto.filter(ImageFilter.GaussianBlur(r)), np.float32) for r in raios]
nivel = suave((0.62 - y) / 0.52) * (len(raios) - 1)              # 0 embaixo, máximo no alto
a = np.zeros_like(camadas[0])
for i in range(len(raios)):
    peso = np.clip(1 - np.abs(nivel - i), 0, 1)[..., None]
    a += camadas[i] * peso

# névoa clara no alto (off-white da marca, um pouco puxado para o Tiffany)
TIFFANY = len(sys.argv) > 1 and sys.argv[1] == 'tiffany'
nevoa = np.array([0x9F, 0xC5, 0xBD] if TIFFANY else [0xF1, 0xF5, 0xF3], np.float32)
forca = ((0.94 if TIFFANY else 0.84) * suave((0.56 - y) / 0.50))[..., None]
a = a * (1 - forca) + nevoa * forca

# granulado
rng = np.random.default_rng(13)
a += rng.normal(0, 4.5, (H, W, 1)).astype(np.float32)
nome = 'v14-nevoa-tiffany.jpg' if TIFFANY else 'v13-nevoa.jpg'
Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).save(AQUI / nome, quality=92)
print('ok', nome)
