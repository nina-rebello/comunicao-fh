# Fundos em glassmorphism para o carrossel amarelo.
# Panorama contínuo (luzes desfocadas em Tiffany, creme e amarelo) + numeral do passo
# + painel de vidro fosco atrás do texto de cada slide. O texto continua editável no HTML.
# Uso: node instagram/ferramentas/medir.mjs instagram/posts/acolhimento/amarelo.html caixas.json
#      python3 instagram/posts/acolhimento/vidro.py caixas.json
#      node instagram/ferramentas/render.mjs instagram/posts/acolhimento/vidro.html instagram/posts/acolhimento/vidro
import json
import pathlib
import sys

AQUI = pathlib.Path(__file__).parent
W, H, N = 1080, 1350, 10
caixas = {c['id']: c for c in json.load(open(sys.argv[1]))}

# luzes do panorama: x, y, tamanho, cor, opacidade
LUZES = [
    (300, 200, 900, '#F0F0E9', .55), (900, 1150, 800, '#F2C14E', .65), (1700, 300, 1000, '#4E8E83', .75),
    (2500, 1100, 900, '#F0F0E9', .6), (3300, 250, 800, '#F2C14E', .6), (4000, 1000, 1000, '#4E8E83', .7),
    (4700, 200, 900, '#F0F0E9', .55), (5500, 1150, 850, '#F2C14E', .62), (6300, 300, 1000, '#4E8E83', .7),
    (7000, 1100, 900, '#F0F0E9', .6), (7800, 250, 800, '#F2C14E', .6), (8600, 1050, 1000, '#4E8E83', .7),
    (9400, 200, 900, '#F0F0E9', .55), (10200, 1100, 850, '#F2C14E', .62),
]
NUMS = {4: '1', 5: '2', 6: '3', 7: '4', 8: '5', 1: '?'}
EXTRA = {9: 260, 10: 200}  # topo do painel inclui ícone / logo

luzes = ''.join(
    f'<div class="luz" style="left:{x - t / 2}px;top:{y - t / 2}px;width:{t}px;height:{t * .7}px;background:{c};opacity:{o}"></div>'
    for x, y, t, c, o in LUZES)

secoes = []
for i in range(1, N + 1):
    c = caixas[f'y-{i:02d}']
    x0, x1 = max(56, c['x0'] - 48), min(W - 56, c['x1'] + 48)
    y0, y1 = EXTRA.get(i, c['y0']) - 48, c['y1'] + 48
    num = f'<div class="num">{NUMS[i]}</div>' if i in NUMS else ''
    secoes.append(f'''<section class="slide" id="v-{i:02d}">
  <div class="pano" style="left:{-(i - 1) * W}px">{luzes}</div>
  {num}
  <div class="vidro" style="left:{x0}px;top:{y0}px;width:{x1 - x0}px;height:{y1 - y0}px"></div>
  <div class="grao"></div>
</section>''')

CSS = """
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
*{margin:0;padding:0;box-sizing:border-box}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#9FC5BD}
.slide>*{position:absolute}
.pano{top:0;width:10800px;height:1350px}
.luz{position:absolute;border-radius:50%;filter:blur(140px)}
.num{right:30px;top:20px;font-family:Raleway;font-size:900px;font-weight:800;font-style:italic;line-height:.85;color:rgba(255,255,255,.38)}
.vidro{border-radius:56px;background:linear-gradient(135deg,rgba(255,255,255,.52),rgba(255,255,255,.24));
  backdrop-filter:blur(34px) saturate(1.2);-webkit-backdrop-filter:blur(34px) saturate(1.2);
  border:2px solid rgba(255,255,255,.7);box-shadow:0 30px 70px rgba(31,58,54,.16),inset 0 1px 0 rgba(255,255,255,.8)}
.grao{inset:0;opacity:.06;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
"""
(AQUI / 'vidro.html').write_text('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS +
                                 '</style></head><body>' + ''.join(secoes) + '</body></html>')
print('ok')
