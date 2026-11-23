"""Prepara as imagens do carrossel de 04/12 (case de adesão): recorta a foto de banco da capa em 1080 x 1350 e gera o
degradê no verde da marca (o mesmo do carrossel de 25/11), como PNG por cima da foto (o Canva não lê degradê de CSS).
A foto é de banco (Licença Unsplash, instagram/marca/fotos-banco/README.md): nunca apresentar como colaborador atendido.
Uso: python3 instagram/posts/case-adesao/gerar.py [arquivo da foto] [posição x 0-1] [posição y 0-1]"""
import sys
from pathlib import Path
from PIL import Image
AQUI = Path(__file__).parent
RAIZ = AQUI.parent.parent.parent
foto = sys.argv[1] if len(sys.argv) > 1 else 'industria2.jpg'
px = float(sys.argv[2]) if len(sys.argv) > 2 else .5
py = float(sys.argv[3]) if len(sys.argv) > 3 else .5
W, H = 1080, 1350
im = Image.open(RAIZ / 'instagram/marca/fotos-banco' / foto).convert('RGB')
w, h = im.size
k = max(W / w, H / h)
cw, ch = W / k, H / k
x0, y0 = (w - cw) * px, (h - ch) * py
im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((W, H), Image.LANCZOS).save(AQUI / 'fotos/capa.jpg', quality=88)
# degradê: transparente até 28%, verde da marca a 60% em 55% e a 95% de 82% para baixo
g = Image.new('RGBA', (216, 270))
px_ = g.load()
for y in range(270):
    t = y / 269
    a = 0 if t <= .28 else (.6 * (t - .28) / .27 if t <= .55 else (.6 + .35 * (t - .55) / .27 if t <= .82 else .95))
    for x in range(216):
        px_[x, y] = (47, 107, 100, round(a * 255))
g.save(AQUI / 'fotos/degrade.png', optimize=True)
print('ok', foto, px, py)
