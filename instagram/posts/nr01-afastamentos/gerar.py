"""Gera as imagens do carrossel de 18/11 que o Canva precisa receber prontas.

- fundos com granulado (Tiffany e verde-escuro); o creme com brilho e o papel vêm do carrossel de 11/11;
- barras do gráfico (slide 3) e fita adesiva (slide 7), com textura de tinta impressa;
- recorte da NR-01 (slide 4), a partir de recorte.html;
- marca-textos: mede cada linha [data-mk] do slides.html, gera a textura no tamanho certo e acerta a posição
  da imagem correspondente (<img data-tx="...">).
- recorte da foto do slide 6 (2x, no tamanho da moldura).

Uso: python3 instagram/posts/nr01-afastamentos/gerar.py
"""
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.dont_write_bytecode = True
sys.path.insert(0, str(RAIZ / 'instagram' / 'ferramentas'))
import textura  # noqa: E402

FOTOS = AQUI / 'fotos'
TIFFANY = (159, 197, 189)
CINZA = (196, 200, 194)
VERDE = (47, 107, 100)


def fundo(cor, nome, brilho=None, seed=1):
    """Fundo 2x com granulado leve e, se pedido, um brilho suave (x, y, raio, cor)."""
    rng = np.random.default_rng(seed)
    W, H = 2160, 2700
    img = np.ones((H, W, 3)) * np.array(cor, float)
    if brilho:
        bx, by, r, bcor = brilho
        yy, xx = np.mgrid[0:H, 0:W]
        d = np.sqrt((xx - bx * 2) ** 2 + (yy - by * 2) ** 2) / (r * 2)
        a = np.clip(1 - d, 0, 1) ** 2 * 0.55
        img = img * (1 - a[..., None]) + np.array(bcor, float) * a[..., None]
    img += rng.normal(0, 4.5, (H, W, 1))
    Image.fromarray(np.clip(img, 0, 255).astype('uint8')).save(FOTOS / nome, quality=90)


def fita(nome):
    """Fita adesiva bege, translúcida, com listras finas e pontas serrilhadas, levemente girada."""
    w, h = 240, 56
    W, H = w * 2, h * 2
    rng = np.random.default_rng(7)
    listras = (np.arange(W) // 6 % 2)[None, :] * 10
    base = np.ones((H, W, 3)) * np.array((236, 228, 202), float) - listras[..., None]
    a = np.full((H, W), 0.88)
    xx = np.arange(W)[None, :]
    serra_e = (np.abs(rng.normal(0, 1, H)) * 5).astype(int)[:, None]
    serra_d = (np.abs(rng.normal(0, 1, H)) * 5).astype(int)[:, None]
    a[(xx < serra_e) | (xx > W - 1 - serra_d)] = 0
    im = Image.fromarray(np.dstack([base, a * 255]).astype('uint8'), 'RGBA')
    tela = Image.new('RGBA', (480, 132), (0, 0, 0, 0))
    tela.paste(im, (0, 10), im)
    tela = tela.rotate(-2.2, resample=Image.BICUBIC, expand=False)
    tela.save(FOTOS / nome)


def medir():
    saida = subprocess.run(['node', str(RAIZ / 'instagram/ferramentas/medir-marcas.mjs'), str(AQUI / 'slides.html')],
                           check=True, capture_output=True, text=True).stdout
    return json.loads(saida)


def marcas():
    html_p = AQUI / 'slides.html'
    html = html_p.read_text(encoding='utf-8')
    for i, m in enumerate(medir()):
        x, y, w, h = m['x'] - 4, m['y'] + 3, m['w'] + 8, m['h'] - 4
        textura.marca(w, h, TIFFANY, seed=11 + i).save(FOTOS / f"tx-mk-{m['id']}.png")
        estilo = f'left:{x:.0f}px;top:{y:.0f}px;width:{w:.0f}px;height:{h:.0f}px'
        html = re.sub(rf'(<img [^>]*data-tx="{m["id"]}"[^>]*style=")[^"]*(")', rf'\g<1>{estilo}\g<2>', html)
        print('marca-texto', m['id'], estilo)
    html_p.write_text(html, encoding='utf-8')


def recorte_foto(orig, nome, w, h, fx, fy):
    im = Image.open(FOTOS / orig).convert('RGB')
    escala = max(2 * w / im.width, 2 * h / im.height)
    im = im.resize((round(im.width * escala), round(im.height * escala)), Image.LANCZOS)
    x = min(max(round(im.width * fx - w), 0), im.width - 2 * w)
    y = min(max(round(im.height * fy - h), 0), im.height - 2 * h)
    im.crop((x, y, x + 2 * w, y + 2 * h)).save(FOTOS / nome, quality=88)


def print_nr01():
    """Recorta do PDF oficial da NR-01 (MTE) o quadro de vigência (pág. 4) e o item 1.5.3.1.4 (pág. 5), com o
    trecho dos riscos psicossociais no marca-texto (aplicado como multiplicação, como caneta sobre o papel)."""
    pdf = FOTOS / 'nr-01-atualizada-2025.pdf'
    dpi = 300
    k = dpi / 72  # pontos do PDF -> pixels
    tmp = FOTOS / '_pg'
    subprocess.run(['pdftoppm', '-f', '4', '-l', '5', '-r', str(dpi), '-png', str(pdf), str(tmp)], check=True)
    p4 = Image.open(f'{tmp}-04.png').convert('RGB')
    p5 = Image.open(f'{tmp}-05.png').convert('RGB')
    # quadro "Redação dada pela Portaria MTE nº 1.419 ... Entra em vigor em 26 de maio de 2026 ... 1.5 Gerenciamento"
    a = p4.crop((int(64 * k), int(559 * k), int(528 * k), int(604 * k)))
    # item 1.5.3.1.4 e item 1.5.3.2 até a alínea f (o que a organização deve fazer)
    b = p5.crop((int(66 * k), int(262 * k), int(524 * k), int(489 * k)))
    # marca-texto em "incluindo os fatores de risco psicossociais relacionados ao trabalho." (linha y 294–306 pt)
    x0, x1, y0, y1 = (137.0 - 66) * k, (466.5 - 66) * k, (293.0 - 262) * k, (307.5 - 262) * k
    mk = textura.marca((x1 - x0) / 2, (y1 - y0) / 2, TIFFANY, seed=31, alfa=.95).resize((int(x1 - x0), int(y1 - y0)))
    camada = Image.new('RGB', b.size, (255, 255, 255))
    camada.paste(mk, (int(x0), int(y0)), mk)
    from PIL import ImageChops
    b = ImageChops.multiply(b, camada)
    a.save(FOTOS / 'nr01-p4.png')
    b.save(FOTOS / 'nr01-p5.png')
    for f in FOTOS.glob('_pg-*.png'):
        f.unlink()
    print('print da NR-01', a.size, b.size)


if __name__ == '__main__':
    fundo((159, 197, 189), 'fundo-tiffany.jpg', brilho=(860, 180, 900, (191, 224, 217)))
    fundo((47, 107, 100), 'fundo-verde.jpg', brilho=(900, 160, 1000, (64, 128, 119)), seed=2)
    textura.marca(300, 484, CINZA, seed=3, alfa=.9, sentido='v').save(FOTOS / 'tx-barra-cinza.png')
    textura.marca(300, 560, TIFFANY, seed=4, alfa=.95, sentido='v').save(FOTOS / 'tx-barra-tiffany.png')
    fita('fita.png')
    recorte_foto('conversa1.jpg', 'n-05.jpg', 1080, 420, 0.50, 0.50)
    print_nr01()
    subprocess.run(['node', str(RAIZ / 'instagram/ferramentas/render-transparente.mjs'), str(AQUI / 'recorte.html'),
                    str(FOTOS)], check=True)
    (FOTOS / 'recorte-nr01-afastamentos.png').unlink(missing_ok=True)
    marcas()
    # a alternativa do slide 3 (recorte digitado) usa as mesmas imagens; não tem marca-texto medido
    print('ok')
