"""Gera o canva.html da versão LinkedIn abaixo de 10 MB (limite de importação do Canva): copia para fotos-canva/ os
fundos (1080 x 1080, JPEG 84), a foto do slide 5 (1080 x 300) e os PNGs com paleta, monta canva-src.html
apontando para eles e roda canva.mjs.
Uso: python3 linkedin/posts/nr01-afastamentos/canva-leve.py"""
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
    if rel == 'n-05.jpg':
        im.convert('RGB').resize((1080, 300), Image.LANCZOS).save(LEVE / rel, quality=88, optimize=True)
    elif rel.endswith('.jpg'):
        im.convert('RGB').resize((1080, 1080), Image.LANCZOS).save(LEVE / rel, quality=84, optimize=True)
    else:
        im.convert('RGBA').quantize(colors=64, method=Image.Quantize.FASTOCTREE).save(LEVE / rel, optimize=True)
html = html.replace('src="fotos/', 'src="fotos-canva/')
(AQUI / 'canva-src.html').write_text(html)
subprocess.run(['node', str(RAIZ / 'instagram/ferramentas/canva.mjs'), str(AQUI / 'canva-src.html'), str(AQUI / 'canva.html')], check=True)
