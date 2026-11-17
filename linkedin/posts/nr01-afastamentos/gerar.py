"""Versão LinkedIn (1080 x 1080) do carrossel de 18/11 (NR-01 e afastamentos). Reaproveita as artes do Instagram
(instagram/posts/nr01-afastamentos/fotos): corta os fundos para o quadrado, corta a foto do slide 5, monta
slides.html (tudo em posição fixa, para o Canva) e mede os marca-textos.
Uso: python3 linkedin/posts/nr01-afastamentos/gerar.py"""
import json, re, shutil, subprocess, sys
from pathlib import Path
from PIL import Image, ImageFilter
AQUI = Path(__file__).parent
RAIZ = AQUI.parent.parent.parent
ORIG = RAIZ / 'instagram/posts/nr01-afastamentos/fotos'
FOTOS = AQUI / 'fotos'
FOTOS.mkdir(exist_ok=True)
sys.path.insert(0, str(RAIZ / 'instagram/ferramentas'))
import textura  # noqa: E402
TIFFANY = (159, 197, 189)

# fundos: o quadrado de cima da arte 4:5
for n in ['fundo-capa', 'fundo-papel', 'fundo-verde', 'fundo-tiffany', 'fundo-fim']:
    Image.open(ORIG / f'{n}.jpg').convert('RGB').crop((0, 0, 2160, 2160)).save(FOTOS / f'{n}.jpg', quality=90)
for n in ['tx-barra-cinza.png', 'tx-barra-tiffany.png', 'print-nr01.png']:
    shutil.copy(ORIG / n, FOTOS / n)
# foto do slide 5 (1080 x 300): do caderno ao smartwatch
im = Image.open(ORIG / 'escuta.jpg').convert('RGB')
esc = 2160 / im.width
im = im.resize((2160, round(im.height * esc)), Image.LANCZOS)
y = round(110 * esc)
im.crop((0, y, 2160, y + 600)).filter(ImageFilter.UnsharpMask(2, 60, 3)).save(FOTOS / 'n-05.jpg', quality=90)

L = [
 'Assédio de qualquer natureza no trabalho', 'Má gestão de mudanças organizacionais', 'Baixa clareza de papel/função',
 'Baixas recompensas e reconhecimento', 'Falta de suporte/apoio no trabalho', 'Baixo controle no trabalho/falta de autonomia',
 'Baixa justiça organizacional', 'Eventos violentos ou traumáticos', 'Baixa demanda no trabalho (subcarga)',
 'Excesso de demandas no trabalho (sobrecarga)', 'Maus relacionamentos no local de trabalho',
 'Trabalho em condições de difícil comunicação', 'Trabalho remoto e isolado']
lista = ''
for i, t in enumerate(L):
    top = 392 + 41 * i
    lista += f'  <p class="li-n" style="left:112px;top:{top + 8}px">{i + 1:02d}</p><p class="li-t" style="left:170px;top:{top}px">{t}</p>\n'
    if i < len(L) - 1:
        lista += f'  <div class="li-fio" style="left:112px;width:856px;top:{top + 37}px"></div>\n'

HTML = '''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>LinkedIn: Recorde de afastamentos por saúde mental e a NR-01</title>
<link rel="stylesheet" href="../../../instagram/marca/base.css">
<link rel="stylesheet" href="estilo.css">
<!-- Versão LinkedIn (1080 x 1080, quadrada como o post #1) do carrossel de 18/11 do Instagram: mesmos 6 slides e o
     mesmo texto, em outro quadro. Muda só o que é do canal: o nome da marca no lugar do @ do Instagram e o convite
     do último slide, que vai para o link no primeiro comentário (não existe "link da bio" no LinkedIn). -->
<style media="canva">
body{background:none;margin:0}
.slide{margin:0}
</style></head><body>

<section class="slide ed q" id="n-01">
  <img src="fotos/fundo-capa.jpg" class="fundo" alt="">
  <div class="topo"><span>fairhealth</span><span></span></div>
  <p class="rotulo" style="left:72px;top:150px">Saúde mental no trabalho</p>
  <p class="tit" style="left:58px;top:206px;font-size:270px;letter-spacing:-14px;line-height:1;color:var(--escuro)">546,2</p>
  <p class="tit" style="left:712px;top:360px;font-size:104px;letter-spacing:-4px;line-height:1;color:var(--escuro)">mil</p>
  <p class="tit" style="left:72px;top:504px;font-size:70px">afastamentos do trabalho</p>
  <img src="fotos/tx-mk-n01-a.png" class="tx" data-tx="n01-a" alt="" style="left:58px;top:581px;width:602px;height:78px">
  <p class="mk" data-mk="n01-a" style="left:62px;top:582px;font-size:70px"><span>&nbsp;por saúde mental&nbsp;</span></p>
  <p class="txt" style="left:72px;top:692px;font-size:38px">no Brasil em 2025, concedidos pelo INSS.</p>
  <p class="fonte-n" style="left:72px;top:770px">Fonte: Ministério da Previdência Social</p>
  <div class="mao" style="left:70px;top:800px"><svg width="440" height="12" viewBox="0 0 440 12"><path d="M2 6 C 110 2, 240 10, 438 5" fill="none" stroke="#141B1B" stroke-width="2" stroke-linecap="round"/></svg></div>
  <div class="balao" style="right:72px;top:868px;width:470px;height:132px"></div>
  <p class="balao-t" style="right:72px;top:907px;width:470px">E agora, RH?</p>
  <p class="arraste" style="left:72px;top:1010px">Deslize para o lado →</p>
</section>

<section class="slide ed q" id="n-02">
  <img src="fotos/fundo-papel.jpg" class="fundo" alt="">
  <div class="topo"><span>fairhealth</span><span></span></div>
  <p class="rotulo" style="left:72px;top:120px">O dado</p>
  <p class="tit" style="left:70px;top:164px;font-size:64px;color:var(--tinta)">546,2 mil licenças por</p>
  <p class="tit" style="left:70px;top:234px;font-size:64px;color:var(--tinta)">transtornos mentais em 2025,</p>
  <img src="fotos/tx-mk-n02-a.png" class="tx" data-tx="n02-a" alt="" style="left:60px;top:308px;width:833px;height:71px">
  <p class="mk" data-mk="n02-a" style="left:64px;top:308px;font-size:64px;letter-spacing:-2.5px"><span>&nbsp;o segundo recorde seguido.&nbsp;</span></p>

  <img src="fotos/tx-barra-cinza.png" class="abs" alt="" style="left:112px;top:540px;width:300px;height:380px">
  <p class="b-val" style="left:138px;top:564px">472,3 mil</p>
  <p class="b-uni" style="left:140px;top:628px">licenças</p>
  <img src="fotos/tx-barra-tiffany.png" class="abs" alt="" style="left:492px;top:480px;width:300px;height:440px">
  <p class="b-val" style="left:518px;top:504px">546,2 mil</p>
  <p class="b-uni" style="left:520px;top:568px">licenças</p>
  <div class="abs" style="left:72px;top:919px;width:936px;height:2px;background:var(--tinta)"></div>
  <p class="b-ano" style="left:112px;top:938px;width:300px;opacity:.6">2024</p>
  <p class="b-ano" style="left:492px;top:938px;width:300px">2025</p>
  <div class="mao" style="left:582px;top:978px"><svg width="120" height="12" viewBox="0 0 120 12"><path d="M2 7 C 30 3, 70 10, 118 5" fill="none" stroke="#141B1B" stroke-width="2.2" stroke-linecap="round"/></svg></div>
  <div class="mao" style="left:250px;top:405px"><svg width="300" height="120" viewBox="0 0 300 180" preserveAspectRatio="none"><path d="M12 172 C 30 60, 150 26, 290 40" fill="none" stroke="#141B1B" stroke-width="2.6" stroke-linecap="round"/><path d="M272 24 L292 40 L270 54" fill="none" stroke="#141B1B" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
  <div class="mao" style="left:806px;top:400px"><svg width="230" height="104" viewBox="0 0 230 104"><path d="M40 60 C 22 22, 120 4, 186 12 C 236 20, 232 80, 156 90 C 86 98, 16 92, 12 58 C 10 38, 30 24, 58 20" fill="none" stroke="#141B1B" stroke-width="2.6" stroke-linecap="round"/></svg></div>
  <p class="abs" style="left:818px;top:426px;width:200px;text-align:center;font-family:'Instrument Serif',serif;font-style:italic;font-size:48px;line-height:1;color:var(--tinta)">+15,7%</p>
  <p class="fonte" style="left:72px;right:72px;top:1006px;font-size:17px">Fonte: Ministério da Previdência Social (nota oficial, jan/2026). Benefícios por incapacidade temporária concedidos pelo INSS por transtornos mentais e comportamentais: 472.328 em 2024 e 546.254 em 2025.</p>
</section>

<section class="slide ed q verde" id="n-03">
  <img src="fotos/fundo-verde.jpg" class="fundo" alt="">
  <div class="topo"><span>fairhealth</span><span></span></div>
  <p class="rotulo" style="left:72px;top:112px">A norma</p>
  <p class="tit" style="left:60px;top:148px;font-size:170px;letter-spacing:-8px;line-height:1;color:var(--menta)">NR-01</p>
  <p class="txt" style="left:72px;width:936px;top:326px;font-size:36px;line-height:1.3;color:#fff">Desde maio de 2026, a <span style="white-space:nowrap">NR-01</span> pede que a empresa <b>identifique e gerencie os riscos psicossociais</b>, junto com os outros riscos ocupacionais.</p>
  <img src="fotos/print-nr01.png" class="abs" alt="Trechos do texto oficial da NR-01: vigência em 26 de maio de 2026 e item 1.5.3.1.4" style="left:110px;top:478px;width:860px;height:516px">
  <p class="fonte" style="left:72px;right:72px;top:1016px;font-size:17px;color:#fff;opacity:.7">Fonte: NR-01 (texto atualizado publicado pelo Ministério do Trabalho e Emprego), item 1.5.3.1.4, na redação da Portaria MTE nº 1.419/2024. Em vigor desde 26/05/2026 (Portaria MTE nº 765/2025).</p>
</section>

<section class="slide ed q" id="n-04">
  <img src="fotos/fundo-tiffany.jpg" class="fundo" alt="">
  <div class="topo"><span>fairhealth</span><span></span></div>
  <p class="tit" style="left:72px;top:100px;font-size:70px;letter-spacing:-3px">O que é</p>
  <p class="serif" style="left:68px;top:176px;font-size:104px">risco psicossocial</p>
  <p class="txt" style="left:72px;top:304px;font-size:28px;font-weight:600;color:var(--texto)">Exemplos da lista do Ministério do Trabalho e Emprego:</p>
  <div class="folha" style="left:72px;top:356px;width:936px;height:598px"></div>
@LISTA@  <p class="fonte" style="left:72px;right:72px;top:974px;font-size:17px;opacity:.75">Fonte: Guia de informações sobre os fatores de riscos psicossociais relacionados ao trabalho, Ministério do Trabalho e Emprego (2025). A lista do guia é exemplificativa.</p>
</section>

<section class="slide ed q" id="n-05">
  <img src="fotos/fundo-papel.jpg" class="fundo" alt="">
  <img src="fotos/n-05.jpg" class="abs" alt="" style="left:0;top:0;width:1080px;height:300px">
  <div class="abs" style="left:52px;top:42px;width:252px;height:54px;background:#2F6B64;border-radius:10px"></div>
  <div class="topo claro"><span>fairhealth</span><span></span></div>
  <p class="tit" style="left:72px;top:326px;font-size:70px;letter-spacing:-3px">Medir e cuidar:</p>
  <p class="serif" style="left:68px;top:402px;font-size:92px">a norma pede os dois.</p>

  <div class="card-m" style="left:72px;top:524px;width:440px;height:470px"></div>
  <p class="k-rot" style="left:108px;top:560px">Medir</p>
  <p class="k-item" style="left:108px;top:616px;width:368px"><b>b)</b> Identificar os perigos</p>
  <p class="k-item" style="left:108px;top:666px;width:368px"><b>c)</b> Avaliar os riscos</p>
  <p class="k-item" style="left:108px;top:716px;width:368px"><b>d)</b> Classificar os riscos</p>
  <div class="k-fio" style="left:108px;width:368px;top:794px"></div>
  <p class="k-rodape" style="left:108px;top:818px;width:368px">Com a <b>fairdata</b>: o diagnóstico dos riscos do grupo.</p>

  <div class="card-c" style="left:568px;top:524px;width:440px;height:470px"></div>
  <p class="k-rot claro" style="left:604px;top:560px">Cuidar</p>
  <p class="k-item claro" style="left:604px;top:616px;width:368px"><b>e)</b> Implementar medidas de prevenção</p>
  <p class="k-item claro" style="left:604px;top:704px;width:368px"><b>f)</b> Acompanhar o controle dos riscos</p>
  <div class="k-fio claro" style="left:604px;width:368px;top:794px"></div>
  <p class="k-rodape claro" style="left:604px;top:810px;width:378px">Com o <b>Escritório do Cuidado</b>: escuta, bioimpedância, smartwatches e acompanhamento.</p>

  <div class="seta-c" style="left:510px;top:729px"></div><p class="seta-t" style="left:510px;top:744px">→</p>
  <p class="fonte" style="left:72px;right:72px;top:1018px">Fonte: NR-01, item 1.5.3.2, alíneas b a f (Ministério do Trabalho e Emprego).</p>
</section>

<section class="slide ed q" id="n-06">
  <img src="fotos/fundo-fim.jpg" class="fundo" alt="">
  <div class="topo"><span>fairhealth</span><span></span></div>
  <div class="balao" style="right:72px;top:120px;width:470px;height:132px"></div>
  <p class="balao-t" style="right:72px;top:159px;width:470px">E agora, RH?</p>
  <p class="tit" style="left:62px;top:270px;font-size:100px;letter-spacing:-4.5px;color:var(--escuro)">Fale com a gente</p>
  <img src="fotos/tx-mk-n06-a.png" class="tx" data-tx="n06-a" alt="" style="left:48px;top:380px;width:736px;height:113px">
  <p class="mk" data-mk="n06-a" style="left:52px;top:382px;font-size:100px;letter-spacing:-4.5px"><span>&nbsp;pelo link abaixo.&nbsp;</span></p>
  <p class="tit" style="left:72px;top:530px;font-size:48px;letter-spacing:-1.5px;font-weight:700;line-height:1.15">e leve o Escritório do Cuidado<br>para a sua empresa.</p>
  <p class="e-rot" style="left:72px;top:690px">O que a empresa recebe</p>
  <div class="e-fio" style="left:72px;width:936px;top:716px"></div>
  <div class="e-dot" style="left:72px;top:738px"></div><p class="e-t" style="left:112px;top:730px">Atendimento dentro da empresa</p>
  <p class="e-s" style="left:112px;top:766px">médicos, psicólogos e assistentes sociais</p>
  <div class="e-fio" style="left:72px;width:936px;top:796px"></div>
  <div class="e-dot" style="left:72px;top:818px"></div><p class="e-t" style="left:112px;top:810px">Medições do grupo</p>
  <p class="e-s" style="left:112px;top:846px">bioimpedância e smartwatches</p>
  <div class="e-fio" style="left:72px;width:936px;top:876px"></div>
  <div class="e-dot" style="left:72px;top:898px"></div><p class="e-t" style="left:112px;top:890px">Indicadores para o RH</p>
  <p class="e-s" style="left:112px;top:926px">do grupo, anonimizados e agregados</p>
  <div class="selo" style="left:77px;top:996px"><div class="anel"></div><img src="../../../instagram/marca/logo-circulo.png" alt=""><span>fairhealth</span></div>
</section>

</body></html>
'''
(AQUI / 'slides.html').write_text(HTML.replace('@LISTA@', lista), encoding='utf-8')

# marca-textos: mede cada linha e refaz a textura no tamanho certo
saida = subprocess.run(['node', str(RAIZ / 'instagram/ferramentas/medir-marcas.mjs'), str(AQUI / 'slides.html')],
                       check=True, capture_output=True, text=True).stdout
html = (AQUI / 'slides.html').read_text(encoding='utf-8')
for i, m in enumerate(json.loads(saida)):
    x, y, w, h = m['x'] - 4, m['y'] + 3, m['w'] + 8, m['h'] - 4
    textura.marca(w, h, TIFFANY, seed=11 + i).save(FOTOS / f"tx-mk-{m['id']}.png")
    estilo = f'left:{x:.0f}px;top:{y:.0f}px;width:{w:.0f}px;height:{h:.0f}px'
    html = re.sub(rf'(<img [^>]*data-tx="{m["id"]}"[^>]*style=")[^"]*(")', rf'\g<1>{estilo}\g<2>', html)
    print('marca-texto', m['id'], estilo)
(AQUI / 'slides.html').write_text(html, encoding='utf-8')
print('ok')
