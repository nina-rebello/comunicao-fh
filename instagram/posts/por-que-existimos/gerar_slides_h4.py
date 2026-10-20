# Versão H4 (20/10) do post de qua 21/10, "Por que a fairhealth existe?": mais enxuta e com mais vida. Pedido da Nina,
# sobre o design H2 do Canva (DAHYfVF20nU): "vamos diminuir a quantidade de slides, juntando os textos, e traga um
# pouco mais de vida para esses slides, texturas, imagens etc".
#   - Textos: os que estão hoje no Canva (com as edições da Nina: sem os números, "Foi aí que nasceu o Escritório do
#     Cuidado", o final com "conheça a [logo] no link da bio!"), juntados de 8 para 6 slides. Sai só "Era preciso mudar
#     essa realidade", que repete o "para mudar essa realidade" do slide seguinte, e o parágrafo da barreira de tempo e
#     acesso (o slide 5 fica com a frase "quando o cuidado está perto, ele acontece").
#   - Vida: fotos em tom Tiffany (../../ferramentas/tonalizar-tiffany.py) recortadas em arco e em círculo, com um arco
#     de contorno deslocado atrás; os desenhos da Nina (hospital e escritório, ../../marca/ilustracoes/); o papel com
#     mais grão; uma luz suave atrás das imagens.
#   - Mesma linha fina atravessando os slides, com as anotações em negrito itálico, como a Nina deixou no Canva.
# Uso: python3 gerar_slides_h4.py slides-h4.html && node ../../ferramentas/render.mjs slides-h4.html png-h4
#      python3 gerar_slides_h4.py --fundo slides-h4-fundo.html (sem os textos e as imagens, para o fundo do Canva)
import sys
from conteudo_v6 import T1, T2, T3, A3, A4, T5, A5, T6, I6, T7, T8, A8, F8

N, W = 6, 1080
LOGO = '../../marca/logo-circulo.png'
IMG = '../../posts/por-que-existimos/img-h4/'  # caminho pela raiz, para o HTML do Canva achar as imagens
ILU = '../../marca/ilustracoes/'
TIFFANY = {1, 3, 5}
FUNDO = len(sys.argv) > 1 and sys.argv[1] == '--fundo'
T4 = 'Foi aí que nasceu o <span class="k">Escritório do Cuidado</span>.'

CSS = r'''
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:400;font-style:italic;src:url(../../marca/fontes/raleway-latin-400-italic.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--tif:#96C5BD;--verde:#1F3A36;--creme:#F0F0E9;--tclaro:#BFE0D9;--vlogo:#2F6B64}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#888;display:flex;flex-wrap:wrap;gap:40px;padding:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-variant-numeric:lining-nums;color:var(--verde)}
.slide>*{position:absolute}
.C{background:var(--creme)} .T{background:var(--tif)}
.k{font-weight:800;font-style:italic;color:var(--vlogo)}
.T .k{color:var(--verde)}
.papel{inset:0;opacity:.8;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='360'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .55 0 0 0 0 .53 0 0 0 0 .48 0 0 0 -1.1 .85'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"),
    repeating-linear-gradient(0deg,rgba(31,58,54,.04) 0 1px,transparent 1px 4px),
    repeating-linear-gradient(90deg,rgba(31,58,54,.035) 0 1px,transparent 1px 4px)}
.T .papel{opacity:.6}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.topo{top:96px;font-size:24px;line-height:30px;font-weight:800;color:var(--tif)}
.T .topo{color:var(--creme)}
.rod{left:96px;top:1236px;font-size:24px;line-height:30px;font-weight:800;color:var(--tif)}
.T .rod{color:var(--creme)}
.rod span{font-weight:400}
.cab{font-size:58px;line-height:66px;font-weight:800;color:var(--vlogo);letter-spacing:-0.01em}
.T .cab{color:var(--verde)}
.txt{font-size:40px;line-height:52px}
.txt2{font-size:34px;line-height:46px}
.num{font-size:72px;line-height:72px;font-weight:800;color:var(--vlogo)}
.T .num{color:var(--verde)}
.nota{font-size:28px;line-height:36px;font-style:italic;font-weight:800;color:var(--vlogo)}
.T .nota{color:var(--verde)}
.lista li{list-style:none;font-size:36px;line-height:48px;padding-left:34px;position:relative}
.lista li+li{margin-top:18px}
.lista li::before{content:'';position:absolute;left:0;top:18px;width:14px;height:14px;border-radius:50%;background:var(--tif)}
.T .lista li::before{background:var(--creme)}
/* fundo para o Canva: some o texto (as bolinhas da lista ficam) e o logo */
.fundo .slide p,.fundo .slide li{color:transparent!important}
.fundo .slide p *{color:transparent!important}
.fundo .slide img{visibility:hidden}
'''

PONTOS = [
    (130, 1060), (420, 1100), (760, 1040), (1080, 1080),
    (1250, 1010), (1330, 940), (1560, 1060), (1720, 1170), (2160, 1180),
    (2260, 1180), (2700, 1170), (2900, 1080), (3000, 960), (3160, 820),
    (3260, 830), (3360, 900), (3420, 860), (3400, 790), (3340, 780), (3310, 840), (3360, 930), (3500, 1080), (3840, 1060), (4320, 1000),
    (4500, 1060), (4800, 1185), (5200, 1170), (5400, 1000),
    (5640, 1080), (5900, 1135), (6100, 1130),
]
BOLAS = [(130, 1060), (1330, 940), (3000, 960), (3500, 1080), (4500, 1060)]
LOGO_C = (6180, 1130)


def caminho(p):
    d = 'M%.1f %.1f' % p[0]
    for i in range(len(p) - 1):
        p0 = p[i - 1] if i else p[i]
        p1, p2 = p[i], p[i + 1]
        p3 = p[i + 2] if i + 2 < len(p) else p[i + 1]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += ' C%.1f %.1f %.1f %.1f %.1f %.1f' % (c1 + c2 + p2)
    return d


LINHA = caminho(PONTOS)


def arco(x, y, w, h, cor):
    r = w / 2
    return '<path d="M%d %d V%d A%d %d 0 0 1 %d %d V%d" fill="none" stroke="%s" stroke-width="2.5"/>' % (x, y + h, y + r, r, r, x + w, y + r, y + h, cor)


def slide(k, corpo, enfeite='', rodape=True):
    t = k in TIFFANY
    cor = '#1F3A36' if t else '#2F6B64'
    linha = ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true">%s<path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>%s'
             '<circle cx="%d" cy="%d" r="64" fill="#F0F0E9" stroke="%s" stroke-width="3"/></svg>'
             % ((k - 1) * W, enfeite, LINHA, cor, ''.join('<circle cx="%d" cy="%d" r="12" fill="%s"/>' % (b + (cor,)) for b in BOLAS), LOGO_C[0], LOGO_C[1], cor))
    seta = ('<svg aria-hidden="true" style="left:864px;top:1236px;width:120px;height:30px" viewBox="0 0 120 30"><path d="M0 15H116M104 4L117 15L104 26" fill="none" '
            'stroke="%s" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>' % ('#F0F0E9' if t else '#96C5BD')) if k < N else ''
    topo = '<p class="topo" style="left:96px">@fairhealth.br</p>\n  ' if rodape else ''
    rod = '\n  <p class="rod">fairhealth <span>| o cuidado começa pela pessoa</span></p>' if rodape else ''
    return ('k%d' % k, 'T' if t else 'C', '<div class="papel"></div>\n  %s\n  %s<p class="topo" style="right:96px;font-weight:400">nossa história</p>\n  %s%s%s'
            % (linha, topo, corpo, rod, ('\n  ' + seta) if seta else ''))


def luz(k, cx, cy, r, cor):
    # luz suave atrás das imagens (vai no fundo do Canva)
    return '<circle cx="%d" cy="%d" r="%d" fill="url(#luz%d)"/><defs><radialGradient id="luz%d"><stop offset="0" stop-color="%s" stop-opacity=".75"/><stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient></defs>' % ((k - 1) * W + cx, cy, r, k, k, cor, cor)


def x(k, v):
    return (k - 1) * W + v


S = [
    slide(1, '''<p class="cab" style="left:96px;top:190px;width:520px">Por que a fairhealth existe?</p>
  <p class="txt" style="left:96px;top:430px;width:430px">%s</p>
  <img src="%scorredor-hospital.png" alt="Corredor de hospital" style="left:560px;top:250px;width:440px;height:622px">''' % (T1, IMG),
          luz(1, 780, 580, 460, '#BFE0D9') + arco(x(1, 584), 274, 440, 622, '#1F3A36')),
    slide(2, '''<p class="txt" style="left:96px;top:200px;width:888px">%s</p>
  <p class="txt2" style="left:96px;top:410px;width:888px">%s</p>
  <img src="%shospital.png" alt="Desenho de um hospital" style="left:470px;top:700px;width:540px;height:335px">
  <p class="nota" style="left:200px;top:870px">2009, no hospital</p>''' % (T2, T3, ILU),
          luz(2, 740, 870, 340, '#FFFFFF')),
    slide(3, '''<p class="txt2" style="left:96px;top:200px;width:888px">%s</p>
  <p class="cab" style="left:96px;top:262px;width:888px">%s</p>
  <p class="txt2" style="left:96px;top:420px;width:888px">%s</p>
  <img src="%ssala-atendimento.png" alt="Sala de atendimento do Escritório do Cuidado" style="left:96px;top:640px;width:400px;height:491px">
  <p class="nota" style="left:640px;top:990px">hoje, nas empresas</p>''' % (A3, T4, A4, IMG),
          luz(3, 300, 860, 380, '#BFE0D9') + arco(x(3, 118), 662, 400, 491, '#1F3A36')),
    slide(4, '''<p class="txt" style="left:96px;top:200px;width:888px;font-size:44px;line-height:56px">%s</p>
  <p class="txt2" style="left:96px;top:350px;width:888px">%s</p>
  <img src="%smaos.png" alt="Mãos dadas, num gesto de acolhimento" style="left:610px;top:600px;width:370px;height:370px">
  <p class="nota" style="left:200px;top:1110px">sem pressa e sem julgamento</p>''' % (T5, A5, IMG),
          luz(4, 795, 785, 300, '#FFFFFF') + '<circle cx="%d" cy="%d" r="185" fill="none" stroke="#96C5BD" stroke-width="2.5"/>' % (x(4, 817), 807)),
    slide(5, '''<p class="txt" style="left:96px;top:200px;width:888px;font-size:48px;line-height:60px">%s</p>
  <ul class="lista" style="left:96px;top:300px;width:860px">%s</ul>
  <p class="txt" style="left:96px;top:600px;width:640px;font-size:44px;line-height:56px">%s</p>
  <img src="%sescritorio.png" alt="Desenho do Escritório do Cuidado" style="left:380px;top:800px;width:600px;height:328px">
  <p class="nota" style="left:96px;top:960px">dentro da empresa</p>''' % (T6, ''.join('<li>%s</li>' % t for t in I6), T7, ILU),
          luz(5, 680, 960, 360, '#BFE0D9')),
    slide(6, '''<p class="nota" style="left:384px;top:200px;width:600px;text-align:right">a gente tá aqui pra te ouvir</p>
  <p class="cab" style="left:284px;top:250px;width:700px;text-align:right">%s</p>
  <p class="txt2" style="left:284px;top:430px;width:700px;text-align:right">%s %s</p>
  <p class="nota" style="left:580px;top:1010px;width:400px;text-align:center">conheça a</p>
  <img src="%s" alt="fairhealth" style="left:%dpx;top:%dpx;width:108px;height:108px">
  <p class="nota" style="left:580px;top:1214px;width:400px;text-align:center">no link da bio!</p>''' % (F8, T8, A8, LOGO, LOGO_C[0] - 5 * W - 54, LOGO_C[1] - 54),
          luz(6, 780, 1130, 260, '#FFFFFF'), rodape=False),
]


def html():
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (H4)</title><style>' + CSS + '</style></head><body%s>\n'
           % (' class="fundo"' if FUNDO else '')]
    for sid, cls, corpo in S:
        out.append('<section class="slide %s" id="%s">\n  %s\n</section>\n' % (cls, sid, corpo))
    out.append('</body></html>\n')
    return ''.join(out)


open(sys.argv[2] if FUNDO else sys.argv[1], 'w').write(html())
print('ok', len(S))
