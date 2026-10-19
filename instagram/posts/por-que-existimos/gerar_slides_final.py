# Versão final (19/10) do post de qua 21/10, "Por que a fairhealth existe?", com o conteúdo final (conteudo_v6.py).
# A Nina escolheu três testes, A, D e H (testes-design.jpg e testes-design-2.jpg), e mandou duas ilustrações
# feitas por ela (o hospital e o Escritório do Cuidado). Pedido: "use de todos os seus dons de design e crie uma
# versão final, dinâmica, que prenda, que siga as nossas regras de branding".
# O que vem de cada teste:
#   A · o caminho largo em creme, liso, que atravessa os 8 slides, com bolinhas; a pílula da página; a barra de
#       progresso; o fundo Tiffany;
#   D · a frase forte (letra grande e apertada) e a bolinha grande que abre o caminho na capa; dois slides escuros
#       (o acolhimento e o final) para dar ritmo;
#   H · o papel com textura, a etiqueta com o número do capítulo (01 a 07) e as anotações curtas em itálico.
# As ilustrações da Nina (../../marca/ilustracoes/) ficam em pé sobre o caminho, como prédios numa rua: o hospital
# no slide 3 e o Escritório do Cuidado no slide 4. Traço verde e interior creme, sobre o Tiffany.
# Regras: só Raleway, Tiffany como cor principal, sem amarelo, fairhealth em minúsculas, sem travessão.
# Uso: python3 gerar_slides_final.py slides-final.html && node ../../ferramentas/render.mjs slides-final.html png-final
#      python3 gerar_slides_final.py --faixa faixa-final.html (os 8 slides lado a lado, para a prévia)
import sys
from conteudo_v6 import T1, T2, A2, T3, A3, T4, A4, T5, A5, T6, I6, T7, A7, T8, A8, F8, CTA

N, W = 8, 1080
ILU = '../../marca/ilustracoes/'
LOGO = '../../marca/logo-circulo.png'

CSS = r'''
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:400;font-style:italic;src:url(../../marca/fontes/raleway-latin-400-italic.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--tif:#96C5BD;--verde:#1F3A36;--creme:#F0F0E9;--tclaro:#BFE0D9;--vlogo:#2F6B64}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#888;display:flex;flex-wrap:wrap;gap:40px;padding:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-variant-numeric:lining-nums}
.slide>*{position:absolute}
.T{background:var(--tif);color:var(--verde)}
.V{background:var(--verde);color:var(--creme)}
.V .k{color:var(--tif)}
.papel{inset:0;opacity:.32;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='360'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .55 0 0 0 0 .52 0 0 0 -1.1 .85'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"),
    repeating-linear-gradient(0deg,rgba(31,58,54,.03) 0 1px,transparent 1px 4px),
    repeating-linear-gradient(90deg,rgba(31,58,54,.025) 0 1px,transparent 1px 4px)}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.k{font-weight:800;font-style:italic}
.handle{left:96px;top:84px;font-size:24px;line-height:30px;font-weight:800}
.pilula{right:84px;top:76px;height:46px;padding:0 20px;border-radius:23px;background:rgba(31,58,54,.82);color:var(--creme);font-size:22px;line-height:46px;letter-spacing:.04em}
.V .pilula{background:rgba(150,197,189,.22);color:var(--tclaro)}
.cap{left:96px;top:178px;font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--vlogo)}
.V .cap{color:var(--tif)}
.cap b{font-weight:800;color:var(--creme);margin-right:14px}
.T .cap b{color:var(--verde)}
.frase{left:96px;width:900px;letter-spacing:-0.035em}
.apoio{left:96px;width:888px;font-size:34px;line-height:46px}
.V .apoio{color:var(--tclaro)}
.nota{font-size:30px;line-height:38px;font-style:italic}
.V .nota{color:var(--tclaro)}
.rod{left:96px;top:1240px;font-size:22px;line-height:28px;font-weight:800}
.rod span{font-weight:400}
.prog{right:96px;top:1252px;width:120px;height:4px;border-radius:2px;background:rgba(240,240,233,.55)}
.V .prog{background:rgba(240,240,233,.22)}
.prog i{position:absolute;left:0;top:0;height:4px;border-radius:2px;background:var(--verde)}
.V .prog i{background:var(--tif)}
.cartao{left:96px;width:888px;border-radius:30px;background:rgba(240,240,233,.55);padding:18px 44px}
.cartao div{display:flex;gap:26px;align-items:baseline;padding:26px 0;font-size:36px;line-height:46px}
.cartao div+div{border-top:2px solid rgba(31,58,54,.14)}
.cartao b{font-weight:800;color:var(--vlogo);font-size:30px;min-width:46px}
'''

# O caminho: pontos por onde ele passa, no carrossel inteiro (8 × 1080). Curva lisa, faixa de espessura constante.
PONTOS = [
    (160, 930), (420, 990), (720, 1080), (1080, 1150),                       # 1 · nasce na bolinha grande
    (1440, 1060), (1800, 1120), (2160, 1170),                                # 2
    (2700, 1182), (3240, 1172),                                              # 3 · a rua do hospital
    (3780, 1180), (4320, 1172),                                              # 4 · a rua do Escritório do Cuidado
    (4740, 1100), (5080, 1060), (5400, 1010),                                # 5
    (5700, 1060), (6100, 1120), (6480, 1060),                                # 6
    (6960, 1110), (7300, 1020), (7560, 880),                                 # 7 · sobe para o final
    (7860, 980), (8080, 1040), (8230, 1010),                                 # 8 · chega ao logo
]
BOLAS = [(1440, 1060), (5080, 1060), (5700, 1060), (6960, 1110)]
INICIO = PONTOS[0]
LOGO_C = (8320, 990)
FAIXA = 56


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


CAMINHO = caminho(PONTOS)


def estrada(k):
    s = ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#F0F0E9" stroke-width="%d" '
         'stroke-linecap="round" stroke-linejoin="round"/>' % ((k - 1) * W, CAMINHO, FAIXA))
    s += ''.join('<circle cx="%d" cy="%d" r="15" fill="#1F3A36"/>' % b for b in BOLAS)
    s += '<circle cx="%d" cy="%d" r="36" fill="#1F3A36"/><circle cx="%d" cy="%d" r="13" fill="#96C5BD"/>' % (INICIO + INICIO)
    s += '<circle cx="%d" cy="%d" r="88" fill="#F0F0E9"/>' % LOGO_C
    return s + '</svg>'


def cap(n, txt):
    return '<p class="cap"><b>%s</b>%s</p>' % (n, txt)


S = []
# 1 · capa: a frase forte e a bolinha grande que abre o caminho
S.append(('w01', 'T', 'capa', '''<p class="cap">por que a fairhealth existe?</p>
  <p class="frase" style="top:236px;font-size:110px;line-height:110px">%s</p>
  <p class="nota" style="left:226px;top:836px">2009 → hoje</p>''' % T1))
# 2 · 2009
S.append(('w02', 'T', '2009', cap('01', 'o porquê') + '''
  <p style="left:80px;top:214px;font-size:250px;line-height:230px;font-weight:800;letter-spacing:-0.05em;color:var(--creme)">2009</p>
  <p class="frase" style="top:478px;font-size:50px;line-height:60px;letter-spacing:-0.02em">%s</p>
  <p class="frase" style="top:690px;font-size:44px;line-height:54px;letter-spacing:-0.02em;font-weight:800">%s</p>''' % (T2, A2)))
# 3 · no hospital: a ilustração do hospital em pé sobre o caminho
S.append(('w03', 'T', 'no hospital', cap('02', 'no hospital') + '''
  <p class="frase" style="top:222px;font-size:50px;line-height:60px;letter-spacing:-0.02em">%s</p>
  <p class="apoio" style="top:420px">%s</p>
  <p class="nota" style="left:690px;top:520px">onde tudo começou</p>
  <img src="%shospital.png" alt="" style="left:110px;top:580px;width:860px;height:533px">''' % (T3, A3, ILU)))
# 4 · hoje: o Escritório do Cuidado
S.append(('w04', 'T', 'hoje', cap('03', 'hoje, nas empresas') + '''
  <p class="frase" style="top:222px;font-size:62px;line-height:70px;letter-spacing:-0.025em">%s</p>
  <p class="apoio" style="top:390px">%s</p>
  <img src="%sescritorio.png" alt="" style="left:70px;top:612px;width:940px;height:513px">''' % (T4, A4, ILU)))
# 5 · o acolhimento (escuro): a pergunta enorme
S.append(('w05', 'V', 'o acolhimento', cap('04', 'o acolhimento') + '''
  <p class="frase" style="top:236px;font-size:50px;line-height:60px;letter-spacing:-0.02em">Tudo começa com uma pergunta:</p>
  <p class="frase" style="top:320px;font-size:104px;line-height:104px;font-weight:800;font-style:italic;color:var(--tif)">o que é importante para você?</p>
  <p class="apoio" style="top:690px">%s</p>
  <p class="nota" style="left:600px;top:1112px">sem pressa e sem julgamento</p>''' % A5))
# 6 · o que levamos: o cartão com os três itens
S.append(('w06', 'T', 'o que levamos', cap('05', 'o que levamos') + '''
  <p class="frase" style="top:222px;font-size:70px;line-height:76px">%s</p>
  <div class="cartao" style="top:420px">%s</div>''' % (T6, ''.join('<div><b>%02d</b><span>%s</span></div>' % (i + 1, t) for i, t in enumerate(I6)))))
# 7 · perto: a frase forte; o caminho sobe para o final
S.append(('w07', 'T', 'perto', cap('06', 'perto') + '''
  <p class="frase" style="top:222px;font-size:94px;line-height:96px">%s</p>
  <p class="apoio" style="top:560px">%s</p>
  <p class="nota" style="left:506px;top:1150px">perto da rotina de quem trabalha</p>''' % (T7, A7)))
# 8 · o propósito (escuro): o caminho chega ao logo
S.append(('w08', 'V', 'o propósito', cap('07', 'o propósito') + '''
  <p class="frase" style="top:222px;font-size:96px;line-height:98px;font-weight:800">%s</p>
  <p class="apoio" style="top:460px;font-size:32px;line-height:44px">%s %s</p>
  <img src="%s" alt="fairhealth" style="left:%dpx;top:%dpx;width:136px;height:136px">
  <p class="nota" style="left:384px;top:1112px;width:600px;text-align:right;color:var(--creme)">%s</p>''' % (
    F8, T8, A8, LOGO, LOGO_C[0] - 7 * W - 68, LOGO_C[1] - 68, CTA.lower().rstrip('.'))))


def html(slides):
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (final)</title><style>' + CSS + '</style></head><body>\n']
    for k, (sid, cls, nota, corpo) in enumerate(slides, 1):
        rod = ('<p class="rod">arraste para o lado →</p>' if k == 1 else
               '<p class="rod">fairhealth <span>| o cuidado começa pela pessoa</span></p>')
        out.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  <div class="papel"></div>\n  %s\n  <p class="handle">@fairhealth.br</p>\n  <p class="pilula">%d/%d</p>\n  %s\n  %s\n  <div class="prog"><i style="width:%dpx"></i></div>\n</section>\n\n'
                   % (k, nota, cls, sid, estrada(k), k, N, corpo, rod, round(120 * k / N)))
    out.append('</body></html>\n')
    return ''.join(out)


def faixa():
    esc = 0.5
    w, h = round(W * esc), round(1350 * esc)
    imgs = ''.join('<img src="png-final/%s.png" alt="" style="width:%dpx;height:%dpx;display:block">' % (s[0], w, h) for s in S)
    return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (faixa)</title>'
            '<style>*{margin:0;padding:0}body{background:#ECECE6;padding:40px;width:max-content}.seq{display:flex;gap:4px;background:#B8B8B0;padding:4px}</style>'
            '</head><body><div class="seq">%s</div></body></html>\n' % imgs)


if sys.argv[1] == '--faixa':
    open(sys.argv[2], 'w').write(faixa())
else:
    open(sys.argv[1], 'w').write(html(S))
print('ok', len(S))
