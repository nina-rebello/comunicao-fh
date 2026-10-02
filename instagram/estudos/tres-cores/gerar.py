# Teste das 4 combinações de 3 cores no modelo "estatística" (número grande + etiqueta + texto + bolinhas).
# Fonte da marca: Raleway. Texto corrido em verde-escuro #1F3A36 (neutro), exceto na ameixa, que já é escura.
# Uso: python3 instagram/estudos/tres-cores/gerar.py
#      node instagram/ferramentas/render.mjs instagram/estudos/tres-cores/slides.html instagram/estudos/tres-cores/png
import pathlib

AQUI = pathlib.Path(__file__).parent
BASE, CREME, TINTA = '#9FC5BD', '#F0F0E9', '#1F3A36'

# slug, nome, acento, acento é escuro?
PALETAS = [
    ('ameixa', 'Tiffany + Ameixa', '#603A42', True),
    ('lima', 'Tiffany + Lima', '#DAFC92', False),
    ('coral', 'Tiffany + Coral', '#E55838', False),
    ('amarelo', 'Tiffany + Amarelo', '#F2C14E', False),
]

CSS = """
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:500;src:url(../../marca/fontes/raleway-latin-500-normal.woff2)}
@font-face{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#ccc}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 40px}
.slide>*{position:absolute}
.tag{top:96px;right:96px;font-size:34px;font-weight:800;letter-spacing:2px;padding:20px 40px;border-radius:60px}
.num{left:84px;font-weight:800;line-height:.85;letter-spacing:-18px}
.num small{font-size:.42em;letter-spacing:-4px;margin-left:10px}
.txt{left:96px;width:830px;font-size:52px;line-height:1.3;font-weight:500}
.dots{right:96px;bottom:96px;display:flex;gap:18px}
.dots i{display:block;width:58px;height:58px;border-radius:50%}
.h{left:96px;bottom:112px;font-size:28px;font-weight:700}
"""


def dots(ativo, cheio, vazio, n=3):
    return '<div class="dots">' + ''.join(
        f'<i style="background:{cheio if k == ativo else vazio}"></i>' for k in range(n)) + '</div>'


def slides(s, ac, escuro):
    texto = ac if escuro else TINTA          # texto corrido nos fundos claros
    on_ac = CREME if escuro else TINTA       # texto dentro da etiqueta na cor
    # slide 3: fundo na cor; número em creme (ameixa e coral) ou na base (lima e amarelo, que são claros)
    num3 = CREME if s in ('ameixa', 'coral') else BASE
    txt3 = CREME if escuro else TINTA
    return f"""
<section class="slide" id="{s}-1" style="background:{BASE}">
  <div class="tag" style="background:{ac};color:{on_ac}">PASSO 3</div>
  <div class="num" style="top:300px;font-size:420px;color:{CREME}">48<small>h</small></div>
  <p class="txt" style="top:720px;color:{texto}">de smartband no pulso, para conhecer seu sono e seu dia a dia de verdade.</p>
  <div class="h" style="color:{texto}">@fairhealth.br</div>
  {dots(0, ac, CREME)}
</section>
<section class="slide" id="{s}-2" style="background:{CREME}">
  <div class="tag" style="background:{ac};color:{on_ac}">A PERGUNTA</div>
  <div class="num" style="top:250px;font-size:520px;color:{BASE};letter-spacing:0">?</div>
  <p class="txt" style="top:760px;font-size:76px;line-height:1.12;font-weight:400;color:{texto}">O que é <b style="font-weight:800">importante</b> para você?</p>
  <p class="txt" style="top:1000px;font-size:40px;color:{texto}">Todo cuidado começa por aqui.</p>
  <div class="h" style="color:{texto}">@fairhealth.br</div>
  {dots(1, ac, BASE)}
</section>
<section class="slide" id="{s}-3" style="background:{ac}">
  <div class="tag" style="background:{CREME};color:{texto}">PASSO 4</div>
  <div class="num" style="top:300px;font-size:420px;color:{num3}">1<small style="letter-spacing:-2px"> plano</small></div>
  <p class="txt" style="top:720px;color:{txt3}">feito para você, a partir do que é importante na sua rotina.</p>
  <div class="h" style="color:{txt3}">@fairhealth.br</div>
  {dots(2, CREME, BASE if not escuro else BASE)}
</section>"""


html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Três cores</title>'
        f'<style>{CSS}</style></head><body>' + ''.join(slides(s, a, e) for s, _, a, e in PALETAS) + '</body></html>')
(AQUI / 'slides.html').write_text(html)

linhas = ''.join(f'''<div class="linha"><div class="cab"><h2>{n}</h2><div class="sw">{''.join(f'<span><i style="background:{x}"></i>{x.upper()}</span>' for x in (BASE, CREME, a))}</div></div>
<div class="row">{''.join(f'<img src="png/{s}-{i}.png">' for i in (1, 2, 3))}</div></div>''' for s, n, a, e in PALETAS)
(AQUI / 'cartaz.html').write_text(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Três cores</title><style>
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
.row img{{width:376px;height:470px;border-radius:18px;box-shadow:0 0 0 1px #e4e4dd,0 8px 20px rgba(0,0,0,.08)}}
</style></head><body><h1>Combinações de <b>três cores</b> · modelo estatística</h1><div class="grid">{linhas}</div></body></html>''')
print('ok')
