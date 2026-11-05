"""Versão clara da v4 (retorno da Nina, 05/11: "muito escuro, não combina com a gente"). A foto fica quase na luz
natural (fria, de esfriar.py); só o alto, onde fica o texto, recebe um véu verde-escuro da marca (#1E3F3B) que
some antes das poltronas. Saída: fotos/capa-clara.jpg.
Uso: python3 instagram/posts/historia-2009/clarear.py"""
from pathlib import Path
import numpy as np
from PIL import Image
AQUI = Path(__file__).parent / 'fotos'
a = np.asarray(Image.open(AQUI / 'capa-fria.jpg').convert('RGB')).astype(np.float32) / 255
H, W, _ = a.shape
y = np.linspace(0, 1, H)[:, None, None]
x = np.linspace(0, 1, W)[None, :, None]
# véu: forte no alto, mais forte à esquerda (onde começa o texto), zero a partir de ~64% da altura
forca = np.clip(1 - y / 0.64, 0, 1) ** 0.9 * (0.64 + 0.16 * (1 - x))
verde = np.array([0x1E, 0x3F, 0x3B], dtype=np.float32) / 255
a = a * (1 - forca) + verde * forca
Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(AQUI / 'capa-clara.jpg', quality=90)
print('ok capa-clara.jpg')
