# Fundos "minimalista e complexo": linhas de contorno finas, tom sobre tom, que atravessam
# os 10 slides sem emenda, e o numeral do passo só em contorno. Gera PNGs de fundo.
# Uso: python3 instagram/posts/acolhimento/linhas.py
#      node instagram/ferramentas/render.mjs instagram/posts/acolhimento/linhas.html instagram/posts/acolhimento/linhas
import math
import pathlib

AQUI = pathlib.Path(__file__).parent
W, H, N = 1080, 1350, 10
T = ('#9FC5BD', '#84AFA6')   # fundo, linha
C = ('#F0F0E9', '#C9DAD3')
FUNDOS = [T, C, C, T, T, C, C, T, C, T]
NUMS = {4: '01', 5: '02', 6: '03', 7: '04', 8: '05'}


def linha(k):
    # feixe de linhas paralelas que sobe e desce devagar ao longo do carrossel
    pts = []
    for x in range(-40, W * N + 60, 10):
        base = 1040 + 140 * math.sin(x / 1400) + 70 * math.sin(x / 530 + 1.3)
        y = base + k * 22 + (8 + k * 1.5) * math.sin(x / 260 + k * .35)
        pts.append(f'{x},{y:.1f}')
    return 'M' + ' L'.join(pts)


feixe = ''.join(f'<path d="{linha(k)}"/>' for k in range(-6, 12))

secoes = []
for i, (bg, cor) in enumerate(FUNDOS, start=1):
    num = (f'<text x="{(i - 1) * W + 1040}" y="560" text-anchor="end" class="num" stroke="{cor}">{NUMS[i]}</text>'
           if i in NUMS else '')
    secoes.append(f'''<section class="slide" id="l-{i:02d}">
<svg width="{W}" height="{H}" viewBox="{(i - 1) * W} 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <rect x="{(i - 1) * W}" y="0" width="{W}" height="{H}" fill="{bg}"/>
  <g fill="none" stroke="{cor}" stroke-width="2.2">{feixe}</g>
  {num}
</svg></section>''')

CSS = """@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
*{margin:0;padding:0}.slide{width:1080px;height:1350px;overflow:hidden}
.num{font-family:Raleway;font-weight:800;font-style:italic;font-size:520px;fill:none;stroke-width:3;letter-spacing:-10px}"""
(AQUI / 'linhas.html').write_text('<!doctype html><html><head><meta charset="utf-8"><style>' + CSS +
                                  '</style></head><body>' + ''.join(secoes) + '</body></html>')
print('ok')
