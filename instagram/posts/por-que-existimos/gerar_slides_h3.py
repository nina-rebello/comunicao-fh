# Versão H3 (19/10, teste): a H2 com elementos no estilo da referência que a Nina mandou (carrossel de terapia em
# grupo, com faixas onduladas grossas, estrelinhas, marca-texto, uma cabeça de perfil com uma explosão de estrelas e
# etiquetas em pílula). Tudo nas cores da marca, sem amarelo:
#   - faixa ondulada grossa saindo pela borda (capa e slide 7);
#   - estrelinhas espalhadas;
#   - marca-texto nas palavras de destaque (Tiffany no creme, creme no Tiffany);
#   - slide 5 (a pergunta): cabeça de perfil em verde com uma explosão de estrelas e bolinhas;
#   - slide 6 (o que levamos): os três itens em etiquetas de pílula, como na referência.
# A H2 (gerar_slides_h2.py) fica guardada.
# Uso: python3 gerar_slides_h3.py slides-h3.html && node ../../ferramentas/render.mjs slides-h3.html png-h3
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
# Uso: python3 gerar_slides_h2.py slides-h2.html && node ../../ferramentas/render.mjs slides-h2.html png-h2
#      python3 gerar_slides_h2.py --fundo slides-h2-fundo.html (sem os textos e o logo, para o fundo do Canva)
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
.k{font-weight:800;font-style:italic;color:var(--vlogo);background:linear-gradient(transparent 58%,rgba(150,197,189,.75) 58%,rgba(150,197,189,.75) 92%,transparent 92%);-webkit-box-decoration-break:clone;box-decoration-break:clone;padding:0 4px}
.T .k{color:var(--verde);background:linear-gradient(transparent 58%,rgba(240,240,233,.7) 58%,rgba(240,240,233,.7) 92%,transparent 92%)}
.pil{display:flex;align-items:center;gap:0}
.pil b{flex:none;height:66px;line-height:66px;padding:0 30px;border-radius:33px;font-size:22px;font-weight:800;letter-spacing:.1em;text-transform:uppercase}
.pil span{flex:1;margin-left:-33px;padding:12px 30px 12px 58px;border:2.5px solid var(--verde);border-radius:40px;font-size:30px;line-height:40px;min-height:66px;display:flex;align-items:center}
.papel{inset:0;opacity:.55;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='360'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .55 0 0 0 0 .53 0 0 0 0 .48 0 0 0 -1.1 .85'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"),
    repeating-linear-gradient(0deg,rgba(31,58,54,.04) 0 1px,transparent 1px 4px),
    repeating-linear-gradient(90deg,rgba(31,58,54,.035) 0 1px,transparent 1px 4px)}
.T .papel{opacity:.4}
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


import math


def estrela(cx, cy, r, cor, giro=0):
    pts = []
    for i in range(10):
        a = math.radians(giro - 90 + i * 36)
        rr = r if i % 2 == 0 else r * .45
        pts.append('%.1f,%.1f' % (cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return '<polygon points="%s" fill="%s" stroke="%s" stroke-width="%.1f" stroke-linejoin="round"/>' % (' '.join(pts), cor, cor, r * .12)


def faixa(pontos, cor, larg=34):
    return '<path d="%s" fill="none" stroke="%s" stroke-width="%d" stroke-linecap="round" stroke-linejoin="round"/>' % (caminho(pontos), cor, larg)


CABECA = ('M120 360C122 318 104 296 84 268C44 214 40 130 84 78C126 26 214 14 258 66C280 92 286 120 282 146L306 190C311 199 305 205 292 207'
          'L291 222C299 228 297 236 288 240C294 249 292 258 280 262C265 268 249 268 240 278L238 318C238 336 244 350 250 360Z')


def cabeca(x, y, esc):
    # cabeça de perfil (olhando para a direita) com uma explosão de estrelas e bolinhas no lugar do pensamento
    s = '<g transform="translate(%d %d) scale(%.3f)"><path d="%s" fill="#1F3A36"/>' % (x, y, esc, CABECA)
    for cx, cy, r, cor, g in [(160, 120, 34, '#F0F0E9', 10), (112, 150, 22, '#96C5BD', -14), (206, 92, 20, '#96C5BD', 20), (190, 160, 16, '#F0F0E9', 0),
                              (128, 96, 14, '#F0F0E9', 30), (236, 136, 12, '#F0F0E9', -8), (150, 186, 11, '#96C5BD', 12), (90, 118, 10, '#F0F0E9', 0)]:
        s += estrela(cx, cy, r, cor, g)
    for cx, cy, r, cor in [(178, 64, 6, '#F0F0E9'), (96, 186, 5, '#96C5BD'), (244, 104, 5, '#F0F0E9'), (134, 210, 4, '#F0F0E9'), (220, 186, 5, '#96C5BD')]:
        s += '<circle cx="%d" cy="%d" r="%d" fill="%s"/>' % (cx, cy, r, cor)
    return s + '</g>'


DECOR = {
    1: faixa([(1130, 140), (1010, 230), (1050, 340), (960, 440), (1020, 540), (1130, 600)], '#F0F0E9')
       + estrela(220, 610, 22, '#F0F0E9', 12) + estrela(1000, 760, 15, '#1F3A36', -10) + estrela(150, 700, 11, '#F0F0E9', 25),
    2: estrela(900, 560, 20, '#96C5BD', 8) + estrela(980, 640, 12, '#2F6B64', -12) + estrela(160, 1180, 14, '#96C5BD', 20),
    3: estrela(160, 560, 22, '#F0F0E9', -6) + estrela(240, 620, 12, '#1F3A36', 14) + estrela(920, 1150, 16, '#F0F0E9', 0),
    4: estrela(900, 600, 18, '#96C5BD', 10) + estrela(160, 1150, 22, '#96C5BD', -8) + estrela(230, 1100, 11, '#2F6B64', 18),
    5: cabeca(660, 560, 1.05) + estrela(620, 600, 14, '#F0F0E9', 0) + estrela(1010, 610, 18, '#F0F0E9', 15),
    6: estrela(900, 860, 20, '#96C5BD', -10) + estrela(980, 800, 12, '#2F6B64', 6),
    7: faixa([(1130, 170), (990, 250), (1040, 350), (960, 420), (1130, 470)], '#F0F0E9') + estrela(860, 300, 16, '#F0F0E9', 18) + estrela(120, 1150, 14, '#F0F0E9', 0),
    8: estrela(560, 1080, 18, '#96C5BD', 8) + estrela(1010, 1060, 14, '#2F6B64', -12) + estrela(620, 1170, 10, '#96C5BD', 30),
}


def slide(k, corpo):
    t = k in TIFFANY
    cor = '#1F3A36' if t else '#2F6B64'
    linha = ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round"/>%s'
             '<circle cx="%d" cy="%d" r="64" fill="#F0F0E9" stroke="%s" stroke-width="3"/></svg>'
             % ((k - 1) * W, LINHA, cor, ''.join('<circle cx="%d" cy="%d" r="12" fill="%s"/>' % (b + (cor,)) for b in BOLAS), LOGO_C[0], LOGO_C[1], cor))
    seta = ('<svg aria-hidden="true" style="left:864px;top:1236px;width:120px;height:30px" viewBox="0 0 120 30"><path d="M0 15H116M104 4L117 15L104 26" fill="none" '
            'stroke="%s" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>' % ('#F0F0E9' if t else '#96C5BD')) if k < N else ''
    linha += '\n  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">%s</svg>' % DECOR.get(k, '')
    return ('k%d' % k, 'T' if t else 'C', '<div class="papel"></div>\n  %s\n  <p class="topo" style="left:96px">@fairhealth.br</p>\n  <p class="topo" style="right:96px;font-weight:400">nossa história</p>\n  %s\n  <p class="rod">fairhealth <span>| o cuidado começa pela pessoa</span></p>%s'
            % (linha, corpo, ('\n  ' + seta) if seta else ''))


S = [
    slide(1, '''<p class="cab" style="left:96px;top:190px;width:700px">Por que a fairhealth existe?</p>
  <p class="txt" style="left:96px;top:350px;width:640px">%s</p>
  <p class="nota" style="left:190px;top:1110px">2009 → hoje</p>
  <img src="../../marca/ilustracoes/capa-mao-hospital.png" alt="Uma mão segurando um pequeno hospital" style="left:260px;top:560px;width:820px;height:500px">''' % T1),
    slide(2, '''<p class="txt" style="left:96px;top:200px;width:888px">%s</p>
  <p class="txt2" style="left:96px;top:400px;width:888px">%s</p>
  <p class="num" style="left:330px;top:890px">01</p>
  <p class="nota" style="left:330px;top:1030px">2009</p>''' % (T2, A2)),
    slide(3, '''<p class="num" style="left:330px;top:290px">02</p>
  <p class="nota" style="left:330px;top:430px">no hospital</p>
  <p class="txt" style="left:400px;top:650px;width:584px">%s</p>
  <p class="txt2" style="left:400px;top:940px;width:584px">%s</p>''' % (T3, A3)),
    slide(4, '''<p class="txt" style="left:96px;top:200px;width:888px;font-size:48px;line-height:60px">%s</p>
  <p class="txt2" style="left:96px;top:350px;width:888px">%s</p>
  <p class="num" style="left:510px;top:790px">03</p>
  <p class="nota" style="left:620px;top:812px">hoje, nas empresas</p>''' % (T4, A4)),
    slide(5, '''<p class="txt" style="left:96px;top:200px;width:888px;font-size:44px;line-height:56px">%s</p>
  <p class="txt2" style="left:96px;top:350px;width:888px">%s</p>
  <p class="nota" style="left:96px;top:600px">sem pressa e sem julgamento</p>
  <p class="num" style="left:630px;top:990px">04</p>''' % (T5, A5)),
    slide(6, '''<p class="txt" style="left:96px;top:200px;width:888px;font-size:48px;line-height:60px">%s</p>
  <div style="left:96px;top:340px;width:888px">%s</div>
  <p class="num" style="left:330px;top:770px">05</p>''' % (T6, ''.join(
        '<div class="pil" style="margin-top:%dpx"><b style="background:%s;color:%s">%s</b><span>%s</span></div>' % (0 if i == 0 else 22, bg, fg, et, tx)
        for i, (bg, fg, et, tx) in enumerate([('#96C5BD', '#1F3A36', 'Atendimento', 'médico e psicológico'),
                                              ('#1F3A36', '#F0F0E9', 'Planos de cuidado', 'individualizados, baseados na Medicina do Estilo de Vida'),
                                              ('#2F6B64', '#F0F0E9', 'Tecnologia', 'humanização e cuidado verdadeiro')])))),
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
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (H3, teste)</title><style>' + CSS + '</style></head><body%s>\n'
           % (' class="fundo"' if FUNDO else '')]
    for sid, cls, corpo in S:
        out.append('<section class="slide %s" id="%s">\n  %s\n</section>\n' % (cls, sid, corpo))
    out.append('</body></html>\n')
    return ''.join(out)


open(sys.argv[2] if FUNDO else sys.argv[1], 'w').write(html())
print('ok', len(S))
