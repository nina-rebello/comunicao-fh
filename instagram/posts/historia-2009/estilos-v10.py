"""Imagens das duas variações da v10 (referências da Nina de 05/11), a partir da foto das poltronas azuis.
- v10a (vidro, como a referência da marcenaria): fotos/v10a-fundo.jpg, a foto fria em tela cheia com o vidro fosco
  assado no cartão de baixo e no selo do alto (o Canva não lê backdrop-filter).
- v10b (papel e foto, como a referência das cadeiras): fotos/v10b-papel.jpg (fundo de papel no off-white da marca),
  fotos/v10b-detalhe.jpg (o abajur e a planta) e fotos/v10b-baixo.jpg (as poltronas, faixa de baixo).
As medidas batem com foto-v10.html. Uso: python3 instagram/posts/historia-2009/estilos-v10.py"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
AQUI = Path(__file__).parent / 'fotos'

def esfria(im, sat=0.78, frio=0.06, luz=1.04):
    a = np.asarray(im.convert('RGB')).astype(np.float32) / 255
    lum = (a @ np.array([0.299, 0.587, 0.114], dtype=np.float32))[..., None]
    a = lum + (a - lum) * sat
    a *= np.array([1 - frio, 1.0, 1 + frio], dtype=np.float32)
    return Image.fromarray((np.clip(a * luz, 0, 1) * 255).astype(np.uint8))

# v10a: vidro
foto = Image.open(AQUI / 'capa-fria.jpg').convert('RGB')
borrada = Image.blend(foto.filter(ImageFilter.GaussianBlur(26)), Image.new('RGB', foto.size, (18, 34, 32)), 0.34)
mascara = Image.new('L', foto.size, 0)
d = ImageDraw.Draw(mascara)
d.rounded_rectangle((-60, 700, 690, 1236), 40, fill=255)     # cartão do texto, sai pela esquerda
d.rounded_rectangle((640, 92, 1140, 236), 36, fill=255)      # selo do alto, sai pela direita
foto.paste(borrada, (0, 0), mascara)
foto.save(AQUI / 'v10a-fundo.jpg', quality=90)

# v10b: papel, detalhe e faixa de baixo
rng = np.random.default_rng(6)
W, H = 1080 * 2, 760 * 2
base = np.array([0xF4, 0xF6, 0xF3], np.float32)
manchas = np.asarray(Image.fromarray((rng.random((H // 40, W // 40)) * 255).astype('uint8')).resize((W, H), Image.BICUBIC), np.float32) / 255
grao = rng.normal(0, 1, (H, W)).astype(np.float32)
papel = base[None, None, :] - 6 * manchas[..., None] + 3.2 * grao[..., None]
Image.fromarray(np.clip(papel, 0, 255).astype(np.uint8)).save(AQUI / 'v10b-papel.jpg', quality=88)

orig = Image.open(AQUI / 'espaco-nina-original.jpg').convert('RGB')
esfria(orig.crop((925, 420, 1215, 697)).resize((340 * 2, 326 * 2), Image.LANCZOS)).save(AQUI / 'v10b-detalhe.jpg', quality=90)
esfria(orig.crop((672, 382, 1672, 941)).resize((1080 * 2 // 2 * 2, 604 * 2), Image.LANCZOS)).save(AQUI / 'v10b-baixo.jpg', quality=90)
print('ok v10a-fundo, v10b-papel, v10b-detalhe, v10b-baixo')
