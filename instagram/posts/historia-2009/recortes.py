"""Recorta as imagens do espaço (instagram/marca/espaco) em 1080x1350 para cada slide (em 2x).
As fotos da capa (capa-a.jpg) e do fecho (capa-b.jpg) são do espaço e não passam por aqui.
Uso: python3 instagram/posts/historia-2009/recortes.py"""
from pathlib import Path
from PIL import Image, ImageEnhance
AQUI = Path(__file__).parent
ESPACO = AQUI.parent.parent / 'marca' / 'espaco'
# slide: (imagem, foco x de 0 a 1)
CORTES = {
    'h-02': ('recepcao-parede-pedra.jpg', 0.18),
    'h-03': ('sala-atendimento-e-espera.jpg', 0.30),
    'h-04': ('copa-parede-verde.jpg', 0.30),
    'h-05': ('sala-atendimento-e-espera.jpg', 0.99),
}
W, H = 2160, 2700
for nome, (arq, fx) in CORTES.items():
    im = Image.open(ESPACO / arq).convert('RGB')
    esc = H / im.height
    im = im.resize((round(im.width * esc), H), Image.LANCZOS)
    x = min(max(round(im.width * fx - W / 2), 0), im.width - W)
    im = im.crop((x, 0, x + W, H))
    im = ImageEnhance.Brightness(im).enhance(1.0)
    # aquece os renders para conversar com as fotos reais da capa e do fecho (luz âmbar)
    r, g, b = im.split()
    im = Image.merge('RGB', (r.point(lambda v: min(255, v * 1.10)), g.point(lambda v: v * 1.0), b.point(lambda v: v * 0.84)))
    im = ImageEnhance.Color(im).enhance(0.9)
    im.save(AQUI / 'fotos' / f'{nome}.jpg', quality=86)
    print(nome, arq)
