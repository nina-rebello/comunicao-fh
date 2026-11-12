"""Gera o canva.html do carrossel abaixo de 10 MB (limite de importação do Canva): copia os fundos e os
marca-textos usados pelo slides.html para fotos-canva/ em versão leve (fundos em 1080 x 1350, JPEG 84;
marca-textos em PNG com paleta), monta canva-src.html apontando para eles e roda canva.mjs.
Uso: python3 instagram/posts/levar-para-empresa/canva-leve.py"""
import re, subprocess
from pathlib import Path
from PIL import Image
AQUI = Path(__file__).parent
RAIZ = AQUI.parent.parent.parent
LEVE = AQUI / 'fotos-canva'
LEVE.mkdir(exist_ok=True)
html = (AQUI / 'slides.html').read_text()
for rel in sorted(set(re.findall(r'src="fotos/([^"]+)"', html))):
    im = Image.open(AQUI / 'fotos' / rel)
    if rel.endswith('.jpg'):
        im.convert('RGB').resize((1080, 1350), Image.LANCZOS).save(LEVE / rel, quality=84, optimize=True)
    else:
        w, h = im.size
        im = im.convert('RGBA')
        im.quantize(colors=48, method=Image.Quantize.FASTOCTREE).save(LEVE / rel, optimize=True)
html = html.replace('src="fotos/', 'src="fotos-canva/')
(AQUI / 'canva-src.html').write_text(html)
subprocess.run(['node', str(RAIZ / 'instagram/ferramentas/canva.mjs'), str(AQUI / 'canva-src.html'), str(AQUI / 'canva.html')], check=True)
