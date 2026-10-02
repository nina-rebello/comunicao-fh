# Gera os slides de teste e os cartazes de comparação de cor complementar.
# Uso: python3 instagram/estudos/cores/gerar.py
# Depois: node instagram/ferramentas/render.mjs instagram/estudos/cores/slides.html instagram/estudos/cores/png
import pathlib

AQUI = pathlib.Path(__file__).parent
CREME, BASE, TINTA = '#F0F0E9', '#9FC5BD', '#1F3A36'

# nome, hex, escura?, nota técnica
CORES = [
    ('ameixa', 'Ameixa', '#603A42', True,
     'Oposta exata do verde-água (347° x 167°) e com a claridade invertida. Sóbria, afetiva e elegante. Pode ser fundo e também cor de texto.'),
    ('coral', 'Coral', '#EC7768', False,
     'Quase oposta ao verde-água e bem saturada: a mais viva e calorosa. Pede texto escuro por cima; sobre o verde-água entra como marca-texto e botão.'),
    ('amarelo', 'Amarelo', '#EDB84A', False,
     'Luz e otimismo. Ótima para destacar. Atenção: é parecida com o amarelo do fairedu (#F7C552), então as marcas podem se confundir no feed.'),
    ('terracota', 'Terracota', '#B4532F', True,
     'Quente e terrosa, conversa com a pedra e a madeira do Escritório do Cuidado. Não lembra nada do fairedu. Aceita texto claro por cima.'),
    ('pessego', 'Pêssego', '#F3A683', False,
     'A versão mais suave e acolhedora do coral. Dá vida sem pesar. Pede texto escuro e funciona melhor em fundos e detalhes do que em letras.'),
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
    tinta = hexa if slug == 'ameixa' else TINTA
    sobre = CREME if escura else TINTA
    destaque_sobre = BASE if escura else CREME
    # palavra-chave nos fundos claros: a própria cor se tiver contraste; senão tinta com marca-texto
    kw_creme = f'color:{hexa};{marca(BASE)}' if escura else f'color:{TINTA};{marca(hexa)}'
    kw_base = f'color:{hexa}' if slug == 'ameixa' else f'color:{TINTA};{marca(hexa if not escura else CREME)}'
    if slug == 'terracota':
        kw_base = f'color:{TINTA};{marca(hexa)}'
    pill_on = CREME if escura else TINTA
    kw_sobre = f'color:{BASE}' if escura else f'color:{TINTA};{marca(CREME)}'
    return f"""
<section class="slide" id="{slug}-1" style="background:{CREME};color:{tinta}"><div class="pag">6/10</div>
  <div class="passo"><div class="n" style="background:{BASE};color:{tinta}">3</div><div class="t">PASSO 3</div></div>
  <h1>Entender <b style="{kw_creme}">antes de propor.</b></h1>
  <div class="pills"><span class="pill" style="background:{hexa};color:{pill_on}">Bioimpedância</span><span class="pill" style="background:{hexa};color:{pill_on}">Smartband por 48 horas</span></div>
  <p class="sub">Para conhecer seu sono e seu dia a dia de verdade. <b>Para entender, não para julgar.</b></p>
  <div class="handle">@fairhealth.br</div>
</section>
<section class="slide centro" id="{slug}-2" style="background:{BASE};color:{tinta}"><div class="pag">10/10</div>
  <img class="logo" src="../../marca/logo-circulo.png" alt="">
  <h1 style="font-size:96px">E para você, <b style="{kw_base}">o que é importante?</b></h1>
  <span class="botao" style="background:{hexa};color:{pill_on}">Conta pra gente nos comentários</span>
  <p class="assina">« Fazemos o certo pelos motivos certos »</p>
  <div class="handle" style="left:0;right:0;text-align:center">@fairhealth.br</div>
</section>
<section class="slide" id="{slug}-3" style="background:{hexa};color:{sobre}"><div class="pag">7/10</div>
  <div class="passo"><div class="n" style="background:{BASE};color:{tinta if slug=='ameixa' else TINTA}">4</div><div class="t">PASSO 4</div></div>
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

# cartazes: um por cor e um geral
CARTAZ_CSS = """
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#FAFAF7;color:#1F3A36;width:1700px;padding:64px 70px}
.topo{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:34px}
h1{font-size:44px;font-weight:700}
.sub{font-size:20px;color:#4a5a57;margin-top:8px}
.paleta{display:flex;gap:10px;align-items:center;font-size:16px;color:#4a5a57}
.paleta i{display:inline-block;width:42px;height:42px;border-radius:50%;border:1px solid rgba(0,0,0,.08)}
.bloco{margin-bottom:56px}
.cab{display:flex;align-items:center;gap:18px;margin-bottom:18px}
.cab .sw{width:56px;height:56px;border-radius:50%}
.cab h2{font-size:34px;font-weight:700}
.cab code{font-size:20px;color:#4a5a57;font-family:ui-monospace,monospace}
.nota{font-size:18px;line-height:1.5;color:#3b4a47;max-width:1300px;margin-bottom:20px}
.trio{display:flex;gap:28px}
.trio figure{width:500px}
.trio img{width:500px;height:625px;display:block;box-shadow:0 6px 24px rgba(0,0,0,.10)}
.trio figcaption{font-size:16px;color:#4a5a57;margin-top:10px}
"""

def bloco(slug, nome, hexa, nota):
    return f"""<div class="bloco"><div class="cab"><div class="sw" style="background:{hexa}"></div><h2>{nome}</h2><code>{hexa}</code></div>
<p class="nota">{nota}</p><div class="trio">
<figure><img src="png/{slug}-1.png"><figcaption>Fundo creme #F0F0E9</figcaption></figure>
<figure><img src="png/{slug}-2.png"><figcaption>Fundo base #9FC5BD</figcaption></figure>
<figure><img src="png/{slug}-3.png"><figcaption>Fundo {nome.lower()} {hexa}</figcaption></figure></div></div>"""

def pagina(titulo, blocos):
    pal = ''.join(f'<i style="background:{c}"></i>' for c in [CREME, BASE])
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title><style>{CARTAZ_CSS}</style></head><body>'
            f'<div class="topo"><div><h1>{titulo}</h1><p class="sub">fairhealth · teste de cor complementar · os mesmos 3 slides em cada cor</p></div>'
            f'<div class="paleta">base da marca {pal}</div></div>{blocos}</body></html>')

for s, n, h, e, nota in CORES:
    (AQUI / f'cartaz-{s}.html').write_text(pagina(f'Cor complementar: {n}', bloco(s, n, h, nota)))
(AQUI / 'cartaz.html').write_text(pagina('Cor complementar: comparação', ''.join(bloco(s, n, h, nota) for s, n, h, e, nota in CORES)))
print('ok')
