# Testes de design (19/10) do post de 21/10, com o conteúdo final (v6 do README). Pedido da Nina: "vamos testar
# designs. Em uma imagem só, crie vários carrosséis em uma única sequência (largura única e grande, com todos os
# slides juntos). Faça uma versão para cada design que vou enviar."
# Cinco referências, cinco versões. A versão A é a arte v7 (png-v7/), feita a partir da Eleken. Este gerador faz as
# outras quatro:
#   B · editorial com capítulos (template "Why We Started Our Business"): cabeçalho com capítulo e marca, foto em
#       moldura, caixa de citação, quadro com dois números, slide final escuro;
#   C · linha do tempo com hastes ("Life of a video editor"): fundo escuro, uma linha fina que atravessa os slides e,
#       nos marcos, bolinha e haste até o rótulo;
#   D · frase forte e linha reta ("The process that founders never talk about"): fundo escuro, frase no centro e uma
#       linha que nasce numa bolinha e sai pela borda;
#   E · palavra gigante e curva grossa ("O poder da sua pausa", nosso): creme, palavra enorme em caixa alta e a curva
#       Tiffany com patamares.
# Só Raleway, sem amarelo, com Tiffany. Fotos do banco Unsplash (fotos-banco/README.md), só para testar.
# Uso: python3 gerar_testes_design.py testes-design-slides.html
#      node ../../ferramentas/render.mjs testes-design-slides.html png-testes
#      python3 gerar_testes_design.py --montagem testes-design.html (página com as cinco faixas, para a imagem única)
import sys

N, W = 8, 1080
FB = '../../marca/fotos-banco/'
LOGO = '../../marca/logo-circulo.png'

# o conteúdo final (v6)
T1 = 'Antes de chegar às empresas, nossa história começou <span class="k">em um hospital</span>.'
T2 = 'Há quase 20 anos, percebemos que os pacientes estavam <span class="k">cada vez mais distantes do centro do cuidado</span>.'
A2 = 'Era preciso mudar essa realidade.'
T3 = 'Assim, dentro de um hospital, desenvolvemos o <span class="k">Escritório do Paciente</span> para mudar essa realidade.'
A3 = 'Com o tempo, levamos esse conceito para as empresas.'
T4 = 'Assim, desenvolvemos o <span class="k">Escritório do Cuidado</span>.'
A4 = 'Um espaço de acolhimento e de medicina preventiva dentro da empresa, que fortalece o cuidado centrado na pessoa.'
T5 = 'Tudo começa com uma pergunta: <span class="k">o que é importante para você?</span>'
A5 = 'Antes de qualquer exame, vem uma conversa: um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado.'
T6 = 'Levamos ao <span class="k">coração da sua empresa</span>:'
I6 = ['Atendimento médico e psicológico', 'Planos de cuidado individualizados, baseados na Medicina do Estilo de Vida',
      'Tecnologia, humanização e cuidado verdadeiro']
T7 = 'Porque, quando o cuidado está perto, <span class="k">ele acontece</span>.'
A7 = 'A maior barreira ao cuidado é tempo e acesso. Por isso, o Escritório do Cuidado fica dentro da empresa, perto da rotina de quem trabalha.'
T8 = 'Nosso propósito é promover <span class="k">qualidade de vida, engajamento e um ambiente de trabalho mais saudável</span>.'
A8 = 'Com resultados demonstrados por indicadores.'
F8 = 'Faça o certo pelos motivos certos.'
CTA = 'Conheça a fairhealth no link da bio.'

CSS = r'''
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:400;font-style:italic;src:url(../../marca/fontes/raleway-latin-400-italic.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--tif:#96C5BD;--verde:#1F3A36;--creme:#F0F0E9;--tclaro:#BFE0D9;--vlogo:#2F6B64;--noite:#14241F}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#888;display:flex;flex-wrap:wrap;gap:40px;padding:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-variant-numeric:lining-nums}
.slide>*{position:absolute}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.k{font-weight:800;font-style:italic}

/* B · editorial */
.Bc{background:var(--creme);color:var(--verde)} .Bt{background:var(--tif);color:var(--verde)} .Bd{background:var(--verde);color:var(--creme)}
.Bd .k{color:var(--tif)}
.Bh{left:96px;right:96px;top:84px;display:flex;justify-content:space-between;font-size:20px;line-height:26px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.Bh span:last-child{letter-spacing:0;text-transform:none;font-size:24px}
.Bregua{left:96px;right:96px;top:128px;height:2px;background:currentColor;opacity:.35}
.Bcol{left:96px;width:888px}
.Bcol h2{font-size:54px;line-height:62px;font-weight:800;letter-spacing:-0.01em}
.Bcol h2 .k{font-weight:800}
.Bcol p{font-size:30px;line-height:44px;margin-top:26px}
.Bd .Bcol p{color:var(--tclaro)}
.Bcita{margin-top:40px;padding:26px 32px;border-left:8px solid var(--verde);background:rgba(150,197,189,.35);font-size:30px;line-height:42px}
.Bnums{display:flex;border:2px solid var(--verde);margin-top:40px}
.Bnums div{flex:1;padding:26px 32px}
.Bnums div+div{border-left:2px solid var(--verde)}
.Bnums b{display:block;font-size:64px;line-height:70px;font-weight:800}
.Bnums span{display:block;font-size:18px;line-height:24px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;margin-top:6px}
.Blista{margin-top:34px}
.Blista div{display:flex;gap:28px;padding:22px 0;border-top:2px solid rgba(31,58,54,.25);font-size:32px;line-height:42px}
.Blista b{font-weight:800;color:var(--vlogo);min-width:52px}
.Bfoto{overflow:hidden;border:4px solid var(--verde);padding:14px;background:var(--creme)}
.Bfoto img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.8)}
.Brod{font-size:20px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;border-bottom:2px solid currentColor;padding-bottom:6px}

/* C · linha do tempo com hastes */
.Cs{background:radial-gradient(ellipse at 50% 45%,#22413C,#14241F 75%);color:var(--creme)}
.Cs .k{color:var(--tif)}
.Ctop{left:0;width:1080px;top:76px;text-align:center;font-size:22px;line-height:28px;color:var(--tclaro)}
.Ctit{left:90px;width:900px;text-align:center;font-size:54px;line-height:64px;letter-spacing:-0.01em}
.Crot{width:320px;text-align:center;font-size:22px;line-height:30px;font-weight:800;letter-spacing:.06em;text-transform:uppercase}
.Cap{left:130px;width:820px;text-align:center;font-size:28px;line-height:40px;color:var(--tclaro)}
.Crod{left:96px;top:1212px;font-size:22px;line-height:28px}
.Crod span{display:block;color:rgba(191,224,217,.6)}
.Cpil{right:96px;top:1210px;border:1.5px solid rgba(240,240,233,.5);border-radius:28px;padding:10px 24px;font-size:22px;line-height:28px}

/* D · frase forte e linha reta */
.Ds{background:#121D1B;color:var(--creme)}
.Ds .k,.Dk{font-weight:800;font-style:normal}
.Dpo{inset:0;background-image:radial-gradient(rgba(240,240,233,.35) 1px,transparent 1.5px);background-size:137px 151px;opacity:.5}
.Dtit{left:176px;width:760px;font-size:62px;line-height:66px;letter-spacing:-0.035em}
.Dap{left:176px;width:740px;font-size:28px;line-height:40px;color:rgba(240,240,233,.72)}
.Drod{left:96px;top:1236px;font-size:20px;line-height:26px;color:rgba(240,240,233,.5)}
.Dpg{right:96px;top:1236px;font-size:20px;line-height:26px;color:rgba(240,240,233,.5)}

/* E · palavra gigante e curva */
.Es{background:var(--creme);color:var(--verde)}
.Es .k{color:var(--vlogo)}
.Ecol{left:96px;top:110px;width:888px}
.Ecol .pq{font-size:44px;line-height:50px;font-weight:800;letter-spacing:.05em;text-transform:uppercase}
.Ecol .gig{font-size:220px;line-height:.92;font-weight:800;letter-spacing:-0.01em;text-transform:uppercase;white-space:nowrap;margin-top:6px}
.Ecol .par{font-size:34px;line-height:46px;width:700px;margin-top:30px}
.Ecol .tag{font-size:22px;line-height:30px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--vlogo);margin-top:28px}
.Ecol ul{list-style:none;margin-top:30px;width:760px}
.Ecol li{font-size:32px;line-height:44px;padding-left:34px;position:relative}
.Ecol li+li{margin-top:16px}
.Ecol li::before{content:'';position:absolute;left:0;top:16px;width:14px;height:14px;border-radius:50%;background:var(--tif)}
.Erot{font-size:26px;line-height:32px;color:var(--vlogo);text-align:center;width:300px}
.Erod{left:96px;top:1236px;font-size:24px;line-height:32px}
'''


def pag(k):
    return '%02d/%02d' % (k, N)


# ------------------------------------------------------------------ B · editorial
def b_cab(cap, dir_='fairhealth', regua=False):
    return '<div class="Bh"><span>%s</span><span>%s</span></div>%s' % (cap, dir_, '\n  <div class="Bregua"></div>' if regua else '')


B = [
    ('b1', 'Bt', '''<p style="left:0;width:1080px;top:96px;text-align:center;font-size:22px;line-height:28px;font-weight:800;letter-spacing:.2em">NOSSA HISTÓRIA</p>
  <div class="Bfoto" style="left:250px;top:180px;width:580px;height:560px"><img src="%sconversa2.jpg" alt=""></div>
  <p style="left:110px;width:860px;top:800px;text-align:center;font-size:56px;line-height:64px;font-weight:800;letter-spacing:-0.01em">%s</p>
  <p style="left:0;width:1080px;top:1040px;text-align:center;font-size:24px;line-height:32px">2009 → hoje · por que a fairhealth existe?</p>
  <p style="left:0;width:1080px;top:1230px;text-align:center;font-size:22px;line-height:28px;font-weight:800">Arraste para ler →</p>''' % (FB, T1)),
    ('b2', 'Bc', b_cab('01 · O porquê', '2009') + '''
  <p style="left:84px;top:180px;font-size:230px;line-height:220px;font-weight:800;letter-spacing:-0.04em;color:var(--tif)">2009</p>
  <div class="Bcol" style="top:470px"><h2>%s</h2><div class="Bcita"><b style="font-weight:800">fairhealth</b> · %s</div></div>''' % (T2, A2)),
    ('b3', 'Bd', b_cab('02 · No hospital', 'Desde 2009') + '''
  <div style="left:96px;top:160px;width:888px;height:430px;overflow:hidden"><img src="%smaos.jpg" alt="" style="width:100%%;height:100%%;object-fit:cover;filter:saturate(.8)"></div>
  <div class="Bcol" style="top:640px"><h2>%s</h2><p>%s</p></div>
  <p class="Brod" style="right:96px;top:1180px">No hospital, onde tudo começou</p>''' % (FB, T3, A3)),
    ('b4', 'Bc', b_cab('03 · Hoje', regua=True) + '''
  <div class="Bcol" style="top:240px"><h2 style="font-size:64px;line-height:72px">%s</h2><p>%s</p>
  <div class="Bnums" style="margin-top:110px"><div><b>2009</b><span>No hospital</span></div><div><b>Hoje</b><span>Nas empresas</span></div></div></div>''' % (T4, A4)),
    ('b5', 'Bt', b_cab('04 · O acolhimento') + '''
  <div class="Bcol" style="top:250px"><h2 style="font-size:46px;line-height:54px">Tudo começa com uma pergunta:</h2>
  <p style="font-size:84px;line-height:92px;font-weight:800;font-style:italic;letter-spacing:-0.01em;margin-top:30px">“O que é importante para você?”</p>
  <p style="margin-top:50px">%s</p></div>''' % A5),
    ('b6', 'Bc', b_cab('05 · O que levamos', regua=True) + '''
  <div class="Bcol" style="top:240px"><h2 style="font-size:64px;line-height:72px">%s</h2>
  <div class="Blista">%s</div></div>''' % (T6, ''.join('<div><b>%02d</b><span>%s</span></div>' % (i + 1, t) for i, t in enumerate(I6)))),
    ('b7', 'Bt', b_cab('06 · Perto') + '''
  <div class="Bcol" style="top:200px"><h2 style="font-size:60px;line-height:68px">%s</h2><p>%s</p></div>
  <div class="Bfoto" style="left:96px;top:700px;width:888px;height:440px"><img src="%scafe-notebook.jpg" alt=""></div>''' % (T7, A7, FB)),
    ('b8', 'Bd', '''<p style="left:0;width:1080px;top:110px;text-align:center;font-size:20px;line-height:26px;font-weight:800;letter-spacing:.16em">07 · O PROPÓSITO</p>
  <p style="left:130px;width:820px;top:240px;text-align:center;font-size:72px;line-height:80px;font-weight:800;letter-spacing:-0.01em">%s</p>
  <div style="left:500px;top:520px;width:80px;height:3px;background:var(--tif)"></div>
  <p style="left:150px;width:780px;top:570px;text-align:center;font-size:30px;line-height:44px;color:var(--tclaro)">%s %s</p>
  <img src="%s" alt="fairhealth" style="left:470px;top:870px;width:140px;height:140px">
  <p style="left:0;width:1080px;top:1050px;text-align:center;font-size:24px;line-height:32px">%s</p>''' % (F8, T8, A8, LOGO, CTA)),
]

# ------------------------------------------------------------------ C · linha do tempo com hastes
CY = 840  # altura da linha


def c_haste(x, rot, y, anel=False, larg=320):
    bola = ('<circle cx="%d" cy="%d" r="11" fill="#14241F" stroke="#96C5BD" stroke-width="3.5"/>' % (x, CY) if anel
            else '<circle cx="%d" cy="%d" r="8" fill="#96C5BD"/>' % (x, CY))
    return ('<svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><path d="M%d %dV%d" stroke="rgba(240,240,233,.7)" stroke-width="2"/>%s</svg>\n  '
            '<p class="Crot" style="left:%dpx;top:%dpx;width:%dpx">%s</p>' % (x, y + 40, CY - (11 if anel else 8), bola, x - larg // 2, y, larg, rot))


def c_linha(ate=1080):
    return ('<svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><defs><linearGradient id="cl" x1="0" x2="1">'
            '<stop offset="0" stop-color="#96C5BD" stop-opacity=".55"/><stop offset=".5" stop-color="#96C5BD"/><stop offset="1" stop-color="#96C5BD" stop-opacity=".55"/></linearGradient>'
            '<filter id="brilho"><feGaussianBlur stdDeviation="4"/></filter></defs>'
            '<path d="M0 %dH%d" stroke="#96C5BD" stroke-opacity=".5" stroke-width="6" filter="url(#brilho)"/>'
            '<path d="M0 %dH%d" stroke="url(#cl)" stroke-width="2.5"/></svg>' % (CY, ate, CY, ate))


def c_slide(sid, tit, hastes, ap='', ap_top=900, rod_dir='Arraste ›', extra=''):
    return (sid, 'Cs', c_linha() + '\n  <p class="Ctop">@fairhealth.br</p>\n  <p class="Ctit" style="top:190px">%s</p>\n  %s\n  %s%s'
            '\n  <p class="Crod">fairhealth<span>o cuidado começa pela pessoa</span></p>\n  <p class="Cpil">%s</p>'
            % (tit, ''.join(c_haste(*h) for h in hastes), ('<p class="Cap" style="top:%dpx">%s</p>' % (ap_top, ap)) if ap else '', extra, rod_dir))


C = [
    c_slide('c1', T1, [(220, '2009<br>no hospital', 600), (540, 'Por que a fairhealth existe?', 540, True), (860, 'Hoje<br>nas empresas', 600)]),
    c_slide('c2', T2, [(540, 'Há quase 20 anos', 600, True)], A2),
    c_slide('c3', T3, [(540, 'Escritório do Paciente', 600, True)], A3),
    c_slide('c4', T4, [(540, 'Hoje · nas empresas', 600, True)], A4),
    c_slide('c5', T5, [(540, 'O acolhimento', 600, True)], A5),
    c_slide('c6', T6, [(200, I6[0], 470, False, 300), (540, I6[1], 470, True, 300), (880, I6[2], 470, False, 300)]),
    c_slide('c7', T7, [(540, 'Perto da rotina', 600, True)], A7),
    ('c8', 'Cs', c_linha(470) + '''
  <p class="Ctop">@fairhealth.br</p>
  <p class="Ctit" style="top:190px">%s</p>
  <p class="Cap" style="top:470px">%s</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><circle cx="540" cy="%d" r="72" fill="#F0F0E9" stroke="#96C5BD" stroke-width="3"/></svg>
  <img src="%s" alt="fairhealth" style="left:480px;top:%dpx;width:120px;height:120px">
  <p class="Cap" style="top:950px;color:var(--creme);font-weight:800;font-size:34px;line-height:44px">%s</p>
  <p class="Cap" style="top:1010px">%s</p>
  <p class="Crod">fairhealth<span>o cuidado começa pela pessoa</span></p>
  <p class="Cpil">Compartilhe ›</p>''' % (T8, A8, CY, LOGO, CY - 60, F8, CTA)),
]

# ------------------------------------------------------------------ D · frase forte e linha reta
DY = 720


def d_linha(k, ini=0, fim=1080, bola=None):
    s = '<svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><path d="M%d %dH%d" stroke="#F0F0E9" stroke-width="4"/>' % (ini, DY, fim)
    if bola:
        s += '<circle cx="%d" cy="%d" r="%d" fill="#96C5BD"/>' % bola
    return s + '</svg>'


def d_slide(sid, k, tit, ap='', bola=None, ini=0, fim=1080, extra=''):
    return (sid, 'Ds', '<div class="Dpo"></div>\n  ' + d_linha(k, ini, fim, bola) +
            '\n  <p class="Dtit" style="bottom:%dpx">%s</p>%s%s\n  <p class="Drod">@fairhealth.br</p>\n  <p class="Dpg">%s</p>'
            % (1350 - DY + 50, tit, ('\n  <p class="Dap" style="top:%dpx">%s</p>' % (DY + 54, ap)) if ap else '', extra, pag(k)))


D = [
    d_slide('d1', 1, T1, bola=(520, DY, 26), ini=520),
    d_slide('d2', 2, T2, A2, bola=(176, DY, 12)),
    d_slide('d3', 3, T3, A3, bola=(176, DY, 12)),
    d_slide('d4', 4, T4, A4, bola=(176, DY, 12)),
    d_slide('d5', 5, T5, A5, bola=(176, DY, 12)),
    d_slide('d6', 6, T6, '<br>'.join('<span style="color:var(--tif);font-weight:800">%02d</span>&nbsp;&nbsp;%s' % (i + 1, t) for i, t in enumerate(I6)), bola=(176, DY, 12)),
    d_slide('d7', 7, T7, A7, bola=(176, DY, 12)),
    d_slide('d8', 8, T8, A8, bola=(176, DY, 12), fim=820, extra='''
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><circle cx="890" cy="%d" r="70" fill="#F0F0E9"/></svg>
  <img src="%s" alt="fairhealth" style="left:832px;top:%dpx;width:116px;height:116px">
  <p class="Dtit" style="top:900px;font-size:40px;line-height:48px;font-weight:800">%s</p>
  <p class="Dap" style="top:970px">%s</p>''' % (DY, LOGO, DY - 58, F8, CTA)),
]

# ------------------------------------------------------------------ E · palavra gigante e curva com patamares
BAIXO, ALTO = 1120, 990


def curva_e():
    # em cada slide: baixo até 300, sobe até 460, alto até 760, desce até 920 (no último, sobe e chega ao logo)
    d = 'M0 %d' % BAIXO
    for k in range(N):
        o = k * W
        d += ' H%d C%d %d %d %d %d %d' % (o + 300, o + 380, BAIXO, o + 380, ALTO, o + 460, ALTO)
        if k < N - 1:
            d += ' H%d C%d %d %d %d %d %d' % (o + 760, o + 840, ALTO, o + 840, BAIXO, o + 920, BAIXO)
        else:
            d += ' H%d' % (o + 700)
    return d


CURVA = curva_e()


def e_curva(k, rotulos=()):
    s = ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#96C5BD" stroke-width="16" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>' % ((k - 1) * W, CURVA))
    for x, y, t in rotulos:
        s += '\n  <p class="Erot" style="left:%dpx;top:%dpx">%s</p>' % (x - 150, y, t)
    return s


def e_slide(sid, k, pq, gig, par='', tag='', lista=None, rotulos=(), extra=''):
    corpo = '<div class="Ecol"><p class="pq">%s</p><p class="gig">%s</p>' % (pq, gig)
    if par:
        corpo += '<p class="par">%s</p>' % par
    if lista:
        corpo += '<ul>%s</ul>' % ''.join('<li>%s</li>' % t for t in lista)
    if tag:
        corpo += '<p class="tag">%s</p>' % tag
    corpo += '</div>'
    return (sid, 'Es', e_curva(k, rotulos) + '\n  ' + corpo + extra + '\n  <p class="Erod">@fairhealth.br</p>')


E = [
    e_slide('e1', 1, 'Antes de chegar às empresas, nossa', 'História', 'começou <span class="k">em um hospital</span>.', '2009 → hoje · por que a fairhealth existe?', rotulos=[(610, 938, '2009')]),
    e_slide('e2', 2, 'Há quase', '20 anos,', 'percebemos que os pacientes estavam <span class="k">cada vez mais distantes do centro do cuidado</span>. ' + A2, rotulos=[(610, 938, 'o porquê')]),
    e_slide('e3', 3, 'Assim, dentro de um', 'hospital,', 'desenvolvemos o <span class="k">Escritório do Paciente</span> para mudar essa realidade. ' + A3, 'Escritório do Paciente', rotulos=[(610, 938, 'no hospital')]),
    e_slide('e4', 4, 'Assim, desenvolvemos o Escritório do', 'Cuidado.', A4, 'Hoje · dentro da sua empresa', rotulos=[(610, 938, 'hoje')]),
    e_slide('e5', 5, 'Tudo começa com uma', 'pergunta:', '<span class="k">o que é importante para você?</span> ' + A5, rotulos=[(610, 938, 'a conversa')]),
    e_slide('e6', 6, 'Levamos ao coração da sua', 'empresa:', lista=I6, rotulos=[(610, 938, 'o que levamos')]),
    e_slide('e7', 7, 'Porque, quando o cuidado está', 'perto,', '<span class="k">ele acontece</span>. ' + A7, rotulos=[(610, 938, 'perto')]),
    e_slide('e8', 8, 'Nosso', 'propósito', 'é promover <span class="k">qualidade de vida, engajamento e um ambiente de trabalho mais saudável</span>. ' + A8, F8, extra='''
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><circle cx="776" cy="%d" r="76" fill="#F0F0E9" stroke="#96C5BD" stroke-width="16"/></svg>
  <img src="%s" alt="fairhealth" style="left:716px;top:%dpx;width:120px;height:120px">
  <p class="Erot" style="left:484px;top:1110px;width:584px">conheça a fairhealth no link da bio</p>''' % (ALTO, LOGO, ALTO - 60)),
]

# a palavra gigante ocupa a largura da coluna (ajuste depois que a fonte carrega)
AJUSTE = '''<script>
document.fonts.ready.then(() => {
  for (const g of document.querySelectorAll('.gig')) {
    let t = 220;
    g.style.fontSize = t + 'px';
    while (g.scrollWidth > 888 && t > 60) { t -= 4; g.style.fontSize = t + 'px'; }
  }
});
</script>'''


def html_slides():
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Testes de design (21/10)</title><style>' + CSS + '</style></head><body>\n']
    for grupo in (B, C, D, E):
        for sid, cls, corpo in grupo:
            out.append('<section class="slide %s" id="%s">\n  %s\n</section>\n' % (cls, sid, corpo))
    out.append(AJUSTE + '\n</body></html>\n')
    return ''.join(out)


FAIXAS = [('A', 'Caminho largo · referência Eleken (arte v7)', 'png-v7/v%02d.png'),
          ('B', 'Editorial com capítulos · referência "Why We Started Our Business"', 'png-testes/b%d.png'),
          ('C', 'Linha do tempo com hastes · referência "Life of a video editor"', 'png-testes/c%d.png'),
          ('D', 'Frase forte e linha reta · referência "The process that founders never talk about"', 'png-testes/d%d.png'),
          ('E', 'Palavra gigante e curva · referência "O poder da sua pausa"', 'png-testes/e%d.png')]


def html_montagem():
    esc = 0.4
    w, h = round(1080 * esc), round(1350 * esc)
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Testes de design (21/10)</title><style>'
           '@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}'
           '@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}'
           '*{margin:0;padding:0;box-sizing:border-box}body{background:#ECECE6;font-family:Raleway,sans-serif;padding:60px;width:%dpx}'
           'h1{font-size:40px;font-weight:800;color:#1F3A36;margin-bottom:10px}h1+p{font-size:22px;color:#2F6B64;margin-bottom:40px}'
           '.faixa{margin-bottom:56px}.faixa h2{font-size:28px;font-weight:800;color:#1F3A36;margin-bottom:14px}'
           '.faixa h2 span{display:inline-block;width:46px;height:46px;border-radius:50%%;background:#1F3A36;color:#F0F0E9;text-align:center;line-height:46px;margin-right:14px}'
           '.seq{display:flex;gap:3px;background:#B8B8B0;padding:3px;width:max-content}.seq img{width:%dpx;height:%dpx;display:block}'
           '</style></head><body>\n<h1>Por que a fairhealth existe? · testes de design</h1>'
           '<p>Post de 21/10, conteúdo final. Cada faixa é um carrossel inteiro, com os 8 slides lado a lado.</p>\n' % (8 * w + 7 * 3 + 6 + 120, w, h)]
    for letra, nome, padrao in FAIXAS:
        imgs = ''.join('<img src="%s" alt="">' % (padrao % k) for k in range(1, N + 1))
        out.append('<div class="faixa"><h2><span>%s</span>%s</h2><div class="seq">%s</div></div>\n' % (letra, nome, imgs))
    out.append('</body></html>\n')
    return ''.join(out)


if sys.argv[1] == '--montagem':
    open(sys.argv[2], 'w').write(html_montagem())
else:
    open(sys.argv[1], 'w').write(html_slides())
print('ok')
