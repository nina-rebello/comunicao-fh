# Gera slides.html: post 02 do calendário de 12 posts, "Antes de chegar às empresas, nossa história começou em
# um hospital". Proposta de roteiro da Nina (13/10), com os ajustes do README desta pasta.
# Uso: python3 gerar_slides.py slides.html
#
# Elemento gráfico: um fio contínuo que atravessa os seis slides (a trajetória de 2009 até hoje). Ele nasce
# num ponto na capa, marca 2009 e hoje com uma bolinha e termina no logo, no último slide.
import sys

SAIDA = sys.argv[1]
N = 6
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
PONTOS = [(120, 1150), (620, 1120), (1080, 1030), (1500, 1090), (1900, 1110), (2300, 1020), (2760, 950),
          (3240, 890), (3700, 810), (4180, 850), (4560, 1000), (4900, 1090), (5300, 1010), (5600, 980), (5868, 980)]
INICIO, DOIS_MIL_E_NOVE, HOJE = PONTOS[0], PONTOS[4], PONTOS[11]
FIM = (5940, 980)        # centro do logo no slide 6 (x local 540)
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
    return ('<svg class="cheia" viewBox="%d 0 1080 1350" aria-hidden="true"><path d="%s" fill="none" stroke="#96C5BD" '
            'stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>%s</svg>') % ((k - 1) * W, FIO, extra)

def bola(p, cor='#96C5BD', r=16):
    return '<circle cx="%.1f" cy="%.1f" r="%d" fill="%s"/>' % (p[0], p[1], r, cor)

def pag(i):
    return '<div class="pag">' + ''.join('<i class="on"></i>' if j == i else '<i></i>' for j in range(1, N + 1)) + '</div>'

def luz(*partes):
    return '\n  '.join(partes) + '\n  <div class="vinheta"></div>\n  <div class="grao"></div>'

S = []
# 1 · capa (luz): o fio nasce aqui
S.append(('h01', 'L', 'capa: a história começa num hospital; o fio nasce num ponto e atravessa o carrossel', luz(
    '<div class="feixe" style="left:300px;top:-420px;transform:rotate(28deg)"></div>',
    '<div class="feixe" style="left:560px;top:-460px;width:160px;transform:rotate(28deg);opacity:.7"></div>',
    '<div class="feixe" style="left:-40px;top:-380px;width:120px;transform:rotate(28deg);opacity:.5"></div>',
    '<div class="brilho" style="left:620px;top:-160px;width:720px;height:720px;opacity:.6"></div>') + '''
  <p class="pilula" style="left:96px;top:96px">Nossa história</p>
  <p class="luzt" style="left:96px;top:520px;width:900px;font-size:92px;line-height:100px">Antes de chegar às empresas, nossa história começou <span class="k">em um hospital</span>.</p>
  ''' + fio(1, bola(INICIO)) + '''
  <p class="marco tclaro" style="left:96px;top:1062px">2009 → hoje</p>
  <p class="handle">@fairhealth.br</p>
  <p class="arr">Arraste para o lado →</p>'''))
# 2 · 2009
S.append(('h02', 'v', 'o início: 2009, o Escritório do Paciente (essencia.md, "De onde veio")', '''<p class="rot">O início</p>
  <p class="ano" style="left:84px;top:200px">2009</p>
  <p class="tit" style="left:96px;top:470px;width:888px">Dentro de um hospital, surgiu o <span class="k">Escritório do Paciente</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:740px;width:860px">Um modelo de cuidado que colocava a escuta e as necessidades de cada pessoa no centro da atenção.</p>
  ''' + fio(2, bola(DOIS_MIL_E_NOVE)) + '''
  <p class="marco" style="left:%dpx;top:%dpx;color:var(--tif)">2009</p>''' % (DOIS_MIL_E_NOVE[0] - W - 40, DOIS_MIL_E_NOVE[1] + 34)))
# 3 · a essência
S.append(('h03', 'c', 'a essência: a pessoa por trás de cada atendimento', '''<p class="rot">A essência</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Por trás de cada atendimento, existe <span class="k">uma pessoa</span>.</p>
  <p class="corpo" style="left:96px;top:500px;width:860px">Com a sua própria história, hábitos, necessidades e prioridades.</p>
  <p class="corpo" style="left:96px;top:660px;width:860px">Por isso, escutar sempre foi parte essencial da nossa maneira de cuidar.</p>
  ''' + fio(3)))
# 4 · evolução
S.append(('h04', 'v', 'evolução: o cuidado ganha um novo endereço, o trabalho', '''<p class="rot">Evolução</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Com o tempo, essa forma de cuidar <span class="k">evoluiu</span>.</p>
  <p class="corpo tclaro" style="left:96px;top:480px;width:860px">E surgiu a possibilidade de aproximar o cuidado preventivo de um lugar que faz parte da rotina das pessoas: <span style="color:var(--creme);font-weight:800">o trabalho</span>.</p>
  ''' + fio(4)))
# 5 · hoje
S.append(('h05', 'c', 'hoje: a fairhealth; o Escritório do Paciente virou o Escritório do Cuidado', '''<p class="rot">Hoje</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Hoje, essa filosofia está presente na <span class="k">fairhealth</span>.</p>
  <p class="corpo" style="left:96px;top:480px;width:860px">Levamos cuidado individualizado, prevenção e acompanhamento para dentro das empresas, conectando profissionais de saúde, conhecimento e tecnologia.</p>
  <p class="nota" style="left:96px;top:760px;width:860px;color:var(--vlogo)">O Escritório do Paciente virou o <b style="font-weight:800">Escritório do Cuidado</b>.</p>
  ''' + fio(5, bola(HOJE, '#1F3A36')) + '''
  <p class="marco" style="left:%dpx;top:%dpx;color:var(--verde)">Hoje</p>''' % (HOJE[0] - 4 * W - 36, HOJE[1] + 34)))
# 6 · o propósito: o fio termina no logo
S.append(('h06', 'v', 'o propósito: os lugares mudaram, a essência permanece; o fio termina no logo', '''<p class="rot">O propósito</p>
  <p class="tit" style="left:96px;top:220px;width:888px">Os lugares mudaram. <span class="k">A essência do cuidado permanece.</span></p>
  <p class="corpo tclaro" style="left:96px;top:500px;width:860px">Da experiência hospitalar ao ambiente corporativo, seguimos com um mesmo princípio: <span style="color:var(--creme);font-weight:800">o cuidado começa pela pessoa.</span></p>
  ''' + fio(6, bola(FIM, '#F0F0E9', R_LOGO)) + '''
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">''' % (
    FIM[0] - 5 * W - 60, FIM[1] - 60, 120, 120)))

html = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Post 02: nossa história começou em um hospital</title><style>' + CSS + '</style></head><body>\n']
for k, (sid, cls, nota, corpo) in enumerate(S, 1):
    fim = '' if sid == 'h01' else '\n  <p class="handle">@fairhealth.br</p>\n  ' + pag(k)
    html.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  %s%s\n</section>\n\n' % (k, nota, cls, sid, corpo, fim))
html.append('</body></html>\n')
open(SAIDA, 'w').write(''.join(html))
print('ok', len(S))
