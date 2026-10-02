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
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 40px}}
.slide>*{{position:absolute}}
.k{{font-size:26px;font-weight:700;letter-spacing:8px;display:flex;align-items:center;gap:22px}}
.k i{{display:block;width:64px;height:4px;background:currentColor}}
h1{{font-weight:400;line-height:1.02;letter-spacing:-2px}}
h1 b{{font-weight:800;font-style:italic;letter-spacing:-1px}}
.p{{font-size:40px;line-height:1.35}}
.p b{{font-weight:800;font-style:italic}}
.pag{{top:96px;right:96px;font-size:28px;font-weight:500;opacity:.7}}
.handle{{bottom:84px;left:96px;font-size:30px;font-weight:700}}
.num{{font-size:1100px;font-weight:800;font-style:italic;line-height:.8;letter-spacing:-40px}}
.pill{{display:inline-block;font-size:34px;font-weight:700;padding:20px 36px;border-radius:60px;margin:0 14px 16px 0}}
"""

def marca(cor):
    return f"background:linear-gradient(transparent 74%,{cor} 74%,{cor} 94%,transparent 94%)"

def slides(slug, hexa, escura):
    escura_txt = slug in ('ameixa', 'petroleo')          # a cor serve como cor de texto nos fundos claros
    tinta = hexa if escura_txt else TINTA                  # texto nos fundos creme e base
    sobre = CREME if escura else TINTA                     # texto sobre o fundo da cor
    kw_creme = f'color:{hexa};{marca(BASE)}' if escura else f'color:{TINTA};{marca(hexa)}'
    kw_base = f'color:{hexa}' if escura_txt else f'color:{TINTA};{marca(hexa)}'
    kw_sobre = f'color:{BASE}' if escura else f'color:{TINTA};{marca(CREME)}'
    if slug == 'framboesa':
        kw_sobre = f'color:{CREME}'
    on = CREME if escura else TINTA                        # texto dentro de etiqueta/botão na cor
    pilares = ''.join(f'<span class="pill" style="border:3px solid {sobre};color:{sobre}">{p}</span>'
                      for p in ['Alimentação', 'Movimento', 'Sono', 'Estresse', 'Vícios', 'Relações'])
    return f"""
<section class="slide" id="{slug}-1" style="background:{CREME};color:{tinta}">
  <div class="num" style="right:-70px;bottom:-140px;font-size:940px;color:{BASE};opacity:.5">3</div>
  <div class="pag">6/10</div>
  <div class="k" style="left:96px;top:96px"><i></i>PASSO 3</div>
  <h1 style="left:96px;top:250px;width:900px;font-size:128px">Entender<br><b style="{kw_creme}">antes de<br>propor.</b></h1>
  <div style="left:96px;top:700px;width:900px">
    <span class="pill" style="background:{hexa};color:{on}">Bioimpedância</span><span class="pill" style="background:{hexa};color:{on}">Smartband por 48 horas</span>
  </div>
  <p class="p" style="left:96px;top:870px;width:640px">Para conhecer seu sono e seu dia a dia de verdade.<br><b>Para entender, não para julgar.</b></p>
  <div class="handle">@fairhealth.br</div>
</section>
<section class="slide" id="{slug}-2" style="background:{BASE};color:{tinta}">
  <div style="left:50%;top:50%;width:1240px;height:1240px;margin:-620px 0 0 -620px;border-radius:50%;border:3px solid {tinta};opacity:.18"></div>
  <div style="left:50%;top:50%;width:900px;height:900px;margin:-450px 0 0 -450px;border-radius:50%;background:{CREME};opacity:.35"></div>
  <div class="pag">10/10</div>
  <img src="../../marca/logo-circulo.png" style="left:50%;top:150px;width:170px;margin-left:-85px;border-radius:50%;box-shadow:0 0 0 14px {CREME}">
  <div class="k" style="left:0;right:0;top:420px;justify-content:center">E PARA VOCÊ,</div>
  <h1 style="left:70px;right:70px;top:490px;text-align:center;font-size:136px">o que é <b style="{kw_base}">importante?</b></h1>
  <div style="left:0;right:0;top:880px;text-align:center"><span class="pill" style="background:{hexa};color:{on};font-size:38px;padding:28px 56px;margin:0">Conta pra gente nos comentários</span></div>
  <p style="left:0;right:0;top:1030px;text-align:center;font-size:30px;font-style:italic">« Fazemos o certo pelos motivos certos »</p>
  <div class="handle" style="left:0;right:0;text-align:center">@fairhealth.br</div>
</section>
<section class="slide" id="{slug}-3" style="background:{hexa};color:{sobre}">
  <div class="num" style="right:-170px;top:-330px;color:{BASE};opacity:{'.22' if escura else '.35'}">4</div>
  <div class="pag">7/10</div>
  <div class="k" style="left:96px;top:96px"><i></i>PASSO 4</div>
  <h1 style="left:96px;top:330px;font-size:150px">O plano<br><b style="{kw_sobre}">é seu.</b></h1>
  <p class="p" style="left:96px;top:690px;width:860px">Montado a partir do que é importante para você, nos pilares da Medicina do Estilo de Vida:</p>
  <div style="left:96px;top:900px;width:900px">{pilares}</div>
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
