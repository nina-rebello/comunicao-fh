# Arte v7 (19/10) do post de qua 21/10, "Por que a fairhealth existe?", conteúdo v6 do README (o final da Nina).
# Referências novas da Nina:
#   - "Customer Journey Map" (Eleken): um caminho largo e liso, como uma estrada, que serpenteia de um slide para o
#     outro, com bolinhas nos marcos; título curto e forte e texto grande ao lado; cartões claros com listas; o nome
#     da marca embaixo; o número da página numa pílula em cima; uma barra de progresso no canto;
#   - "Life of a video editor", Silvio Santos (Grids) e "founders": linha limpa, bolinha que abre o caminho, curvas
#     abertas, nada de canto quadrado;
#   - "O poder da sua pausa" (nosso): curva lisa e regular.
# Pedido dela: "reta eu não quis dizer quadrada, só não queria aquele aspecto de rabisco torto". O caminho aqui é uma
# faixa larga, de espessura constante, com curvas suaves (poucos pontos, bem espaçados).
# Fundo Tiffany (foco no Tiffany), caminho creme, bolinhas verdes. Só Raleway. As versões anteriores ficam guardadas.
# Uso: python3 gerar_slides_v7.py slides-v7.html && node ../../ferramentas/render.mjs slides-v7.html png-v7
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
.papel{inset:0;opacity:.3;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='360'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .5 0 0 0 0 .55 0 0 0 0 .52 0 0 0 -1.1 .85'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.k{font-weight:800;font-style:italic}
.cab{font-size:84px;line-height:92px;font-weight:800;letter-spacing:-0.02em}
.num{font-size:120px;line-height:120px;font-weight:800;letter-spacing:-0.03em}
.par{font-size:40px;line-height:56px}
.par2{font-size:36px;line-height:50px}
.sub{font-size:26px;line-height:40px;letter-spacing:.1em;text-transform:uppercase}
.marca{font-size:34px;line-height:40px;font-weight:800;letter-spacing:-0.01em}
.pilula{right:72px;top:72px;height:52px;padding:0 22px;border-radius:26px;background:rgba(31,58,54,.78);color:var(--creme);font-size:24px;line-height:52px}
.prog{right:96px;top:1253px;width:120px;height:4px;border-radius:2px;background:rgba(240,240,233,.6)}
.prog i{position:absolute;left:0;top:0;height:4px;border-radius:2px;background:var(--verde)}
.cartao{left:96px;width:888px;border-radius:28px;background:rgba(240,240,233,.5);padding:40px 48px}
.cartao p{font-size:34px;line-height:46px;padding-left:30px;position:relative}
.cartao p+p{margin-top:22px}
.cartao p::before{content:'';position:absolute;left:0;top:19px;width:10px;height:10px;border-radius:50%;background:var(--verde)}
.anota{font-size:28px;line-height:36px;font-style:italic}
'''

# O caminho: pontos por onde ele passa, em coordenadas do carrossel inteiro (8 × 1080 de largura). Curva lisa
# (Catmull-Rom convertida em Bézier cúbica) e faixa de espessura constante.
PONTOS = [
    (110, 1140), (330, 1110), (520, 1000), (650, 840), (740, 650), (810, 480), (890, 390), (970, 400), (1010, 500), (995, 720), (1010, 910), (1080, 1030),  # 1 · nasce na bolinha e serpenteia pela direita
    (1340, 1090), (1560, 1010), (1780, 900), (1980, 950), (2160, 1060),                  # 2 · 2009
    (2460, 1110), (2720, 1060), (2980, 900), (3080, 700), (3120, 500), (3240, 380),     # 3 · sobe pela direita
    (3480, 300), (3720, 380), (3960, 470), (4160, 420), (4320, 330),                     # 4 · faixa em cima (hoje)
    (4480, 420), (4530, 640), (4490, 860), (4580, 1060), (4840, 1110), (5120, 1070), (5400, 1100),  # 5 · desce pela esquerda
    (5660, 1060), (5900, 1110), (6160, 1040), (6480, 1080),                              # 6
    (6780, 1000), (7020, 1060), (7280, 1130), (7560, 1050),                              # 7
    (7820, 1110), (8040, 1040), (8200, 985), (8300, 990),                                # 8 · chega ao logo
]
BOLAS = [(1780, 900), (2720, 1060), (3720, 380), (4840, 1110), (5900, 1110), (7020, 1060)]
INICIO = PONTOS[0]
LOGO = (8380, 1000)
FAIXA = 52


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
    bolas = ''.join('<circle cx="%d" cy="%d" r="24" fill="#1F3A36"/>' % b for b in BOLAS)
    bolas += '<circle cx="%d" cy="%d" r="30" fill="#1F3A36"/>' % INICIO
    bolas += '<circle cx="%d" cy="%d" r="84" fill="#F0F0E9"/>' % LOGO
    return ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#F0F0E9" '
            'stroke-width="%d" stroke-linecap="round" stroke-linejoin="round"/>%s</svg>') % ((k - 1) * W, CAMINHO, FAIXA, bolas)


S = []
# 1 · capa
S.append(('v01', 'capa', '''<p class="marca" style="left:96px;top:84px">fairhealth</p>
  <p class="cab" style="left:96px;top:230px;width:680px;font-size:66px;line-height:76px;font-weight:400;letter-spacing:-0.01em">Antes de chegar às empresas, nossa história começou <span class="k">em um hospital</span>.</p>
  <p class="sub" style="left:96px;top:640px;width:700px">2009 → hoje<br>por que a fairhealth existe?</p>'''))
# 2 · 2009
S.append(('v02', '2009: os pacientes distantes do centro do cuidado', '''<p class="num" style="left:90px;top:170px">2009</p>
  <p class="par" style="left:96px;top:330px;width:888px">Há quase 20 anos, percebemos que os pacientes estavam <span class="k">cada vez mais distantes do centro do cuidado</span>.</p>
  <p class="par" style="left:96px;top:590px;width:888px">Era preciso mudar essa realidade.</p>'''))
# 3 · no hospital (texto à esquerda; o caminho sobe pela direita)
S.append(('v03', 'no hospital: o Escritório do Paciente', '''<p class="cab" style="left:96px;top:170px;width:700px">No hospital</p>
  <p class="par" style="left:96px;top:300px;width:640px">Assim, dentro de um hospital, desenvolvemos o <span class="k">Escritório do Paciente</span> para mudar essa realidade.</p>
  <p class="par2" style="left:96px;top:580px;width:640px">Com o tempo, levamos esse conceito para as empresas.</p>'''))
# 4 · hoje (o caminho em cima; texto embaixo)
S.append(('v04', 'hoje: o Escritório do Cuidado', '''<p class="num" style="left:90px;top:540px">hoje</p>
  <p class="par" style="left:96px;top:690px;width:888px">Assim, desenvolvemos o <span class="k">Escritório do Cuidado</span>.</p>
  <p class="par2" style="left:96px;top:800px;width:888px">Um espaço de acolhimento e de medicina preventiva dentro da empresa, que fortalece o cuidado centrado na pessoa.</p>'''))
# 5 · o acolhimento (texto à direita; o caminho desce pela esquerda)
S.append(('v05', 'o acolhimento: tudo começa com uma pergunta', '''<p class="cab" style="left:380px;top:170px;width:604px;font-size:72px;line-height:80px">O acolhimento</p>
  <p class="par" style="left:380px;top:290px;width:604px">Tudo começa com uma pergunta: <span class="k">o que é importante para você?</span></p>
  <p class="par2" style="left:380px;top:500px;width:604px">Antes de qualquer exame, vem uma conversa: um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado.</p>'''))
# 6 · o que levamos (cartão com a lista, como os cartões da referência)
S.append(('v06', 'o que levamos: atendimento, planos de cuidado, tecnologia e humanização', '''<p class="cab" style="left:96px;top:170px;width:888px">O que levamos</p>
  <p class="par" style="left:96px;top:300px;width:888px">Levamos ao <span class="k">coração da sua empresa</span>:</p>
  <div class="cartao" style="top:400px"><p>Atendimento médico e psicológico</p><p>Planos de cuidado individualizados, baseados na Medicina do Estilo de Vida</p><p>Tecnologia, humanização e cuidado verdadeiro</p></div>'''))
# 7 · perto
S.append(('v07', 'perto: quando o cuidado está perto, ele acontece', '''<p class="cab" style="left:96px;top:170px;width:888px">Perto</p>
  <p class="par" style="left:96px;top:300px;width:888px">Porque, quando o cuidado está perto, <span class="k">ele acontece</span>.</p>
  <p class="par2" style="left:96px;top:450px;width:888px">A maior barreira ao cuidado é tempo e acesso. Por isso, o Escritório do Cuidado fica dentro da empresa, perto da rotina de quem trabalha.</p>'''))
# 8 · o propósito: o caminho chega ao logo
S.append(('v08', 'o propósito; faça o certo pelos motivos certos; o caminho chega ao logo', '''<p class="cab" style="left:96px;top:170px;width:888px">O propósito</p>
  <p class="par" style="left:96px;top:300px;width:888px">Nosso propósito é promover <span class="k">qualidade de vida, engajamento e um ambiente de trabalho mais saudável</span>.</p>
  <p class="par2" style="left:96px;top:540px;width:888px">Com resultados demonstrados por indicadores.</p>
  <p class="par" style="left:96px;top:640px;width:888px;font-weight:800">Faça o certo pelos motivos certos.</p>
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:%dpx;top:%dpx;width:132px;height:132px">
  <p class="anota" style="left:384px;top:1110px;width:600px;text-align:right">conheça a fairhealth no link da bio</p>''' % (LOGO[0] - 7 * W - 66, LOGO[1] - 66)))


def html(slides):
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (v7)</title><style>'
           + CSS + '</style></head><body>\n']
    for k, (sid, nota, corpo) in enumerate(slides, 1):
        pil = '<p class="pilula">%d/%d</p>' % (k, N)
        if k == 1:
            rod = '<p class="anota" style="left:96px;top:1232px;font-style:normal;font-size:24px">@fairhealth.br</p>'
        else:
            rod = '<p class="marca" style="left:96px;top:1232px;font-size:30px">fairhealth</p>'
        rod += '\n  <div class="prog"><i style="width:%dpx"></i></div>' % round(120 * k / N)
        out.append('<!-- %d · %s -->\n<section class="slide" id="%s">\n  <div class="papel"></div>\n  %s\n  %s\n  %s\n  %s\n</section>\n\n'
                   % (k, nota, sid, estrada(k), pil, corpo, rod))
    out.append('</body></html>\n')
    return ''.join(out)


open(SAIDA, 'w').write(html(S))
print('ok', len(S))
