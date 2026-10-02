# Carrossel de teste com layouts inspirados nas referências (pasta "inspo cores e templates").
# Uma paleta por referência, sempre com o verde-água #9FC5BD como base.
# Uso: python3 instagram/estudos/inspo/gerar.py
#      node instagram/ferramentas/render.mjs instagram/estudos/inspo/slides.html instagram/estudos/inspo/png
import pathlib

AQUI = pathlib.Path(__file__).parent
BASE = '#9FC5BD'

# slug, nome, escuro, claro, acento, texto sobre o acento, referência
PALETAS = [
    ('coral', 'Petróleo + coral', '#0B3A42', '#F2E5DD', '#E55838', '#FFFFFF', 'paleta #033744 · #F2E5DD · #E55838 · #84D1BF'),
    ('lima', 'Verde + lima', '#1F3A36', '#F2F7F9', '#DAFC92', '#1F3A36', 'paleta Catskill White · Half Baked · Mindaro'),
    ('vermelho', 'Ardósia + vermelho', '#26383A', '#F3EFE6', '#C8372D', '#FFFFFF', 'listras cinza-azulado, creme e vermelho'),
    ('marinho', 'Marinho', '#1B2D5B', '#F4F6F8', '#4C6FD8', '#FFFFFF', 'cartazes Wellnex'),
]

GRAO = ("url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'>"
        "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/>"
        "<feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 0'/></filter>"
        "<rect width='100%' height='100%' filter='url(%23n)'/></svg>\")")

CSS = """
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:500;src:url(../../marca/fontes/raleway-latin-500-normal.woff2)}
@font-face{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:normal;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#ccc}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 40px}
.slide>*{position:absolute}
.grao{inset:0;background-image:GRAO;opacity:.10;mix-blend-mode:multiply;pointer-events:none}
.k{font-size:26px;font-weight:700;letter-spacing:7px}
.h{font-size:28px;font-weight:700}
.pag{font-size:26px;font-weight:500;opacity:.65}
h1{font-weight:800;letter-spacing:-4px;line-height:.98}
.p{font-size:40px;line-height:1.38}
.mk{padding:2px 12px;box-decoration-break:clone;-webkit-box-decoration-break:clone;font-weight:700}
.tag{border-radius:30px;font-size:44px;font-weight:700;padding:34px 46px;box-shadow:0 14px 30px rgba(0,0,0,.14);white-space:nowrap}
""".replace('GRAO', GRAO)


def carrossel(s, nome, esc, cla, ac, sob):
    return f"""
<section class="slide" id="{s}-1" style="background:radial-gradient(120% 90% at 20% 30%,{cla} 0%,{cla} 35%,{BASE} 100%)">
  <div class="grao"></div>
  <div class="h" style="left:96px;top:96px;color:{esc}">@fairhealth.br</div>
  <div class="pag" style="right:96px;top:96px;color:{esc}">1/5</div>
  <h1 style="left:96px;top:240px;width:900px;font-size:136px;color:{esc}">Aqui, o cuidado começa com uma pergunta.</h1>
  <p class="p" style="left:96px;top:1060px;width:860px;color:{esc}">Como funciona o Escritório do Cuidado? <span class="mk" style="background:{ac};color:{sob}">Arrasta para o lado</span> e vem com a gente.</p>
</section>

<section class="slide" id="{s}-2" style="background:{cla}">
  <div class="grao"></div>
  <div class="k" style="left:96px;top:96px;color:{esc}">COMO FUNCIONA</div>
  <div class="pag" style="right:96px;top:96px;color:{esc}">2/5</div>
  <h1 style="left:96px;top:170px;width:880px;font-size:110px;color:{esc}">Do primeiro oi ao <span style="font-style:italic;color:{ac if s!='lima' else esc};{'background:'+ac+';padding:0 12px' if s=='lima' else ''}">seu plano.</span></h1>
  <svg style="left:0;top:470px" width="1080" height="760" viewBox="0 0 1080 760"><path d="M-40 120 C 260 -40, 420 260, 240 330 S 120 560, 460 520 S 980 300, 900 560 S 520 760, 1120 700" fill="none" stroke="{BASE}" stroke-width="22" stroke-linecap="round"/></svg>
  <div class="tag" style="left:110px;top:540px;transform:rotate(-3deg);background:{BASE};color:{esc}">1 · A gente te conhece</div>
  <div class="tag" style="left:300px;top:690px;transform:rotate(2deg);background:{esc};color:{cla}">2 · Pergunta o que é importante</div>
  <div class="tag" style="left:90px;top:850px;transform:rotate(-2deg);background:{BASE};color:{esc}">3 · Entende antes de propor</div>
  <div class="tag" style="left:340px;top:1010px;transform:rotate(3deg);background:{ac};color:{sob}">4 · Monta o plano com você</div>
  <div class="h" style="left:96px;bottom:80px;color:{esc}">@fairhealth.br</div>
</section>

<section class="slide" id="{s}-3" style="background:{esc};color:{cla}">
  <div class="grao" style="mix-blend-mode:screen;opacity:.06;filter:invert(1)"></div>
  <div class="k" style="left:96px;top:96px;color:{BASE}">PASSO 3 · ENTENDER</div>
  <div class="pag" style="right:96px;top:96px">3/5</div>
  <div style="left:80px;top:260px;font-size:440px;font-weight:800;letter-spacing:-22px;line-height:1;color:{ac if s!='marinho' else BASE}">48h</div>
  <p class="p" style="left:96px;top:760px;width:820px;font-size:46px">de smartband no pulso, para conhecer seu sono e seu dia a dia <b>de verdade.</b></p>
  <div style="left:96px;top:930px;display:flex;align-items:flex-end;gap:16px;height:150px">
    {''.join(f'<div style="width:46px;height:{h}px;border-radius:10px 10px 0 0;background:{BASE};opacity:{o}"></div>' for h,o in [(60,.35),(110,.5),(80,.4),(140,.8),(95,.5),(150,1),(70,.4),(120,.6),(100,.5),(135,.8)])}
  </div>
  <p class="p" style="left:96px;top:1130px;width:900px;font-size:40px"><span class="mk" style="background:{BASE};color:{esc}">Para entender, não para julgar.</span></p>
  <div class="h" style="right:96px;bottom:80px">@fairhealth.br</div>
</section>

<section class="slide" id="{s}-4" style="background:{BASE}">
  <div class="grao"></div>
  <div class="k" style="left:0;right:0;top:96px;text-align:center;color:{esc}">PASSO 5 · RETORNO</div>
  <div class="pag" style="right:96px;top:96px;color:{esc}">4/5</div>
  <h1 style="left:80px;right:80px;top:170px;text-align:center;font-size:100px;color:{esc}">A gente explica cada passo.</h1>
  <div style="left:150px;right:150px;top:430px;background:{cla};border-radius:36px;padding:44px 56px;text-align:center;font-size:38px;line-height:1.4;color:{esc}">E segue junto, ajustando o plano <b>quando a vida muda.</b></div>
  <div style="left:96px;right:96px;top:700px;bottom:96px;border-radius:44px;background:url(../../marca/espaco/sala-atendimento-e-espera.jpg) 25% center/cover"></div>
  <div style="right:130px;bottom:130px;width:120px;height:120px;border-radius:50%;background:{ac};display:flex;align-items:center;justify-content:center"><svg width="56" height="56" viewBox="0 0 24 24" fill="none" stroke="{sob}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h15M13 6l6 6-6 6"/></svg></div>
</section>

<section class="slide" id="{s}-5" style="background:{esc};color:{cla}">
  <svg style="left:0;top:0" width="1080" height="1350" viewBox="0 0 1080 1350">
    <defs><path id="fx-{s}" d="M-80 1060 C 200 1000, 260 760, 520 700 S 900 520, 1180 260"/></defs>
    <path d="M-80 1060 C 200 1000, 260 760, 520 700 S 900 520, 1180 260" fill="none" stroke="{cla}" stroke-width="190" stroke-linecap="round"/>
    <text font-family="Raleway" font-weight="800" font-style="italic" font-size="78" fill="{esc}" dy="26" letter-spacing="-1"><textPath href="#fx-{s}" startOffset="9%">o que é importante para você?</textPath></text>
  </svg>
  <div style="left:96px;top:150px;font-size:96px;font-weight:400;letter-spacing:-2px;color:{BASE}">E para você,</div>
  <div class="pag" style="right:96px;top:96px">5/5</div>
  <p class="p" style="left:96px;top:1150px;width:700px;font-size:40px">Conta pra gente <span class="mk" style="background:{ac};color:{sob}">nos comentários.</span></p>
  <div class="h" style="right:96px;bottom:80px">@fairhealth.br</div>
</section>"""


html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Carrossel teste: inspirações</title>'
        f'<style>{CSS}</style></head><body>' + ''.join(carrossel(s, n, e, c, a, o) for s, n, e, c, a, o, _ in PALETAS) + '</body></html>')
(AQUI / 'slides.html').write_text(html)

# cartaz: uma linha por paleta, 5 slides lado a lado
linhas = ''.join(f'''<div class="linha"><div class="cab"><h2>{n}</h2><div class="sw">{''.join(f'<i style="background:{x}"></i>' for x in (BASE, e, c, a))}</div><small>Inspiração: {ref}</small></div>
<div class="row">{''.join(f'<img src="png/{s}-{i}.png">' for i in range(1, 6))}</div></div>''' for s, n, e, c, a, o, ref in PALETAS)
(AQUI / 'cartaz.html').write_text(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Carrosséis de teste</title><style>
@font-face{{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Raleway,sans-serif;background:#fff;color:#2b3332;width:2520px;padding:100px 110px}}
h1{{font-size:90px;font-weight:400;letter-spacing:-2px;margin-bottom:70px}} h1 b{{font-weight:800;font-style:italic}}
.linha{{margin-bottom:70px}}
.cab{{display:flex;align-items:center;gap:26px;margin-bottom:24px}}
.cab h2{{font-size:44px;font-weight:800;font-style:italic}}
.sw{{display:flex;gap:8px}} .sw i{{width:40px;height:40px;border-radius:50%;box-shadow:0 0 0 1px #ddd}}
.cab small{{font-size:22px;color:#6a7372}}
.row{{display:flex;gap:30px}}
.row img{{width:436px;height:545px;border-radius:20px;box-shadow:0 0 0 1px #e4e4dd,0 10px 24px rgba(0,0,0,.08)}}
</style></head><body><h1>Carrosséis de <b>teste</b> · base verde-água #9FC5BD</h1>{linhas}</body></html>''')
print('ok')
