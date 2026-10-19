# Arte v1 (19/10) do post de qua 21/10, "Por que a fairhealth existe?", conteúdo v3 (README.md desta pasta).
# Duplicado de nossa-historia/gerar_slides_v2.py, a arte do post da origem que a Nina aprovou: capa de luz, fio
# creme contínuo, "2009" grande, Tiffany como cor principal. O que muda:
#   - 7 slides (entra o slide do acolhimento, "Antes de qualquer exame, uma conversa");
#   - o slide do acolhimento tem uma foto num círculo por onde o fio passa (maos.jpg, Unsplash, 75% de saturação);
#   - o slide do Escritório do Cuidado tem "Hoje" grande, no mesmo modelo do "2009": são dois projetos, cada um no
#     seu tempo e no seu lugar (etiquetas "No hospital" e "Nas empresas");
#   - fundos: luz, Tiffany, verde, Tiffany, verde, Tiffany, verde (o fio creme aparece em todos).
# Uso: python3 gerar_slides.py slides.html && node ../../ferramentas/render.mjs slides.html png
#
# Elemento gráfico: um fio contínuo que atravessa os sete slides (a trajetória de 2009 até hoje). Ele nasce
# num ponto na capa, marca 2009 e hoje com uma bolinha, passa pela foto do acolhimento e termina no logo.
import sys

SAIDA = sys.argv[1]
N = 7
W = 1080

CSS = r'''
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:400;font-style:italic;src:url(../../marca/fontes/raleway-latin-400-italic.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--tif:#96C5BD;--verde:#1F3A36;--creme:#F0F0E9;--tclaro:#BFE0D9;--vlogo:#2F6B64;--noite:#0D1816}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#888;display:flex;flex-wrap:wrap;gap:40px;padding:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-variant-numeric:lining-nums}
.slide>*{position:absolute}
.v{background:var(--verde);color:var(--creme)}
.c{background:var(--creme);color:var(--verde)}
.L{background:var(--noite);color:var(--creme)}
.t{background:var(--tif);color:var(--verde)}
.t .rot{color:var(--verde)}
.t .pag i{background:var(--creme)} .t .pag i.on{background:var(--verde)}
.t .ano{color:var(--verde)}
.k{font-weight:800;font-style:italic}
.v .k,.L .k{color:var(--tif);-webkit-text-fill-color:var(--tif)}
.rot{left:96px;top:96px;font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.v .rot{color:var(--tif)} .c .rot{color:var(--vlogo)}
.tit{font-size:72px;line-height:80px;letter-spacing:-0.01em}
.corpo{font-size:36px;line-height:48px}
.nota{font-size:26px;line-height:34px}
.tclaro{color:var(--tclaro)}
.ano{font-size:240px;line-height:220px;font-weight:800;letter-spacing:-0.04em;color:var(--tif)}
.marco{font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.handle{left:96px;top:1238px;font-size:24px;line-height:32px}
.v .handle,.L .handle{color:var(--tclaro)}
.arr{right:96px;top:1238px;font-size:24px;line-height:32px;color:var(--tclaro)}
.pag{right:96px;top:1248px;display:flex;gap:8px}
.pag i{display:block;width:20px;height:12px;border-radius:6px}
.pag i.on{width:48px}
.v .pag i,.L .pag i{background:rgba(191,224,217,.3)} .v .pag i.on,.L .pag i.on{background:var(--tif)}
.c .pag i{background:var(--tif)} .c .pag i.on{background:var(--verde)}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.feixe{width:240px;height:2000px;background:linear-gradient(180deg,rgba(150,197,189,0),rgba(150,197,189,.55) 45%,rgba(150,197,189,0));filter:blur(40px);transform-origin:center}
.brilho{border-radius:50%;background:radial-gradient(circle,rgba(150,197,189,.55),rgba(150,197,189,0) 65%);filter:blur(30px)}
.grao{inset:0;opacity:.22;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='320' height='320'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.vinheta{inset:0;background:radial-gradient(ellipse at 50% 40%,rgba(13,24,22,0) 35%,rgba(13,24,22,.85) 100%)}
.luzt{font-weight:400;letter-spacing:-0.015em;background:linear-gradient(180deg,#F7F7F2,#B9C9C5);-webkit-background-clip:text;background-clip:text;color:transparent}
.pilula{border:2px solid rgba(240,240,233,.85);border-radius:999px;padding:16px 40px;font-size:24px;line-height:30px;letter-spacing:.16em;text-transform:uppercase;white-space:nowrap}
'''

# ---------------------------------------------------------------- o fio (coordenadas dos seis slides lado a lado)
# Pontos de passagem; a curva passa por todos (Catmull-Rom convertida em Bézier cúbica).
PONTOS = [(120, 1150), (620, 1120), (1080, 1040), (1500, 1090), (1900, 1110), (2300, 1030), (2760, 950),
          (3240, 900), (3560, 930), (3960, 960), (4320, 980), (4800, 1000), (5150, 940), (5400, 1000),
          (5800, 1090), (6100, 1110), (6480, 1040), (6800, 1000), (6948, 980)]
INICIO, DOIS_MIL_E_NOVE, FOTO_C, HOJE = PONTOS[0], PONTOS[4], PONTOS[9], PONTOS[15]
FIM = (7020, 980)        # centro do logo no slide 7 (x local 540)
R_FOTO = 160             # círculo da foto do acolhimento (slide 4), centrado no fio
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

FIO = caminho(PONTOS)

def fio(k, extra=''):
    return ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#F0F0E9" '
            'stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>%s</svg>') % ((k - 1) * W, FIO, extra)

def bola(p, cor='#F0F0E9', r=16):
    return '<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (p[0], p[1], r, cor)

def pag(i):
    return '<div class="pag">' + ''.join('<i class="on"></i>' if j == i else '<i></i>' for j in range(1, N + 1)) + '</div>'

def luz(*partes):
    return '\n  '.join(partes) + '\n  <div class="vinheta"></div>\n  <div class="grao"></div>'

S = []
# 1 · capa (luz): o fio nasce aqui
S.append(('e01', 'L', 'capa: a história começa num hospital; o fio nasce num ponto e atravessa o carrossel', luz(
    '<div class="feixe" style="left:300px;top:-420px;transform:rotate(28deg)"></div>',
    '<div class="feixe" style="left:560px;top:-460px;width:160px;transform:rotate(28deg);opacity:.7"></div>',
    '<div class="feixe" style="left:-40px;top:-380px;width:120px;transform:rotate(28deg);opacity:.5"></div>',
    '<div class="brilho" style="left:620px;top:-160px;width:720px;height:720px;opacity:.6"></div>') + '''
  <p class="pilula" style="left:96px;top:96px">Nossa história</p>
  <p class="luzt" style="left:96px;top:520px;width:900px;font-size:92px;line-height:100px">Antes de chegar às empresas, nossa história começou <span class="k">em um hospital</span>.</p>
  ''' + fio(1, bola(INICIO, '#96C5BD')) + '''
  <p class="marco" style="left:96px;top:1062px;color:var(--tif)">2009 → hoje</p>
  <p class="handle">@fairhealth.br</p>
  <p class="arr">Arraste para o lado →</p>'''))
# 2 · 2009, no hospital: o Escritório do Paciente
S.append(('e02', 't', '2009, no hospital: o Escritório do Paciente e o porquê (roteiro do reel do Dr. Ronald)', '''<p class="rot">No hospital</p>
  <p class="ano" style="left:84px;top:200px">2009</p>
  <p class="tit" style="left:96px;top:470px;width:888px">Dentro de um hospital, surgiu o <span class="k">Escritório do Paciente</span>.</p>
  <p class="corpo" style="left:96px;top:740px;width:860px">Um modelo de cuidado criado para trazer o paciente de volta ao centro, com a escuta, o acolhimento e as necessidades de cada pessoa em primeiro lugar.</p>
  ''' + fio(2, bola(DOIS_MIL_E_NOVE, '#1F3A36')) + '''
  <p class="marco" style="left:%dpx;top:%dpx;color:var(--verde)">2009</p>''' % (DOIS_MIL_E_NOVE[0] - W - 40, DOIS_MIL_E_NOVE[1] + 34)))
# 3 · a essência
S.append(('e03', 'v', 'a essência: a pessoa por trás de cada atendimento', '''<p class="rot">A essência</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Por trás de cada atendimento, existe <span class="k">uma pessoa</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:500px;width:860px">Com a sua própria história, hábitos, necessidades e prioridades.</p>
  <p class="corpo tclaro" style="left:96px;top:660px;width:860px">Por isso, escutar sempre foi parte essencial da nossa maneira de cuidar.</p>
  ''' + fio(3)))
# 4 · o acolhimento: o fio passa por uma foto em círculo
FB = '../../marca/fotos-banco/'
fx, fy = FOTO_C[0] - 3 * W, FOTO_C[1]
foto = ('<defs><clipPath id="ce04"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>'
        '<filter id="se04"><feColorMatrix type="saturate" values=".75"/></filter></defs>'
        '<image href="{foto}" x="{ix}" y="{iy}" width="{iw}" height="{ih}" preserveAspectRatio="xMidYMid slice" clip-path="url(#ce04)" filter="url(#se04)"/>'
        '<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#F0F0E9" stroke-width="12"/>').format(
    cx=FOTO_C[0], cy=FOTO_C[1], r=R_FOTO, foto=FB + 'maos.jpg', ix=FOTO_C[0] - 240, iy=FOTO_C[1] - R_FOTO, iw=480, ih=2 * R_FOTO)
S.append(('e04', 't', 'o acolhimento: antes de qualquer exame, uma conversa; o fio passa pela foto', '''<p class="rot">O acolhimento</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Antes de qualquer exame, <span class="k">uma conversa</span>.</p>
  <p class="corpo" style="left:96px;top:480px;width:860px">Um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado.</p>
  ''' + fio(4, foto)))
# 5 · evolução: o fio sobe
S.append(('e05', 'v', 'evolução: o conceito chega ao trabalho; quando o cuidado está perto, ele acontece', '''<p class="rot">Evolução</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Com o tempo, essa forma de cuidar <span class="k">evoluiu</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:480px;width:860px">E o conceito chegou a um lugar que faz parte da rotina das pessoas: <span style="font-weight:800;color:var(--creme)">o trabalho</span>. Porque, quando o cuidado está perto, ele acontece.</p>
  ''' + fio(5)))
# 6 · hoje, nas empresas: o Escritório do Cuidado (outro projeto, inspirado no primeiro)
S.append(('e06', 't', 'hoje, nas empresas: o Escritório do Cuidado, um projeto novo inspirado no Escritório do Paciente', '''<p class="rot">Nas empresas</p>
  <p class="ano" style="left:84px;top:200px">Hoje</p>
  <p class="tit" style="left:96px;top:470px;width:888px">Assim surgiu o <span class="k">Escritório do Cuidado</span>, da fairhealth.</p>
  <p class="corpo" style="left:96px;top:690px;width:888px;font-size:32px;line-height:44px">Um projeto novo, inspirado no Escritório do Paciente e pensado para as empresas: um espaço de acolhimento e de medicina preventiva, com cuidado individualizado e acompanhamento.</p>
  ''' + fio(6, bola(HOJE, '#1F3A36', 18)) + '''
  <p class="marco" style="left:%dpx;top:%dpx;color:var(--verde)">Hoje</p>''' % (HOJE[0] - 5 * W - 36, HOJE[1] + 34)))
# 7 · o propósito: o fio termina no logo
S.append(('e07', 'v', 'o propósito: os lugares mudaram, a essência permanece; o fio termina no logo', '''<p class="rot">O propósito</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Os lugares mudaram. <span class="k">A essência do cuidado permanece.</span></p>
  <p class="corpo tclaro" style="left:96px;top:500px;width:860px">Do hospital às empresas, seguimos com um mesmo princípio: <span style="font-weight:800;color:var(--creme)">o cuidado começa pela pessoa.</span></p>
  ''' + fio(7, bola(FIM, '#F0F0E9', R_LOGO)) + '''
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">''' % (
    FIM[0] - 6 * W - 60, FIM[1] - 60, 120, 120)))

html = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe?</title><style>' + CSS + '</style></head><body>\n']
for k, (sid, cls, nota, corpo) in enumerate(S, 1):
    fim = '' if sid == 'e01' else '\n  <p class="handle">@fairhealth.br</p>\n  ' + pag(k)
    html.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  %s%s\n</section>\n\n' % (k, nota, cls, sid, corpo, fim))
html.append('</body></html>\n')
open(SAIDA, 'w').write(''.join(html))
print('ok', len(S))
