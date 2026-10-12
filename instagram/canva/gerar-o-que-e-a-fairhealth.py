# Monta canva/o-que-e-a-fairhealth.html, a versão do carrossel v7 para importar no Canva.
# Cada texto, linha, cartão, bolinha e círculo vira um elemento solto e editável. Só a luz dos slides 1, 4 e 10
# e as fatias de foto da rosca entram como imagem (PNG em canva/o-que-e-a-fairhealth/).
#
# Uso: python3 gerar-o-que-e-a-fairhealth.py dump.json BASE saida.html
#   dump.json: posições tiradas de slides-v7.html (dump.mjs, no README desta pasta)
#   BASE: raiz de instagram/ (URL raw do GitHub para importar, ou caminho local para conferir)
import json, math, sys

DUMP, BASE, SAIDA = sys.argv[1:4]
GER = BASE + '/' if not BASE.endswith('/') else BASE
src = open(__file__.rsplit('/', 2)[0] + '/posts/o-que-e-a-fairhealth/gerar_slides_v7.py').read()
ns = {}
exec(src[:src.index('S = []')].replace('SAIDA = sys.argv[1]', 'SAIDA = None'), ns)
CX, CY, R, r, PASSO, ANG, PIL = ns['CX'], ns['CY'], ns['R'], ns['r'], ns['PASSO'], ns['ANG'], ns['PILARES']
pol = ns['pol']

TIF, VERDE, CREME, TCLARO, VLOGO = '#96C5BD', '#1F3A36', '#F0F0E9', '#BFE0D9', '#2F6B64'
A = GER + 'canva/o-que-e-a-fairhealth/'

def div(x, y, w, h, estilo):
    return '<div style="left:%.1fpx;top:%.1fpx;width:%.1fpx;height:%.1fpx;%s"></div>' % (x, y, w, h, estilo)

def bola(cx, cy, raio, estilo):
    return div(cx - raio, cy - raio, 2 * raio, 2 * raio, 'border-radius:50%;' + estilo)

def svg(x, y, w, h, corpo):
    return ('<svg style="left:%.1fpx;top:%.1fpx;width:%.1fpx;height:%.1fpx" viewBox="%.1f %.1f %.1f %.1f" '
            'xmlns="http://www.w3.org/2000/svg">%s</svg>') % (x, y, w, h, x, y, w, h, corpo)

def img(src, x, y, w, h):
    return '<img src="%s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">' % (src, x, y, w, h)

# ---------------------------------------------------------------- formas de cada slide
def venn():
    C = [(640, 760), (540, 930), (740, 930)]; rv = 170
    out = [bola(cx, cy, rv, 'background:rgba(150,197,189,.5)') for cx, cy in C]
    # encontro dos três: três arcos entre os pontos de cruzamento que ficam dentro do terceiro círculo
    def cruz(p, q, outro):
        (x0, y0), (x1, y1) = p, q
        d = math.hypot(x1 - x0, y1 - y0); a = d / 2; h = math.sqrt(rv * rv - a * a)
        mx, my = x0 + (x1 - x0) / 2, y0 + (y1 - y0) / 2
        for s in (1, -1):
            px, py = mx + s * h * (y1 - y0) / d, my - s * h * (x1 - x0) / d
            if math.hypot(px - outro[0], py - outro[1]) < rv: return px, py
    pab, pbc, pca = cruz(C[0], C[1], C[2]), cruz(C[1], C[2], C[0]), cruz(C[2], C[0], C[1])
    d = 'M%.1f %.1f A%d %d 0 0 1 %.1f %.1fA%d %d 0 0 1 %.1f %.1fA%d %d 0 0 1 %.1f %.1fZ' % (
        pab + (rv, rv) + pca + (rv, rv) + pbc + (rv, rv) + pab)
    xs = [pab[0], pbc[0], pca[0]]; ys = [pab[1], pbc[1], pca[1]]
    out.append(svg(min(xs) - 30, min(ys) - 30, max(xs) - min(xs) + 60, max(ys) - min(ys) + 60, '<path d="%s" fill="%s"/>' % (d, VLOGO)))
    tx, ty = sum(c[0] for c in C) / 3, sum(c[1] for c in C) / 3
    out.append(div(96, ty - 1, tx - 96, 2, 'background:' + VLOGO))
    out.append(bola(tx, ty, 6, 'background:' + CREME))
    return out

def linha_do_tempo():
    out = [div(110, 698.5, 860, 3, 'background:rgba(191,224,217,.5)'),
           svg(934, 682, 42, 36, '<path d="M940 686l30 14-30 14" fill="none" stroke="#BFE0D9" stroke-opacity=".5" stroke-width="3" stroke-linejoin="round"/>')]
    out += [bola(x, 700, 14, 'background:' + TIF) for x in (160, 340)]
    # formas com contorno vão como vetor: no Canva, div com borda perde o arredondado
    out += [svg(x - 16, 684, 32, 32, '<circle cx="%d" cy="700" r="12" fill="#1F3A36" stroke="#BFE0D9" stroke-opacity=".6" stroke-width="3"/>' % x) for x in (520, 700, 880)]
    out.append(div(110, 560, 290, 70, 'border-radius:35px;background:' + TIF))
    out.append(svg(468, 558, 464, 74, '<rect x="470" y="560" width="460" height="70" rx="35" fill="none" stroke="#BFE0D9" stroke-opacity=".55" stroke-width="2"/>'))
    return out

def rosca():
    out = []
    for k, ((n, nome, foto, alin, lado), ang) in enumerate(zip(PIL, ANG)):
        x, y, w, h = ns['caixa'](CX, CY, R, r, ang - PASSO / 2, ang + PASSO / 2)
        out.append(img(A + 'fatia-%s.png' % n, int(x) - 2, int(y) - 2, int(w) + 5, int(h) + 5))
    for k, ((n, nome, foto, alin, lado), ang) in enumerate(zip(PIL, ANG)):
        x0, y0 = pol(CX, CY, R + 10, ang)
        if lado == 'baixo':
            pts = [(x0, y0), (x0, y0 + 34)]
        elif lado in ('dir', 'esq'):
            x1, y1 = pol(CX, CY, R + 40, ang); pts = [(x0, y0), (x1, y1), (984 if lado == 'dir' else 96, y1)]
        else:
            x1, y1 = pol(CX, CY, R + 52, ang); pts = [(x0, y0), (x1, y1), (984 if lado.startswith('dir') else 96, y1)]
        xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
        d = 'M' + ' L'.join('%.1f %.1f' % p for p in pts)
        out.append(svg(min(xs) - 8, min(ys) - 8, max(xs) - min(xs) + 16, max(ys) - min(ys) + 16,
                       '<path d="%s" fill="none" stroke="#1F3A36" stroke-opacity=".45" stroke-width="2"/><circle cx="%.1f" cy="%.1f" r="5" fill="#1F3A36"/>' % (d, x0, y0)))
    return out

FIO = ns['FIO']
def fio6():
    return [svg(0, 420, 1080, 730, '<path d="%s" fill="none" stroke="#96C5BD" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>' % FIO)]

def fio7():
    out = ['<svg style="left:0px;top:430px;width:150px;height:620px" viewBox="1080 430 150 620" xmlns="http://www.w3.org/2000/svg">'
           '<path d="%s" fill="none" stroke="#96C5BD" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>' % FIO]
    out += [bola(136, y, 30, 'background:' + VERDE) for y in (486, 671, 856, 1041)]
    return out

def passos11():
    return [div(130, 440, 12, 412, 'border-radius:6px;background:' + CREME)] + [bola(136, y, 30, 'background:' + VERDE) for y in (446, 646, 846)]

EXTRA = {'a02': venn, 'a03': linha_do_tempo, 'a05': rosca, 'a06': fio6, 'a07': fio7, 'a11': passos11}
LUZ = {'a01', 'a04', 'a10'}

# ---------------------------------------------------------------- textos e formas tirados da v7
def texto(it):
    html = it['html']
    if it['tt'] == 'uppercase':
        html = html.upper()
    w, x = it['w'], it['x']
    um = it['lines'] <= 1
    ta = {'start': 'left', 'left': 'left', 'center': 'center', 'right': 'right', 'end': 'right'}[it['ta']]
    if um and ta == 'left':
        w = it['tw'] + 16
    est = ['left:%.1fpx' % x, 'top:%.1fpx' % it['y'], 'width:%.1fpx' % w, 'font-size:%s' % it['fs'], 'line-height:%s' % it['lh'],
           'font-weight:%s' % it['fw'], 'font-style:%s' % it['fst'], 'color:%s' % it['color'], 'text-align:%s' % ta]
    if it['ls'] != 'normal': est.append('letter-spacing:%s' % it['ls'])
    if um: est.append('white-space:nowrap')
    if it['op'] < 0.99: est.append('opacity:%.2f' % it['op'])
    return '<p style="%s">%s</p>' % (';'.join(est), html)

def caixa(it):
    if it.get('border'):  # contorno arredondado (etiquetas da luz) vai como vetor
        bw, _, cor = it['border'].split(' ', 2)
        bw = float(bw[:-2]); rad = min(float(it['radius'][:-2]), it['h'] / 2)
        # no vetor, o Canva ignora cor rgba: vai em hexadecimal com stroke-opacity
        v = [float(t) for t in cor[cor.index('(') + 1:cor.index(')')].split(',')]
        hexa, op = '#%02X%02X%02X' % tuple(int(t) for t in v[:3]), (v[3] if len(v) > 3 else 1)
        return svg(it['x'], it['y'], it['w'], it['h'], '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="none" stroke="%s" stroke-opacity="%.2f" stroke-width="%.1f"/>' % (
            it['x'] + bw / 2, it['y'] + bw / 2, it['w'] - bw, it['h'] - bw, rad - bw / 2, hexa, op, bw))
    est = ['border-radius:%s' % it['radius']]
    if it.get('bg'): est.append('background:%s' % it['bg'])
    if it.get('border'): est.append('border:%s;box-sizing:border-box' % it['border'])
    if it['op'] < 0.99: est.append('opacity:%.2f' % it['op'])
    return div(it['x'], it['y'], it['w'], it['h'], ';'.join(est))

dump = json.load(open(DUMP))
pags = []
for s in dump:
    els = []
    if s['id'] in LUZ:
        els.append(img(A + 'fundo-luz-%s.jpg' % s['id'], 0, 0, 1080, 1350))
    els += EXTRA.get(s['id'], lambda: [])()
    for it in s['items']:
        if it['t'] == 'text': els.append(texto(it))
        elif it['t'] == 'box': els.append(caixa(it))
        elif it['t'] == 'img': els.append(img(GER + it['src'].split('../')[-1], it['x'], it['y'], it['w'], it['h']))
    pags.append('<section data-document-role="page" class="slide" id="%s" style="background:%s">\n  %s\n</section>' % (s['id'], s['bg'], '\n  '.join(els)))

fontes = ''.join('@font-face{font-family:Raleway;font-weight:%s;font-style:%s;src:url(%smarca/fontes/raleway-latin-%s-%s.woff2)}\n' % (p, e, GER, p, e)
                 for p in ('400', '800') for e in ('normal', 'italic'))
open(SAIDA, 'w').write('''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>O que é a fairhealth (carrossel v7, para o Canva)</title><style>
%s*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#ccc}
.slide{width:1080px;min-width:1080px;height:1350px;flex:none;position:relative;overflow:hidden;font-family:Raleway,sans-serif;font-variant-numeric:lining-nums}
.slide>*{position:absolute}
</style></head><body>
%s
</body></html>
''' % (fontes, '\n\n'.join(pags)))
print('ok', len(pags))
