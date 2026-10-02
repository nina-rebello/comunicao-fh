# Gera os slides de teste e os cartazes de comparação de cor complementar.
# Uso: python3 instagram/estudos/cores/gerar.py
# Depois: node instagram/ferramentas/render.mjs instagram/estudos/cores/slides.html instagram/estudos/cores/png
import pathlib

AQUI = pathlib.Path(__file__).parent
CREME, BASE, TINTA = '#F0F0E9', '#9FC5BD', '#1F3A36'

# nome, hex, escura?, nota técnica
CORES = [
    ('ameixa', 'Bordô', '#603A42', True, ' (atual)'),
    ('coral', 'Coral', '#EC7768', False, ''),
    ('amarelo', 'Amarelo', '#F2C14E', False, ''),
    ('petroleo', 'Azul petróleo', '#1F5560', True, ''),
    ('framboesa', 'Framboesa', '#C2456B', True, ''),
]

CSS = f"""
@font-face{{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:500;src:url(../../marca/fontes/raleway-latin-500-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Raleway,sans-serif;background:#ccc}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 40px;padding:0 120px;
  display:flex;flex-direction:column;justify-content:center}}
.k{{position:absolute;top:120px;left:120px;font-size:24px;font-weight:700;letter-spacing:8px}}
.pag{{position:absolute;top:120px;right:120px;font-size:24px;font-weight:500;opacity:.6}}
.handle{{position:absolute;bottom:110px;left:120px;font-size:26px;font-weight:700}}
.traco{{width:72px;height:6px;margin-bottom:56px}}
h1{{font-size:132px;font-weight:400;line-height:1.02;letter-spacing:-2.5px}}
h1 b{{font-weight:800;font-style:italic;letter-spacing:-1px}}
.p{{font-size:38px;line-height:1.4;margin-top:56px;max-width:720px;opacity:.9}}
.centro{{align-items:center;text-align:center}}
.centro .p{{margin-left:auto;margin-right:auto}}
"""

def slides(slug, hexa, escura):
    escura_txt = slug in ('ameixa', 'petroleo')      # a cor tem contraste para ser letra nos fundos claros
    tinta = hexa if escura_txt else TINTA
    sobre = CREME if escura else TINTA
    sub = lambda cor: f'text-decoration:underline;text-decoration-color:{cor};text-decoration-thickness:8px;text-underline-offset:16px'
    kw_creme = f'color:{hexa}' if escura else f'color:{TINTA};{sub(hexa)}'
    kw_base = f'color:{hexa}' if escura_txt else f'color:{TINTA};{sub(hexa)}'
    kw_sobre = f'color:{BASE}' if escura else f'color:{TINTA};{sub(CREME)}'
    if slug == 'framboesa':
        kw_sobre = f'color:{CREME};{sub(CREME)}'
    traco_creme = hexa
    return f"""
<section class="slide" id="{slug}-1" style="background:{CREME};color:{tinta}">
  <div class="k">PASSO 3</div><div class="pag">6/10</div>
  <div class="traco" style="background:{traco_creme}"></div>
  <h1>Entender<br><b style="{kw_creme}">antes de propor.</b></h1>
  <p class="p">Bioimpedância e smartband por 48 horas. Para entender, não para julgar.</p>
  <div class="handle">@fairhealth.br</div>
</section>
<section class="slide centro" id="{slug}-2" style="background:{BASE};color:{tinta}">
  <div class="pag">10/10</div>
  <div class="traco" style="background:{hexa}"></div>
  <h1 style="font-size:124px">E para você,<br><b style="{kw_base}">o que é importante?</b></h1>
  <p class="p">Conta pra gente nos comentários.</p>
  <div class="handle" style="left:0;right:0;text-align:center">@fairhealth.br</div>
</section>
<section class="slide" id="{slug}-3" style="background:{hexa};color:{sobre}">
  <div class="k">PASSO 4</div><div class="pag">7/10</div>
  <div class="traco" style="background:{BASE if escura else TINTA}"></div>
  <h1 style="font-size:150px">O plano<br><b style="{kw_sobre}">é seu.</b></h1>
  <p class="p">Montado a partir do que é importante para você, nos pilares da Medicina do Estilo de Vida.</p>
  <div class="handle">@fairhealth.br</div>
</section>"""

html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Testes de cor</title><style>{CSS}</style></head><body>'
html += ''.join(slides(s, h, e) for s, _, h, e, _ in CORES) + '</body></html>'
(AQUI / 'slides.html').write_text(html)

# cartaz em colunas (mesmo formato do PDF "Combinações de cores")
col = ''.join(f'''<div class="col"><h2>{i+1} · <b>{n}</b><small>{x}</small></h2>
<img src="png/{s}-1.png"><span>Creme {CREME}</span>
<img src="png/{s}-2.png"><span>Base {BASE}</span>
<img src="png/{s}-3.png"><span>{n} {h}</span></div>''' for i, (s, n, h, e, x) in enumerate(CORES))
(AQUI / 'cartaz-colunas.html').write_text(f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Combinações de cores</title><style>
@font-face{{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}}
@font-face{{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Raleway,sans-serif;background:#fff;color:#2b3332;width:2520px;padding:110px 110px 90px}}
.topo{{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:80px}}
h1{{font-size:96px;font-weight:400;letter-spacing:-2px}} h1 b{{font-weight:800;font-style:italic}}
.at{{font-size:34px;font-weight:700}}
.cols{{display:flex;gap:46px}} .col{{width:424px}}
.col h2{{font-size:46px;font-weight:400;margin-bottom:30px;white-space:nowrap}} .col h2 b{{font-weight:800;font-style:italic}}
.col h2 small{{font-size:24px;font-weight:700;margin-left:6px}}
.col img{{width:424px;height:530px;display:block;border-radius:22px;box-shadow:0 0 0 1px #e4e4dd,0 10px 26px rgba(0,0,0,.08)}}
.col span{{display:block;font-size:24px;font-weight:700;margin:14px 0 34px 6px;color:#4a5352}}
</style></head><body><div class="topo"><h1>Combinações de <b>cores</b></h1><div class="at">@fairhealth.br</div></div>
<div class="cols">{col}</div></body></html>''')
print('ok')
