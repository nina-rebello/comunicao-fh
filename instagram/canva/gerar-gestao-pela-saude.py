# Monta canva/gestao-pela-saude.html, a versão do post "Gestão de pessoas que começa pela saúde" (v4) para importar
# no Canva com tudo editável. Slides: j01, j02, j03, j04, j05b (ecossistema, opção B) e j06t (final em Tiffany,
# escolha da Nina em 15/10).
# Cada texto, cartão, linha, bolinha e paginação vira um elemento solto. Os logos entram como imagem.
# Não vão no HTML, porque no Canva ficam melhores como formas nativas, criadas depois da importação:
#   - o triângulo com a foto (forma de triângulo preenchida com a foto, trocável);
#   - o contorno do triângulo.
# Atenção: formas criadas pela API do Canva não aceitam foto dentro. Para o triângulo com foto, use uma forma que
# veio na importação (uma das bolinhas da j01): troque a forma pelo triângulo "M340 0 L680 410 L0 410 Z", ajuste
# para 680 × 410 em x 200, y 600, preencha com a foto e desenhe de novo a bolinha usada. Feito assim em 15/10
# (design DAHYHdC4cus).
#
# Uso:
#   node ../ferramentas/dump-posicoes.mjs ../posts/gestao-pela-saude/slides-v4.html dump.json
#   python3 gerar-gestao-pela-saude.py dump.json BASE gestao-pela-saude.html
#   BASE: raiz de instagram/ (URL raw do GitHub para importar, ou caminho local para conferir)
import json, sys

DUMP, BASE, SAIDA = sys.argv[1:4]
G = BASE if BASE.endswith('/') else BASE + '/'
TIF, VERDE, CREME = '#96C5BD', '#1F3A36', '#F0F0E9'
ORDEM = ['j01', 'j02', 'j03', 'j04', 'j05b', 'j06t']
COR = {'fairdata': '#767171', 'fairhealth': '#96C5BD', 'fairedu': '#6E35A2', 'fairtrust': '#145C9D'}


def div(x, y, w, h, estilo):
    return '<div style="left:%.1fpx;top:%.1fpx;width:%.1fpx;height:%.1fpx;%s"></div>' % (x, y, w, h, estilo)


def bola(cx, cy, r, cor):
    return div(cx - r, cy - r, 2 * r, 2 * r, 'border-radius:50%;background:' + cor)


def texto(it):
    html = it['html'].upper() if it['tt'] == 'uppercase' else it['html']
    w, x = it['w'], it['x']
    um = it['lines'] <= 1
    ta = {'start': 'left', 'left': 'left', 'center': 'center', 'right': 'right', 'end': 'right'}[it['ta']]
    if um and ta == 'left':
        w = it['tw'] + 16
    est = ['left:%.1fpx' % x, 'top:%.1fpx' % it['y'], 'width:%.1fpx' % w, 'font-size:%s' % it['fs'], 'line-height:%s' % it['lh'],
           'font-weight:%s' % it['fw'], 'font-style:%s' % it['fst'], 'color:%s' % it['color'], 'text-align:%s' % ta]
    if it['ls'] != 'normal':
        est.append('letter-spacing:%s' % it['ls'])
    if um:
        est.append('white-space:nowrap')
    return '<p style="%s">%s</p>' % (';'.join(est), html)


def caixa(it):
    est = ['border-radius:%s' % it['radius']]
    if it.get('bg'):
        est.append('background:%s' % it['bg'])
    return div(it['x'], it['y'], it['w'], it['h'], ';'.join(est))


# formas que no HTML original estão em SVG (o dump não lê SVG)
def extra(sid):
    out = []
    if sid == 'j01':
        # pontas do triângulo: círculo vazado (verde por fora, Tiffany por dentro)
        for cx, cy in ((540, 600), (200, 1010), (880, 1010)):
            out += [bola(cx, cy, 14.25, VERDE), bola(cx, cy, 11.75, TIF)]
    elif sid == 'j02':
        out.append(div(131, 560, 10, 340, 'border-radius:5px;background:' + TIF))
        out += [bola(136, y, 26, TIF) for y in (560, 730, 900)]
    elif sid == 'j05b':
        xs = [186, 422, 658, 894]
        meios = [(xs[i] + xs[i + 1]) / 2 for i in range(3)]
        nomes = ['fairdata', 'fairhealth', 'fairedu', 'fairtrust']
        for i, n in enumerate(nomes):
            a = xs[0] if i == 0 else meios[i - 1]
            b = xs[-1] if i == 3 else meios[i]
            out.append(div(a, 556, b - a, 8, 'background:' + COR[n]))
        for x, n in zip(xs, nomes):
            out.append(bola(x, 560, 26 if n == 'fairhealth' else 16, COR[n]))
    return out


dump = {s['id']: s for s in json.load(open(DUMP))}
pags = []
for sid in ORDEM:
    s = dump[sid]
    els = extra(sid)
    for it in s['items']:
        if it['t'] == 'text':
            els.append(texto(it))
        elif it['t'] == 'box':
            els.append(caixa(it))
        elif it['t'] == 'img':
            src = G + it['src'].split('../')[-1]
            els.append('<img src="%s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">' % (src, it['x'], it['y'], it['w'], it['h']))
    pags.append('<section data-document-role="page" class="slide" id="%s" style="background:%s">\n  %s\n</section>' % (sid, s['bg'], '\n  '.join(els)))

fontes = ''.join('@font-face{font-family:Raleway;font-weight:%s;font-style:%s;src:url(%smarca/fontes/raleway-latin-%s-%s.woff2)}\n' % (p, e, G, p, e)
                 for p in ('400', '800') for e in ('normal', 'italic'))
open(SAIDA, 'w').write('''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Gestão de pessoas que começa pela saúde (para o Canva)</title><style>
%s*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#ccc}
.slide{width:1080px;min-width:1080px;height:1350px;flex:none;position:relative;overflow:hidden;font-family:Raleway,sans-serif;font-variant-numeric:lining-nums}
.slide>*{position:absolute}
</style></head><body>
%s
</body></html>
''' % (fontes, '\n\n'.join(pags)))
print('ok', len(pags))
