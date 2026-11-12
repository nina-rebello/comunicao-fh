"""Gera os marca-textos com textura do carrossel de 13/11: mede cada [data-mk] do slides.html
(instagram/ferramentas/medir-marcas.mjs), desenha a textura em Tiffany (instagram/ferramentas/textura.py) e
grava o tamanho e a posição de cada <img data-tx> no slides.html.
Uso: python3 instagram/posts/levar-para-empresa/gerar.py"""
import json, re, subprocess, sys
from pathlib import Path
AQUI = Path(__file__).parent
RAIZ = AQUI.parent.parent.parent
sys.path.insert(0, str(RAIZ / 'instagram/ferramentas'))
import textura
html = AQUI / 'slides.html'
medidas = json.loads(subprocess.check_output(['node', str(RAIZ / 'instagram/ferramentas/medir-marcas.mjs'), str(html)]))
s = html.read_text()
for i, m in enumerate(medidas):
    x, y, w, h = round(m['x']) - 4, round(m['y']) + 4, round(m['w']) + 8, round(m['h']) - 4
    img = textura.marca(w, h, (159, 197, 189), seed=i + 3)
    img.save(AQUI / 'fotos' / f"tx-{m['id']}.png")
    s = re.sub(rf'<img src="fotos/tx-{m["id"]}.png" class="abs" data-tx="{m["id"]}" alt=""[^>]*>',
               f'<img src="fotos/tx-{m["id"]}.png" class="abs" data-tx="{m["id"]}" alt="" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">', s)
    print(m['id'], x, y, w, h)
html.write_text(s)
