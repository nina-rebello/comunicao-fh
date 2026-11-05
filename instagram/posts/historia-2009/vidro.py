"""Assa o efeito de vidro fosco na foto (o Canva não lê backdrop-filter): desfoca e escurece de leve só a área
do cartão, com cantos arredondados. Entrada: fotos/capa-fria.jpg (esfriar.py). Saída: fotos/capa-vidro.jpg.
Uso: python3 instagram/posts/historia-2009/vidro.py"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter
AQUI = Path(__file__).parent / 'fotos'
X, Y, W, H, R = 72, 140, 936, 500, 36          # igual ao .vidro de foto-v3.html
im = Image.open(AQUI / 'capa-fria.jpg').convert('RGB')
borrada = im.filter(ImageFilter.GaussianBlur(28))
escuro = Image.new('RGB', im.size, (16, 34, 32))
borrada = Image.blend(borrada, escuro, 0.38)
mascara = Image.new('L', im.size, 0)
ImageDraw.Draw(mascara).rounded_rectangle((X, Y, X + W, Y + H), R, fill=255)
im.paste(borrada, (0, 0), mascara)
im.save(AQUI / 'capa-vidro.jpg', quality=90)
print('ok capa-vidro.jpg')
