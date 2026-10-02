# Fundos do carrossel amarelo: uma onda tom sobre tom e uma linha fina que atravessam
# os 10 slides sem emenda (panorama), mais grão leve. Gera PNGs usados como fundo.
# Uso: python3 instagram/posts/acolhimento/fundos.py
#      node instagram/ferramentas/render.mjs instagram/posts/acolhimento/fundos.html instagram/posts/acolhimento/fundos
import math
import pathlib

AQUI = pathlib.Path(__file__).parent
W, H, N = 1080, 1350, 10
# cor de fundo, tom da onda, cor da linha
T = ('#9FC5BD', '#88B5AB', '#7EAAA0', '#B3D3CC')
C = ('#F0F0E9', '#D3E5E0', '#BFD9D3', '#FFFFFF')
FUNDOS = [T, C, C, T, T, C, C, T, C, T]


def onda(y0, amp, fase, passo=12):
    pts = []
    for x in range(-20, W * N + 40, passo):
        y = (y0 + amp * math.sin(x / 520 + fase) + amp * .45 * math.sin(x / 210 + fase * 2)
             + 60 * math.sin(x / 1700))
        pts.append(f'{x},{y:.1f}')
    return pts


area = 'M' + ' L'.join(onda(1080, 55, 0)) + f' L{W * N + 40},{H + 10} L-20,{H + 10} Z'
area2 = 'M' + ' L'.join(onda(1180, 45, 2.1)) + f' L{W * N + 40},{H + 10} L-20,{H + 10} Z'
linha = 'M' + ' L'.join(onda(1000, 48, .9))

GRAO = ("<filter id='g'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/>"
        "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .07 0'/></filter>")

secoes = []
for i, (bg, tom, tom2, luz) in enumerate(FUNDOS):
    secoes.append(f'''<section class="slide" id="f-{i + 1:02d}">
<svg width="{W}" height="{H}" viewBox="{i * W} 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">
  <defs>{GRAO}<radialGradient id="l{i}" cx="{i * W + 150}" cy="80" r="1100" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{luz}" stop-opacity=".55"/><stop offset="1" stop-color="{luz}" stop-opacity="0"/></radialGradient></defs>
  <rect x="{i * W}" y="0" width="{W}" height="{H}" fill="{bg}"/>
  <rect x="{i * W}" y="0" width="{W}" height="{H}" fill="url(#l{i})"/>
  <path d="{area}" fill="{tom}"/>
  <path d="{area2}" fill="{tom2}"/>
  <path d="{linha}" fill="none" stroke="#F2C14E" stroke-width="7" stroke-linecap="round"/>
  <rect x="{i * W}" y="0" width="{W}" height="{H}" filter="url(#g)"/>
</svg></section>''')

(AQUI / 'fundos.html').write_text(
    '<!doctype html><html><head><meta charset="utf-8"><style>*{margin:0;padding:0}'
    f'.slide{{width:{W}px;height:{H}px;overflow:hidden}}</style></head><body>' + ''.join(secoes) + '</body></html>')
print('ok')
