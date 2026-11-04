"""Recorta as imagens do espaço (instagram/marca/espaco) em 1080x1350 para cada slide (em 2x).
Uso: python3 instagram/posts/historia-2009/recortes.py"""
from pathlib import Path
from PIL import Image, ImageEnhance
AQUI = Path(__file__).parent
ESPACO = AQUI.parent.parent / 'marca' / 'espaco'
# slide: (imagem, foco x de 0 a 1)
CORTES = {
    'h-01': ('sala-atendimento-e-espera.jpg', 0.62),
    'h-02': ('recepcao-parede-pedra.jpg', 0.18),
    'h-03': ('sala-atendimento-e-espera.jpg', 0.30),
    'h-04': ('copa-parede-verde.jpg', 0.30),
    'h-05': ('sala-atendimento-e-espera.jpg', 0.99),
    'h-06': ('copa-parede-verde.jpg', 0.62),
}
W, H = 2160, 2700
for nome, (arq, fx) in CORTES.items():
    im = Image.open(ESPACO / arq).convert('RGB')
    esc = H / im.height
    im = im.resize((round(im.width * esc), H), Image.LANCZOS)
    x = min(max(round(im.width * fx - W / 2), 0), im.width - W)
    im = im.crop((x, 0, x + W, H))
    im = ImageEnhance.Brightness(im).enhance(0.92)  # um pouco mais quente e baixo, como a referência
    im.save(AQUI / 'fotos' / f'{nome}.jpg', quality=86)
    print(nome, arq)
