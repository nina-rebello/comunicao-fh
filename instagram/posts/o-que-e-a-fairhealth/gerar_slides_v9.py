# Gera slides-v9.html (12 slides, ids c01..c12). Uso: python3 gerar_slides_v9.py slides-v9.html
# v9 (12/10): fotos novas de sono e estresse; relacionamentos recortado para mostrar melhor as pessoas.
# v7 (12/10): "Diagnóstico" sem "gratuito" no slide 11.
# v6 (12/10): sem ícones no slide 9, sem o coração no 12 e sem a etiqueta "do último post" no 8.
# v5 (12/10): slides 3 e 9 no desenho da v2, trilha das três perguntas, rosca com 7 pilares, números sem brilho.
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
/* trilha das três perguntas (da v2) */
.trilha{left:96px;top:96px;width:888px;display:flex;gap:40px;font-size:20px;line-height:26px;font-weight:800;letter-spacing:.14em;text-transform:uppercase}
.trilha span{opacity:.42;padding-bottom:12px;border-bottom:4px solid transparent}
.trilha span.on{opacity:1}
.v .trilha span.on,.L .trilha span.on{border-color:var(--tif);color:var(--tif)}
.c .trilha span.on,.t .trilha span.on{border-color:var(--verde)}
/* ícones em quadrado tiffany (da v2) */
.ic{width:96px;height:96px;flex:none;border-radius:18px;background:var(--tif);display:flex;align-items:center;justify-content:center}
.ic svg{width:56px;height:56px;fill:none;stroke:var(--verde);stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.linha-ic{display:flex;gap:36px;align-items:center;padding:36px 0;border-top:2px solid rgba(31,58,54,.25)}
.linha-ic p{font-size:34px;line-height:44px}
.linha-ic b{font-weight:800}
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
.dado .n{font-size:150px;line-height:130px;font-weight:800;letter-spacing:-0.04em;color:var(--tif);width:400px;flex:none}
.dado .l{font-size:40px;line-height:50px}
.dado .f{display:block;font-size:22px;line-height:30px;color:var(--tclaro);opacity:.85;margin-top:8px}
'''

def trilha(i):
    nomes = ['O que é', 'O que fazemos', 'O que oferecemos']
    return '<div class="trilha">' + ''.join('<span class="on">%s</span>' % n if k == i else '<span>%s</span>' % n for k, n in enumerate(nomes, 1)) + '</div>'

ICONES = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <symbol id="i-graf" viewBox="0 0 48 48"><path d="M6 40h36"/><path d="M12 36V26M21 36V17M30 36V22M39 36V11"/></symbol>
  <symbol id="i-escudo" viewBox="0 0 48 48"><path d="M24 6l14 5v10c0 9-6 16-14 20-8-4-14-11-14-20V11z"/><path d="M18 23l4 4 8-8"/></symbol>
  <symbol id="i-rel" viewBox="0 0 48 48"><circle cx="17" cy="16" r="5"/><circle cx="31" cy="16" r="5"/><path d="M8 38c0-7 4-11 9-11s9 4 9 11"/><path d="M22 38c0-7 4-11 9-11s9 4 9 11"/></symbol>
  <symbol id="i-cor" viewBox="0 0 48 48"><path d="M24 39S10 31 10 20a7 7 0 0 1 14-3 7 7 0 0 1 14 3c0 11-14 19-14 19z"/></symbol>
</defs></svg>
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
CX, CY, R, r = 540, 780, 250, 118
PASSO = 360 / 7
PILARES = [  # (nº, nome com quebra, foto, alinhamento da foto, lado do rótulo), em sentido horário a partir de cima à direita
    ('01', 'Alimentação saudável', 'alimentacao-figos.jpg', 'xMidYMid', 'dir-cima'),
    ('02', 'Movimento', 'movimento-corrida.jpg', 'xMidYMid', 'dir'),
    ('03', 'Gerenciamento<br>de estresse', 'estresse-trigo-recorte.jpg', 'xMidYMid', 'dir-baixo'),
    ('04', 'Sono de qualidade', 'sono-homem-recorte.jpg', 'xMidYMid', 'baixo'),
    ('05', 'Relacionamentos', 'relacionamentos-parque-recorte.jpg', 'xMidYMid', 'esq-baixo'),
    ('06', 'Manejo<br>de vícios', 'vicios-passaros.jpg', 'xMidYMid', 'esq'),
    ('07', 'Espiritualidade e propósito', 'espiritualidade-maos.jpg', 'xMidYMid', 'esq-cima'),
]
ANG = [90 - PASSO * (3 - k) for k in range(7)]  # a fatia 04 fica embaixo, centrada

def rosca():
    defs, imgs, fios, legs = [], [], [], []
    linha = '<path d="M%s L%s%s" fill="none" stroke="#1F3A36" stroke-opacity=".45" stroke-width="2"/>'
    for k, ((n, nome, foto, alin, lado), ang) in enumerate(zip(PILARES, ANG)):
        a0, a1 = ang - PASSO / 2, ang + PASSO / 2
        d = setor(CX, CY, R, r, a0, a1)
        defs.append('<clipPath id="ps%d"><path d="%s"/></clipPath>' % (k, d))
        x, y, w, h = caixa(CX, CY, R, r, a0, a1)
        imgs.append('<image href="%s%s" x="%.0f" y="%.0f" width="%.0f" height="%.0f" preserveAspectRatio="%s slice" clip-path="url(#ps%d)" filter="url(#suave)"/>' % (FOTOS, foto, x - 4, y - 4, w + 8, h + 8, alin, k))
        x0, y0 = pol(CX, CY, R + 10, ang)
        if lado == 'baixo':
            fios.append(linha % (P(x0, y0), P(x0, y0 + 34), ''))
            legs.append('<p class="leg" style="left:%dpx;top:%dpx;width:400px;text-align:center"><span class="w">%s</span><span class="n" style="margin-top:6px">%s</span></p>' % (CX - 200, y0 + 44, nome, n))
        elif lado in ('dir', 'esq'):
            x1, y1 = pol(CX, CY, R + 40, ang)
            fios.append(linha % (P(x0, y0), P(x1, y1), ' H%d' % (984 if lado == 'dir' else 96)))
            if lado == 'dir':
                legs.append('<p class="leg" style="right:96px;top:%dpx;text-align:right"><span class="n">%s</span><span class="w">%s</span></p>' % (y1 - 74, n, nome))
            else:
                legs.append('<p class="leg" style="left:96px;top:%dpx"><span class="n">%s</span><span class="w">%s</span></p>' % (y1 - 110, n, nome))
        else:
            x1, y1 = pol(CX, CY, R + 52, ang)
            fios.append(linha % (P(x0, y0), P(x1, y1), ' H%d' % (984 if lado.startswith('dir') else 96)))
            al = 'right:96px;text-align:right' if lado.startswith('dir') else 'left:96px'
            if lado.endswith('cima'):
                legs.append('<p class="leg" style="%s;top:%dpx;width:440px"><span class="n">%s</span><span class="w">%s</span></p>' % (al, y1 - 74, n, nome))
            else:
                legs.append('<p class="leg" style="%s;top:%dpx;width:440px"><span class="w">%s</span><span class="n" style="margin-top:6px">%s</span></p>' % (al, y1 + 12, nome, n))
        fios.append('<circle cx="%.1f" cy="%.1f" r="5" fill="#1F3A36"/>' % (x0, y0))
    bordas = ''.join('<path d="%s"/>' % setor(CX, CY, R, r, a - PASSO / 2, a + PASSO / 2) for a in ANG)
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
S.append(('c01', 'L', 'capa (luz): o que é a fairhealth', luz(
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
S.append(('c02', 'c', 'o que é: Venn de prevenção, MEV e cuidado centrado na pessoa (posicionamento 3.1 e 3.7; one-pager)', trilha(1) + '''
  <p class="tit" style="left:96px;top:220px;width:888px">Medicina preventiva <span class="k">dentro da empresa</span>.</p>
  <p class="corpo" style="left:96px;top:410px;width:860px;font-size:32px;line-height:42px">A solução de cuidado do ecossistema fairjob: atendimento individualizado, com tecnologia e acompanhamento contínuo.</p>
  ''' + venn()))
# 3 · cuidar antes: linha do tempo
S.append(('c03', 'v', 'cuidar antes: linha do tempo da v2 (posicionamento: o que nos diferencia, tom de voz)', trilha(1) + '''
  <p class="tit" style="left:96px;top:220px;width:888px">Preventiva quer dizer cuidar <span class="k">antes</span>.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <path d="M110 700H970" stroke="#BFE0D9" stroke-opacity=".5" stroke-width="3"/>
    <path d="M940 686l30 14-30 14" fill="none" stroke="#BFE0D9" stroke-opacity=".5" stroke-width="3" stroke-linejoin="round"/>
    <g fill="#96C5BD"><circle cx="160" cy="700" r="14"/><circle cx="340" cy="700" r="14"/></g>
    <g fill="#1F3A36" stroke="#BFE0D9" stroke-opacity=".6" stroke-width="3"><circle cx="520" cy="700" r="12"/><circle cx="700" cy="700" r="12"/><circle cx="880" cy="700" r="12"/></g>
    <rect x="110" y="560" width="290" height="70" rx="35" fill="#96C5BD"/>
    <rect x="470" y="560" width="460" height="70" rx="35" fill="none" stroke="#BFE0D9" stroke-opacity=".55" stroke-width="2"/>
  </svg>
  <p style="left:110px;top:579px;width:290px;text-align:center;font-size:24px;line-height:32px;font-weight:800;color:var(--verde)">a fairhealth entra aqui</p>
  <p class="tclaro" style="left:470px;top:579px;width:460px;text-align:center;font-size:24px;line-height:32px">o plano de saúde entra aqui</p>
  <div style="left:70px;top:740px;width:940px;display:flex;font-size:24px;line-height:30px;text-align:center">
    <span style="width:180px;font-weight:800;color:var(--tif)">Rotina</span><span style="width:180px;font-weight:800;color:var(--tif)">Primeiros<br>sinais</span><span class="tclaro" style="width:180px">Diagnóstico</span><span class="tclaro" style="width:180px">Atestado</span><span class="tclaro" style="width:180px">Afastamento</span>
  </div>
  <p class="corpo tclaro" style="left:96px;top:930px;width:860px">Antes do diagnóstico, antes do atestado, antes do afastamento. O plano de saúde entra quando a doença já apareceu. <span style="color:var(--creme)">A gente entra antes.</span></p>'''))
# 4 · a base (luz)
S.append(('c04', 'L', 'a base é a MEV (luz; one-pager e posicionamento 3.4)', luz(
    '<div class="brilho" style="left:-200px;top:-260px;width:1000px;height:1000px;opacity:.5"></div>',
    '<div class="feixe" style="left:760px;top:-300px;width:200px;transform:rotate(-32deg);opacity:.55"></div>') + '''
  ''' + trilha(1) + '''
  <p class="luzt" style="left:96px;top:470px;width:900px;font-size:88px;line-height:96px">A base é a <span class="k">Medicina do Estilo de Vida</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:800px;width:860px">Uma abordagem baseada em evidências para prevenir e tratar doenças crônicas por meio de mudanças no estilo de vida.</p>
  <p class="nota tclaro" style="left:96px;top:1110px;width:888px;opacity:.8">Referências: American College of Lifestyle Medicine e Colégio Brasileiro de Medicina do Estilo de Vida.</p>'''))
# 5 · os seis pilares: rosca de fotos
S.append(('c05', 'c', 'os sete pilares: rosca de fotos com legenda em fio (one-pager + espiritualidade e propósito, decisão da Nina em 12/10)', trilha(1) + '''
  <p class="tit" style="left:96px;top:200px;width:888px">Sete pilares, com <span class="k">a pessoa no centro</span>.</p>
  ''' + rosca()))
# 6 · o que fazemos: fio com laço
S.append(('c06', 'v', 'o que fazemos: médicos e psicólogos (one-pager; posicionamento 3.3); o fio continua no slide 7', trilha(2) + '''
  <p class="tit" style="left:96px;top:220px;width:888px">Médicos e psicólogos <span class="k">dentro da empresa</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:410px;width:800px">Atendimento presencial, em plantões alternados. Diferente das soluções só digitais, o cuidado acontece perto de quem trabalha, e isso aumenta o engajamento.</p>
  ''' + fio(0)))
# 7 · o plano: passos no fio
S.append(('c07', 'c', 'cada pessoa recebe um plano de cuidado (one-pager; bordão do posicionamento 3.7)', trilha(2) + '''
  <p class="tit" style="left:96px;top:200px;width:888px">Cada pessoa recebe um <span class="k">plano de cuidado</span>.</p>
  ''' + fio(1080) + '\n  ' + passos([
    ('Escuta', '“O que é importante para você?”'),
    ('Anamnese e medições', 'Coleta de dados com instrumentos digitais.'),
    ('Plano individualizado', 'Plano de ação personalizado e encaminhamento clínico.'),
    ('Acompanhamento', 'Contínuo, com médicos e psicólogos.')], 460, 185, '#1F3A36', '#F0F0E9', x_bola=136)))
# 8 · quatro frentes: cartões
S.append(('c08', 't', 'as quatro frentes em cartões (one-pager; posicionamento 3.0 e 3.4)', trilha(3) + '''
  <p class="tit" style="left:96px;top:200px;width:888px">Quatro frentes,<br><span class="k">um cuidado só</span>.</p>
  <div class="cartao dest" style="top:410px"><span class="n">01</span><span class="w">Escritório do Cuidado</span><span class="d">Atendimento médico e psicológico presencial.</span></div>
  <div class="cartao" style="top:592px"><span class="n">02</span><span class="w">Programa de Medicina do Estilo de Vida</span><span class="d">Letramento e sensibilização.</span></div>
  <div class="cartao" style="top:774px"><span class="n">03</span><span class="w">Plataforma digital</span><span class="d">Prontuário, histórico e metas.</span></div>
  <div class="cartao" style="top:956px"><span class="n">04</span><span class="w">Wearables</span><span class="d">Monitoramento remoto contínuo e bioimpedância.</span></div>
  <p style="left:96px;top:1150px;width:888px;font-size:26px;line-height:34px">O Programa e o Escritório rendem mais juntos: um dá a base, o outro garante o acompanhamento.</p>'''))
# 9 · para a empresa
S.append(('c09', 'c', 'e para a empresa: linhas com fio, sem ícones (one-pager; posicionamento, subpromessas)', trilha(3) + '''
  <p class="tit" style="left:96px;top:220px;width:888px">E para a <span class="k">empresa</span>?</p>
  <div class="lista" style="top:420px">
    <p><b>Prevenção de riscos psicossociais</b> (NR-1), com programa e plataforma de indicadores.</p>
    <p><b>Qualidade de vida, engajamento</b> e clima organizacional.</p>
    <p><b>Um cuidado concreto</b>, que vai além dos benefícios tradicionais e fortalece a marca empregadora.</p>
  </div>'''))
# 10 · números (luz)
S.append(('c10', 'L', 'por que prevenir: números do one-pager, com as fontes (luz)', luz(
    '<div class="brilho" style="left:520px;top:-340px;width:900px;height:900px;opacity:.4"></div>',
    '<div class="feixe" style="left:820px;top:-360px;width:180px;transform:rotate(28deg);opacity:.5"></div>') + '''
  <p class="pilula" style="left:96px;top:96px">Por que prevenir</p>
  <p class="luzt" style="left:96px;top:250px;width:900px;font-size:80px;line-height:88px">Prevenção também é <span class="k">investimento</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:470px;width:888px">O que os estudos apontam:</p>
  <div class="dado" style="top:560px"><span class="n">−28%</span><span class="l">de absenteísmo<span class="f">Harvard Business Review, 2022</span></span></div>
  <div class="dado" style="top:800px;border-bottom:2px solid rgba(191,224,217,.25)"><span class="n">−22%</span><span class="l">de custos com saúde<span class="f">SHRM, 2023</span></span></div>'''))
# 11 · como começar
S.append(('c11', 't', 'como começar (one-pager, "Vem com a gente!")', '''<p class="rot" style="color:var(--verde)">Vem com a gente</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Como <span class="k">começar</span>.</p>
  ''' + passos([
    ('Diagnóstico', 'Uma reunião para mapear as necessidades da sua empresa.'),
    ('Proposta personalizada', 'Um programa sob medida para o seu time.'),
    ('Implementação', 'Onboarding e primeiros atendimentos.')], 420, 200, '#1F3A36', '#96C5BD', cor_fio='#F0F0E9')))
# 12 · fechamento com o traço que vira coração
S.append(('c12', 'c', 'assinatura: logo, slogan e convite', '''<img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:460px;top:300px;width:160px;height:160px">
  <p class="tit" style="left:96px;top:560px;width:888px;text-align:center">Fazemos o certo pelos <span class="k">motivos certos</span>.</p>
  <p class="corpo" style="left:146px;top:830px;width:788px;text-align:center">Quer levar esse cuidado para a sua empresa? Fale com a gente pelo direct.</p>'''))

html = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Carrossel v9: O que é a fairhealth</title><style>' + CSS + '</style></head><body>\n' + ICONES]
for k, (sid, cls, nota, corpo) in enumerate(S, 1):
    fim = '' if sid == 'c01' else '\n  <p class="handle">@fairhealth.br</p>\n  ' + pag(k)
    html.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  %s%s\n</section>\n\n' % (k, nota, cls, sid, corpo, fim))
html.append('</body></html>\n')
open(SAIDA, 'w').write(''.join(html))
print('ok', len(S))
