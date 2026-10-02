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
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:center;
  align-items:flex-start;text-align:left;padding:120px 110px;margin:0 0 40px}}
h1{{font-size:104px;line-height:1.04;letter-spacing:-1.5px;font-weight:400;width:100%}}
h1 b{{font-weight:800;font-style:italic}}
.sub{{font-size:42px;line-height:1.32;margin-top:40px;max-width:840px}}
.sub b{{font-weight:800;font-style:italic}}
.pag{{position:absolute;top:72px;right:110px;font-size:28px;font-weight:500;opacity:.7}}
.handle{{position:absolute;bottom:72px;left:110px;font-size:30px;font-weight:700}}
.passo{{display:flex;align-items:center;gap:28px;margin-bottom:56px}}
.n{{width:132px;height:132px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:56px;font-weight:800;font-style:italic}}
.t{{font-size:26px;font-weight:700;letter-spacing:7px}}
.pills{{display:flex;flex-wrap:wrap;gap:18px;margin-top:48px;max-width:880px}}
.pill{{font-size:32px;font-weight:700;padding:18px 32px;border-radius:60px}}
.centro{{align-items:center;text-align:center}}
.logo{{width:180px;margin-bottom:64px}}
.botao{{display:inline-block;margin-top:56px;font-size:36px;font-weight:700;padding:26px 52px;border-radius:70px}}
.assina{{font-size:30px;font-style:italic;margin-top:52px;opacity:.85}}
"""

def marca(cor):
    return f"background:linear-gradient(transparent 76%,{cor} 76%,{cor} 94%,transparent 94%)"

def slides(slug, hexa, escura):
    # tinta = cor de texto nos fundos claros; sobre a cor = cor do texto no fundo da cor em teste
    tinta = hexa if slug in ('ameixa', 'petroleo') else TINTA
    sobre = CREME if escura else TINTA
    destaque_sobre = BASE if escura else CREME
    # palavra-chave nos fundos claros: a própria cor se tiver contraste; senão tinta com marca-texto
    kw_creme = f'color:{hexa};{marca(BASE)}' if escura else f'color:{TINTA};{marca(hexa)}'
    kw_base = f'color:{hexa}' if slug in ('ameixa', 'petroleo') else f'color:{TINTA};{marca(hexa if not escura else CREME)}'
    if slug == 'framboesa':
        kw_base = f'color:{TINTA};{marca(hexa)}'
    pill_on = CREME if escura else TINTA
    kw_sobre = f'color:{BASE}' if escura else f'color:{TINTA};{marca(CREME)}'
    if slug == 'framboesa':
        kw_sobre = f'color:{CREME}'
    return f"""
<section class="slide" id="{slug}-1" style="background:{CREME};color:{tinta}"><div class="pag">6/10</div>
  <div class="passo"><div class="n" style="background:{BASE};color:{tinta}">3</div><div class="t">PASSO 3</div></div>
  <h1>Entender <b style="{kw_creme}">antes de propor.</b></h1>
  <div class="pills"><span class="pill" style="background:{hexa};color:{pill_on}">Bioimpedância</span><span class="pill" style="background:{hexa};color:{pill_on}">Smartband por 48 horas</span></div>
  <p class="sub">Para conhecer seu sono e seu dia a dia de verdade. <b>Para entender, não para julgar.</b></p>
  <div class="handle">@fairhealth.br</div>
</section>
<section class="slide centro" id="{slug}-2" style="background:{BASE};color:{TINTA};justify-content:center;padding:0">
  <div style="position:absolute;left:50%;top:50%;width:1320px;height:1320px;margin:-660px 0 0 -660px;border-radius:50%;background:{CREME}"></div>
  <div style="position:relative;width:860px;text-align:center">
    <p style="font-size:64px;font-weight:400;line-height:1.1;color:{tinta}">E para você,</p>
    <h1 style="font-size:148px;line-height:.98;letter-spacing:-3px;margin-top:10px;color:{hexa if (escura) else TINTA}"><b>o que é importante?</b></h1>
    <p style="font-size:54px;line-height:1.55;margin-top:56px;font-weight:500"><span style="background:{hexa};color:{pill_on};padding:2px 14px;box-decoration-break:clone;-webkit-box-decoration-break:clone">Conta pra gente</span><br><span style="background:{hexa};color:{pill_on};padding:2px 14px;box-decoration-break:clone;-webkit-box-decoration-break:clone">nos comentários.</span></p>
  </div>
  <div class="handle" style="left:0;right:0;text-align:center;bottom:60px">@fairhealth.br</div>
</section>
<section class="slide" id="{slug}-3" style="background:{hexa};color:{sobre}"><div class="pag">7/10</div>
  <div class="passo"><div class="n" style="background:{BASE};color:{tinta if slug in ('ameixa','petroleo') else TINTA}">4</div><div class="t">PASSO 4</div></div>
  <h1>O plano <b style="{kw_sobre}">é seu.</b></h1>
  <p class="sub">Montado a partir do que é importante para você, nos pilares da Medicina do Estilo de Vida:</p>
  <div class="pills" style="margin-top:40px">""" + ''.join(
        f'<span class="pill" style="border:3px solid {sobre};color:{sobre}">{p}</span>'
        for p in ['Alimentação', 'Movimento', 'Sono', 'Estresse', 'Vícios', 'Relações']) + """</div>
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
