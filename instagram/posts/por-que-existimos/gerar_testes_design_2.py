# Testes de design, rodada 2 (19/10), do post de 21/10, com o conteúdo final (conteudo_v6.py). Mesmo pedido da
# rodada 1: uma imagem só, cada carrossel numa faixa com os 8 slides lado a lado, uma versão por referência.
#   F · "Jornada" (Jornada de conteúdo imobiliário): fundo escuro, blocos de cor na capa, um objeto grande (aqui, o
#       coração da marca), número do slide em cima, título em cor de destaque, medidor em meia-lua, lista com
#       ícones, foto em cartão arredondado; final com o objeto, a frase e os ícones do Instagram;
#   G · "Toda empresa começa com uma história": caixa alta enorme e apertada, etiqueta inclinada, ilustrações em
#       traço (aqui, ícones grandes em traço fino, sem personagens), texto em itálico centralizado, slide escuro com
#       trechos sublinhados, foto com papel rasgado e bilhete, final em caixa alta;
#   H · Polina (processo de trabalho), fiel à referência: papel com textura, linha fina com um laço, números grandes
#       ao lado das bolinhas, texto grande, anotações, cabeçalho e rodapé discretos.
# Só Raleway, sem amarelo, Tiffany em destaque. Fotos do banco Unsplash e o render do espaço, só para testar.
# Uso: python3 gerar_testes_design_2.py testes-design-2-slides.html
#      node ../../ferramentas/render.mjs testes-design-2-slides.html png-testes-2
#      python3 gerar_testes_design_2.py --montagem testes-design-2.html
import sys
from conteudo_v6 import T1, T2, A2, T3, A3, T4, A4, T5, A5, T6, I6, T7, A7, T8, A8, F8, CTA

N, W = 8, 1080
FB = '../../marca/fotos-banco/'
CORACAO = '../../marca/logo-coracao.png'
LOGO = '../../marca/logo-circulo.png'

# ícones Lucide (licença ISC), em traço
IC = {
    'coracao': ['M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z'],
    'escudo': ['M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z', 'm9 12 2 2 4-4'],
    'predio': ['M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z', 'M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2', 'M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2',
               'M10 6h4', 'M10 10h4', 'M10 14h4', 'M10 18h4'],
    'estetoscopio': ['M11 2v2', 'M5 2v2', 'M5 3H4a2 2 0 0 0-2 2v4a6 6 0 0 0 12 0V5a2 2 0 0 0-2-2h-1', 'M8 15a6 6 0 0 0 12 0v-3',
                     'M18 10a2 2 0 1 0 4 0a2 2 0 1 0-4 0'],
    'prancheta': ['M9 2h6a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1V3a1 1 0 0 1 1-1z', 'M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2',
                  'M12 11h4', 'M12 16h4', 'M8 11h.01', 'M8 16h.01'],
    'relogio': ['M6 12a6 6 0 1 0 12 0a6 6 0 1 0-12 0', 'M12 10v2l1 1', 'm16.13 7.66-.81-4.05a2 2 0 0 0-2-1.61h-2.68a2 2 0 0 0-2 1.61l-.78 4.05',
                'm7.88 16.36.8 4a2 2 0 0 0 2 1.61h2.72a2 2 0 0 0 2-1.61l.81-4.05'],
    'conversa': ['M7.9 20A9 9 0 1 0 4 16.1L2 22Z'],
    'enviar': ['M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z', 'm21.854 2.147-10.94 10.939'],
    'salvar': ['m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16z'],
    'hospital': ['M12 6v4', 'M14 14h-4', 'M14 18h-4', 'M14 8h-4', 'M18 12h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2',
                 'M18 22V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v18'],
    'pino': ['M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0', 'M9 10a3 3 0 1 0 6 0a3 3 0 1 0-6 0'],
}


def icone(nome, x, y, tam, cor, traco=1.6, extra=''):
    return ('<svg aria-hidden="true" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx%s" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (x, y, tam, tam, extra, cor, traco, ''.join('<path d="%s"/>' % d for d in IC[nome])))


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
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.k{font-weight:800;font-style:italic}

/* F · jornada */
.Fs{background:var(--verde);color:var(--creme)}
.Fs .k{color:var(--tif)}
.Fn{right:96px;top:70px;font-size:76px;line-height:80px;font-weight:800}
.Fcab{left:96px;top:190px;width:430px;font-size:46px;line-height:54px;font-weight:800;color:var(--tif)}
.Fcorpo{left:96px;width:430px;font-size:30px;line-height:42px}
.Fcorpo p+p{margin-top:20px;color:var(--tclaro)}
.Flista{left:96px;width:430px}
.Flista div{display:flex;align-items:center;gap:22px;font-size:26px;line-height:34px;margin-top:20px}
.Flista svg{flex:none;width:46px;height:46px}
.Ffoto{left:580px;top:420px;width:404px;height:700px;border-radius:30px;overflow:hidden}
.Ffoto img{width:100%;height:100%;object-fit:cover;filter:saturate(.85)}
.Fmed{left:600px;top:190px;width:300px;height:170px}

/* G · toda empresa começa com uma história */
.Gc{background:var(--creme);color:var(--verde)} .Gt{background:var(--tif);color:var(--verde)} .Gd{background:var(--verde);color:var(--creme)}
.Gd .k{color:var(--tif)}
.Gcab{left:96px;right:96px;top:84px;display:flex;justify-content:space-between;font-size:18px;line-height:24px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}
.Ggig{left:80px;width:920px;font-weight:800;text-transform:uppercase;letter-spacing:-0.035em;line-height:.92}
.Gmini{font-size:21px;line-height:30px;letter-spacing:.06em;text-transform:uppercase;text-align:justify}
.Gu{text-decoration:underline;text-decoration-thickness:3px;text-underline-offset:8px}
.Gd .Gu{text-decoration-color:var(--tif)}
.Gnota{background:#FBFBF6;color:var(--verde);padding:30px 34px;font-size:26px;line-height:36px;font-style:italic;box-shadow:0 10px 30px rgba(0,0,0,.25)}

/* H · Polina */
.Hs{background:var(--creme);color:var(--verde)}
.Hs .k{color:var(--vlogo)}
.Hpapel{inset:0;opacity:.55;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='360'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .55 0 0 0 0 .53 0 0 0 0 .48 0 0 0 -1.1 .85'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"),
    repeating-linear-gradient(0deg,rgba(31,58,54,.04) 0 1px,transparent 1px 4px),
    repeating-linear-gradient(90deg,rgba(31,58,54,.035) 0 1px,transparent 1px 4px)}
.Htopo{top:96px;font-size:24px;line-height:30px;font-weight:800;color:var(--tif)}
.Hrod{left:96px;top:1236px;font-size:24px;line-height:30px;font-weight:800;color:var(--tif)}
.Hrod span{font-weight:400}
.Hcab{font-size:58px;line-height:66px;font-weight:800;color:var(--vlogo);letter-spacing:-0.01em}
.Htxt{font-size:40px;line-height:52px}
.Htxt2{font-size:34px;line-height:46px}
.Hnum{font-size:72px;line-height:72px;font-weight:800;color:var(--vlogo)}
.Hnota{font-size:28px;line-height:36px;font-style:italic;color:var(--vlogo)}
.Hlista li{list-style:none;font-size:36px;line-height:48px;padding-left:34px;position:relative}
.Hlista li+li{margin-top:18px}
.Hlista li::before{content:'';position:absolute;left:0;top:18px;width:14px;height:14px;border-radius:50%;background:var(--tif)}
'''


# ------------------------------------------------------------------ F · jornada
def medidor(frac, rot):
    import math
    cx, cy, r = 150, 150, 118
    ang = math.pi * (1 - frac)
    x, y = cx + r * math.cos(ang), cy - r * math.sin(ang)
    return ('<svg class="Fmed" viewBox="0 0 300 170" aria-hidden="true"><path d="M32 150A118 118 0 0 1 268 150" fill="none" stroke="#F0F0E9" stroke-width="40"/>'
            '<path d="M32 150A118 118 0 0 1 %.1f %.1f" fill="none" stroke="#96C5BD" stroke-width="40"/>'
            '<text x="150" y="140" text-anchor="middle" font-family="Raleway" font-size="34" font-weight="800" fill="#F0F0E9">%s</text></svg>' % (x, y, rot))


def f_lista(itens):
    return '<div class="Flista" style="top:%dpx">%s</div>' % (itens[0], ''.join(
        '<div>%s<span>%s</span></div>' % ('<svg viewBox="0 0 24 24" fill="none" stroke="#96C5BD" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
                                         % ''.join('<path d="%s"/>' % d for d in IC[ic]), t) for ic, t in itens[1]))


def f_slide(k, cab, corpo, foto, frac, rot, top_corpo=260, lista=None, foto_estilo=''):
    s = '<p class="Fn">%d</p>\n  %s\n  <p class="Fcab">%s</p>\n  <div class="Fcorpo" style="top:%dpx">%s</div>' % (k, medidor(frac, rot), cab, top_corpo, corpo)
    if lista:
        s += '\n  ' + f_lista(lista)
    s += '\n  <div class="Ffoto"%s><img src="%s" alt=""></div>' % (foto_estilo, foto)
    return ('f%d' % k, 'Fs', s)


F = [
    ('f1', 'Fs', '''<div style="left:0;top:0;width:170px;height:150px;background:var(--tif)"></div>
  <div style="left:0;top:420px;width:170px;height:930px;background:var(--tif)"></div>
  <div style="left:50px;top:190px;width:330px;height:470px;border-radius:30px;background:var(--creme)"></div>
  <img src="%s" alt="fairhealth" style="left:120px;top:250px;width:560px;height:484px;transform:rotate(-7deg)">
  <p style="left:240px;top:830px;width:760px;font-size:64px;line-height:70px;font-weight:800;font-style:italic">%s</p>
  <p style="left:240px;top:1130px;font-size:26px;line-height:34px;color:var(--tif);font-weight:800">2009 → hoje · por que a fairhealth existe?</p>''' % (CORACAO, T1.replace('class="k"', 'style="color:var(--tif)"'))),
    f_slide(2, 'O porquê:<br>2009', '<p>%s</p><p>%s</p>' % (T2, A2), FB + 'retrato.jpg', 1 / 6, '1/6', 390),
    f_slide(3, 'No hospital:<br>o Escritório do Paciente', '<p>%s</p><p>%s</p>' % (T3, A3), FB + 'maos.jpg', 2 / 6, '2/6', 390),
    f_slide(4, 'Hoje:<br>o Escritório do Cuidado', '<p>%s</p><p>%s</p>' % (T4, A4), '../../marca/espaco/sala-atendimento-e-espera.jpg', 3 / 6, '3/6', 390,
            lista=(880, [('coracao', 'Acolhimento'), ('escudo', 'Medicina preventiva'), ('predio', 'Dentro da empresa')])),
    f_slide(5, 'O acolhimento:<br>uma pergunta', '<p>%s</p><p>%s</p>' % (T5, A5), FB + 'conversa2.jpg', 4 / 6, '4/6', 390),
    f_slide(6, 'O que levamos:<br>ao coração da empresa', '<p>%s</p>' % T6, '../../marca/objetos/smartband.png', 5 / 6, '5/6', 390,
            lista=(470, [('estetoscopio', I6[0]), ('prancheta', I6[1]), ('relogio', I6[2])]), foto_estilo=' style="background:var(--tif)"'),
    f_slide(7, 'Perto:<br>dentro da rotina', '<p>%s</p><p>%s</p>' % (T7, A7), FB + 'cafe-notebook.jpg', 6 / 6, '6/6', 390),
    ('f8', 'Fs', '''<img src="%s" alt="fairhealth" style="left:600px;top:120px;width:400px;height:346px;transform:rotate(8deg)">
  <p style="left:96px;top:560px;width:888px;font-size:70px;line-height:78px;font-weight:800">%s</p>
  <p style="left:96px;top:740px;width:820px;font-size:30px;line-height:42px;color:var(--tclaro)">%s %s</p>
  <p style="left:96px;top:950px;width:820px;font-size:30px;line-height:42px;color:var(--tif);font-weight:800">%s</p>
  %s%s%s%s''' % (CORACAO, F8, T8.replace('class="k"', 'style="font-weight:800;color:var(--creme)"'), A8, CTA,
                 icone('coracao', 96, 1100, 56, '#F0F0E9'), icone('conversa', 186, 1100, 56, '#F0F0E9'),
                 icone('enviar', 276, 1100, 56, '#F0F0E9'), icone('salvar', 366, 1100, 56, '#F0F0E9'))),
]

# ------------------------------------------------------------------ G · toda empresa começa com uma história
def g_cab(esq='@fairhealth.br', dir_='nossa história'):
    return '<div class="Gcab"><span>%s</span><span>%s</span></div>' % (esq, dir_)


RASGO = ('<svg aria-hidden="true" style="left:0;top:0;width:90px;height:1350px" viewBox="0 0 90 1350" preserveAspectRatio="none">'
         '<path d="M0 0H52L38 60L60 120L34 190L58 250L40 320L66 380L36 450L56 520L30 590L54 660L38 730L62 800L34 870L58 940L36 1010L60 1080L32 1150L56 1220L40 1290L52 1350H0Z" fill="#1F3A36"/></svg>')

G = [
    ('g1', 'Gc', '''%s
  <p class="Ggig" style="top:150px;font-size:112px">Antes de chegar às empresas, nossa história começou em um hospital.</p>
  <p style="left:120px;top:1080px;background:var(--verde);color:var(--creme);padding:16px 30px;font-size:30px;line-height:36px;font-weight:800;letter-spacing:.04em;transform:rotate(-5deg)">2009 → HOJE</p>''' % icone('hospital', 700, 40, 300, '#2F6B64', 0.9, ';opacity:.85')),
    ('g2', 'Gt', g_cab() + '''
  <p style="left:150px;top:300px;width:780px;text-align:center;font-size:46px;line-height:60px;font-style:italic">%s</p>
  <p class="Gmini" style="left:200px;top:640px;width:680px">%s</p>
  %s''' % (T2.replace('class="k"', 'style="font-weight:800"'), A2, icone('conversa', 300, 780, 480, '#1F3A36', 0.7, ';opacity:.18'))),
    ('g3', 'Gd', g_cab() + '''
  %s
  <p style="left:96px;top:360px;width:820px;font-size:52px;line-height:66px">Assim, dentro de um hospital, desenvolvemos o <span class="Gu k">Escritório do Paciente</span> para <span class="Gu">mudar essa realidade</span>.</p>
  <p class="Gmini" style="left:96px;top:900px;width:780px;color:var(--tclaro)">%s</p>''' % (icone('estetoscopio', 96, 160, 150, '#96C5BD', 1.1), A3)),
    ('g4', 'Gd', '''<img src="../../marca/espaco/sala-atendimento-e-espera.jpg" alt="" style="left:0;top:0;width:1080px;height:1350px;object-fit:cover;filter:saturate(.85)">
  <div style="inset:0;background:linear-gradient(180deg,rgba(20,36,31,.65),rgba(20,36,31,.2) 45%,rgba(20,36,31,.7))"></div>
  ''' + RASGO + '''
  <p class="Ggig" style="left:120px;top:150px;font-size:200px;color:var(--creme)">Hoje,</p>
  <p style="left:120px;top:360px;width:800px;font-size:50px;line-height:62px;font-weight:800;color:var(--creme)">desenvolvemos o <span class="Gu">Escritório do Cuidado</span>.</p>
  <p class="Gnota" style="left:560px;top:880px;width:420px;transform:rotate(5deg)">%s</p>
  <div style="left:700px;top:858px;width:120px;height:36px;background:rgba(150,197,189,.85);transform:rotate(-3deg)"></div>''' % A4),
    ('g5', 'Gc', g_cab() + '''
  <p style="left:96px;top:200px;width:888px;font-size:44px;line-height:56px">Tudo começa com uma pergunta:</p>
  <p class="Ggig" style="top:290px;font-size:118px">O que é importante para você?</p>
  <p class="Gmini" style="left:96px;top:880px;width:888px">%s</p>
  %s''' % (A5, icone('coracao', 820, 1040, 160, '#2F6B64', 1.1))),
    ('g6', 'Gt', g_cab() + '''
  <p class="Ggig" style="top:200px;font-size:84px;letter-spacing:-0.02em">Levamos ao coração da sua empresa:</p>
  %s''' % ''.join('<p style="left:96px;top:%dpx;width:888px;font-size:36px;line-height:48px;border-top:2px solid rgba(31,58,54,.35);padding-top:22px"><b style="font-weight:800;margin-right:24px">%02d</b>%s</p>' % (560 + i * 160, i + 1, t) for i, t in enumerate(I6))),
    ('g7', 'Gd', g_cab() + '''
  %s
  <p style="left:96px;top:380px;width:860px;font-size:56px;line-height:70px">Porque, quando o cuidado está perto, <span class="Gu k">ele acontece</span>.</p>
  <p class="Gmini" style="left:96px;top:740px;width:820px;color:var(--tclaro)">%s</p>''' % (icone('pino', 96, 170, 150, '#96C5BD', 1.1), A7)),
    ('g8', 'Gt', '''<p style="left:0;width:1080px;top:84px;text-align:center;font-size:20px;line-height:26px;font-weight:800;letter-spacing:.1em">LINK NA BIO | @FAIRHEALTH.BR</p>
  <p class="Ggig" style="top:300px;font-size:128px">Faça o certo pelos motivos certos.</p>
  <img src="%s" alt="fairhealth" style="left:730px;top:640px;width:260px;height:224px;transform:rotate(10deg)">
  <p class="Gmini" style="left:150px;top:1030px;width:780px">%s %s</p>''' % (CORACAO, T8.replace('<span class="k">', '').replace('</span>', ''), A8)),
]

# ------------------------------------------------------------------ H · Polina
HPONTOS = [
    (230, 640), (300, 780), (420, 870), (560, 860), (640, 790), (610, 710), (530, 700), (500, 780), (560, 880), (720, 980), (900, 1080), (1080, 1120),
    (1240, 1090), (1380, 1000), (1680, 1060), (1900, 1010), (2160, 900),
    (2300, 780), (2380, 560), (2460, 400), (2700, 380), (2980, 470), (3160, 580), (3240, 640),
    (3420, 740), (3720, 900), (4000, 960), (4320, 860),
    (4500, 940), (4620, 1000), (4700, 930), (4670, 850), (4590, 840), (4560, 920), (4620, 1020), (4920, 1100), (5200, 1020), (5400, 900),
    (5700, 880), (6100, 1000), (6480, 940),
    (6880, 1050), (7280, 900), (7480, 640), (7560, 520),
    (7760, 640), (7860, 760), (7980, 1000), (8160, 1120), (8276, 1130),
]
HBOLAS = [(1380, 1000), (2460, 400), (3720, 900), (4920, 1100), (5700, 880), (6880, 1050), (7860, 760)]
HLOGO = (8340, 1130)


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


HLINHA = caminho(HPONTOS)


def h_slide(k, corpo):
    linha = ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#2F6B64" stroke-width="3" stroke-linecap="round"/>%s'
             '<circle cx="%d" cy="%d" r="64" fill="#F0F0E9" stroke="#2F6B64" stroke-width="3"/></svg>'
             % ((k - 1) * W, HLINHA, ''.join('<circle cx="%d" cy="%d" r="12" fill="#2F6B64"/>' % b for b in HBOLAS), HLOGO[0], HLOGO[1]))
    seta = ('<svg aria-hidden="true" style="left:864px;top:1236px;width:120px;height:30px" viewBox="0 0 120 30"><path d="M0 15H116M104 4L117 15L104 26" fill="none" '
            'stroke="#96C5BD" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>') if k < N else ''
    return ('h%d' % k, 'Hs', '<div class="Hpapel"></div>\n  %s\n  <p class="Htopo" style="left:96px">@fairhealth.br</p>\n  <p class="Htopo" style="right:96px;font-weight:400">nossa história</p>\n  %s\n  <p class="Hrod">fairhealth <span>| o cuidado começa pela pessoa</span></p>%s'
            % (linha, corpo, ('\n  ' + seta) if seta else ''))


H = [
    h_slide(1, '''<p class="Hcab" style="left:96px;top:190px;width:700px">Por que a fairhealth existe?</p>
  <p class="Htxt" style="left:96px;top:350px;width:640px">%s</p>
  <p class="Hnota" style="left:290px;top:612px">2009 → hoje</p>''' % T1),
    h_slide(2, '''<p class="Htxt" style="left:96px;top:200px;width:888px">%s</p>
  <p class="Htxt2" style="left:96px;top:400px;width:888px">%s</p>
  <p class="Hnum" style="left:330px;top:890px">01</p>
  <p class="Hnota" style="left:330px;top:1030px">2009</p>''' % (T2, A2)),
    h_slide(3, '''<p class="Hnum" style="left:330px;top:290px">02</p>
  <p class="Hnota" style="left:330px;top:430px">no hospital</p>
  <p class="Htxt" style="left:400px;top:650px;width:584px">%s</p>
  <p class="Htxt2" style="left:400px;top:940px;width:584px">%s</p>''' % (T3, A3)),
    h_slide(4, '''<p class="Htxt" style="left:96px;top:200px;width:888px;font-size:48px;line-height:60px">%s</p>
  <p class="Htxt2" style="left:96px;top:350px;width:888px">%s</p>
  <p class="Hnum" style="left:510px;top:790px">03</p>
  <p class="Hnota" style="left:620px;top:812px">hoje, nas empresas</p>''' % (T4, A4)),
    h_slide(5, '''<p class="Htxt" style="left:96px;top:200px;width:888px;font-size:44px;line-height:56px">%s</p>
  <p class="Htxt2" style="left:96px;top:350px;width:888px">%s</p>
  <p class="Hnota" style="left:450px;top:800px">sem pressa e sem julgamento</p>
  <p class="Hnum" style="left:630px;top:990px">04</p>''' % (T5, A5)),
    h_slide(6, '''<p class="Htxt" style="left:96px;top:200px;width:888px;font-size:48px;line-height:60px">%s</p>
  <ul class="Hlista" style="left:96px;top:330px;width:860px">%s</ul>
  <p class="Hnum" style="left:330px;top:770px">05</p>''' % (T6, ''.join('<li>%s</li>' % t for t in I6))),
    h_slide(7, '''<p class="Htxt" style="left:96px;top:200px;width:640px;font-size:44px;line-height:56px">%s</p>
  <p class="Htxt2" style="left:96px;top:400px;width:640px">%s</p>
  <p class="Hnum" style="left:430px;top:940px">06</p>
  <p class="Hnota" style="left:430px;top:1080px">dentro da empresa</p>''' % (T7, A7)),
    h_slide(8, '''<p class="Hnota" style="left:384px;top:200px;width:600px;text-align:right">a gente tá aqui pra te ouvir</p>
  <p class="Hcab" style="left:284px;top:250px;width:700px;text-align:right">%s</p>
  <p class="Htxt2" style="left:284px;top:430px;width:700px;text-align:right">%s %s</p>
  <p class="Hnum" style="left:330px;top:650px">07</p>
  <img src="%s" alt="fairhealth" style="left:%dpx;top:%dpx;width:108px;height:108px">
  <p class="Hnota" style="left:384px;top:1020px;width:600px;text-align:right">conheça a fairhealth no link da bio</p>''' % (F8, T8, A8, LOGO, HLOGO[0] - 7 * W - 54, HLOGO[1] - 54)),
]

AJUSTE = '''<script>
document.fonts.ready.then(() => {
  for (const g of document.querySelectorAll('.Ggig')) {
    let t = parseFloat(getComputedStyle(g).fontSize);
    while (g.scrollWidth > g.clientWidth + 1 && t > 40) { t -= 2; g.style.fontSize = t + 'px'; }
  }
});
</script>'''


def html_slides():
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Testes de design 2 (21/10)</title><style>' + CSS + '</style></head><body>\n']
    for grupo in (F, G, H):
        for sid, cls, corpo in grupo:
            out.append('<section class="slide %s" id="%s">\n  %s\n</section>\n' % (cls, sid, corpo))
    out.append(AJUSTE + '\n</body></html>\n')
    return ''.join(out)


FAIXAS = [('F', 'Jornada · referência "Jornada de conteúdo imobiliário"', 'png-testes-2/f%d.png'),
          ('G', 'Caixa alta e papel rasgado · referência "Toda empresa começa com uma história"', 'png-testes-2/g%d.png'),
          ('H', 'Papel, linha e números · referência Polina (processo de trabalho)', 'png-testes-2/h%d.png')]


def html_montagem():
    esc = 0.4
    w, h = round(1080 * esc), round(1350 * esc)
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Testes de design 2 (21/10)</title><style>'
           '@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}'
           '@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}'
           '*{margin:0;padding:0;box-sizing:border-box}body{background:#ECECE6;font-family:Raleway,sans-serif;padding:60px;width:%dpx}'
           'h1{font-size:40px;font-weight:800;color:#1F3A36;margin-bottom:10px}h1+p{font-size:22px;color:#2F6B64;margin-bottom:40px}'
           '.faixa{margin-bottom:56px}.faixa h2{font-size:28px;font-weight:800;color:#1F3A36;margin-bottom:14px}'
           '.faixa h2 span{display:inline-block;width:46px;height:46px;border-radius:50%%;background:#1F3A36;color:#F0F0E9;text-align:center;line-height:46px;margin-right:14px}'
           '.seq{display:flex;gap:3px;background:#B8B8B0;padding:3px;width:max-content}.seq img{width:%dpx;height:%dpx;display:block}'
           '</style></head><body>\n<h1>Por que a fairhealth existe? · testes de design, rodada 2</h1>'
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
