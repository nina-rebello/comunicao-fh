"""Recorta as fotos de cada slide no tamanho exato da moldura (em 2x), para o Canva não precisar de
object-fit. A capa (fotos/capa-a.jpg) já está pronta e não passa por aqui.
Uso: python3 instagram/posts/historia-2009/recortes.py"""
from pathlib import Path
from PIL import Image, ImageEnhance
AQUI = Path(__file__).parent
ESPACO = AQUI.parent.parent / 'marca' / 'espaco'
FOTOS = AQUI / 'fotos'
# saída: (arquivo de origem, largura, altura no slide, foco x, foco y, aquecer?)
CORTES = {
    'h-02': (ESPACO / 'copa-parede-verde.jpg', 1080, 480, 0.50, 0.55, True),
    'h-04': (ESPACO / 'sala-atendimento-e-espera.jpg', 368, 600, 0.30, 0.50, True),
    'h-05': (ESPACO / 'sala-atendimento-e-espera.jpg', 408, 460, 0.97, 0.45, True),
    'h-06': (FOTOS / 'capa-b.jpg', 1080, 520, 0.50, 0.30, False),
}
for nome, (arq, w, h, fx, fy, quente) in CORTES.items():
    W, H = w * 2, h * 2
    im = Image.open(arq).convert('RGB')
    esc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * esc), round(im.height * esc)), Image.LANCZOS)
    x = min(max(round(im.width * fx - W / 2), 0), im.width - W)
    y = min(max(round(im.height * fy - H / 2), 0), im.height - H)
    im = im.crop((x, y, x + W, y + H))
    if quente:  # aproxima os renders da luz âmbar das fotos reais
        r, g, b = im.split()
        im = Image.merge('RGB', (r.point(lambda v: min(255, v * 1.08)), g, b.point(lambda v: v * 0.88)))
        im = ImageEnhance.Brightness(im).enhance(1.08)
    im.save(FOTOS / f'{nome}.jpg', quality=86)
    print(nome, arq.name, w, h)
