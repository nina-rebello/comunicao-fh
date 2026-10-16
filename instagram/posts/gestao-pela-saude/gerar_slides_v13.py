# v13 (16/10): slide novo (p01), a pedido da Nina, a partir de uma referência dela: "No caminho rumo à qualidade de
#   vida, existe um plano especial e individualizado pra você." Triângulo com foto (sorriso2.jpg: a pessoa no centro do cuidado) e três pontas:
#   Escritório do Cuidado, Saúde integral e Qualidade de vida, com ícones em traço (Lucide, licença ISC); embaixo o
#   logo e "Você no centro do cuidado". Nada dos outros slides muda.
# Uso: python3 gerar_slides_v13.py slides-v13.html && node ../../ferramentas/render.mjs slides-v13.html png-v13
#
# v12 (16/10): slide 3 (k03e) no modelo do site (fairjob.com.br/fairhealth), a pedido da Nina: título "Segurança
#   psicossocial no trabalho", subtítulo e três cartões com ícone (balança, cérebro, escudo), título e texto do site.
#   Ícones: Lucide (licença ISC), em traço.
# Uso: python3 gerar_slides_v12.py slides-v12.html && node ../../ferramentas/render.mjs slides-v12.html png-v12
#
# v11 (16/10): slide 3 (k03d) sem tom de aula, a pedido da Nina: mostra como a fairhealth trabalha nos riscos
#   psicossociais (ouvir e mapear, cuidar, acompanhar); a NR-1 entra no último cartão, como contexto.
# Uso: python3 gerar_slides_v11.py slides-v11.html && node ../../ferramentas/render.mjs slides-v11.html png-v11
#
# v10 (16/10): slide 3 (k03c) muda de ideia, a pedido da Nina: o título foca em riscos psicossociais e a NR-1 entra
#   no texto, como contexto. Mantém os três cartões do Canva, com o terceiro em verde-escuro (ajuste da Nina).
# Uso: python3 gerar_slides_v10.py slides-v10.html && node ../../ferramentas/render.mjs slides-v10.html png-v10
#
# v9 (15/10): slide NR-1 (k03b) mostra, além de citar, como a fairhealth ajuda em cada exigência: à esquerda
#   o que a norma pede, à direita como a gente ajuda. Base: estrategia.md (contexto → diagnóstico → cuidado
#   individualizado → acompanhamento), posicionamento (diagnóstico e indicadores com a fairdata) e o site (dados
#   integráveis ao PGR). Sem prometer conformidade. Sem a textura (a Nina tirou no Canva). Sem cabeçalho de
#   coluna: o título já diz "o que a norma pede e como ajudamos" (e no Canva o texto novo não sai em Raleway).
# Uso: python3 gerar_slides_v9.py slides-v9.html && node ../../ferramentas/render.mjs slides-v9.html png-v9
#
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
        if sid == 'p01':
            fim = ''  # o rodapé deste slide é o logo e "Você no centro do cuidado"
        elif k == 1:
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

# v9 · NR-1: o que a norma pede x como a fairhealth ajuda
NR1 = [('Identificar os riscos', 'Diagnóstico com a fairdata e escuta individual de cada pessoa.'),
       ('Agir para prevenir', 'Um plano de cuidado para cada pessoa, com médicos e psicólogos dentro da empresa.'),
       ('Acompanhar e registrar', 'Acompanhamento contínuo e indicadores do grupo, sem identificar ninguém, integráveis ao PGR.')]
linhas = ''
for i, (pede, ajuda) in enumerate(NR1):
    y = 470 + i * 215
    linhas += ('<div style="left:96px;top:%dpx;width:888px;height:185px;background:#fff;border-radius:28px"></div>\n  '
               '<div style="left:376px;top:%dpx;width:2px;height:125px;background:var(--tif)"></div>\n  '
               '<p style="left:136px;top:%dpx;width:220px;font-size:32px;line-height:40px;font-weight:800;color:var(--vlogo)">%s</p>\n  '
               '<p style="left:408px;top:%dpx;width:536px;font-size:28px;line-height:38px;color:var(--verde)">%s</p>\n  '
               % (y, y + 30, y + 34, pede, y + 32, ajuda))
K03B = ('k03b', 't', 'NR-1: o que a norma pede e como a fairhealth ajuda', '''<p class="rot">Conformidade regulatória</p>
  <p class="tit" style="left:96px;top:170px;width:888px">NR-1: o que a norma pede e <span class="k">como ajudamos</span>.</p>
  ''' + linhas)

# v10 · slide 3: riscos psicossociais no título, NR-1 como contexto
K03C = ('k03c', 't', 'o que são riscos psicossociais; a NR-1 como contexto', '''<p class="rot">Conformidade regulatória</p>
  <p class="tit" style="left:96px;top:170px;width:888px">O que são <span class="k">riscos psicossociais</span>?</p>
  <div class="cartao" style="top:430px"><b>Na prática</b><span>Pressão, excesso de demanda e conflitos que podem levar a estresse, burnout e ansiedade.</span></div>
  <div class="cartao" style="top:665px"><b>O que diz a NR-1</b><span>A norma atualizada inclui esses riscos no PGR, a gestão de riscos da empresa, para todos os portes.</span></div>
  <div class="cartao" style="top:900px;background:var(--verde)"><b style="color:var(--tclaro)">Como a fairhealth ajuda</b><span style="color:#fff">Escritório do Cuidado e Programa MEV: escuta, plano de cuidado e indicadores integráveis ao PGR.</span></div>''')

# v11 · slide 3: como cuidamos dos riscos psicossociais
K03D = ('k03d', 't', 'como cuidamos dos riscos psicossociais; NR-1 como contexto', '''<p class="rot">Conformidade regulatória</p>
  <p class="tit" style="left:96px;top:170px;width:888px">Como cuidamos dos <span class="k">riscos psicossociais</span>.</p>
  <div class="cartao" style="top:430px"><b>Ouvir e mapear</b><span>Escuta individual e, com a fairdata, o diagnóstico dos riscos do grupo.</span></div>
  <div class="cartao" style="top:665px"><b>Cuidar</b><span>Médicos e psicólogos dentro da empresa e um plano de cuidado para cada pessoa.</span></div>
  <div class="cartao" style="top:900px;background:var(--verde)"><b style="color:var(--tclaro)">Acompanhar</b><span style="color:#fff">Indicadores do grupo, sem identificar ninguém, integráveis ao PGR que a NR-1 exige.</span></div>''')

# v12 · slide 3 no modelo do site
ICONES = {
    'balanca': ['m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z', 'm2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z',
                'M7 21h10', 'M12 3v18', 'M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2'],
    'cerebro': ['M12 5a3 3 0 1 0-5.997.125 4 4 0 0 0-2.526 5.77 4 4 0 0 0 .556 6.588A4 4 0 1 0 12 18Z',
                'M12 5a3 3 0 1 1 5.997.125 4 4 0 0 1 2.526 5.77 4 4 0 0 1-.556 6.588A4 4 0 1 1 12 18Z',
                'M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4', 'M17.599 6.5a3 3 0 0 0 .399-1.375',
                'M6.003 5.125A3 3 0 0 0 6.401 6.5', 'M3.477 10.896a4 4 0 0 1 .585-.396', 'M19.938 10.5a4 4 0 0 1 .585.396',
                'M6 18a4 4 0 0 1-1.967-.516', 'M19.967 17.484A4 4 0 0 1 18 18'],
    'escudo': ['M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z',
               'm9 12 2 2 4-4'],
}
CARTOES = [('balanca', 'Obrigação legal', 'A NR-1 atualizada (2025) inclui a gestão de riscos psicossociais como requisito obrigatório para empresas de todos os portes.'),
           ('cerebro', 'Riscos psicossociais', 'Estresse, burnout, ansiedade e conflitos interpessoais devem ser identificados, monitorados e mitigados.'),
           ('escudo', 'Solução para NR-1 e ambiente na empresa', 'O Escritório do Cuidado e o Programa MEV oferecem estrutura completa para cumprir as exigências da NR-1, com registros e rastreabilidade.')]
TOPO, ALT, VAO = 500, 212, 18
cartoes = ''
for i, (ic, tit, txt) in enumerate(CARTOES):
    y = TOPO + i * (ALT + VAO)
    cartoes += ('<div style="left:96px;top:%dpx;width:888px;height:%dpx;background:#fff;border-radius:28px"></div>\n  '
                '<div style="left:132px;top:%dpx;width:76px;height:76px;background:#E3F0EC;border-radius:20px"></div>\n  '
                '<svg aria-hidden="true" style="left:150px;top:%dpx;width:40px;height:40px" viewBox="0 0 24 24" fill="none" stroke="#2F6B64" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg>\n  '
                '<p style="left:240px;top:%dpx;width:708px;font-size:29px;line-height:37px;font-weight:800;color:var(--vlogo)">%s</p>\n  '
                '<p style="left:240px;top:%dpx;width:708px;font-size:25px;line-height:34px;color:var(--verde)">%s</p>\n  '
                % (y, ALT, y + 34, y + 52, ''.join('<path d="%s"/>' % d for d in ICONES[ic]), y + 32, tit, y + 76, txt))
K03E = ('k03e', 't', 'segurança psicossocial no trabalho, no modelo do site', '''<p class="rot">Conformidade regulatória</p>
  <p class="tit" style="left:96px;top:170px;width:888px"><span class="k">Segurança psicossocial</span> no trabalho.</p>
  <p style="left:96px;top:356px;width:888px;font-size:28px;line-height:38px">A fairhealth assegura programa e práticas totalmente alinhados com as novas exigências da Norma Regulamentadora NR-01.</p>
  ''' + cartoes)

# v13 · slide novo: o plano individualizado
ICONES.update({
    'pessoa': ['M9 9a3 3 0 1 0 6 0a3 3 0 1 0-6 0Z', 'M6 21 C6 17.7 8.7 15 12 15 C15.3 15 18 17.7 18 21',
               'M12 1.5 L12 3.5', 'M5.2 4.2 L6.6 5.6', 'M18.8 4.2 L17.4 5.6', 'M2.5 9.5 L4.5 9.5', 'M19.5 9.5 L21.5 9.5'],
    'coracao': ['M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z',
                'M3.22 12 L9.5 12 L10 11 L12 15.5 L14 8.5 L15.5 12 L20.77 12'],
    'folha': ['M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z',
              'M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12'],
})
PT, PE, PD = (540, 630), (250, 970), (830, 970)
R = 52


def ponta(c, ic):
    return ('<div style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;background:var(--creme)"></div>\n  '
            '<svg aria-hidden="true" style="left:%dpx;top:%dpx;width:44px;height:44px" viewBox="0 0 24 24" fill="none" stroke="#1F3A36" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">%s</svg>\n  '
            % (c[0] - R, c[1] - R, 2 * R, 2 * R, c[0] - 22, c[1] - 22, ''.join('<path d="%s"/>' % d for d in ICONES[ic])))


TRI = 'M%d %d L%d %d L%d %d Z' % (PT + PE + PD)
P01 = ('p01', 't', 'plano individualizado: Escritório do Cuidado, saúde integral, qualidade de vida', '''<p class="rot">Plano de cuidado</p>
  <p class="tit" style="left:96px;top:160px;width:888px;font-size:64px;line-height:74px">No caminho rumo à <span class="k">qualidade de vida</span>, existe um plano especial e individualizado pra você.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <defs><clipPath id="trip01"><path d="''' + TRI + '''"/></clipPath>
      <filter id="sp01"><feColorMatrix type="saturate" values=".8"/></filter></defs>
    <image href="''' + FB + '''sorriso2.jpg" x="225" y="370" width="700" height="1050" preserveAspectRatio="xMidYMid slice" clip-path="url(#trip01)" filter="url(#sp01)"/>
    <path d="''' + TRI + '''" fill="none" stroke="#F0F0E9" stroke-width="3" stroke-linejoin="round"/>
  </svg>
  ''' + ponta(PT, 'pessoa') + ponta(PE, 'coracao') + ponta(PD, 'folha') + '''<p class="vert" style="left:340px;top:508px;width:400px;font-weight:800">Escritório<br>do cuidado</p>
  <p class="vert" style="left:100px;top:1040px;width:300px;font-weight:800">Saúde<br>integral</p>
  <p class="vert" style="left:680px;top:1040px;width:300px;font-weight:800">Qualidade<br>de vida</p>
  <div style="left:226px;top:1110px;width:48px;height:3px;background:var(--vlogo)"></div>
  <div style="left:806px;top:1110px;width:48px;height:3px;background:var(--vlogo)"></div>
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:485px;top:1135px;width:110px;height:110px">
  <p class="vert" style="left:240px;top:1252px;width:600px;font-size:20px">Você no centro do cuidado</p>''')

# o HTML tem as duas opções do slide 5 (5A e 5B, ambas na página 5 de 6)
slides = [s + (k,) for k, s in enumerate(S, 1)] + [S5B + (5,), S6 + (6,), S6T + (6,), KA + (2,), KB + (2,), K03 + (3,), K02C + (2,), K03B + (3,), K03C + (3,), K03D + (3,), K03E + (3,), P01 + (3,)]
open(SAIDA, 'w').write(html(slides, 'Gestão de pessoas que começa pela saúde (v13)'))
print('ok', len(slides), 'bolinhas na textura:', NTEX, 'caixa:', (TX, TY, TW, TH), 'caminho:', len(TEX), 'caracteres')
