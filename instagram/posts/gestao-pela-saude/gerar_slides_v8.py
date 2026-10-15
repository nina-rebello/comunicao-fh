# v8 (15/10): slide 2 refeito com o conteúdo que a Nina pediu: o cuidado real é o acolhimento (alguém para
#   ouvir) e começa com a pergunta-assinatura da marca, "O que é importante para você?". Sai a linha do tempo;
#   a pergunta vira o destaque. Mantém a foto em círculo ao lado do título, como está no Canva. O slide novo é o
#   k02c; os anteriores ficam guardados.
# Uso: python3 gerar_slides_v8.py slides-v8.html && node ../../ferramentas/render.mjs slides-v8.html png-v8
#
# v7 (15/10): a Nina escolheu a opção A do slide 2 (foto em círculo) e pediu uma textura de bolinhas, estilo
#   tecnológico, em um dos slides. A textura foi para o slide 3 (NR-1, o slide dos registros e da
#   rastreabilidade): meio-tom de bolinhas verdes saindo do canto de cima à direita, sumindo antes do texto.
#   O slide 3 com textura é o k03; o j03 fica guardado. Também grava textura-bolinhas.svg (a forma sozinha).
# Uso: python3 gerar_slides_v7.py slides-v7.html && node ../../ferramentas/render.mjs slides-v7.html png-v7
#
# v6 (15/10): simulação de foto no slide 2 (pedido da Nina: "manda uma simulação para eu ver"). Duas opções:
#   k02a · foto num círculo à direita da linha do tempo, com um anel fino em Tiffany (conversa2.jpg);
#   k02b · foto numa meia-lua que sai da borda direita, maior (conversa2.jpg, recortada em quem escuta).
#   As fotos levam a mesma saturação da capa (75%). A v5 fica guardada.
# Uso: python3 gerar_slides_v6.py slides-v6.html && node ../../ferramentas/render.mjs slides-v6.html png-v6
#
# v5 (15/10): slide 2 com outro contexto para o cuidado real (pedido da Nina). O plano de cuidado nasce de uma
#   longa conversa (hábitos, rotina, expectativas), num espaço seguro: ninguém cobra, a gente torce junto.
#   O slide novo é o k02; o j02 da v4 fica guardado. Os outros slides são os da v4.
# Uso: python3 gerar_slides_v5.py slides-v5.html && node ../../ferramentas/render.mjs slides-v5.html png-v5
#
# v4 (15/10): a Nina escolheu a opção B do ecossistema.
#   - Slide 5: opção B com fundo claro (creme) e a fairhealth em Tiffany (bolinha e metade do fio).
#   - Slide 6: sem a borda do logo, com fundo claro (j06) ou Tiffany (j06t). As duas vão para a prévia.
#   A opção A e a v3 ficam guardadas.
#
# v3 (15/10), pedidos da Nina sobre a v2:
#   - triângulo mais elegante (referência: linhas finas, pontas em círculo vazado, rótulos em caixa alta espaçada),
#     com uma foto dentro para humanizar;
#   - ecossistema em duas opções para escolher:
#       A · só os logos, sem repetir o nome da empresa embaixo (só o verbo);
#       B · o modelo da v1 (fio com bolinhas), com a cor de cada marca na bolinha e na metade do fio de cada lado;
#   - slide final sem a lista de ícones: logo da fairhealth maior, no meio e mais para cima, e a chamada
#     "Gostou? Leve esse cuidado adiante."
# Os slides 2, 3 e 4 são os da v2. A v1 e a v2 ficam guardadas.
# Uso: python3 gerar_slides_v4.py slides-v4.html && node ../../ferramentas/render.mjs slides-v4.html png-v4
#   O HTML tem os dois slides do ecossistema (j05a e j05b); a prévia monta uma versão com cada um.
import sys

SAIDA = sys.argv[1]
N = 6
ECO_DIR = '../../marca/ecossistema/'
FOTO = '../../marca/fotos-banco/cafe-notebook.jpg'   # Unsplash (fotos-banco/README.md): pessoa trabalhando, na rotina
COR = {'fairdata': '#767171', 'fairhealth': '#96C5BD', 'fairedu': '#6E35A2', 'fairtrust': '#145C9D'}  # medidas nos logos
# na opção B (fundo Tiffany), a bolinha e o fio da fairhealth vão no verde-escuro da marca: o Tiffany sumiria no fundo
COR_B = dict(COR)  # v4: fundo claro, então a fairhealth volta ao Tiffany

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
.t{background:var(--tif);color:var(--verde)}
.v{background:var(--verde);color:var(--creme)}
.c{background:var(--creme);color:var(--verde)}
.k{font-weight:800;font-style:italic}
.v .k{color:var(--tif)}
.rot{left:96px;top:96px;font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.v .rot{color:var(--tif)} .c .rot{color:var(--vlogo)}
.tit{font-size:70px;line-height:80px;letter-spacing:-0.01em}
.corpo{font-size:36px;line-height:48px}
.nota{font-size:28px;line-height:38px}
.handle{left:96px;top:1238px;font-size:24px;line-height:32px}
.v .handle{color:var(--tclaro)}
.arr{right:96px;top:1238px;font-size:24px;line-height:32px}
.pag{right:96px;top:1248px;display:flex;gap:8px}
.pag i{display:block;width:20px;height:12px;border-radius:6px}
.pag i.on{width:48px}
.t .pag i{background:var(--creme)} .t .pag i.on{background:var(--verde)}
.v .pag i{background:rgba(191,224,217,.3)} .v .pag i.on{background:var(--tif)}
.c .pag i{background:var(--tif)} .c .pag i.on{background:var(--verde)}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.vert{font-size:21px;line-height:28px;letter-spacing:.18em;text-transform:uppercase;text-align:center}
.cartao{left:96px;width:888px;background:#fff;border-radius:28px;padding:34px 40px}
.cartao b{display:block;font-size:32px;line-height:40px;font-weight:800;color:var(--vlogo);margin-bottom:8px}
.cartao span{display:block;font-size:30px;line-height:40px;color:var(--verde)}
.arg{left:96px;width:888px;border-top:3px solid var(--tif);padding-top:26px}
.arg b{display:block;font-size:34px;line-height:42px;font-weight:800;color:var(--creme);margin-bottom:8px}
.arg span{display:block;font-size:30px;line-height:40px;color:var(--tclaro)}
.passo{left:210px;width:774px}
.passo p{font-size:40px;line-height:48px;font-weight:800}
.eco{width:220px;text-align:center}
.eco b{display:block;font-size:28px;line-height:34px;font-weight:800}
.eco span{display:block;font-size:24px;line-height:30px;margin-top:4px}
.c .eco span{color:var(--vlogo)}
'''

def pag(i):
    return '<div class="pag">' + ''.join('<i class="on"></i>' if j == i else '<i></i>' for j in range(1, N + 1)) + '</div>'

S = []
# 1 · capa: triângulo fino com a foto dentro
T, E, D = (540, 600), (200, 1010), (880, 1010)
tri = 'M%d %d L%d %d L%d %d Z' % (T + E + D)
CAPA = """<p class="rot">O espaço que falta</p>
  <p class="tit" style="left:96px;top:170px;width:900px">Entre a medicina do trabalho e o plano de saúde, existe um espaço que <span class="k">ninguém cuida</span>.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <defs><clipPath id="tri"><path d="{tri}"/></clipPath>
      <filter id="suave"><feColorMatrix type="saturate" values=".75"/></filter></defs>
    <image href="{foto}" x="{ix}" y="{iy}" width="{iw}" height="{ih}" preserveAspectRatio="xMidYMid slice" clip-path="url(#tri)" filter="url(#suave)"/>
    <path d="{tri}" fill="none" stroke="#1F3A36" stroke-width="2.5" stroke-linejoin="round"/>
    <g fill="#96C5BD" stroke="#1F3A36" stroke-width="2.5"><circle cx="{tx}" cy="{ty}" r="13"/><circle cx="{ex}" cy="{ey}" r="13"/><circle cx="{dx}" cy="{dy}" r="13"/></g>
  </svg>
  <p class="vert" style="left:{lt}px;top:{tt}px;width:400px;font-weight:800">fairhealth</p>
  <p class="vert" style="left:{le}px;top:{tb}px;width:300px">Medicina<br>do trabalho</p>
  <p class="vert" style="left:{ld}px;top:{tb}px;width:300px">Plano<br>de saúde</p>
  <p class="corpo" style="left:96px;top:1145px;width:888px">É nele que a <b style="font-weight:800">fairhealth</b> trabalha.</p>""".format(
    tri=tri, foto=FOTO, ix=E[0], iy=T[1], iw=D[0] - E[0], ih=D[1] - T[1], tx=T[0], ty=T[1], ex=E[0], ey=E[1], dx=D[0], dy=D[1],
    lt=T[0] - 200, tt=T[1] - 58, le=E[0] - 150, ld=D[0] - 150, tb=E[1] + 30)
S.append(('j01', 't', 'capa: triângulo fino com foto dentro; fairhealth no topo', CAPA))
# 2 · cuidado real (v2)
S.append(('k02', 'v', 'cuidado real: o plano nasce de uma longa conversa, num espaço seguro', '''<p class="rot">Um cuidado real</p>
  <p class="tit" style="left:96px;top:180px;width:888px">Todo plano de cuidado começa com uma <span class="k">longa conversa</span>.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <path d="M136 534V814" stroke="#96C5BD" stroke-width="10" stroke-linecap="round"/>
    <g fill="#96C5BD"><circle cx="136" cy="534" r="26"/><circle cx="136" cy="674" r="26"/><circle cx="136" cy="814" r="26"/></g>
  </svg>
  <div class="passo" style="top:510px"><p>Entender seus hábitos</p></div>
  <div class="passo" style="top:650px"><p>Conhecer sua rotina</p></div>
  <div class="passo" style="top:790px"><p>Ouvir suas expectativas</p></div>
  <p class="corpo" style="left:96px;top:940px;width:888px;color:var(--tif)">Um espaço seguro, do começo ao fim. Sem medo, sem cobrança, sem frustração. <b style="font-weight:800;color:var(--creme)">A gente torce pelo seu resultado tanto quanto você.</b></p>'''))
# 3 · NR-1 (v2)
S.append(('j03', 't', 'NR-1: segurança psicossocial no trabalho (site, encurtado)', '''<p class="rot">Conformidade regulatória</p>
  <p class="tit" style="left:96px;top:170px;width:888px">NR-1: <span class="k">segurança psicossocial</span> no trabalho.</p>
  <div class="cartao" style="top:430px"><b>Obrigação legal</b><span>A gestão de riscos psicossociais agora vale para empresas de todos os portes.</span></div>
  <div class="cartao" style="top:665px"><b>Riscos psicossociais</b><span>Estresse, burnout e ansiedade precisam ser identificados, monitorados e mitigados.</span></div>
  <div class="cartao" style="top:900px"><b>Como a fairhealth ajuda</b><span>Escritório do Cuidado e Programa MEV, com registros e rastreabilidade.</span></div>'''))
# 4 · três argumentos (v2)
S.append(('j04', 'v', 'o argumento certo para cada decisor (site, encurtado)', '''<p class="rot">O argumento certo para cada decisor</p>
  <p class="tit" style="left:96px;top:170px;width:888px">Mesmo programa. Três argumentos, <span class="k">um para cada mesa</span>.</p>
  <div class="arg" style="top:470px"><b>Para o RH</b><span>Um programa preventivo real, com impacto na marca empregadora.</span></div>
  <div class="arg" style="top:690px"><b>Para o médico do trabalho</b><span>Evidência clínica de Medicina do Estilo de Vida e dados integráveis ao PGR.</span></div>
  <div class="arg" style="top:910px"><b>Para o financeiro</b><span>Indicadores de saúde e de custo para apresentar ao board.</span></div>'''))

# 5A · ecossistema só com os logos (sem repetir o nome) e o verbo embaixo
ECO = [('fairdata', 'medir', 186), ('fairhealth', 'cuidar', 422), ('fairedu', 'conscientizar', 658), ('fairtrust', 'comprovar', 894)]
FRASE = '<p class="tit" style="left:96px;top:930px;width:888px">Gestão de pessoas que começa pela <span class="k">saúde</span>.</p>'
TITULO_ECO = '<p class="tit" style="left:96px;top:170px;width:888px;font-size:60px;line-height:70px">A fairhealth é o <span class="k">cuidar</span> do ecossistema fairjob.</p>'
logos = ''
for nome, verbo, x in ECO:
    d = 150 if nome == 'fairhealth' else 124
    logos += '<img src="%slogo-%s.png" alt="%s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">' % (ECO_DIR, nome, nome, x - d // 2, 590 - d // 2, d, d)
    logos += '<p class="vert" style="left:%dpx;top:690px;width:220px;%s">%s</p>' % (x - 110, 'font-weight:800' if nome == 'fairhealth' else '', verbo)
S5A = ('j05a', 'c', 'ecossistema, opção A: só os logos, com o verbo embaixo', '''<p class="rot">Ecossistema fairjob</p>
  ''' + TITULO_ECO + '''
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><path d="M186 590H894" stroke="#96C5BD" stroke-width="2"/></svg>
  ''' + logos + '''
  ''' + FRASE)

# 5B · o modelo da v1: fio com bolinhas na cor de cada marca e a metade do fio de cada lado na mesma cor
xs = [x for _, _, x in ECO]
meios = [(xs[i] + xs[i + 1]) / 2 for i in range(3)]
seg = ''
for i, (nome, _, x) in enumerate(ECO):
    a = xs[0] if i == 0 else meios[i - 1]
    b = xs[-1] if i == 3 else meios[i]
    seg += '<path d="M%.0f 560H%.0f" stroke="%s" stroke-width="8" stroke-linecap="%s"/>' % (a, b, COR_B[nome], 'round' if i in (0, 3) else 'butt')
bolas = ''
for nome, _, x in ECO:
    if nome == 'fairhealth':
        bolas += '<circle cx="%d" cy="560" r="26" fill="%s"/>' % (x, COR_B[nome])
    else:
        bolas += '<circle cx="%d" cy="560" r="16" fill="%s"/>' % (x, COR_B[nome])
rot_b = ''.join('<div class="eco" style="left:%dpx;top:610px"><b>%s</b><span>%s</span></div>' % (x - 110, n, v) for n, v, x in ECO)
S5B = ('j05b', 'c', 'ecossistema, opção B (escolhida), fundo claro: o modelo da v1 com a cor de cada marca na bolinha e no fio', '''<p class="rot">Ecossistema fairjob</p>
  ''' + TITULO_ECO + '''
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">''' + seg + bolas + '''</svg>
  ''' + rot_b + '''
  ''' + FRASE)

# 6 · final: logo grande no meio e a chamada
FINAL = """<img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:390px;top:250px;width:300px;height:300px">
  <p class="tit" style="left:96px;top:640px;width:888px;text-align:center">Gostou?<br><span class="k">Leve esse cuidado adiante.</span></p>
  <p class="nota" style="left:146px;top:860px;width:788px;text-align:center;color:var(--vlogo)">Salve, compartilhe e conheça mais no link da bio.</p>"""
S6 = ('j06', 'c', 'final: logo grande sem borda, fundo claro', FINAL)
S6T = ('j06t', 't', 'final: logo grande sem borda, fundo Tiffany', FINAL)


def html(slides, titulo):
    # slides: (id, classe, nota, corpo, página)
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>' + titulo + '</title><style>' + CSS + '</style></head><body>\n']
    for sid, cls, nota, corpo, k in slides:
        if k == 1:
            fim = '\n  <p class="handle">@fairhealth.br</p>\n  <p class="arr">Arraste para o lado →</p>'
        else:
            fim = '\n  <p class="handle">@fairhealth.br</p>\n  ' + pag(k)
        out.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  %s%s\n</section>\n\n' % (k, nota, cls, sid, corpo, fim))
    out.append('</body></html>\n')
    return ''.join(out)


# v6 · slide 2 com foto, em duas opções
FB = '../../marca/fotos-banco/'
K02 = [x for x in S if x[0] == 'k02'][0]


def com_foto(sid, nota, foto, cx, cy, r, anel, fx, fy, fw, fh):
    # foto recortada em círculo (centro cx, cy, raio r); a imagem cobre a caixa fx, fy, fw, fh
    svg = """
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <defs><clipPath id="c{sid}"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>
      <filter id="s{sid}"><feColorMatrix type="saturate" values=".75"/></filter></defs>
    <image href="{foto}" x="{fx}" y="{fy}" width="{fw}" height="{fh}" preserveAspectRatio="xMidYMid slice" clip-path="url(#c{sid})" filter="url(#s{sid})"/>
    {anel}
  </svg>""".format(sid=sid, cx=cx, cy=cy, r=r, foto=FB + foto, fx=fx, fy=fy, fw=fw, fh=fh, anel=anel)
    return (sid, 'v', nota, K02[3] + svg)


# A · círculo de 260 px à direita da linha do tempo, com anel fino em Tiffany
KA = com_foto('k02a', 'opção A: foto em círculo ao lado da linha do tempo', 'conversa2.jpg', 854, 674, 130,
              '<circle cx="854" cy="674" r="142" fill="none" stroke="#96C5BD" stroke-width="2.5"/>',
              614, 544, 390, 260)
# B · meia-lua: círculo grande cortado pela borda direita
# (a meia-lua é estreita: cabe uma pessoa só, então o recorte fica em quem escuta e anota, na conversa2.jpg)
KB = com_foto('k02b', 'opção B: foto em meia-lua saindo da borda direita', 'conversa2.jpg', 1080, 664, 280,
              '<circle cx="1080" cy="664" r="292" fill="none" stroke="#96C5BD" stroke-width="2.5"/>',
              470, 384, 840, 560)

# v7 · textura de bolinhas (meio-tom) no canto de cima à direita do slide 3
def textura(cx=1080, cy=0, raio=370, passo=24, rmax=6.0, rmin=0.8):
    # grade quadrada; o raio de cada bolinha diminui com a distância até o canto (cx, cy)
    # devolve o caminho SVG (coordenadas relativas à caixa) e a caixa (x, y, largura, altura)
    pts = []
    y = passo / 2
    while y < cy + raio:
        x = cx - passo / 2
        while x > cx - raio:
            d = ((x - cx) ** 2 + (y - cy) ** 2) ** .5
            r = rmax * (1 - d / raio)
            if r >= rmin:
                pts.append((x, y, r))
            x -= passo
        y += passo
    x0, y0 = min(p[0] - p[2] for p in pts), min(p[1] - p[2] for p in pts)
    x1, y1 = max(p[0] + p[2] for p in pts), max(p[1] + p[2] for p in pts)
    caminho = ''.join('M%.1f %.1fa%.1f %.1f 0 1 0 %.1f 0a%.1f %.1f 0 1 0 %.1f 0Z' % (x - r - x0, y - y0, r, r, 2 * r, r, r, -2 * r)
                      for x, y, r in pts)
    return caminho, (round(x0, 1), round(y0, 1), round(x1 - x0, 1), round(y1 - y0, 1)), len(pts)


TEX, (TX, TY, TW, TH), NTEX = textura()
TEX_COR, TEX_OPAC = '#1F3A36', .45
open('textura-bolinhas.svg', 'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s" width="%s" height="%s"><path d="%s" fill="%s"/></svg>\n'
                                        % (TW, TH, TW, TH, TEX, TEX_COR))
J03 = [x for x in S if x[0] == 'j03'][0]
K03 = ('k03', 't', J03[2] + ', com textura de bolinhas no canto',
       '<svg aria-hidden="true" style="left:%spx;top:%spx;width:%spx;height:%spx" viewBox="0 0 %s %s"><path d="%s" fill="%s" fill-opacity="%s"/></svg>\n  '
       % (TX, TY, TW, TH, TW, TH, TEX, TEX_COR, TEX_OPAC) + J03[3])

# v8 · slide 2: acolhimento e a pergunta
K02C = ('k02c', 'v', 'cuidado real: acolhimento, alguém para ouvir, e a pergunta', '''<p class="rot">Um cuidado real</p>
  <p class="tit" style="left:96px;top:199px;width:640px">Tudo começa com alguém para ouvir.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <defs><clipPath id="ck02c"><circle cx="872" cy="360" r="100"/></clipPath>
      <filter id="sk02c"><feColorMatrix type="saturate" values=".75"/></filter></defs>
    <image href="''' + FB + '''conversa2.jpg" x="684" y="260" width="300" height="200" preserveAspectRatio="xMidYMid slice" clip-path="url(#ck02c)" filter="url(#sk02c)"/>
    <circle cx="872" cy="360" r="112" fill="none" stroke="#96C5BD" stroke-width="2.5"/>
  </svg>
  <p style="left:96px;top:530px;width:888px;font-size:32px;line-height:42px;color:var(--tclaro)">E com uma pergunta:</p>
  <p style="left:96px;top:584px;width:760px;font-size:72px;line-height:84px;font-weight:800;font-style:italic;color:var(--tif);letter-spacing:-0.01em">“O que é importante para você?”</p>
  <p class="corpo" style="left:96px;top:830px;width:850px;color:var(--tif)">É dessa conversa, sem pressa, que nasce um plano de cuidado só seu. Sem cobrança, sem julgamento. <b style="font-weight:800;color:var(--creme)">A gente torce pelo seu resultado tanto quanto você.</b></p>''')

# o HTML tem as duas opções do slide 5 (5A e 5B, ambas na página 5 de 6)
slides = [s + (k,) for k, s in enumerate(S, 1)] + [S5B + (5,), S6 + (6,), S6T + (6,), KA + (2,), KB + (2,), K03 + (3,), K02C + (2,)]
open(SAIDA, 'w').write(html(slides, 'Gestão de pessoas que começa pela saúde (v8)'))
print('ok', len(slides), 'bolinhas na textura:', NTEX, 'caixa:', (TX, TY, TW, TH), 'caminho:', len(TEX), 'caracteres')
