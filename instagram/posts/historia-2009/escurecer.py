"""Versão escura e elegante da foto (referência da Nina de 05/11: foto em penumbra, texto branco direto sobre ela).
Baixa a exposição, aumenta um pouco o contraste e escurece mais o alto e as bordas, onde fica o texto.
Entrada: fotos/capa-fria.jpg (esfriar.py). Saída: fotos/capa-escura.jpg.
Uso: python3 instagram/posts/historia-2009/escurecer.py"""
from pathlib import Path
import numpy as np
from PIL import Image
AQUI = Path(__file__).parent / 'fotos'
a = np.asarray(Image.open(AQUI / 'capa-fria.jpg').convert('RGB')).astype(np.float32) / 255
H, W, _ = a.shape
a = np.clip((a - 0.5) * 1.12 + 0.5, 0, 1) ** 1.35 * 0.78      # contraste, gama e exposição
y = np.linspace(0, 1, H)[:, None]
x = np.linspace(-1, 1, W)[None, :]
vert = 0.55 + 0.45 * np.clip((y - 0.15) / 0.55, 0, 1)            # alto mais escuro, onde fica o texto
vinheta = 1 - 0.35 * (x ** 2) * (0.6 + 0.4 * y)                   # bordas mais escuras
a *= (vert * vinheta)[..., None]
Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).save(AQUI / 'capa-escura.jpg', quality=90)
print('ok capa-escura.jpg')
