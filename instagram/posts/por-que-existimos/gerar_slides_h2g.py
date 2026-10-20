# Versão H2G (20/10): a H2F com outra capa, a partir de um esboço da Nina no Canva ("faça esse slide com essa ideia
# aqui, indo de um hospital para a empresa, usando imagens"). No lugar da mão com o hospital, duas fotos lado a lado
# (Pexels, ../../marca/fotos-banco/pexels/): um corredor de hospital e, um pouco mais alta, uma sala de reunião, cada
# uma com a sua anotação ("2009, no hospital" e "hoje, nas empresas"). A linha continua correndo embaixo. O resto é
# igual à H2F (gerar_slides_h2f.py, que fica guardado).
#
# Teste H2F (20/10): a H2 com uma foto do espaço no fundo do slide 4, num tom mais Tiffany, a pedido da Nina ("no
# slide 4, duplique ele e teste colocar uma imagem de fundo, mas com um tom mais Tiffany"). As fotos são os renders do
# Escritório do Cuidado (../../marca/espaco/, ainda [PENDENTE] em referencias.md), passados para o Tiffany com
# ../../ferramentas/tonalizar-tiffany.py (../../marca/espaco/tiffany/). São três opções seguidas no lugar do
# slide 4 (k4a, sala de atendimento; k4b, copa; k4c, recepção), para a Nina escolher. O slide 4 passa a ter fundo
# Tiffany: o texto fica no Tiffany liso do alto, e a foto aparece da metade para baixo. O resto é igual à H2
# (gerar_slides_h2.py, que fica guardado).
#
# Versão H2 (19/10): a H com uma imagem na capa, a pedido da Nina ("pode adicionar uma imagem assim no primeiro slide,
# porém, ao invés de uma casa, ser um hospital?", com a referência de uma mão segurando uma casa). A imagem
# (../../marca/ilustracoes/capa-mao-hospital.png) junta a foto de uma mão (Pexels, uso livre) e o hospital desenhado
# pela Nina, sem a médica. Na capa, a linha deixa de fazer o laço e corre embaixo, sob a mão. O resto é igual à H
# (gerar_slides_h.py, que fica guardado).
#
# Versão H final (19/10) do post de qua 21/10, "Por que a fairhealth existe?", com o conteúdo final (conteudo_v6.py).
# A Nina não gostou da versão final A + D + H ("eu odiei") e escolheu o teste H (referência Polina, em
# testes-design-2.jpg): "faça nessa versão mesmo, mas faça alguns em Tiffany ao invés de tudo creme e já adicione no
# Canva". Duplicado da faixa H de gerar_testes_design_2.py (que fica guardado).
#   - Mesmo desenho: papel com textura, linha fina com dois laços, números de 01 a 07 nas bolinhas, texto grande,
#     anotações curtas, cabeçalho e rodapé discretos, final alinhado à direita com a linha chegando ao logo.
#   - Fundos alternados: Tiffany nos slides 1, 3, 5 e 7; creme nos 2, 4, 6 e 8. No Tiffany, a linha, os números e as
#     anotações passam para o verde-escuro, e o cabeçalho e o rodapé para o creme.
# Uso: python3 gerar_slides_h2g.py slides-h2g.html && node ../../ferramentas/render.mjs slides-h2g.html png-h2g
#      python3 gerar_slides_h2g.py --fundo slides-h2g-fundo.html (sem os textos e o logo, para o fundo do Canva)
import sys
from conteudo_v6 import T1, T2, A2, T3, A3, T4, A4, T5, A5, T6, I6, T7, A7, T8, A8, F8

N, W = 8, 1080
LOGO = '../../marca/logo-circulo.png'
TIFFANY = {1, 3, 5, 7}
FUNDO = len(sys.argv) > 1 and sys.argv[1] == '--fundo'

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
.papel{inset:0;opacity:.55;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='360'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .55 0 0 0 0 .53 0 0 0 0 .48 0 0 0 -1.1 .85'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"),
    repeating-linear-gradient(0deg,rgba(31,58,54,.04) 0 1px,transparent 1px 4px),
    repeating-linear-gradient(90deg,rgba(31,58,54,.035) 0 1px,transparent 1px 4px)}
.T .papel{opacity:.4}
.foto{left:0;width:1080px;background-size:cover;background-repeat:no-repeat}
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
.nota{font-size:28px;line-height:36px;font-style:italic;color:var(--vlogo)}
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
    (150, 1175), (500, 1190), (800, 1150), (1080, 1120),
    (1240, 1090), (1380, 1000), (1680, 1060), (1900, 1010), (2160, 900),
    (2300, 780), (2380, 560), (2460, 400), (2700, 380), (2980, 470), (3160, 580), (3240, 640),
    (3420, 740), (3720, 900), (4000, 960), (4320, 860),
    (4500, 940), (4620, 1000), (4700, 930), (4670, 850), (4590, 840), (4560, 920), (4620, 1020), (4920, 1100), (5200, 1020), (5400, 900),
    (5700, 880), (6100, 1000), (6480, 940),
    (6880, 1050), (7280, 900), (7480, 640), (7560, 520),
    (7760, 640), (7860, 760), (7980, 1000), (8160, 1120), (8276, 1130),
]
BOLAS = [(150, 1175), (1380, 1000), (2460, 400), (3720, 900), (4920, 1100), (5700, 880), (6880, 1050), (7860, 760)]
LOGO_C = (8340, 1130)


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


def slide(k, corpo, sid=None, foto=''):
    t = k in TIFFANY or bool(foto)
    cor = '#1F3A36' if t else '#2F6B64'
    linha = ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>%s'
             '<circle cx="%d" cy="%d" r="64" fill="#F0F0E9" stroke="%s" stroke-width="3"/></svg>'
             % ((k - 1) * W, LINHA, cor, ''.join('<circle cx="%d" cy="%d" r="12" fill="%s"/>' % (b + (cor,)) for b in BOLAS), LOGO_C[0], LOGO_C[1], cor))
    seta = ('<svg aria-hidden="true" style="left:864px;top:1236px;width:120px;height:30px" viewBox="0 0 120 30"><path d="M0 15H116M104 4L117 15L104 26" fill="none" '
            'stroke="%s" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>' % ('#F0F0E9' if t else '#96C5BD')) if k < N else ''
    return (sid or 'k%d' % k, 'T' if t else 'C', foto + '<div class="papel"></div>\n  %s\n  <p class="topo" style="left:96px">@fairhealth.br</p>\n  <p class="topo" style="right:96px;font-weight:400">nossa história</p>\n  %s\n  <p class="rod">fairhealth <span>| o cuidado começa pela pessoa</span></p>%s'
            % (linha, corpo, ('\n  ' + seta) if seta else ''))


# slide 4: o mesmo texto da H2, sobre uma das fotos do espaço em tom Tiffany. A foto ocupa a parte de baixo (de 470
# a 1350) e se dissolve no Tiffany liso do alto, onde fica o texto. Um véu Tiffany (42%) clareia a foto para o número e
# a anotação continuarem legíveis; embaixo, um véu verde leve segura o rodapé creme.
CORPO4 = '''<p class="txt" style="left:96px;top:200px;width:888px;font-size:48px;line-height:60px">%s</p>
  <p class="txt2" style="left:96px;top:350px;width:888px">%s</p>
  <p class="num" style="left:510px;top:790px">03</p>
  <p class="nota" style="left:620px;top:812px">hoje, nas empresas</p>''' % (T4, A4)


def foto(arq, pos):
    return ('<div class="foto" style="top:470px;height:880px;background-image:url(../../marca/espaco/tiffany/%s.jpg);background-position:%s"></div>\n  '
            '<div style="left:0;top:470px;width:1080px;height:880px;background:linear-gradient(180deg,#96C5BD 6%%,rgba(150,197,189,.42) 46%%,rgba(150,197,189,.42))"></div>\n  '
            '<div style="left:0;top:1130px;width:1080px;height:220px;background:linear-gradient(180deg,rgba(31,58,54,0),rgba(31,58,54,.4))"></div>\n  '
            % (arq, pos))


S = [
    slide(1, '''<p class="cab" style="left:96px;top:190px;width:700px">Por que a fairhealth existe?</p>
  <p class="txt" style="left:96px;top:350px;width:640px">%s</p>
  <img src="../../marca/fotos-banco/pexels/corredor-hospital.jpg" alt="Corredor de hospital" style="left:96px;top:650px;width:430px;height:400px">
  <img src="../../marca/fotos-banco/pexels/sala-reuniao-empresa.jpg" alt="Sala de reunião de uma empresa" style="left:554px;top:600px;width:430px;height:400px">
  <p class="nota" style="left:96px;top:1066px">2009, no hospital</p>
  <p class="nota" style="left:554px;top:1016px">hoje, nas empresas</p>''' % T1),
    slide(2, '''<p class="txt" style="left:96px;top:200px;width:888px">%s</p>
  <p class="txt2" style="left:96px;top:400px;width:888px">%s</p>
  <p class="num" style="left:330px;top:890px">01</p>
  <p class="nota" style="left:330px;top:1030px">2009</p>''' % (T2, A2)),
    slide(3, '''<p class="num" style="left:330px;top:290px">02</p>
  <p class="nota" style="left:330px;top:430px">no hospital</p>
  <p class="txt" style="left:400px;top:650px;width:584px">%s</p>
  <p class="txt2" style="left:400px;top:940px;width:584px">%s</p>''' % (T3, A3)),
    slide(4, CORPO4, sid='k4a', foto=foto('sala-atendimento-e-espera', '78% 60%')),
    slide(4, CORPO4, sid='k4b', foto=foto('copa-parede-verde', '55% 70%')),
    slide(4, CORPO4, sid='k4c', foto=foto('recepcao-parede-pedra-larga', '48% 80%')),
    slide(5, '''<p class="txt" style="left:96px;top:200px;width:888px;font-size:44px;line-height:56px">%s</p>
  <p class="txt2" style="left:96px;top:350px;width:888px">%s</p>
  <p class="nota" style="left:450px;top:800px">sem pressa e sem julgamento</p>
  <p class="num" style="left:630px;top:990px">04</p>''' % (T5, A5)),
    slide(6, '''<p class="txt" style="left:96px;top:200px;width:888px;font-size:48px;line-height:60px">%s</p>
  <ul class="lista" style="left:96px;top:330px;width:860px">%s</ul>
  <p class="num" style="left:330px;top:770px">05</p>''' % (T6, ''.join('<li>%s</li>' % t for t in I6))),
    slide(7, '''<p class="txt" style="left:96px;top:200px;width:640px;font-size:44px;line-height:56px">%s</p>
  <p class="txt2" style="left:96px;top:400px;width:640px">%s</p>
  <p class="num" style="left:430px;top:940px">06</p>
  <p class="nota" style="left:430px;top:1080px">dentro da empresa</p>''' % (T7, A7)),
    slide(8, '''<p class="nota" style="left:384px;top:200px;width:600px;text-align:right">a gente tá aqui pra te ouvir</p>
  <p class="cab" style="left:284px;top:250px;width:700px;text-align:right">%s</p>
  <p class="txt2" style="left:284px;top:430px;width:700px;text-align:right">%s %s</p>
  <p class="num" style="left:330px;top:650px">07</p>
  <img src="%s" alt="fairhealth" style="left:%dpx;top:%dpx;width:108px;height:108px">
  <p class="nota" style="left:384px;top:1020px;width:600px;text-align:right">conheça a fairhealth no link da bio</p>''' % (F8, T8, A8, LOGO, LOGO_C[0] - 7 * W - 54, LOGO_C[1] - 54)),
]


def html():
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (H2G)</title><style>' + CSS + '</style></head><body%s>\n'
           % (' class="fundo"' if FUNDO else '')]
    for sid, cls, corpo in S:
        out.append('<section class="slide %s" id="%s">\n  %s\n</section>\n' % (cls, sid, corpo))
    out.append('</body></html>\n')
    return ''.join(out)


open(sys.argv[2] if FUNDO else sys.argv[1], 'w').write(html())
print('ok', len(S))
