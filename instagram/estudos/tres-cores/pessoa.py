# Modelo "etiquetas" (referência Nürnberg, sem foto) nas 4 combinações de três cores.
# Uso: python3 instagram/estudos/tres-cores/pessoa.py
#      node instagram/ferramentas/render.mjs instagram/estudos/tres-cores/pessoa.html instagram/estudos/tres-cores/png-pessoa
import pathlib

AQUI = pathlib.Path(__file__).parent
BASE, CREME, TINTA = '#9FC5BD', '#F0F0E9', '#1F3A36'
PALETAS = [
    ('ameixa', 'Tiffany + Ameixa', '#603A42', True),
    ('lima', 'Tiffany + Lima', '#DAFC92', False),
    ('coral', 'Tiffany + Coral', '#E55838', False),
    ('amarelo', 'Tiffany + Amarelo', '#F2C14E', False),
]
FOTOS = '../../posts/time/fotos/'

CSS = """
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:500;src:url(../../marca/fontes/raleway-latin-500-normal.woff2)}
@font-face{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#ccc}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 40px;
  display:flex;flex-direction:column;justify-content:center;padding:0 110px}
.top{position:absolute;top:100px;left:110px;right:110px;display:flex;justify-content:space-between;font-size:28px;font-weight:700}
.top span:last-child{font-weight:500;opacity:.7}
h1{font-size:100px;font-weight:800;line-height:1.06;letter-spacing:-2px}
.sub{font-size:40px;font-weight:400;line-height:1.4;margin-top:40px;max-width:780px}
.pills{display:flex;flex-wrap:wrap;gap:14px;margin-top:64px}
.pill{font-size:28px;font-weight:700;padding:18px 28px;border-radius:50px}
.seta{position:absolute;right:110px;bottom:100px;width:104px;height:104px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.mk{padding:0 14px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
"""


def seta(cor):
    return f'<svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'


def slides(s, ac, escuro):
    tit = ac if escuro else TINTA          # títulos e textos
    on = CREME if escuro else TINTA        # texto sobre a cor extra
    pills = lambda itens, bg, cor: ''.join(f'<span class="pill" style="background:{bg};color:{cor}">{p}</span>' for p in itens)
    # A: fundo Tiffany, cor extra nas etiquetas
    # B: fundo creme, Tiffany nas etiquetas, cor extra só no marca-texto
    return f"""
<section class="slide" id="{s}-a" style="background:{BASE};color:{tit}">
  <div class="top"><span>@fairhealth.br</span><span>1/2</span></div>
  <h1>Um cuidado mais perto começa com uma conversa.</h1>
  <p class="sub">Um espaço dentro da empresa para cuidar de você, com escuta e sem pressa.</p>
  <div class="pills">{pills(['Médicos', 'Psicólogos', 'Escuta', 'Plano individual'], ac, on)}</div>
  <div class="seta" style="background:{tit}">{seta(BASE)}</div>
</section>
<section class="slide" id="{s}-b" style="background:{CREME};color:{TINTA}">
  <div class="top"><span>@fairhealth.br</span><span>2/2</span></div>
  <h1>O que é <span class="mk" style="background:{ac};color:{on}">importante</span> para você?</h1>
  <p class="sub">É a primeira pergunta de todo atendimento. O plano nasce da sua resposta.</p>
  <div class="pills">{pills(['Sono', 'Alimentação', 'Movimento', 'Estresse'], BASE, TINTA)}</div>
  <div class="seta" style="background:{BASE}">{seta(TINTA)}</div>
</section>"""


html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Etiquetas</title>'
        f'<style>{CSS}</style></head><body>' + ''.join(slides(s, a, e) for s, _, a, e in PALETAS) + '</body></html>')
(AQUI / 'pessoa.html').write_text(html)

linhas = ''.join(f'''<div><div class="cab"><h2>{n}</h2><div class="sw">{''.join(f'<span><i style="background:{x}"></i>{x.upper()}</span>' for x in (BASE, CREME, a))}</div></div>
<div class="row"><img src="png-pessoa/{s}-a.png"><img src="png-pessoa/{s}-b.png"></div></div>''' for s, n, a, e in PALETAS)
(AQUI / 'cartaz-pessoa.html').write_text(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Etiquetas</title><style>
@font-face{{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Raleway,sans-serif;background:#fff;color:#2b3332;width:2600px;padding:100px 110px}}
h1{{font-size:88px;font-weight:400;letter-spacing:-2px;margin-bottom:70px}} h1 b{{font-weight:800}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:70px 90px}}
.cab{{display:flex;align-items:center;gap:30px;margin-bottom:22px}}
.cab h2{{font-size:42px;font-weight:800}}
.sw{{display:flex;gap:22px;font-size:20px;font-weight:700;color:#5a6463}}
.sw span{{display:flex;align-items:center;gap:8px}}
.sw i{{width:34px;height:34px;border-radius:50%;box-shadow:0 0 0 1px #ddd}}
.row{{display:flex;gap:24px}}
.row img{{width:568px;height:710px;border-radius:18px;box-shadow:0 0 0 1px #e4e4dd,0 8px 20px rgba(0,0,0,.08)}}
</style></head><body><h1>Combinações de <b>três cores</b> · modelo etiquetas</h1><div class="grid">{linhas}</div></body></html>''')
print('ok')
