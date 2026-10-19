# Arte v4 (19/10) do post de qua 21/10, "Por que a fairhealth existe?", conteúdo v3 (README.md desta pasta).
# Recomeço a pedido da Nina: "tire todos esses personagens, faça algo mais chique e elegante, foque mais no Tiffany
# que no creme". A inspiração é o carrossel de processo de trabalho que ela mandou:
#   - fundo único em papel com textura (aqui, Tiffany em todos os slides);
#   - uma linha fina e lisa que atravessa os slides, com curvas e um laço, e bolinhas nos marcos;
#   - números grandes ao lado das bolinhas (aqui, "2009" e "hoje");
#   - blocos de texto grandes, soltos de um lado e da linha do outro;
#   - anotações curtas perto da linha;
#   - cabeçalho e rodapé discretos, em creme, e uma seta fina no canto.
# Sem desenhos e sem personagens. Só Raleway. As versões v1 a v3 ficam guardadas.
# Uso: python3 gerar_slides_v4.py slides-v4.html && node ../../ferramentas/render.mjs slides-v4.html png-v4
import sys

SAIDA = sys.argv[1]
N = 7
W = 1080

CSS = r'''
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:400;font-style:italic;src:url(../../marca/fontes/raleway-latin-400-italic.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--tif:#96C5BD;--verde:#1F3A36;--creme:#F0F0E9;--tclaro:#BFE0D9;--vlogo:#2F6B64}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#888;display:flex;flex-wrap:wrap;gap:40px;padding:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-variant-numeric:lining-nums;background:var(--tif);color:var(--verde)}
.slide>*{position:absolute}
.papel{inset:0;opacity:.4;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='360'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .55 0 0 0 0 .52 0 0 0 -1.1 .85'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"),
    repeating-linear-gradient(0deg,rgba(31,58,54,.045) 0 1px,transparent 1px 4px),
    repeating-linear-gradient(90deg,rgba(31,58,54,.035) 0 1px,transparent 1px 4px)}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.k{font-weight:800;font-style:italic}
.topo{top:96px;font-size:24px;line-height:30px;font-weight:800;color:var(--creme)}
.rodape{left:96px;top:1236px;font-size:24px;line-height:30px;font-weight:800;color:var(--creme)}
.rodape span{font-weight:400}
.tit{font-size:66px;line-height:76px;letter-spacing:-0.01em}
.corpo{font-size:36px;line-height:48px}
.num{font-size:150px;line-height:150px;font-weight:800;letter-spacing:-0.03em;color:var(--creme)}
.marco{font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.anota{font-size:30px;line-height:38px;font-style:italic}
'''

# A linha: pontos por onde ela passa, em coordenadas do carrossel inteiro (7 × 1080 de largura). A curva passa por
# todos (Catmull-Rom convertida em Bézier cúbica), lisa.
PONTOS = [
    (200, 800),                                                    # 1 · começo (bolinha)
    (420, 900), (600, 935), (760, 900), (820, 800), (740, 715), (650, 760), (665, 880), (820, 960), (1080, 980),  # 1 · laço
    (1320, 800),                                                   # 2 · bolinha de 2009
    (1700, 1060), (2160, 1000),
    (2560, 1060), (2800, 1000),                                    # 3 · bolinha da essência
    (3060, 820), (3160, 580), (3240, 440),
    (3440, 430), (3600, 400), (3650, 320), (3580, 260), (3510, 310), (3540, 390), (3660, 440),  # 4 · laço da conversa
    (3880, 470), (4060, 540),                                      # 4 · bolinha do acolhimento
    (4200, 640), (4320, 700),
    (4500, 860), (4620, 1000), (4840, 1040),                       # 5 · bolinha da evolução
    (5120, 960), (5400, 760),
    (5600, 800),                                                   # 6 · bolinha de hoje
    (5920, 1000), (6220, 1080), (6480, 1050),
    (6730, 1065), (6920, 1000), (6975, 975),                       # 7 · chega ao logo
]
BOLAS = [PONTOS[0], PONTOS[10], PONTOS[14], PONTOS[26], PONTOS[31], PONTOS[34]]
LOGO = (7030, 950)
R_LOGO = 72


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


def linha(k):
    bolas = ''.join('<circle cx="%d" cy="%d" r="12" fill="#1F3A36"/>' % b for b in BOLAS)
    return ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#1F3A36" '
            'stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>%s</svg>') % ((k - 1) * W, LINHA, bolas)


SETA = ('<svg aria-hidden="true" style="left:864px;top:1236px;width:120px;height:30px" viewBox="0 0 120 30">'
        '<path d="M0 15H116M104 4L117 15L104 26" fill="none" stroke="#F0F0E9" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

S = []
# 1 · capa
S.append(('t01', 'capa: a história começa num hospital; a linha nasce numa bolinha e faz um laço', '''<p class="tit" style="left:96px;top:220px;width:860px;font-size:76px;line-height:86px">Antes de chegar às empresas, nossa história começou <span class="k">em um hospital</span>.</p>
  <p class="anota" style="left:236px;top:700px">de 2009 até hoje</p>'''))
# 2 · 2009, no hospital
S.append(('t02', '2009, no hospital: o Escritório do Paciente', '''<p class="tit" style="left:96px;top:190px;width:888px;font-size:58px;line-height:68px">Dentro de um hospital, surgiu o <span class="k">Escritório do Paciente</span>.</p>
  <p class="corpo" style="left:96px;top:360px;width:888px;font-size:34px;line-height:46px">Um modelo de cuidado criado para trazer o paciente de volta ao centro, com a escuta, o acolhimento e as necessidades de cada pessoa em primeiro lugar.</p>
  <p class="num" style="left:272px;top:690px">2009</p>
  <p class="anota" style="left:672px;top:792px">onde tudo começou</p>'''))
# 3 · a essência: texto à esquerda; a linha sobe pela direita
S.append(('t03', 'a essência: a pessoa por trás de cada atendimento', '''<p class="tit" style="left:96px;top:190px;width:640px;font-size:60px;line-height:70px">Por trás de cada atendimento, existe <span class="k">uma pessoa</span>.</p>
  <p class="corpo" style="left:96px;top:440px;width:620px">Com a sua própria história, hábitos, necessidades e prioridades.</p>
  <p class="corpo" style="left:96px;top:620px;width:620px">Por isso, escutar sempre foi parte essencial da nossa maneira de cuidar.</p>
  <p class="marco" style="left:600px;top:1050px">A essência</p>'''))
# 4 · o acolhimento: a linha faz o laço em cima; texto embaixo, à esquerda
S.append(('t04', 'o acolhimento: antes de qualquer exame, uma conversa; o laço da conversa', '''<p class="anota" style="left:470px;top:236px">o que é importante para você?</p>
  <p class="marco" style="left:560px;top:578px">O acolhimento</p>
  <p class="tit" style="left:96px;top:720px;width:760px;font-size:60px;line-height:70px">Antes de qualquer exame, <span class="k">uma conversa</span>.</p>
  <p class="corpo" style="left:96px;top:890px;width:760px">Um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado.</p>'''))
# 5 · evolução: texto em cima, à direita; a linha desce e volta a subir
S.append(('t05', 'evolução: o conceito chega ao trabalho', '''<p class="tit" style="left:360px;top:190px;width:624px;font-size:60px;line-height:70px">Com o tempo, essa forma de cuidar <span class="k">evoluiu</span>.</p>
  <p class="corpo" style="left:360px;top:420px;width:624px">E o conceito chegou a um lugar que faz parte da rotina das pessoas: <b style="font-weight:800">o trabalho</b>. Porque, quando o cuidado está perto, ele acontece.</p>
  <p class="marco" style="left:440px;top:1086px">Evolução</p>'''))
# 6 · hoje, nas empresas
S.append(('t06', 'hoje, nas empresas: o Escritório do Cuidado', '''<p class="tit" style="left:96px;top:190px;width:888px;font-size:58px;line-height:68px">Assim surgiu o <span class="k">Escritório do Cuidado</span>, da fairhealth.</p>
  <p class="corpo" style="left:96px;top:360px;width:888px;font-size:34px;line-height:46px">Um projeto novo, inspirado no Escritório do Paciente e pensado para as empresas: um espaço de acolhimento e de medicina preventiva, com cuidado individualizado e acompanhamento.</p>
  <p class="num" style="left:252px;top:690px">hoje</p>
  <p class="anota" style="left:596px;top:770px">perto da rotina das pessoas</p>'''))
# 7 · o propósito: texto à direita, alinhado à direita; a linha termina no logo
S.append(('t07', 'o propósito: os lugares mudaram, a essência permanece; a linha termina no logo', '''<p class="anota" style="left:300px;top:250px;width:684px;text-align:right">a gente tá aqui pra te ouvir</p>
  <p class="tit" style="left:244px;top:320px;width:740px;font-size:62px;line-height:72px;text-align:right">Os lugares mudaram. <span class="k">A essência do cuidado permanece.</span></p>
  <p class="corpo" style="left:304px;top:570px;width:680px;text-align:right">Do hospital às empresas, seguimos com um mesmo princípio: <b style="font-weight:800">o cuidado começa pela pessoa.</b></p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><circle cx="%d" cy="%d" r="%d" fill="#F0F0E9" stroke="#1F3A36" stroke-width="3"/></svg>
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:%dpx;top:%dpx;width:120px;height:120px">''' % (
    LOGO[0] - 6 * W, LOGO[1], R_LOGO, LOGO[0] - 6 * W - 60, LOGO[1] - 60)))


def html(slides):
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (v4)</title><style>'
           + CSS + '</style></head><body>\n']
    for k, (sid, nota, corpo) in enumerate(slides, 1):
        topo = ('<p class="topo" style="left:96px">@fairhealth.br</p>\n  '
                '<p class="topo" style="right:96px;font-weight:400">nossa história</p>')
        rodape = '<p class="rodape">fairhealth <span>| o cuidado começa pela pessoa</span></p>'
        fim = '\n  ' + rodape + ('\n  ' + SETA if k < N else '')
        out.append('<!-- %d · %s -->\n<section class="slide" id="%s">\n  <div class="papel"></div>\n  %s\n  %s\n  %s%s\n</section>\n\n'
                   % (k, nota, sid, linha(k), topo, corpo, fim))
    out.append('</body></html>\n')
    return ''.join(out)


open(SAIDA, 'w').write(html(S))
print('ok', len(S))
