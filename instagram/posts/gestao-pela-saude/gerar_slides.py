# Gera slides.html: post rápido que fecha a semana e dá continuidade aos dois primeiros posts publicados
# ("O que é a fairhealth?" e "Conheça o Escritório do Cuidado"). Roteiro da Nina (15/10):
#   1 o espaço entre a medicina do trabalho e o plano de saúde · 2 cuidado real · 3 NR-1 (como no site)
#   4 os três argumentos (como no site) · 5 ecossistema fairjob (fairjob.com.br) e a frase "Gestão de pessoas que
#   começa pela saúde."
# Uso: python3 gerar_slides.py slides.html && node ../../ferramentas/render.mjs slides.html png
import sys

SAIDA = sys.argv[1]
N = 5

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
.k{font-weight:800;font-style:italic}
.v .k{color:var(--tif)}
.rot{left:96px;top:96px;font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.v .rot{color:var(--tif)}
.tit{font-size:70px;line-height:80px;letter-spacing:-0.01em}
.corpo{font-size:34px;line-height:46px}
.nota{font-size:26px;line-height:36px}
.tclaro{color:var(--tclaro)}
.handle{left:96px;top:1238px;font-size:24px;line-height:32px}
.v .handle{color:var(--tclaro)}
.arr{right:96px;top:1238px;font-size:24px;line-height:32px}
.pag{right:96px;top:1248px;display:flex;gap:8px}
.pag i{display:block;width:20px;height:12px;border-radius:6px}
.pag i.on{width:48px}
.t .pag i{background:var(--creme)} .t .pag i.on{background:var(--verde)}
.v .pag i{background:rgba(191,224,217,.3)} .v .pag i.on{background:var(--tif)}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.cartao{left:96px;width:888px;background:#fff;border-radius:28px;padding:34px 40px}
.cartao b{display:block;font-size:30px;line-height:38px;font-weight:800;color:var(--vlogo);margin-bottom:10px}
.cartao span{display:block;font-size:26px;line-height:36px;color:var(--verde)}
.arg{left:96px;width:888px;border-top:3px solid var(--tif);padding-top:26px}
.arg b{display:block;font-size:32px;line-height:40px;font-weight:800;color:var(--creme);margin-bottom:10px}
.arg span{display:block;font-size:26px;line-height:36px;color:var(--tclaro)}
.passo{left:210px;width:774px}
.passo p{font-size:40px;line-height:48px;font-weight:800}
.eco{width:200px;text-align:center}
.eco b{display:block;font-size:28px;line-height:34px;font-weight:800}
.eco span{display:block;font-size:24px;line-height:30px;margin-top:4px}
'''

def pag(i):
    return '<div class="pag">' + ''.join('<i class="on"></i>' if j == i else '<i></i>' for j in range(1, N + 1)) + '</div>'

S = []
# 1 · capa: o espaço entre a medicina do trabalho e o plano de saúde
S.append(('g01', 't', 'capa: o espaço que ninguém cuida', '''<p class="rot">O espaço que falta</p>
  <p class="tit" style="left:96px;top:250px;width:900px">Entre a medicina do trabalho e o plano de saúde, existe um espaço que <span class="k">ninguém cuida</span>.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <path d="M150 860H930" stroke="#1F3A36" stroke-width="3"/>
    <circle cx="150" cy="860" r="18" fill="#1F3A36"/>
    <circle cx="930" cy="860" r="18" fill="#1F3A36"/>
    <path d="M300 860C380 760 700 760 780 860" fill="none" stroke="#F0F0E9" stroke-width="12" stroke-linecap="round"/>
    <circle cx="540" cy="785" r="26" fill="#F0F0E9"/>
  </svg>
  <p style="left:60px;top:900px;width:180px;text-align:center;font-size:24px;line-height:30px;font-weight:800">Medicina<br>do trabalho</p>
  <p style="left:840px;top:900px;width:180px;text-align:center;font-size:24px;line-height:30px;font-weight:800">Plano<br>de saúde</p>
  <p style="left:390px;top:700px;width:300px;text-align:center;font-size:26px;line-height:32px;font-weight:800">a fairhealth</p>
  <p class="corpo" style="left:96px;top:1040px;width:888px">É nele que a <b style="font-weight:800">fairhealth</b> trabalha.</p>
  <p class="handle">@fairhealth.br</p>
  <p class="arr">Arraste para o lado →</p>'''))
# 2 · cuidado real
S.append(('g02', 'v', 'cuidado real, todo dia, dentro da empresa', '''<p class="rot">Um cuidado real</p>
  <p class="tit" style="left:96px;top:200px;width:888px">Cuidado de verdade, <span class="k">todo dia</span>, dentro da empresa.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <path d="M136 560V900" stroke="#96C5BD" stroke-width="10" stroke-linecap="round"/>
    <g fill="#96C5BD"><circle cx="136" cy="560" r="26"/><circle cx="136" cy="730" r="26"/><circle cx="136" cy="900" r="26"/></g>
  </svg>
  <div class="passo" style="top:536px"><p>Médicos e psicólogos presentes</p></div>
  <div class="passo" style="top:706px"><p>Um plano de cuidado para cada pessoa</p></div>
  <div class="passo" style="top:876px"><p>Acompanhamento contínuo</p></div>
  <p class="corpo" style="left:96px;top:1040px;width:888px;color:var(--tif)">Não é campanha. Não é app. <b style="font-weight:800;color:var(--creme)">É gente cuidando de gente.</b></p>'''))
# 3 · NR-1 (como no site)
S.append(('g03', 't', 'NR-1: segurança psicossocial no trabalho (texto do site, fairjob.com.br/fairhealth)', '''<p class="rot">Conformidade regulatória</p>
  <p class="tit" style="left:96px;top:160px;width:888px">NR-1: <span class="k">segurança psicossocial</span> no trabalho.</p>
  <div class="cartao" style="top:420px"><b>Obrigação legal</b><span>A NR-1 atualizada inclui a gestão de riscos psicossociais como requisito obrigatório para empresas de todos os portes.</span></div>
  <div class="cartao" style="top:680px"><b>Riscos psicossociais</b><span>Estresse, burnout, ansiedade e conflitos interpessoais devem ser identificados, monitorados e mitigados.</span></div>
  <div class="cartao" style="top:940px"><b>Como a fairhealth ajuda</b><span>O Escritório do Cuidado e o Programa MEV oferecem estrutura para atender às exigências psicossociais da NR-1, com registros e rastreabilidade.</span></div>'''))
# 4 · os três argumentos (como no site)
S.append(('g04', 'v', 'o argumento certo para cada decisor (texto do site)', '''<p class="rot">O argumento certo para cada decisor</p>
  <p class="tit" style="left:96px;top:160px;width:888px">Mesmo programa. Três argumentos, <span class="k">um para cada mesa</span>.</p>
  <div class="arg" style="top:440px"><b>Para o RH</b><span>Um programa preventivo real para apresentar ao financeiro. Não campanha, não app: um Escritório do Cuidado dentro da empresa, com atendimento de verdade e impacto na marca empregadora.</span></div>
  <div class="arg" style="top:690px"><b>Para o médico do trabalho</b><span>Sinistralidade não cai com plano de saúde reativo. Um programa in company, com evidência clínica de Medicina do Estilo de Vida e dados integráveis ao PGR.</span></div>
  <div class="arg" style="top:940px"><b>Para o financeiro</b><span>Sinistralidade alta encarece o plano na renovação. A fairhealth acompanha o cuidado com dados clínicos e indicadores para apresentar ao board.</span></div>'''))
# 5 · ecossistema fairjob e a frase final
ECO = [('fairdata', 'medir', 180), ('fairhealth', 'cuidar', 420), ('fairedu', 'conscientizar', 660), ('fairtrust', 'comprovar', 900)]
pontos = ''.join('<circle cx="%d" cy="560" r="%d" fill="%s"/>' % (x, 26 if n == 'fairhealth' else 14, '#1F3A36' if n == 'fairhealth' else '#F0F0E9') for n, v, x in ECO)
rotulos = ''.join('<div class="eco" style="left:%dpx;top:600px"><b>%s</b><span>%s</span></div>' % (x - 100, n, v) for n, v, x in ECO)
S.append(('g05', 't', 'ecossistema fairjob (fairjob.com.br) e a frase de impacto', '''<p class="rot">Ecossistema fairjob</p>
  <p class="tit" style="left:96px;top:200px;width:888px;font-size:60px;line-height:70px">A fairhealth é o <span class="k">cuidar</span> do ecossistema fairjob.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <path d="M180 560H900" stroke="#F0F0E9" stroke-width="8" stroke-linecap="round"/>''' + pontos + '''
  </svg>
  ''' + rotulos + '''
  <p class="nota" style="left:96px;top:740px;width:888px">O único ecossistema brasileiro que mede, cuida, conscientiza e comprova o bem-estar organizacional com evidência científica.</p>
  <p class="tit" style="left:96px;top:870px;width:888px">Gestão de pessoas que começa pela <span class="k">saúde</span>.</p>
  <div style="left:96px;top:1076px;width:116px;height:116px;border-radius:50%;background:var(--creme)"></div>
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:104px;top:1084px;width:100px;height:100px">'''))

html = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Gestão de pessoas que começa pela saúde</title><style>' + CSS + '</style></head><body>\n']
for k, (sid, cls, nota, corpo) in enumerate(S, 1):
    fim = '' if sid == 'g01' else '\n  <p class="handle">@fairhealth.br</p>\n  ' + pag(k)
    html.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  %s%s\n</section>\n\n' % (k, nota, cls, sid, corpo, fim))
html.append('</body></html>\n')
open(SAIDA, 'w').write(''.join(html))
print('ok', len(S))
