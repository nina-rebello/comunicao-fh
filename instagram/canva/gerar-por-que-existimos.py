# Monta o HTML de importação no Canva do post de 21/10, "Por que a fairhealth existe?" (versão H, escolhida pela
# Nina em 19/10). Cada slide vira uma página: o fundo entra como imagem (papel, linha, bolinhas, círculo do logo e
# seta, já desenhados em png-h-fundo/), e por cima vão os textos, soltos e editáveis, em Raleway, e o logo.
# Mesma lógica de texto de gerar-gestao-pela-saude.py.
# Uso:
#   node ../ferramentas/dump-posicoes.mjs ../posts/por-que-existimos/slides-h.html por-que-existimos-h-dump.json
#   python3 gerar-por-que-existimos.py por-que-existimos-h-dump.json BASE por-que-existimos-h.html
#   BASE: raiz de instagram/ (URL raw do GitHub num commit, para importar, ou caminho local, para conferir)
#   Versão H2 (com a mão na capa): ... por-que-existimos-h2-dump.json BASE por-que-existimos-h2.html png-h2-fundo
import json
import sys

DUMP, BASE, SAIDA = sys.argv[1:4]
G = BASE if BASE.endswith('/') else BASE + '/'
# quarto argumento opcional: a pasta dos fundos (png-h-fundo, da H; png-h2-fundo, da H2, com a mão na capa)
FUNDO = G + 'posts/por-que-existimos/%s/%%s.png' % (sys.argv[4] if len(sys.argv) > 4 else 'png-h-fundo')


def texto(it):
    html = it['html'].upper() if it['tt'] == 'uppercase' else it['html']
    w, x = it['w'], it['x']
    um = it['lines'] <= 1
    ta = {'start': 'left', 'left': 'left', 'center': 'center', 'right': 'right', 'end': 'right'}[it['ta']]
    if um and ta == 'left':
        w = it['tw'] + 16
    elif um and ta == 'right':
        x, w = it['tx'] - 16, it['tw'] + 16
    est = ['left:%.1fpx' % x, 'top:%.1fpx' % it['y'], 'width:%.1fpx' % w, 'font-size:%s' % it['fs'], 'line-height:%s' % it['lh'],
           'font-weight:%s' % it['fw'], 'font-style:%s' % it['fst'], 'color:%s' % it['color'], 'text-align:%s' % ta]
    if it['ls'] != 'normal':
        est.append('letter-spacing:%s' % it['ls'])
    if um:
        est.append('white-space:nowrap')
    return '<p style="%s">%s</p>' % (';'.join(est), html)


dump = json.load(open(DUMP))
pags = []
for s in dump:
    els = ['<img src="%s" style="left:0;top:0;width:1080px;height:1350px">' % (FUNDO % s['id'])]
    for it in s['items']:
        if it['t'] == 'text':
            els.append(texto(it))
        elif it['t'] == 'img':
            src = G + it['src'].split('../')[-1]
            els.append('<img src="%s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">' % (src, it['x'], it['y'], it['w'], it['h']))
    pags.append('<section data-document-role="page" class="slide" id="%s" style="background:%s">\n  %s\n</section>' % (s['id'], s['bg'], '\n  '.join(els)))

fontes = ''.join('@font-face{font-family:Raleway;font-weight:%s;font-style:%s;src:url(%smarca/fontes/raleway-latin-%s-%s.woff2)}\n' % (p, e, G, p, e)
                 for p in ('400', '800') for e in ('normal', 'italic'))
open(SAIDA, 'w').write('''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (21/10)</title><style>
%s*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#ccc}
.slide{width:1080px;min-width:1080px;height:1350px;flex:none;position:relative;overflow:hidden;font-family:Raleway,sans-serif;font-variant-numeric:lining-nums}
.slide>*{position:absolute}
</style></head><body>
%s
</body></html>
''' % (fontes, '\n\n'.join(pags)))
print('ok', len(pags))
