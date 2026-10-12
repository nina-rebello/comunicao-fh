# Gera slides-v4.html (12 slides, ids x01..x12). Uso: python3 gerar_slides_v4.py slides-v4.html
# v3 + elementos do livro da marca: luz, Venn com legenda em fio, linha do tempo,
# rosca de fotos dos pilares, fio contínuo entre slides, cartões e traço que vira coração.
import math, sys

SAIDA = sys.argv[1]
N = 12
FOTOS = '../../marca/fotos-banco/'

CSS = r'''
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:400;font-style:italic;src:url(../../marca/fontes/raleway-latin-400-italic.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--tif:#96C5BD;--verde:#1F3A36;--creme:#F0F0E9;--tclaro:#BFE0D9;--tesc:#5FA89A;--vlogo:#2F6B64;--noite:#0D1816}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#888;display:flex;flex-wrap:wrap;gap:40px;padding:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-variant-numeric:lining-nums}
.slide>*{position:absolute}
.v{background:var(--verde);color:var(--creme)}
.c{background:var(--creme);color:var(--verde)}
.t{background:var(--tif);color:var(--verde)}
.L{background:var(--noite);color:var(--creme)}
.k{font-weight:800;font-style:italic}
.v .k,.L .k{color:var(--tif);-webkit-text-fill-color:var(--tif)}
.rot{left:96px;top:96px;font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.v .rot{color:var(--tif)} .c .rot{color:var(--vlogo)}
.tit{font-size:72px;line-height:80px;letter-spacing:-0.01em}
.sub{font-size:40px;line-height:52px}
.corpo{font-size:34px;line-height:46px}
.nota{font-size:24px;line-height:32px}
.tclaro{color:var(--tclaro)}
.handle{left:96px;top:1238px;font-size:24px;line-height:32px}
.v .handle,.L .handle{color:var(--tclaro)}
.arr{right:96px;top:1238px;font-size:24px;line-height:32px;color:var(--tclaro)}
.pag{right:96px;top:1248px;display:flex;gap:8px}
.pag i{display:block;width:20px;height:12px;border-radius:6px}
.pag i.on{width:48px}
.v .pag i,.L .pag i{background:rgba(191,224,217,.3)} .v .pag i.on,.L .pag i.on{background:var(--tif)}
.c .pag i{background:var(--tif)} .c .pag i.on{background:var(--verde)}
.t .pag i{background:var(--creme)} .t .pag i.on{background:var(--verde)}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
/* luz (série Luz tiffany) */
.feixe{width:240px;height:2000px;background:linear-gradient(180deg,rgba(150,197,189,0),rgba(150,197,189,.55) 45%,rgba(150,197,189,0));filter:blur(40px);transform-origin:center}
.brilho{border-radius:50%;background:radial-gradient(circle,rgba(150,197,189,.55),rgba(150,197,189,0) 65%);filter:blur(30px)}
.grao{inset:0;opacity:.22;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='320' height='320'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.vinheta{inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(13,24,22,0) 35%,rgba(13,24,22,.85) 100%)}
.luzt{font-weight:400;letter-spacing:-0.015em;background:linear-gradient(180deg,#F7F7F2,#B9C9C5);-webkit-background-clip:text;background-clip:text;color:transparent}
.pilula{border:2px solid rgba(240,240,233,.85);border-radius:999px;padding:16px 40px;font-size:24px;line-height:30px;letter-spacing:.16em;text-transform:uppercase;white-space:nowrap}
/* listas com fio */
.lista{left:96px;width:888px}
.lista p{font-size:36px;line-height:46px;padding:26px 0;border-top:2px solid rgba(31,58,54,.28)}
.lista p:last-child{border-bottom:2px solid rgba(31,58,54,.28)}
.lista b{font-weight:800}
.v .lista p{border-color:rgba(191,224,217,.3)}
.v .lista b{color:var(--tif)}
/* passos com bolinhas no fio */
.passo .w{font-size:46px;line-height:52px;font-weight:800;letter-spacing:-0.01em}
.passo .d{font-size:30px;line-height:40px;margin-top:6px}
/* legenda dos pilares */
.leg .n{display:block;font-size:20px;line-height:26px;font-weight:800;letter-spacing:.16em;color:var(--vlogo)}
.leg .w{display:block;font-size:30px;line-height:36px}
/* cartões das frentes */
.cartao{left:96px;width:888px;border-radius:28px;background:var(--creme);padding:30px 40px 30px 40px;display:grid;grid-template-columns:70px 1fr;column-gap:16px}
.cartao .n{font-size:22px;line-height:44px;font-weight:800;letter-spacing:.16em;color:var(--vlogo)}
.cartao .w{font-size:36px;line-height:44px;font-weight:800}
.cartao .d{grid-column:2;font-size:28px;line-height:38px;margin-top:4px}
.cartao.dest{background:var(--verde);color:var(--creme)}
.cartao.dest .n{color:var(--tif)}
.cartao .chip{display:inline-block;vertical-align:middle;margin-left:16px;background:var(--tif);color:var(--verde);border-radius:8px;padding:4px 14px;font-size:20px;line-height:28px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
/* números */
.dado{left:96px;width:888px;display:flex;align-items:center;gap:40px;padding:36px 0;border-top:2px solid rgba(191,224,217,.25)}
.dado .n{font-size:150px;line-height:130px;font-weight:800;letter-spacing:-0.04em;color:var(--tif);width:400px;flex:none;text-shadow:0 0 60px rgba(150,197,189,.45)}
.dado .l{font-size:40px;line-height:50px}
.dado .f{display:block;font-size:22px;line-height:30px;color:var(--tclaro);opacity:.85;margin-top:8px}
'''

def pag(i):
    return '<div class="pag">' + ''.join('<i class="on"></i>' if j == i else '<i></i>' for j in range(1, N + 1)) + '</div>'

def luz(*partes):
    return '\n  '.join(partes) + '\n  <div class="vinheta"></div>\n  <div class="grao"></div>'

def P(x, y):
    return '%.1f %.1f' % (x, y)

def pol(cx, cy, raio, ang):
    a = math.radians(ang)
    return cx + raio * math.cos(a), cy + raio * math.sin(a)

def setor(cx, cy, R, r, a0, a1):
    g = 1 if (a1 - a0) > 180 else 0
    return ('M%s A%d %d 0 %d 1 %s L%s A%d %d 0 %d 0 %s Z' % (
        P(*pol(cx, cy, R, a0)), R, R, g, P(*pol(cx, cy, R, a1)),
        P(*pol(cx, cy, r, a1)), r, r, g, P(*pol(cx, cy, r, a0))))

def caixa(cx, cy, R, r, a0, a1):
    pts = [pol(cx, cy, rr, a0 + (a1 - a0) * k / 20) for rr in (r, R) for k in range(21)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys)

# ---------------------------------------------------------------- rosca dos pilares
CX, CY, R, r = 540, 800, 250, 118
PILARES = [  # (ângulo do centro do setor, nº, nome com quebra, foto, alinhamento da foto, lado do rótulo)
    (-60, '01', 'Alimentação saudável', 'comida.jpg', 'xMidYMid', 'dir-cima'),
    (0, '02', 'Movimento', 'escada.jpg', 'xMidYMid', 'dir'),
    (60, '03', 'Gerenciamento de estresse', 'respira.jpg', 'xMidYMid', 'dir-baixo'),
    (120, '04', 'Sono de qualidade', 'sono-limpa.jpg', 'xMinYMid', 'esq-baixo'),
    (180, '05', 'Manejo<br>de vícios', 'agua.jpg', 'xMidYMid', 'esq'),
    (240, '06', 'Relacionamentos', 'amigos.jpg', 'xMidYMid', 'esq-cima'),
]

def rosca():
    defs, imgs, fios, legs = [], [], [], []
    for k, (ang, n, nome, foto, alin, lado) in enumerate(PILARES):
        a0, a1 = ang - 30, ang + 30
        d = setor(CX, CY, R, r, a0, a1)
        defs.append('<clipPath id="ps%d"><path d="%s"/></clipPath>' % (k, d))
        x, y, w, h = caixa(CX, CY, R, r, a0, a1)
        imgs.append('<image href="%s%s" x="%.0f" y="%.0f" width="%.0f" height="%.0f" preserveAspectRatio="%s slice" clip-path="url(#ps%d)" filter="url(#suave)"/>' % (FOTOS, foto, x - 4, y - 4, w + 8, h + 8, alin, k))
        x0, y0 = pol(CX, CY, R + 10, ang)
        if lado in ('dir', 'esq'):
            x1, y1 = pol(CX, CY, R + 40, ang)
            xe = 984 if lado == 'dir' else 96
            fios.append('<path d="M%s L%s H%d" fill="none" stroke="#1F3A36" stroke-opacity=".45" stroke-width="2"/>' % (P(x0, y0), P(x1, y1), xe))
            if lado == 'dir':
                legs.append('<p class="leg" style="right:96px;top:%dpx;text-align:right"><span class="n">%s</span><span class="w">%s</span></p>' % (y1 - 74, n, nome))
            else:
                legs.append('<p class="leg" style="left:96px;top:%dpx"><span class="n">%s</span><span class="w">%s</span></p>' % (y1 - 110, n, nome))
        else:
            x1, y1 = pol(CX, CY, R + 52, ang)
            xe = 984 if lado.startswith('dir') else 96
            fios.append('<path d="M%s L%s H%d" fill="none" stroke="#1F3A36" stroke-opacity=".45" stroke-width="2"/>' % (P(x0, y0), P(x1, y1), xe))
            al = 'right:96px;text-align:right' if lado.startswith('dir') else 'left:96px'
            if lado.endswith('cima'):
                legs.append('<p class="leg" style="%s;top:%dpx;width:420px"><span class="n">%s</span><span class="w">%s</span></p>' % (al, y1 - 74, n, nome))
            else:
                legs.append('<p class="leg" style="%s;top:%dpx;width:420px"><span class="w">%s</span><span class="n" style="margin-top:6px">%s</span></p>' % (al, y1 + 12, nome, n))
        fios.append('<circle cx="%.1f" cy="%.1f" r="5" fill="#1F3A36"/>' % (x0, y0))
    bordas = ''.join('<path d="%s"/>' % setor(CX, CY, R, r, a - 30, a + 30) for a, *_ in PILARES)
    svg = ('<svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><defs>'
           '<filter id="suave"><feColorMatrix type="saturate" values=".8"/></filter>' + ''.join(defs) + '</defs>'
           + ''.join(imgs)
           + '<g fill="none" stroke="#F0F0E9" stroke-width="14" stroke-linejoin="round">' + bordas + '</g>'
           + ''.join(fios) + '</svg>')
    centro = ('<p style="left:%dpx;top:%dpx;width:%dpx;text-align:center;font-size:30px;line-height:36px">'
              '<span class="k">a pessoa</span><br>no centro</p>') % (CX - 110, CY - 36, 220)
    return svg + '\n  ' + '\n  '.join(legs) + '\n  ' + centro

# ---------------------------------------------------------------- Venn de três círculos
def venn():
    A, B, C, rv = (640, 760), (540, 930), (740, 930), 170
    cc = lambda p, extra='': '<circle cx="%d" cy="%d" r="%d"%s/>' % (p[0], p[1], rv, extra)
    tri = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)
    svg = ('<svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><defs>'
           '<clipPath id="vb">' + cc(B) + '</clipPath><clipPath id="vc">' + cc(C) + '</clipPath></defs>'
           '<g fill="#96C5BD" fill-opacity=".5">' + cc(A) + cc(B) + cc(C) + '</g>'
           '<g clip-path="url(#vb)"><g clip-path="url(#vc)">' + cc(A, ' fill="#2F6B64"') + '</g></g>'
           '<path d="M96 %d H%.0f" stroke="#2F6B64" stroke-width="2"/><circle cx="%.0f" cy="%d" r="6" fill="#F0F0E9"/>'
           '</svg>') % (tri[1], tri[0], tri[0], tri[1])
    t = lambda x, y, w, txt: '<p style="left:%dpx;top:%dpx;width:%dpx;text-align:center;font-size:28px;line-height:34px">%s</p>' % (x - w // 2, y, w, txt)
    return (svg + '\n  ' + t(A[0], A[1] - 118, 260, 'Medicina do<br>Estilo de Vida')
            + '\n  ' + t(B[0] - 50, B[1] + 34, 200, 'Prevenção')
            + '\n  ' + t(C[0] + 50, C[1] + 16, 200, 'Cuidado<br>centrado<br>na pessoa')
            + '\n  <p class="rot" style="left:96px;top:%dpx;font-size:18px;line-height:24px;color:var(--vlogo)">Onde a<br>fairhealth<br>atua</p>' % (tri[1] - 84))

# ---------------------------------------------------------------- fio contínuo dos slides 6 e 7 (2160 px)
FIO = ('M-30 1130 C220 1130 420 1080 560 990 C700 900 780 770 700 720 C620 670 520 760 560 860 '
       'C600 960 760 980 860 900 C960 820 990 560 1150 470 C1190 448 1216 470 1216 520 L1216 1041')
def fio(offset):
    return ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#96C5BD" '
            'stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>') % (offset, FIO)

def passos(itens, topo, passo, cor_bola, cor_num, cor_fio=None, x_bola=136):
    out, ys = [], []
    for k, (w, d) in enumerate(itens):
        y = topo + k * passo
        ys.append(y + 26)
        out.append('<div class="passo" style="left:210px;top:%dpx;width:774px"><p class="w">%s</p><p class="d">%s</p></div>' % (y, w, d))
    linha = ''
    if cor_fio:
        linha = '<path d="M%d %d V%d" stroke="%s" stroke-width="12" stroke-linecap="round"/>' % (x_bola, ys[0], ys[-1], cor_fio)
    bolas = ''.join('<circle cx="%d" cy="%d" r="30" fill="%s"/>' % (x_bola, y, cor_bola) for y in ys)
    svg = '<svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">%s%s</svg>' % (linha, bolas)
    nums = ''.join('<p style="left:%dpx;top:%dpx;width:60px;text-align:center;font-size:24px;line-height:30px;font-weight:800;color:%s">%02d</p>' % (x_bola - 30, y - 15, cor_num, k + 1) for k, y in enumerate(ys))
    return svg + '\n  ' + '\n  '.join(out) + '\n  ' + nums

CORACAO = ('<svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><path transform="translate(540 1130) scale(.62) translate(-540 -1080)" '
           'd="M-900 1080H540C470 1030 300 940 320 800C335 700 470 680 540 780C610 680 745 700 760 800C780 940 610 1030 540 1080H2000" '
           'fill="none" stroke="#96C5BD" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/></svg>')

S = []
# 1 · capa luz
S.append(('x01', 'L', 'capa (luz): o que é a fairhealth', luz(
    '<div class="feixe" style="left:300px;top:-420px;transform:rotate(28deg)"></div>',
    '<div class="feixe" style="left:560px;top:-460px;width:160px;transform:rotate(28deg);opacity:.7"></div>',
    '<div class="feixe" style="left:-40px;top:-380px;width:120px;transform:rotate(28deg);opacity:.5"></div>',
    '<div class="brilho" style="left:620px;top:-160px;width:720px;height:720px;opacity:.6"></div>') + '''
  <p class="pilula" style="left:96px;top:96px">Quem somos</p>
  <p class="luzt" style="left:96px;top:760px;width:900px;font-size:120px;line-height:120px">O que é a <span class="k">fairhealth</span>?</p>
  <p class="sub tclaro" style="left:96px;top:1030px;width:820px">O que somos, o que fazemos e o que oferecemos.</p>
  <p class="handle">@fairhealth.br</p>
  <p class="arr">Arraste para o lado →</p>'''))
# 2 · o que é: Venn com legenda em fio
S.append(('x02', 'c', 'o que é: Venn de prevenção, MEV e cuidado centrado na pessoa (posicionamento 3.1 e 3.7; one-pager)', '''<p class="rot">O que é</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Medicina preventiva <span class="k">dentro da empresa</span>.</p>
  <p class="corpo" style="left:96px;top:410px;width:860px;font-size:32px;line-height:42px">A solução de cuidado do ecossistema fairjob: atendimento individualizado, com tecnologia e acompanhamento contínuo.</p>
  ''' + venn()))
# 3 · cuidar antes: linha do tempo
S.append(('x03', 't', 'cuidar antes: linha do tempo (posicionamento: o que nos diferencia, diferenciais)', '''<p class="rot" style="color:var(--verde)">O que é</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Cuidar <span class="k">antes</span>.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <path d="M-20 640H1100" stroke="#1F3A36" stroke-opacity=".55" stroke-width="3"/>
    <path d="M150 640H560" stroke="#F0F0E9" stroke-width="16" stroke-linecap="round"/>
    <circle cx="150" cy="640" r="20" fill="#1F3A36"/>
    <path d="M560 616V664" stroke="#1F3A36" stroke-width="3"/>
    <circle cx="930" cy="640" r="18" fill="#96C5BD" stroke="#1F3A36" stroke-width="3"/>
  </svg>
  <p style="left:96px;top:480px;width:430px"><span style="display:block;font-size:36px;line-height:44px;font-weight:800">fairhealth</span><span style="display:block;font-size:28px;line-height:36px">atua antes, na prevenção</span></p>
  <p style="left:360px;top:690px;width:400px;text-align:center;font-size:28px;line-height:36px;font-style:italic">a doença aparece</p>
  <p style="right:96px;top:480px;width:430px;text-align:right"><span style="display:block;font-size:36px;line-height:44px;font-weight:800">plano de saúde</span><span style="display:block;font-size:28px;line-height:36px">trata depois</span></p>
  <div class="lista" style="top:860px">
    <p><b>Não é um benefício.</b> É uma infraestrutura de cuidado contínuo, não um programa pontual.</p>
  </div>'''))
# 4 · a base (luz)
S.append(('x04', 'L', 'a base é a MEV (luz; one-pager e posicionamento 3.4)', luz(
    '<div class="brilho" style="left:-200px;top:-260px;width:1000px;height:1000px;opacity:.5"></div>',
    '<div class="feixe" style="left:760px;top:-300px;width:200px;transform:rotate(-32deg);opacity:.55"></div>') + '''
  <p class="pilula" style="left:96px;top:96px">A base</p>
  <p class="luzt" style="left:96px;top:470px;width:900px;font-size:88px;line-height:96px">A base é a <span class="k">Medicina do Estilo de Vida</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:800px;width:860px">Uma abordagem baseada em evidências para prevenir e tratar doenças crônicas por meio de mudanças no estilo de vida.</p>
  <p class="nota tclaro" style="left:96px;top:1110px;width:888px;opacity:.8">Referências: American College of Lifestyle Medicine e Colégio Brasileiro de Medicina do Estilo de Vida.</p>'''))
# 5 · os seis pilares: rosca de fotos
S.append(('x05', 'c', 'os seis pilares: rosca de fotos com legenda em fio (one-pager)', '''<p class="rot">Os seis pilares</p>
  <p class="tit" style="left:96px;top:200px;width:888px">Seis pilares, com <span class="k">a pessoa no centro</span>.</p>
  ''' + rosca()))
# 6 · o que fazemos: fio com laço
S.append(('x06', 'v', 'o que fazemos: médicos e psicólogos (one-pager; posicionamento 3.3); o fio continua no slide 7', '''<p class="rot">O que fazemos</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Médicos e psicólogos <span class="k">dentro da empresa</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:410px;width:800px">Atendimento presencial, em plantões alternados. Diferente das soluções só digitais, o cuidado acontece perto de quem trabalha, e isso aumenta o engajamento.</p>
  ''' + fio(0)))
# 7 · o plano: passos no fio
S.append(('x07', 'c', 'cada pessoa recebe um plano de cuidado (one-pager; bordão do posicionamento 3.7)', '''<p class="rot">O que fazemos</p>
  <p class="tit" style="left:96px;top:200px;width:888px">Cada pessoa recebe um <span class="k">plano de cuidado</span>.</p>
  ''' + fio(1080) + '\n  ' + passos([
    ('Escuta', '“O que é importante para você?”'),
    ('Anamnese e medições', 'Coleta de dados com instrumentos digitais.'),
    ('Plano individualizado', 'Plano de ação personalizado e encaminhamento clínico.'),
    ('Acompanhamento', 'Contínuo, com médicos e psicólogos.')], 460, 185, '#1F3A36', '#F0F0E9', x_bola=136)))
# 8 · quatro frentes: cartões
S.append(('x08', 't', 'as quatro frentes em cartões (one-pager; posicionamento 3.0 e 3.4)', '''<p class="rot" style="color:var(--verde)">O que oferecemos</p>
  <p class="tit" style="left:96px;top:200px;width:888px">Quatro frentes,<br><span class="k">um cuidado só</span>.</p>
  <div class="cartao dest" style="top:410px"><span class="n">01</span><span class="w">Escritório do Cuidado<span class="chip">do último post</span></span><span class="d">Atendimento médico e psicológico presencial.</span></div>
  <div class="cartao" style="top:592px"><span class="n">02</span><span class="w">Programa de Medicina do Estilo de Vida</span><span class="d">Letramento e sensibilização.</span></div>
  <div class="cartao" style="top:774px"><span class="n">03</span><span class="w">Plataforma digital</span><span class="d">Prontuário, histórico e metas.</span></div>
  <div class="cartao" style="top:956px"><span class="n">04</span><span class="w">Wearables</span><span class="d">Monitoramento remoto contínuo e bioimpedância.</span></div>
  <p style="left:96px;top:1150px;width:888px;font-size:26px;line-height:34px">O Programa e o Escritório rendem mais juntos: um dá a base, o outro garante o acompanhamento.</p>'''))
# 9 · para a empresa
S.append(('x09', 'c', 'e para a empresa (one-pager; posicionamento, subpromessas)', '''<p class="rot">O que oferecemos</p>
  <p class="tit" style="left:96px;top:220px;width:888px">E para a <span class="k">empresa</span>?</p>
  <div class="lista" style="top:400px">
    <p><b>Prevenção de riscos psicossociais</b>, com programa e plataforma de indicadores (NR-1).</p>
    <p><b>Qualidade de vida, engajamento</b> e clima organizacional.</p>
    <p><b>Retenção de talentos</b> e uma marca empregadora mais forte.</p>
  </div>
'''))
# 10 · números (luz)
S.append(('x10', 'L', 'por que prevenir: números do one-pager, com as fontes (luz)', luz(
    '<div class="brilho" style="left:-160px;top:380px;width:900px;height:900px;opacity:.38"></div>',
    '<div class="feixe" style="left:820px;top:-360px;width:180px;transform:rotate(28deg);opacity:.5"></div>') + '''
  <p class="pilula" style="left:96px;top:96px">Por que prevenir</p>
  <p class="luzt" style="left:96px;top:250px;width:900px;font-size:80px;line-height:88px">Prevenção também é <span class="k">investimento</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:470px;width:888px">O que os estudos apontam:</p>
  <div class="dado" style="top:560px"><span class="n">−28%</span><span class="l">de absenteísmo<span class="f">Harvard Business Review, 2022</span></span></div>
  <div class="dado" style="top:800px;border-bottom:2px solid rgba(191,224,217,.25)"><span class="n">−22%</span><span class="l">de custos com saúde<span class="f">SHRM, 2023</span></span></div>'''))
# 11 · como começar
S.append(('x11', 't', 'como começar (one-pager, "Vem com a gente!")', '''<p class="rot" style="color:var(--verde)">Vem com a gente</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Como <span class="k">começar</span>.</p>
  ''' + passos([
    ('Diagnóstico gratuito', 'Uma reunião para mapear as necessidades da sua empresa.'),
    ('Proposta personalizada', 'Um programa sob medida para o seu time.'),
    ('Implementação', 'Onboarding e primeiros atendimentos.')], 420, 200, '#1F3A36', '#96C5BD', cor_fio='#F0F0E9')))
# 12 · fechamento com o traço que vira coração
S.append(('x12', 'c', 'assinatura: logo, slogan, convite e o traço que vira coração', '''<img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:460px;top:200px;width:160px;height:160px">
  <p class="tit" style="left:96px;top:430px;width:888px;text-align:center">Fazemos o certo pelos <span class="k">motivos certos</span>.</p>
  <p class="corpo" style="left:146px;top:650px;width:788px;text-align:center">Quer levar esse cuidado para a sua empresa? Fale com a gente pelo direct.</p>
  ''' + CORACAO))

html = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Carrossel v4: O que é a fairhealth</title><style>' + CSS + '</style></head><body>\n']
for k, (sid, cls, nota, corpo) in enumerate(S, 1):
    fim = '' if sid == 'x01' else '\n  <p class="handle">@fairhealth.br</p>\n  ' + pag(k)
    html.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  %s%s\n</section>\n\n' % (k, nota, cls, sid, corpo, fim))
html.append('</body></html>\n')
open(SAIDA, 'w').write(''.join(html))
print('ok', len(S))
