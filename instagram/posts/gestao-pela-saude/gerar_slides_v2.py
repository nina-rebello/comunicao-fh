# v2 (15/10), pedidos da Nina:
#   - capa em triângulo: a fairhealth na ponta de cima, medicina do trabalho e plano de saúde na base;
#   - ecossistema com a identidade de cada marca (logos em círculo, de instagram/marca/ecossistema/);
#   - slide final como o do primeiro post, com chamada para salvar, compartilhar, link da bio e direct;
#   - menos texto: NR-1 e os três argumentos encurtados (de 66 e 101 palavras para cerca de 45 cada).
# A v1 (slides.html, png/) fica guardada.
# Uso: python3 gerar_slides_v2.py slides-v2.html && node ../../ferramentas/render.mjs slides-v2.html png-v2
import sys

SAIDA = sys.argv[1]
N = 6
ECO_DIR = '../../marca/ecossistema/'

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
.rotulo{font-size:26px;line-height:32px;font-weight:800;text-align:center}
.cartao{left:96px;width:888px;background:#fff;border-radius:28px;padding:34px 40px}
.cartao b{display:block;font-size:32px;line-height:40px;font-weight:800;color:var(--vlogo);margin-bottom:8px}
.cartao span{display:block;font-size:30px;line-height:40px;color:var(--verde)}
.arg{left:96px;width:888px;border-top:3px solid var(--tif);padding-top:26px}
.arg b{display:block;font-size:34px;line-height:42px;font-weight:800;color:var(--creme);margin-bottom:8px}
.arg span{display:block;font-size:30px;line-height:40px;color:var(--tclaro)}
.passo{left:210px;width:774px}
.passo p{font-size:40px;line-height:48px;font-weight:800}
.marca{width:220px;text-align:center}
.marca b{display:block;font-size:26px;line-height:32px;font-weight:800}
.marca span{display:block;font-size:24px;line-height:30px;color:var(--vlogo)}
.acao{left:200px;width:784px;font-size:34px;line-height:44px}
.acao b{font-weight:800}
'''

def pag(i):
    return '<div class="pag">' + ''.join('<i class="on"></i>' if j == i else '<i></i>' for j in range(1, N + 1)) + '</div>'

# ícones lineares (Feather, licença MIT) para o slide final
ICONE = {
    'salvar': '<path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/>',
    'compartilhar': '<path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4 20-7z"/>',
    'link': '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    'direct': '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
}

def icone(nome, x, y):
    return ('<svg style="left:%dpx;top:%dpx;width:72px;height:72px" viewBox="-6 -6 36 36" fill="none" stroke="#1F3A36" '
            'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="17" fill="#F0F0E9" stroke="none"/>%s</svg>') % (x, y, ICONE[nome])

S = []
# 1 · capa: o triângulo, com a fairhealth na ponta de cima
TOPO, BE, BD = (540, 680), (210, 1000), (870, 1000)
S.append(('h01', 't', 'capa: o triângulo (medicina do trabalho e plano de saúde na base, fairhealth no topo)', '''<p class="rot">O espaço que falta</p>
  <p class="tit" style="left:96px;top:170px;width:900px">Entre a medicina do trabalho e o plano de saúde, existe um espaço que <span class="k">ninguém cuida</span>.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <path d="M%d %d L%d %d L%d %d Z" fill="#F0F0E9" fill-opacity=".28"/>
    <path d="M%d %d H%d" stroke="#1F3A36" stroke-width="3" stroke-dasharray="2 12" stroke-linecap="round"/>
    <path d="M%d %d L%d %d L%d %d" fill="none" stroke="#F0F0E9" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="%d" cy="%d" r="18" fill="#1F3A36"/><circle cx="%d" cy="%d" r="18" fill="#1F3A36"/>
    <circle cx="%d" cy="%d" r="34" fill="#F0F0E9"/><circle cx="%d" cy="%d" r="12" fill="#1F3A36"/>
  </svg>''' % (TOPO + BE + BD + (BE[0], BE[1], BD[0]) + BE + TOPO + BD + BE + BD + TOPO + TOPO) + '''
  <p class="rotulo" style="left:%dpx;top:%dpx;width:300px">fairhealth</p>
  <p class="rotulo" style="left:%dpx;top:%dpx;width:240px">Medicina<br>do trabalho</p>
  <p class="rotulo" style="left:%dpx;top:%dpx;width:240px">Plano<br>de saúde</p>
  <p class="nota" style="left:390px;top:870px;width:300px;text-align:center;font-style:italic">a rotina e os<br>primeiros sinais</p>
  <p class="corpo" style="left:96px;top:1145px;width:888px">É nele que a <b style="font-weight:800">fairhealth</b> trabalha.</p>''' % (TOPO[0] - 150, TOPO[1] - 84, BE[0] - 120, BE[1] + 32, BD[0] - 120, BD[1] + 32)))
# 2 · cuidado real
S.append(('h02', 'v', 'cuidado real, todo dia, dentro da empresa', '''<p class="rot">Um cuidado real</p>
  <p class="tit" style="left:96px;top:200px;width:888px">Cuidado de verdade, <span class="k">todo dia</span>, dentro da empresa.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <path d="M136 560V900" stroke="#96C5BD" stroke-width="10" stroke-linecap="round"/>
    <g fill="#96C5BD"><circle cx="136" cy="560" r="26"/><circle cx="136" cy="730" r="26"/><circle cx="136" cy="900" r="26"/></g>
  </svg>
  <div class="passo" style="top:536px"><p>Médicos e psicólogos presentes</p></div>
  <div class="passo" style="top:706px"><p>Um plano de cuidado para cada pessoa</p></div>
  <div class="passo" style="top:876px"><p>Acompanhamento contínuo</p></div>
  <p class="corpo" style="left:96px;top:1040px;width:888px;color:var(--tif)">Não é campanha. Não é app. <b style="font-weight:800;color:var(--creme)">É gente cuidando de gente.</b></p>'''))
# 3 · NR-1 (do site, encurtado)
S.append(('h03', 't', 'NR-1: segurança psicossocial no trabalho (site, encurtado)', '''<p class="rot">Conformidade regulatória</p>
  <p class="tit" style="left:96px;top:170px;width:888px">NR-1: <span class="k">segurança psicossocial</span> no trabalho.</p>
  <div class="cartao" style="top:430px"><b>Obrigação legal</b><span>A gestão de riscos psicossociais agora vale para empresas de todos os portes.</span></div>
  <div class="cartao" style="top:665px"><b>Riscos psicossociais</b><span>Estresse, burnout e ansiedade precisam ser identificados, monitorados e mitigados.</span></div>
  <div class="cartao" style="top:900px"><b>Como a fairhealth ajuda</b><span>Escritório do Cuidado e Programa MEV, com registros e rastreabilidade.</span></div>'''))
# 4 · três argumentos (do site, encurtado)
S.append(('h04', 'v', 'o argumento certo para cada decisor (site, encurtado)', '''<p class="rot">O argumento certo para cada decisor</p>
  <p class="tit" style="left:96px;top:170px;width:888px">Mesmo programa. Três argumentos, <span class="k">um para cada mesa</span>.</p>
  <div class="arg" style="top:470px"><b>Para o RH</b><span>Um programa preventivo real, com impacto na marca empregadora.</span></div>
  <div class="arg" style="top:690px"><b>Para o médico do trabalho</b><span>Evidência clínica de Medicina do Estilo de Vida e dados integráveis ao PGR.</span></div>
  <div class="arg" style="top:910px"><b>Para o financeiro</b><span>Indicadores de saúde e de custo para apresentar ao board.</span></div>'''))
# 5 · ecossistema fairjob, com os logos de cada marca
ECO = [('fairdata', 'medir', 186), ('fairhealth', 'cuidar', 422), ('fairedu', 'conscientizar', 658), ('fairtrust', 'comprovar', 894)]
logos = ''
for nome, verbo, x in ECO:
    d = 168 if nome == 'fairhealth' else 132
    anel = ('<div style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:50%%;border:4px solid var(--verde)"></div>'
            % (x - d // 2 - 10, 600 - d // 2 - 10, d + 20, d + 20)) if nome == 'fairhealth' else ''
    logos += anel + '<img src="%slogo-%s.png" alt="%s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">' % (ECO_DIR, nome, nome, x - d // 2, 600 - d // 2, d, d)
    logos += '<div class="marca" style="left:%dpx;top:%dpx"><b>%s</b><span>%s</span></div>' % (x - 110, 712, nome, verbo)
S.append(('h05', 'c', 'ecossistema fairjob com os logos (fairjob.com.br) e a frase de impacto', '''<p class="rot">Ecossistema fairjob</p>
  <p class="tit" style="left:96px;top:170px;width:888px;font-size:60px;line-height:70px">A fairhealth é o <span class="k">cuidar</span> do ecossistema fairjob.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true"><path d="M186 600H894" stroke="#96C5BD" stroke-width="4"/></svg>
  ''' + logos + '''
  <p class="tit" style="left:96px;top:930px;width:888px">Gestão de pessoas que começa pela <span class="k">saúde</span>.</p>'''))
# 6 · final: salvar, compartilhar, link e direct (como o último slide do primeiro post)
ACOES = [('salvar', 'Salve', 'para consultar depois.'), ('compartilhar', 'Compartilhe', 'com quem cuida das pessoas na sua empresa.'),
         ('link', 'Conheça o programa', 'no link da bio.'), ('direct', 'Fale com a gente', 'pelo direct.')]
acoes = ''.join(icone(n, 96, 452 + i * 150) + '<p class="acao" style="top:%dpx"><b>%s</b> %s</p>' % (466 + i * 150, a, b) for i, (n, a, b) in enumerate(ACOES))
S.append(('h06', 't', 'final: chamada para salvar, compartilhar, link da bio e direct', '''<p class="rot">Vem com a gente</p>
  <p class="tit" style="left:96px;top:200px;width:888px">Gostou? <span class="k">Leve esse cuidado adiante.</span></p>
  ''' + acoes + '''
  <div style="left:96px;top:1062px;width:888px;height:2px;background:rgba(31,58,54,.3)"></div>
  <div style="left:96px;top:1100px;width:96px;height:96px;border-radius:50%;background:var(--creme)"></div>
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:104px;top:1108px;width:80px;height:80px">
  <p class="nota" style="left:220px;top:1129px;width:760px">Fazemos o certo pelos <span class="k">motivos certos</span>.</p>'''))

html = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Gestão de pessoas que começa pela saúde (v2)</title><style>' + CSS + '</style></head><body>\n']
for k, (sid, cls, nota, corpo) in enumerate(S, 1):
    if sid == 'h01':
        fim = '\n  <p class="handle">@fairhealth.br</p>\n  <p class="arr">Arraste para o lado →</p>'
    else:
        fim = '\n  <p class="handle">@fairhealth.br</p>\n  ' + pag(k)
    html.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  %s%s\n</section>\n\n' % (k, nota, cls, sid, corpo, fim))
html.append('</body></html>\n')
open(SAIDA, 'w').write(''.join(html))
print('ok', len(S))
