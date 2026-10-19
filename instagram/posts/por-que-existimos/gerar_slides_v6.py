# Arte v6 (19/10) do post de qua 21/10, duplicada da v5 (gerar_slides_v5.py, que fica guardada). Mesmo conteúdo (v6
# do README) e mesmo estilo. Pedido da Nina: "essas linhas, faça elas sem parecer rabisco, faça linhas retas".
#   - A linha passa a ser feita só de trechos retos, horizontais e verticais, com cantos levemente arredondados.
#   - Saem os laços. As bolinhas, o "2009", o "hoje" e os textos continuam, com a posição ajustada à linha nova.
# Uso: python3 gerar_slides_v6.py slides-v6.html && node ../../ferramentas/render.mjs slides-v6.html png-v6
import sys

SAIDA = sys.argv[1]
N = 8
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
.item{font-size:36px;line-height:46px}
.marco{font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.anota{font-size:30px;line-height:38px;font-style:italic}
'''

# A linha: os cantos por onde ela passa, em coordenadas do carrossel inteiro (8 × 1080 de largura). Entre um canto e
# outro, a linha é reta (só horizontal ou vertical); os cantos levam um arredondamento pequeno (RAIO).
PONTOS = [
    (200, 880), (700, 880), (700, 1000),                           # 1 · começa na bolinha e desce um degrau
    (3060, 1000), (3060, 440),                                     # 2 e 3 · reta embaixo; no 3, sobe pela direita
    (3540, 440), (3540, 640), (4200, 640), (4200, 1100),           # 4 · bolinha de hoje no canto; desce pela direita
    (5220, 1100), (5220, 420),                                     # 5 · reta embaixo; sobe pela direita
    (5580, 420), (5580, 1060),                                     # 6 · desce pelas três bolinhas
    (8028, 1060),                                                  # 7 e 8 · reta embaixo até o logo
]
RAIO = 16
BOLAS = [(200, 880), (1320, 1000), (2800, 1000), (3540, 440), (4960, 1100), (5580, 520), (5580, 720), (5580, 920), (7000, 1060)]
LOGO = (8100, 1060)
R_LOGO = 72


def caminho(p):
    # retas entre os cantos; em cada canto, uma curva curta (quadrática) de raio RAIO
    d = 'M%.1f %.1f' % p[0]
    for i in range(1, len(p) - 1):
        (x0, y0), (x1, y1), (x2, y2) = p[i - 1], p[i], p[i + 1]
        ax, ay = x1 - (x1 > x0) * RAIO + (x1 < x0) * RAIO, y1 - (y1 > y0) * RAIO + (y1 < y0) * RAIO
        bx, by = x1 + (x2 > x1) * RAIO - (x2 < x1) * RAIO, y1 + (y2 > y1) * RAIO - (y2 < y1) * RAIO
        d += ' L%.1f %.1f Q%.1f %.1f %.1f %.1f' % (ax, ay, x1, y1, bx, by)
    d += ' L%.1f %.1f' % p[-1]
    return d


LINHA = caminho(PONTOS)


def linha(k):
    bolas = ''.join('<circle cx="%d" cy="%d" r="12" fill="#1F3A36"/>' % b for b in BOLAS)
    return ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#1F3A36" '
            'stroke-width="3" stroke-linecap="square" stroke-linejoin="miter"/>%s</svg>') % ((k - 1) * W, LINHA, bolas)


SETA = ('<svg aria-hidden="true" style="left:864px;top:1236px;width:120px;height:30px" viewBox="0 0 120 30">'
        '<path d="M0 15H116M104 4L117 15L104 26" fill="none" stroke="#F0F0E9" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

S = []
# 1 · capa
S.append(('u01', 'capa: a história começa num hospital; a linha nasce numa bolinha e faz um laço', '''<p class="tit" style="left:96px;top:220px;width:860px;font-size:76px;line-height:86px">Antes de chegar às empresas, nossa história começou <span class="k">em um hospital</span>.</p>
  <p class="anota" style="left:236px;top:806px">2009 → hoje</p>'''))
# 2 · há quase 20 anos
S.append(('u02', 'há quase 20 anos: os pacientes distantes do centro do cuidado', '''<p class="tit" style="left:96px;top:190px;width:888px;font-size:58px;line-height:68px">Há quase 20 anos, percebemos que os pacientes estavam <span class="k">cada vez mais distantes do centro do cuidado</span>.</p>
  <p class="corpo" style="left:96px;top:510px;width:888px">Era preciso mudar essa realidade.</p>
  <p class="num" style="left:272px;top:826px">2009</p>'''))
# 3 · no hospital: texto à esquerda; a linha sobe pela direita
S.append(('u03', 'no hospital: desenvolvemos o Escritório do Paciente; o conceito vai para as empresas', '''<p class="tit" style="left:96px;top:190px;width:660px;font-size:56px;line-height:66px">Assim, dentro de um hospital, desenvolvemos o <span class="k">Escritório do Paciente</span> para mudar essa realidade.</p>
  <p class="corpo" style="left:96px;top:560px;width:640px">Com o tempo, levamos esse conceito para as empresas.</p>
  <p class="marco" style="left:600px;top:1050px">No hospital</p>'''))
# 4 · hoje: o Escritório do Cuidado; "hoje" em cima, texto embaixo
S.append(('u04', 'hoje, nas empresas: desenvolvemos o Escritório do Cuidado', '''<p class="num" style="left:340px;top:300px">hoje</p>
  <p class="anota" style="left:690px;top:394px">nas empresas</p>
  <p class="tit" style="left:96px;top:720px;width:760px;font-size:60px;line-height:70px">Assim, desenvolvemos o <span class="k">Escritório do Cuidado</span>.</p>
  <p class="corpo" style="left:96px;top:890px;width:760px">Um espaço de acolhimento e de medicina preventiva dentro da empresa, que fortalece o cuidado centrado na pessoa.</p>'''))
# 5 · o acolhimento: texto à esquerda, em cima; a linha faz o laço embaixo e sobe pela direita
S.append(('u05', 'o acolhimento: tudo começa com uma pergunta; o laço da conversa', '''<p class="tit" style="left:96px;top:190px;width:720px;font-size:60px;line-height:70px">Tudo começa com uma pergunta: <span class="k">o que é importante para você?</span></p>
  <p class="corpo" style="left:96px;top:500px;width:700px">Antes de qualquer exame, vem uma conversa: um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado.</p>
  <p class="marco" style="left:560px;top:1140px">O acolhimento</p>'''))
# 6 · o que levamos: três bolinhas na linha, uma por item
ITENS = [(520, '<b style="font-weight:800">atendimento</b> médico e psicológico'),
         (720, '<b style="font-weight:800">planos de cuidado individualizados</b>, baseados na Medicina do Estilo de Vida'),
         (920, '<b style="font-weight:800">tecnologia</b>, humanização e cuidado verdadeiro')]
itens = ''.join('<p class="item" style="left:230px;top:%dpx;width:720px">%s</p>\n  ' % (y - 24, t) for y, t in ITENS)
S.append(('u06', 'o que levamos: atendimento, planos de cuidado, tecnologia e humanização', '''<p class="tit" style="left:96px;top:190px;width:888px;font-size:60px;line-height:70px">Levamos ao <span class="k">coração da sua empresa</span>:</p>
  ''' + itens))
# 7 · perto
S.append(('u07', 'perto: quando o cuidado está perto, ele acontece', '''<p class="tit" style="left:96px;top:190px;width:888px;font-size:64px;line-height:74px">Porque, quando o cuidado está perto, <span class="k">ele acontece</span>.</p>
  <p class="corpo" style="left:96px;top:440px;width:888px">A maior barreira ao cuidado é tempo e acesso. Por isso, o Escritório do Cuidado fica dentro da empresa, perto da rotina de quem trabalha.</p>
  <p class="anota" style="left:560px;top:990px">dentro da empresa</p>'''))
# 8 · o propósito: texto à direita, alinhado à direita; a linha termina no logo
S.append(('u08', 'o propósito; faça o certo pelos motivos certos; a linha termina no logo', '''<p class="anota" style="left:300px;top:230px;width:684px;text-align:right">faça o certo pelos motivos certos</p>
  <p class="tit" style="left:204px;top:300px;width:780px;font-size:58px;line-height:68px;text-align:right">Nosso propósito é promover <span class="k">qualidade de vida, engajamento e um ambiente de trabalho mais saudável</span>.</p>
  <p class="corpo" style="left:304px;top:670px;width:680px;text-align:right">Com resultados demonstrados por indicadores.</p>
  <p class="anota" style="left:240px;top:1150px;width:600px;text-align:center">conheça a fairhealth no link da bio</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><circle cx="%d" cy="%d" r="%d" fill="#F0F0E9" stroke="#1F3A36" stroke-width="3"/></svg>
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:%dpx;top:%dpx;width:120px;height:120px">''' % (
    LOGO[0] - 7 * W, LOGO[1], R_LOGO, LOGO[0] - 7 * W - 60, LOGO[1] - 60)))


def html(slides):
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (v6)</title><style>'
           + CSS + '</style></head><body>\n']
    for k, (sid, nota, corpo) in enumerate(slides, 1):
        topo = ('<p class="topo" style="left:96px">@fairhealth.br</p>\n  '
                '<p class="topo" style="right:96px;font-weight:400">por que a fairhealth existe?</p>')
        rodape = '<p class="rodape">fairhealth <span>| o cuidado começa pela pessoa</span></p>'
        fim = '\n  ' + rodape + ('\n  ' + SETA if k < N else '')
        out.append('<!-- %d · %s -->\n<section class="slide" id="%s">\n  <div class="papel"></div>\n  %s\n  %s\n  %s%s\n</section>\n\n'
                   % (k, nota, sid, linha(k), topo, corpo, fim))
    out.append('</body></html>\n')
    return ''.join(out)


open(SAIDA, 'w').write(html(S))
print('ok', len(S))
