# Modelo "pessoa + etiquetas" (referência Nürnberg) nas 4 combinações de três cores.
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
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 40px}
.slide>*{position:absolute}
.foto{bottom:0;background-repeat:no-repeat;background-size:contain;background-position:right bottom}
.col{left:84px;top:250px;width:600px}
h1{font-size:76px;font-weight:800;line-height:1.08;letter-spacing:-1.5px}
.sub{font-size:36px;font-weight:400;line-height:1.35;margin-top:34px}
.pills{display:flex;flex-wrap:wrap;gap:16px;margin-top:52px;align-items:center}
.pill{font-size:29px;font-weight:700;padding:18px 30px;border-radius:50px}
.mais{width:66px;height:66px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:700;line-height:1}
.rod{left:84px;bottom:84px;display:flex;align-items:center;gap:22px}
.rod img{width:96px;height:96px;border-radius:50%}
.url{display:flex;align-items:center;gap:14px;font-size:24px;font-weight:700;letter-spacing:2px;padding:12px 26px 12px 12px;border-radius:40px;border:2px solid}
.url i{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-style:normal}
"""


def seta(cor):
    return f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'


def slides(s, ac, escuro):
    tit = ac if escuro else TINTA
    on = CREME if escuro else TINTA
    def rodape(cor):
        return (f'<div class="rod"><img src="../../marca/logo-circulo.png">'
                f'<div class="url" style="border-color:{cor};color:{cor}"><i style="background:{cor}">{seta(CREME if cor != CREME else TINTA)}</i>@FAIRHEALTH.BR</div></div>')
    pills = lambda itens, bg, cor: ''.join(f'<span class="pill" style="background:{bg};color:{cor}">{p}</span>' for p in itens)
    return f"""
<section class="slide" id="{s}-a" style="background:{CREME}">
  <div class="foto" style="right:-150px;width:820px;height:1250px;background-image:url({FOTOS}floriana-recorte-ext.png)"></div>
  <div class="col" style="color:{tit}">
    <h1>Um cuidado mais perto começa com uma conversa.</h1>
    <p class="sub" style="color:{TINTA if not escuro else tit}">Um espaço dentro da empresa para cuidar de você, com escuta e sem pressa.</p>
    <div class="pills">{pills(['Médicos', 'Psicólogos', 'Bioimpedância', 'Smartband'], ac, on)}<span class="mais" style="background:{TINTA if not escuro else ac};color:{CREME}">+</span></div>
  </div>
  {rodape(tit)}
</section>
<section class="slide" id="{s}-b" style="background:{BASE}">
  <div class="foto" style="right:-200px;width:880px;height:1260px;background-image:url({FOTOS}nina-recorte-ext.png)"></div>
  <div class="col" style="color:{tit}">
    <h1>O que é <span style="background:{ac};color:{on};padding:0 12px;box-decoration-break:clone;-webkit-box-decoration-break:clone">importante</span> para você?</h1>
    <p class="sub" style="color:{TINTA if not escuro else tit}">É a primeira pergunta de todo atendimento. O plano nasce da sua resposta.</p>
    <div class="pills">{pills(['Sono', 'Alimentação', 'Movimento', 'Estresse'], CREME, tit)}<span class="mais" style="background:{ac};color:{on}">+</span></div>
  </div>
  {rodape(tit)}
</section>"""


html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Pessoa + etiquetas</title>'
        f'<style>{CSS}</style></head><body>' + ''.join(slides(s, a, e) for s, _, a, e in PALETAS) + '</body></html>')
(AQUI / 'pessoa.html').write_text(html)

linhas = ''.join(f'''<div><div class="cab"><h2>{n}</h2><div class="sw">{''.join(f'<span><i style="background:{x}"></i>{x.upper()}</span>' for x in (BASE, CREME, a))}</div></div>
<div class="row"><img src="png-pessoa/{s}-a.png"><img src="png-pessoa/{s}-b.png"></div></div>''' for s, n, a, e in PALETAS)
(AQUI / 'cartaz-pessoa.html').write_text(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Pessoa + etiquetas</title><style>
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
</style></head><body><h1>Combinações de <b>três cores</b> · modelo pessoa + etiquetas</h1><div class="grid">{linhas}</div></body></html>''')
print('ok')
