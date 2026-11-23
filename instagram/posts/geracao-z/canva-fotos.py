"""Prepara o carrossel da Geração Z para o Canva: cada vaga de foto vira uma imagem do mesmo tamanho (um quadro liso,
para trocar pela foto no Canva), os degradês viram camadas PNG por cima, e tudo é achatado em posição absoluta
(instagram/ferramentas/achatar.mjs) antes de gerar o canva.html autocontido.
As fotos escolhidas (Pinterest) não entram aqui: o repositório é público e os direitos ainda não estão confirmados.
Elas vão direto para o Canva por upload e entram no lugar dos quadros.
Uso: python3 instagram/posts/geracao-z/canva-fotos.py"""
import json, subprocess
from pathlib import Path
from PIL import Image
AQUI = Path(__file__).parent
RAIZ = AQUI.parent.parent.parent
LEVE = AQUI / 'fotos-canva'
LEVE.mkdir(exist_ok=True)

# quadros lisos no tamanho de cada vaga (a foto entra no lugar deles, no Canva)
VAGAS = {'gz-01': (1080, 1350), 'gz-02': (936, 420), 'gz-03': (340, 520), 'gz-04': (1080, 1350)}
for k, (w, h) in VAGAS.items():
    Image.new('RGB', (w // 4, h // 4), (42, 53, 51)).save(LEVE / f'vaga-{k}.png', optimize=True)

def degrade(w, h, paradas, cor, nome):
    """paradas: [(posição 0 a 1, opacidade)], interpolação linear, como o linear-gradient do CSS"""
    im = Image.new('RGBA', (w, h))
    px = im.load()
    for y in range(h):
        t = y / (h - 1)
        a = paradas[0][1] if t <= paradas[0][0] else paradas[-1][1]
        for (t0, a0), (t1, a1) in zip(paradas, paradas[1:]):
            if t0 <= t <= t1:
                a = a0 + (a1 - a0) * (t - t0) / (t1 - t0)
        for x in range(w):
            px[x, y] = (*cor, round(a * 255))
    im.save(LEVE / nome, optimize=True)

# .gz.foto::before: linear-gradient(rgba(10,16,15,.15) 30%, rgba(10,16,15,.9) 78%)
degrade(216, 270, [(0, .15), (.30, .15), (.78, .9), (1, .9)], (10, 16, 15), 'degrade-foto.png')
# a sombra no alto da foto do Escritório (slide 6): rgba(10,16,15,.55) -> transparente, 150 px
degrade(216, 30, [(0, .55), (1, 0)], (10, 16, 15), 'sombra-topo.png')

vagas = {
    'gz-01': [{'sel': 'section', 'src': 'fotos-canva/vaga-gz-01.png', 'alt': 'FOTO capa', 'sobre': 'fotos-canva/degrade-foto.png'}],
    'gz-02': [{'sel': '.bloco.vaga', 'src': 'fotos-canva/vaga-gz-02.png', 'alt': 'FOTO grupo de jovens', 'z': 2}],
    'gz-03': [{'sel': '.bloco.vaga', 'src': 'fotos-canva/vaga-gz-03.png', 'alt': 'FOTO jovem com celular', 'z': 2}],
    'gz-04': [{'sel': 'section', 'src': 'fotos-canva/vaga-gz-04.png', 'alt': 'FOTO jovem no metrô', 'sobre': 'fotos-canva/degrade-foto.png'}],
    'gz-06': [{'sel': 'div[style*="linear-gradient"]', 'src': 'fotos-canva/sombra-topo.png', 'alt': '', 'z': 2.5}],
}
(AQUI / 'canva-vagas.json').write_text(json.dumps(vagas, ensure_ascii=False, indent=1))
# nos slides de foto, a vaga e o aviso saem (como na versão final, com a foto): a vaga muda o espaçamento do topo
import re
base = (AQUI / 'slides.html').read_text().replace('class="slide gz foto vaga"', 'class="slide gz foto"')
base = re.sub(r'\s*<span class="aviso">.*?</span>', '', base, flags=re.S)
(AQUI / '_canva-base.html').write_text(base)
subprocess.run(['node', str(RAIZ / 'instagram/ferramentas/achatar.mjs'), str(AQUI / '_canva-base.html'), str(AQUI / 'canva-src.html'),
                str(AQUI / 'canva-vagas.json')], check=True)
(AQUI / '_canva-base.html').unlink()
subprocess.run(['node', str(RAIZ / 'instagram/ferramentas/canva.mjs'), str(AQUI / 'canva-src.html'), str(AQUI / 'canva.html')], check=True)
