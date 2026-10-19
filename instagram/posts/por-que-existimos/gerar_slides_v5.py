# Arte v5 (19/10) do post de qua 21/10, "Por que a fairhealth existe?", com o conteúdo final da Nina (README.md,
# conteúdo v6): foco no Escritório do Cuidado, "desenvolvemos" no lugar de "surgiu", 8 slides.
# Duplicada da v4 (gerar_slides_v4.py, que fica guardada), no mesmo estilo:
#   - fundo Tiffany com textura de papel;
#   - linha fina e lisa que atravessa os slides, com laços e bolinhas;
#   - números grandes em creme ("2009" e "hoje");
#   - textos grandes de um lado da linha;
#   - anotações curtas;
#   - cabeçalho e rodapé em creme.
# Novo: no slide 6, os três itens do que levamos para a empresa ficam em bolinhas ao longo da linha. O cabeçalho
# leva "por que a fairhealth existe?".
# Uso: python3 gerar_slides_v5.py slides-v5.html && node ../../ferramentas/render.mjs slides-v5.html png-v5
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

# A linha: pontos por onde ela passa, em coordenadas do carrossel inteiro (8 × 1080 de largura). A curva passa por
# todos (Catmull-Rom convertida em Bézier cúbica), lisa.
PONTOS = [
    (200, 800),                                                    # 1 · começo (bolinha)
    (420, 900), (600, 935), (760, 900), (820, 800), (740, 715), (650, 760), (665, 880), (820, 960), (1080, 980),  # 1 · laço
    (1320, 800),                                                   # 2 · bolinha de 2009
    (1700, 1060), (2160, 1000),
    (2560, 1060), (2800, 1000),                                    # 3 · bolinha do hospital
    (3060, 820), (3160, 580), (3240, 440),
    (3540, 440),                                                   # 4 · bolinha de hoje
    (3720, 600), (4040, 640), (4220, 760), (4320, 900),
    (4520, 910), (4680, 940), (4730, 1020), (4660, 1080), (4590, 1030), (4620, 950), (4740, 900),  # 5 · laço da conversa
    (4960, 1040),                                                  # 5 · bolinha do acolhimento
    (5220, 820), (5340, 560), (5400, 420),
    (5520, 460), (5580, 520), (5580, 720), (5580, 920),            # 6 · as três bolinhas do que levamos
    (5700, 1060), (6100, 1090), (6480, 1000),
    (6800, 1040), (7000, 1060), (7300, 1040), (7560, 1060),        # 7 · bolinha de perto
    (7810, 1070), (7960, 1030), (8030, 995),                       # 8 · chega ao logo
]
BOLAS = [(200, 800), (1320, 800), (2800, 1000), (3540, 440), (4960, 1040), (5580, 520), (5580, 720), (5580, 920), (7000, 1060)]
LOGO = (8100, 990)
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
S.append(('u01', 'capa: a história começa num hospital; a linha nasce numa bolinha e faz um laço', '''<p class="tit" style="left:96px;top:220px;width:860px;font-size:76px;line-height:86px">Antes de chegar às empresas, nossa história começou <span class="k">em um hospital</span>.</p>
  <p class="anota" style="left:236px;top:700px">2009 → hoje</p>'''))
# 2 · há quase 20 anos
S.append(('u02', 'há quase 20 anos: os pacientes distantes do centro do cuidado', '''<p class="tit" style="left:96px;top:190px;width:888px;font-size:58px;line-height:68px">Há quase 20 anos, percebemos que os pacientes estavam <span class="k">cada vez mais distantes do centro do cuidado</span>.</p>
  <p class="corpo" style="left:96px;top:510px;width:888px">Era preciso mudar essa realidade.</p>
  <p class="num" style="left:272px;top:690px">2009</p>'''))
# 3 · no hospital: texto à esquerda; a linha sobe pela direita
S.append(('u03', 'no hospital: desenvolvemos o Escritório do Paciente; o conceito vai para as empresas', '''<p class="tit" style="left:96px;top:190px;width:660px;font-size:56px;line-height:66px">Assim, dentro de um hospital, desenvolvemos o <span class="k">Escritório do Paciente</span> para mudar essa realidade.</p>
  <p class="corpo" style="left:96px;top:560px;width:640px">Com o tempo, levamos esse conceito para as empresas.</p>
  <p class="marco" style="left:600px;top:1050px">No hospital</p>'''))
# 4 · hoje: o Escritório do Cuidado; "hoje" em cima, texto embaixo
S.append(('u04', 'hoje, nas empresas: desenvolvemos o Escritório do Cuidado', '''<p class="num" style="left:340px;top:330px">hoje</p>
  <p class="anota" style="left:690px;top:420px">nas empresas</p>
  <p class="tit" style="left:96px;top:720px;width:760px;font-size:60px;line-height:70px">Assim, desenvolvemos o <span class="k">Escritório do Cuidado</span>.</p>
  <p class="corpo" style="left:96px;top:890px;width:760px">Um espaço de acolhimento e de medicina preventiva dentro da empresa, que fortalece o cuidado centrado na pessoa.</p>'''))
# 5 · o acolhimento: texto à esquerda, em cima; a linha faz o laço embaixo e sobe pela direita
S.append(('u05', 'o acolhimento: tudo começa com uma pergunta; o laço da conversa', '''<p class="tit" style="left:96px;top:190px;width:720px;font-size:60px;line-height:70px">Tudo começa com uma pergunta: <span class="k">o que é importante para você?</span></p>
  <p class="corpo" style="left:96px;top:500px;width:700px">Antes de qualquer exame, vem uma conversa: um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado.</p>
  <p class="marco" style="left:560px;top:1090px">O acolhimento</p>'''))
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
  <p class="anota" style="left:560px;top:960px">dentro da empresa</p>'''))
# 8 · o propósito: texto à direita, alinhado à direita; a linha termina no logo
S.append(('u08', 'o propósito; faça o certo pelos motivos certos; a linha termina no logo', '''<p class="anota" style="left:300px;top:230px;width:684px;text-align:right">faça o certo pelos motivos certos</p>
  <p class="tit" style="left:204px;top:300px;width:780px;font-size:58px;line-height:68px;text-align:right">Nosso propósito é promover <span class="k">qualidade de vida, engajamento e um ambiente de trabalho mais saudável</span>.</p>
  <p class="corpo" style="left:304px;top:670px;width:680px;text-align:right">Com resultados demonstrados por indicadores.</p>
  <p class="anota" style="left:240px;top:1086px;width:600px;text-align:center">conheça a fairhealth no link da bio</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><circle cx="%d" cy="%d" r="%d" fill="#F0F0E9" stroke="#1F3A36" stroke-width="3"/></svg>
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:%dpx;top:%dpx;width:120px;height:120px">''' % (
    LOGO[0] - 7 * W, LOGO[1], R_LOGO, LOGO[0] - 7 * W - 60, LOGO[1] - 60)))


def html(slides):
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (v5)</title><style>'
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
