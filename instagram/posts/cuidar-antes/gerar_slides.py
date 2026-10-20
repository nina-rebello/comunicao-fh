# v1 da arte (19/10): post de sex 23/10, "Cuidar das pessoas não deveria começar quando algo vai mal", conteúdo v4
#   aprovado pela Nina (README.md). Para CEOs. 7 slides no design do post de gestão (gestao-pela-saude, v13):
#   Raleway, Tiffany, verde e creme, rótulo em caixa alta, destaque em negrito itálico, fio com bolinhas.
#   1 capa (Tiffany): o fio do "antes" e do "depois";
#   2 (verde): a estratégia e as pessoas;
#   3 (creme): além da saúde, com o fio de quatro pontos;
#   4 (Tiffany): acolher x prevenir em dois cartões do mesmo tamanho;
#   5 (verde): um não funciona sem o outro, com dois círculos iguais;
#   6 (creme): alguém para ouvir, com foto (conversa1.jpg, recortada e com 75% de saturação em foto-conversa.jpg);
#   7 (Tiffany): final com o logo.
#   Ícones: Lucide (licença ISC), em traço.
# Uso: python3 gerar_slides.py slides.html && node ../../ferramentas/render.mjs slides.html png
import sys

SAIDA = sys.argv[1]
N = 7

CSS = r'''
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:400;font-style:italic;src:url(../../marca/fontes/raleway-latin-400-italic.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--tif:#96C5BD;--verde:#1F3A36;--creme:#F0F0E9;--tclaro:#BFE0D9;--vlogo:#2F6B64}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#888;display:flex;flex-wrap:wrap;gap:40px;padding:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-variant-numeric:lining-nums}
.slide>*{position:absolute}
.t{background:var(--tif);color:var(--verde)}
.v{background:var(--verde);color:var(--creme)}
.c{background:var(--creme);color:var(--verde)}
.k{font-weight:800;font-style:italic}
.v .k{color:var(--tif)}
.c .k{color:var(--vlogo)}
.rot{left:96px;top:96px;font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase}
.v .rot{color:var(--tif)} .c .rot{color:var(--vlogo)}
.tit{font-size:70px;line-height:80px;letter-spacing:-0.01em}
.corpo{font-size:36px;line-height:48px}
.nota{font-size:28px;line-height:38px}
.handle{left:96px;top:1238px;font-size:24px;line-height:32px}
.v .handle{color:var(--tclaro)}
.arr{right:96px;top:1238px;font-size:24px;line-height:32px}
.pag{right:96px;top:1248px;display:flex;gap:8px}
.pag i{display:block;width:20px;height:12px;border-radius:6px}
.pag i.on{width:48px}
.t .pag i{background:var(--creme)} .t .pag i.on{background:var(--verde)}
.v .pag i{background:rgba(191,224,217,.3)} .v .pag i.on{background:var(--tif)}
.c .pag i{background:var(--tif)} .c .pag i.on{background:var(--verde)}
svg.cheia{left:0;top:0;width:1080px;height:1350px}
.vert{font-size:21px;line-height:28px;letter-spacing:.18em;text-transform:uppercase;text-align:center}
.passo{left:210px;width:774px}
.passo p{font-size:40px;line-height:48px;font-weight:800}
.arg{left:96px;width:888px;border-top:3px solid var(--tif);padding-top:26px}
.arg b{display:block;font-size:40px;line-height:48px;font-weight:800;color:var(--creme);margin-bottom:8px}
.arg span{display:block;font-size:34px;line-height:44px;color:var(--tclaro)}
'''

ICONES = {
    # message-circle (conversa) e shield-check (escudo), Lucide
    'conversa': ['M7.9 20A9 9 0 1 0 4 16.1L2 22Z'],
    'escudo': ['M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z',
               'm9 12 2 2 4-4'],
}


def pag(i):
    return '<div class="pag">' + ''.join('<i class="on"></i>' if j == i else '<i></i>' for j in range(1, N + 1)) + '</div>'


S = []

# 1 · capa (v2, 20/10): ilustração chapada, no estilo dos pôsteres de design universal que a Nina mandou: cor única
#   de fundo, título em negrito no topo, figura grande sem contorno embaixo. A planta murchando na mesa é o "quando algo
#   vai mal"; o regador parado ao lado é o cuidado que podia ter vindo antes.
S.append(('c01', 't', 'capa: cuidar das pessoas antes, não depois (ilustrada)', '''<p class="rot">Para quem lidera</p>
  <p class="tit" style="left:96px;top:160px;width:888px;font-size:78px;line-height:86px;font-weight:800;letter-spacing:-0.02em">Cuidar das pessoas não deveria começar <span class="k" style="color:var(--creme)">quando algo vai mal</span>.</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <circle cx="820" cy="700" r="150" fill="#BFE0D9"/>
    <rect x="0" y="1060" width="1080" height="290" fill="#2F6B64"/>
    <rect x="0" y="1036" width="1080" height="34" fill="#1F3A36"/>
    <path d="M395 1036L375 870H595L575 1036Z" fill="#F0F0E9"/>
    <rect x="360" y="840" width="250" height="48" rx="6" fill="#E2E2D6"/>
    <path d="M485 842C485 760 470 690 500 640C535 585 620 600 650 660C670 700 668 750 650 790" fill="none" stroke="#1F3A36" stroke-width="14" stroke-linecap="round"/>
    <path d="M488 760C440 770 405 800 395 840C440 832 478 806 488 760Z" fill="#1F3A36"/>
    <path d="M492 700C450 690 410 710 390 745C432 752 470 735 492 700Z" fill="#1F3A36"/>
    <path d="M560 615C590 570 640 565 670 590C640 620 600 630 560 615Z" fill="#1F3A36"/>
    <path d="M640 680C690 680 715 715 712 760C675 748 650 720 640 680Z" fill="#1F3A36"/>
    <path d="M650 790C690 805 705 845 694 880C665 862 650 830 650 790Z" fill="#1F3A36"/>
    <path d="M650 985C680 960 718 968 730 995C695 1010 665 1006 650 985Z" fill="#2F6B64"/>
    <path d="M790 1036V940C790 925 800 915 815 915H905C920 915 930 925 930 940V1036Z" fill="#F0F0E9"/>
    <path d="M905 935C960 935 965 1000 930 1010" fill="none" stroke="#F0F0E9" stroke-width="16"/>
    <path d="M795 965L745 925" stroke="#F0F0E9" stroke-width="18" stroke-linecap="round"/>
    <rect x="722" y="903" width="40" height="26" rx="6" transform="rotate(38 742 916)" fill="#E2E2D6"/>
    <rect x="830" y="898" width="60" height="20" rx="8" fill="#E2E2D6"/>
  </svg>
  <style>#c01 .handle,#c01 .arr{color:var(--creme)}</style>'''))

# 2 · antes, não depois: a estratégia e as pessoas
S.append(('c02', 'v', 'você não espera o problema para cuidar da estratégia', '''<p class="rot">Antes, não depois</p>
  <p class="tit" style="left:96px;top:170px;width:888px">Você não espera o problema aparecer para cuidar da estratégia.</p>
  <div style="left:96px;top:640px;width:120px;height:4px;background:var(--tif);border-radius:2px"></div>
  <p class="k" style="left:96px;top:700px;width:888px;font-size:84px;line-height:94px;letter-spacing:-0.01em;color:var(--tif)">Por que esperar para cuidar das pessoas?</p>'''))

# 3 · além da saúde: o fio de quatro pontos (o último é a pergunta da marca)
ITENS = ['a rotina', 'a pressão', 'o que pesa', 'o que é importante para ela']
Y0, PASSO = 620, 140
fio = '<path d="M136 %dV%d" stroke="#96C5BD" stroke-width="10" stroke-linecap="round"/>' % (Y0, Y0 + PASSO * 3)
fio += ''.join('<circle cx="136" cy="%d" r="26" fill="%s"/>' % (Y0 + i * PASSO, '#2F6B64' if i == 3 else '#96C5BD') for i in range(4))
passos = ''.join('<div class="passo" style="top:%dpx"><p%s>%s</p></div>\n  ' % (Y0 - 24 + i * PASSO, ' class="k" style="color:var(--vlogo)"' if i == 3 else '', t)
                 for i, t in enumerate(ITENS))
S.append(('c03', 'c', 'cuidar antes não é só cuidar da saúde', '''<p class="rot">Além da saúde</p>
  <p class="tit" style="left:96px;top:170px;width:888px">Cuidar antes não é <span class="k">só cuidar da saúde</span>.</p>
  <p class="corpo" style="left:96px;top:470px;width:888px">É saber como cada pessoa está:</p>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">''' + fio + '''</svg>
  ''' + passos))

# 4 · a diferença: dois cartões do mesmo tamanho
CARTOES = [('conversa', 'Acolher', 'é ouvir.', 'Olha para como a pessoa está hoje.', 'Cria um espaço seguro para falar.', False),
           ('escudo', 'Prevenir', 'é agir antes.', 'Olha para o que vem pela frente.', 'Vira um plano de cuidado, com acompanhamento.', True)]
TOPO, LARG, ALT = 470, 432, 650
cart = ''
for i, (ic, nome, verbo, a, b, escuro) in enumerate(CARTOES):
    x = 96 + i * (LARG + 24)
    fundo, cor_nome, cor_verbo, cor_txt, cor_ic, fundo_ic, cor_linha = (
        ('var(--verde)', 'var(--creme)', 'var(--tif)', 'var(--tclaro)', '#96C5BD', 'rgba(150,197,189,.18)', 'var(--tif)') if escuro else
        ('#fff', 'var(--vlogo)', 'var(--verde)', 'var(--verde)', '#2F6B64', '#E3F0EC', 'var(--tif)'))
    cart += ('<div style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:%s;border-radius:28px"></div>\n  '
             '<div style="left:%dpx;top:%dpx;width:84px;height:84px;background:%s;border-radius:22px"></div>\n  '
             '<svg aria-hidden="true" style="left:%dpx;top:%dpx;width:44px;height:44px" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</svg>\n  '
             '<p style="left:%dpx;top:%dpx;width:352px;font-size:52px;line-height:60px;font-weight:800;color:%s">%s</p>\n  '
             '<p class="k" style="left:%dpx;top:%dpx;width:352px;font-size:38px;line-height:46px;color:%s">%s</p>\n  '
             '<div style="left:%dpx;top:%dpx;width:64px;height:3px;background:%s"></div>\n  '
             '<p style="left:%dpx;top:%dpx;width:352px;font-size:30px;line-height:40px;color:%s">%s</p>\n  '
             '<p style="left:%dpx;top:%dpx;width:352px;font-size:30px;line-height:40px;color:%s">%s</p>\n  '
             % (x, TOPO, LARG, ALT, fundo,
                x + 40, TOPO + 44, fundo_ic,
                x + 60, TOPO + 64, cor_ic, ''.join('<path d="%s"/>' % d for d in ICONES[ic]),
                x + 40, TOPO + 168, cor_nome, nome,
                x + 40, TOPO + 232, cor_verbo, verbo,
                x + 40, TOPO + 316, cor_linha,
                x + 40, TOPO + 350, cor_txt, a,
                x + 40, TOPO + 490, cor_txt, b))
S.append(('c04', 't', 'acolher x prevenir: a diferença, em dois cartões iguais', '''<p class="rot">A diferença</p>
  <p class="tit" style="left:96px;top:170px;width:888px">Acolher e prevenir <span class="k">não são a mesma coisa</span>.</p>
  ''' + cart))

# 5 · o mesmo peso: os dois argumentos e dois círculos iguais que se cruzam
S.append(('c05', 'v', 'um não funciona sem o outro', '''<p class="rot">O mesmo peso</p>
  <p class="tit" style="left:96px;top:170px;width:888px">E um não funciona <span class="k">sem o outro</span>.</p>
  <div class="arg" style="top:420px"><b>Prevenção sem acolhimento</b><span>vira campanha que ninguém usa.</span></div>
  <div class="arg" style="top:640px"><b>Acolhimento sem prevenção</b><span>vira conversa que não muda a rotina.</span></div>
  <svg class="cheia" viewBox="0 0 1080 1350" aria-hidden="true">
    <circle cx="450" cy="1010" r="130" fill="none" stroke="#96C5BD" stroke-width="3"/>
    <circle cx="630" cy="1010" r="130" fill="none" stroke="#96C5BD" stroke-width="3"/>
  </svg>
  <p class="vert" style="left:320px;top:996px;width:180px;font-size:19px;font-weight:800;color:var(--creme)">Acolher</p>
  <p class="vert" style="left:580px;top:996px;width:180px;font-size:19px;font-weight:800;color:var(--creme)">Prevenir</p>'''))

# 6 · alguém para ouvir: foto, o argumento para o CEO e três etiquetas
TAGS = [('perto', 150), ('dentro da empresa', 320), ('com sigilo', 210)]
tags, x = '', 96
for t, w in TAGS:
    tags += ('<div style="left:%dpx;top:1120px;width:%dpx;height:60px;background:var(--tif);border-radius:30px"></div>\n  '
             '<p style="left:%dpx;top:1131px;width:%dpx;font-size:26px;line-height:38px;font-weight:800;text-align:center">%s</p>\n  ' % (x, w, x, w, t))
    x += w + 16
S.append(('c06', 'c', 'seu time precisa de alguém para ouvir', '''<p class="rot">Alguém para ouvir</p>
  <p class="tit" style="left:96px;top:170px;width:888px">Seu time precisa de <span class="k">alguém para ouvir</span>.</p>
  <img src="foto-conversa.jpg" alt="" style="left:96px;top:440px;width:888px;height:400px;border-radius:28px">
  <p class="corpo" style="left:96px;top:890px;width:888px">Você não consegue ouvir todo mundo. Mas pode decidir que <b style="font-weight:800">todos tenham com quem falar</b>:</p>
  ''' + tags))

# 7 · final: logo, a decisão de quem lidera, o valor da marca e a chamada
S.append(('c07', 't', 'final: cuidar antes é uma decisão de quem lidera', '''<img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:410px;top:230px;width:260px;height:260px">
  <p class="tit" style="left:96px;top:580px;width:888px;text-align:center">Cuidar antes é uma decisão <span class="k">de quem lidera</span>.</p>
  <p class="nota k" style="left:146px;top:860px;width:788px;text-align:center;color:var(--vlogo)">Fazemos o certo pelos motivos certos.</p>
  <p class="nota" style="left:146px;top:930px;width:788px;text-align:center">Conheça o Escritório do Cuidado no link da bio.</p>'''))


def html(slides, titulo):
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>' + titulo + '</title><style>' + CSS + '</style></head><body>\n']
    for k, (sid, cls, nota, corpo) in enumerate(slides, 1):
        if k == 1:
            fim = '\n  <p class="handle">@fairhealth.br</p>\n  <p class="arr">Arraste para o lado →</p>'
        else:
            fim = '\n  <p class="handle">@fairhealth.br</p>\n  ' + pag(k)
        out.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  %s%s\n</section>\n\n' % (k, nota, cls, sid, corpo, fim))
    out.append('</body></html>\n')
    return ''.join(out)


open(SAIDA, 'w').write(html(S, 'Cuidar das pessoas não deveria começar quando algo vai mal'))
print('ok', len(S))
