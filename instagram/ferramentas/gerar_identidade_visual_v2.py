# Gera a v2 do brand book visual da fairhealth: foto como protagonista, tiffany como acento
# e elementos de movimento. A v1 continua em identidade-visual.html (gerar_identidade_visual.py).
# Uso: python3 instagram/ferramentas/gerar_identidade_visual_v2.py <pasta-fotos-web> <logo-circulo.png> <logo-coracao.png> <saida.html>
import base64
import os
import re
import sys

FOTOS, LC, LH, OUT = sys.argv[1:5]
b64 = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
LOGO_C = 'data:image/png;base64,' + b64(LC)
LOGO_H = 'data:image/png;base64,' + b64(LH)
USADAS = set()


def k(t):
    return f'<span class="k">{t}</span>'


def mt(t):
    """marca-texto tiffany atrás da palavra-chave"""
    return f'<span class="k mt">{t}</span>'


def A(x, y, html, w=888, cls='', style=''):
    return f'<div class="a {cls}" style="--x:{x};--y:{y};--w:{w};{style}">{html}</div>'


def PH(nome, x, y, w, h, px=50, py=50, duo=False, cls='', style=''):
    n = nome + ('-d' if duo else '')
    USADAS.add(n)
    return f'<div class="ph f-{n} {cls}" style="--x:{x};--y:{y};--w:{w};--h:{h};--px:{px}%;--py:{py}%;{style}"></div>'


def BX(x, y, w, h, cor, cls='', style=''):
    return f'<div class="bx {cls}" style="--x:{x};--y:{y};--w:{w};--h:{h};background:var(--{cor});{style}"></div>'


def GR(y, h):
    """degradê verde sob o texto em foto"""
    return f'<div class="gr" style="--y:{y};--h:{h}"></div>'


VEU = '<div class="veu"></div>'


def RESP(x, y, w, txt, r=-3, cls=''):
    return f'<div class="resp {cls}" style="--x:{x};--y:{y};--w:{w};--r:{r}deg"><p class="f-corpo">“{txt}”</p></div>'


def etq(t, x=96, y=96, cls=''):
    return A(x, y, f'<p class="f-etq">{t}</p><span class="fio-c"></span>', w=888, cls=cls)


SETA = '<svg class="seta" viewBox="0 0 48 16" aria-hidden="true"><path d="M0 8H46M38 1l8 7-8 7" fill="none" stroke="currentColor" stroke-width="2"/></svg>'


def rod(direita='arraste', cls=''):
    d = f'<span class="arr">Arraste para o lado {SETA}</span>' if direita == 'arraste' else f'<span>{direita}</span>'
    return f'<div class="rod {cls}"><span>@fairhealth.br</span>{d}</div>'


def ab(inner, cls='', label=''):
    aria = f' role="img" aria-label="{label}"' if label else ''
    return f'<div class="ab {cls}"{aria}><div class="in">{inner}</div></div>'


ICON = {
    'Alimentação': '<path d="M24 15c-6-6-16-2-14 10 2 10 8 14 14 12 6 2 12-2 14-12 2-12-8-16-14-10z"/><path d="M24 15c0-4 2-7 6-8"/>',
    'Atividade física': '<path d="M4 26h9l4-10 7 20 5-14 3 4h12"/>',
    'Sono': '<path d="M30 6a18 18 0 1 0 12 28A15 15 0 0 1 30 6z"/>',
    'Manejo do estresse': '<path d="M6 18c6-6 12 6 18 0s12 6 18 0"/><path d="M6 30c6-6 12 6 18 0s12 6 18 0"/>',
    'Relacionamentos': '<circle cx="17" cy="16" r="5"/><circle cx="31" cy="16" r="5"/><path d="M8 38c0-7 4-11 9-11s9 4 9 11"/><path d="M22 38c0-7 4-11 9-11s9 4 9 11"/>',
    'Evitar substâncias': '<circle cx="24" cy="24" r="16"/><path d="M13 13l22 22"/>',
}


def icone(nome, cls='ic'):
    return f'<svg class="{cls}" viewBox="0 0 48 48" aria-hidden="true">{ICON[nome]}</svg>'


# ---------------- as peças do Mês 1, com foto ----------------
P = {}
P[1] = ab(PH('conversa1', 0, 0, 1080, 880, 45, 40) +
          BX(0, 860, 1080, 490, 'tif') + etq('Boas-vindas', y=920) +
          A(96, 1000, f'<p class="f-titulo">Antes de qualquer exame, uma {k("conversa")}.</p>') + rod('Reel · 30 s'),
          label='Capa de reel com foto de duas pessoas conversando e faixa tiffany')
P[2] = ab(PH('sorriso1', 560, 0, 520, 1350, 50, 30) +
          etq('Como funciona o cuidado') +
          A(96, 330, f'<p class="f-display">Aqui, o cuidado começa com uma {k("pergunta")}.</p>', w=520) +
          RESP(420, 900, 560, 'Ter energia no fim do dia.', -3) + rod(),
          label='Capa de carrossel com foto de mulher sorrindo e cartão de resposta inclinado')
P[3] = ab(PH('estresse', 0, 0, 1080, 1350, 50, 40, duo=True) + GR(480, 870) +
          etq('Cuidar antes', cls='creme') +
          A(96, 820, f'<p class="f-display creme">Antes do afastamento, teve um {mt("sinal")}.</p>') + rod('Reel · 20 s', cls='on-esc'),
          label='Capa de reel com foto em duotone verde e marca-texto tiffany')
P[4] = ab(PH('industria1', 0, 0, 1080, 700, 40, 45) +
          '<div class="folha-b"></div>' + etq('Na imprensa', y=760) +
          A(96, 850, f'<p class="f-titulo">O trabalho pode adoecer. Mas não é o único {k("vilão")}.</p>') +
          A(96, 1110, '<span class="chip out">RH Pra Você · 25/09/2026</span>') + rod(),
          label='Carrossel de artigo com foto de indústria e folha creme')
P[5] = ab(PH('comida', 0, 0, 352, 640, 50, 50) + PH('tenis', 364, 0, 352, 640, 65, 50) + PH('sono', 728, 0, 352, 640, 35, 50) +
          etq('Pilares da MEV', y=700) +
          A(96, 780, f'<p class="f-titulo">Medicina do Estilo de Vida em 1 {k("minuto")}.</p>') +
          A(96, 1040, '<div class="icos">' + ''.join(icone(n) for n in ICON) + '</div>') + rod('Reel · 60 s'),
          label='Capa de reel com tiras de foto: comida, tênis e sono')
P[6] = ab('<div class="split"></div>' + etq('O que acreditamos') +
          A(96, 330, f'<p class="f-titulo">Não é {k("benefício")}.</p>', w=400) +
          A(600, 330, f'<p class="f-titulo">É infraestrutura de {k("cuidado")}.</p>', w=400, cls='creme') +
          A(96, 760, '<div class="lista"><p>Usa se lembrar</p><p>Espera o problema</p><p>É um cartão</p></div>', w=380) +
          A(600, 760, '<div class="lista on-esc"><p>Está lá todo dia</p><p>Começa antes</p><p>Gente acompanhando</p></div>', w=380) +
          '<div class="rod meia"><span>@fairhealth.br</span></div><div class="rod meia-d"><span class="arr">Arraste ' + SETA + '</span></div>',
          label='Comparativo: Não é benefício. É infraestrutura de cuidado')
barras = ''.join(f'<div class="barra"><span class="f-leg">{n}</span><span class="trilho"><span style="width:{v}%"></span></span></div>'
                 for n, v in (('Adesão', 82), ('Retornos', 68), ('Procura por sono', 44)))
P[7] = ab(PH('sorriso2', 0, 0, 1080, 760, 50, 22) +
          A(96, 520, f'<div class="card"><p class="f-nota card-head">Painel do Escritório do Cuidado · dados ilustrativos</p>{barras}</div>') +
          A(96, 1040, f'<p class="f-titulo">O que o RH {k("vê")}. E o que não vê.</p>') + rod('Reel · 30 s'),
          label='Capa de reel com foto de profissional de RH e cartão de painel sobreposto')
itens = ''.join(f'<div class="chk"><span class="box"></span><span class="f-corpo">{t}</span></div>'
                for t in ('Dormir 30 min mais cedo', 'Caminhar 10 min no almoço', 'Conversa com a psicóloga'))
P[8] = ab(BX(96, 120, 440, 640, 'verde') + PH('retrato', 64, 88, 440, 640, 50, 25) +
          A(560, 120, f'<p class="f-display">O plano é {k("seu")}.</p>', w=440) +
          A(96, 800, f'<div class="card"><p class="f-nota card-head">Plano de cuidado · Clara, 41 anos</p>{itens}</div>') +
          A(560, 520, '<p class="f-leg">“Quero voltar a ter energia para brincar com meu filho.”</p>', w=424) +
          A(96, 1160, '<p class="f-nota aviso">História e imagem ilustrativas. Personagem fictícia.</p>') + rod(),
          label='Carrossel com foto ilustrativa sobre bloco verde deslocado e card de plano')
P[9] = ab(PH('conversa2', 0, 0, 1080, 460, 55, 40) +
          A(96, 540, f'<p class="f-titulo">Ninguém volta a um lugar onde não se sentiu {k("cuidado")}.</p>') +
          A(96, 800, '<p class="f-num">8 em cada 10</p><p class="f-sub">voltaram para mais de um atendimento.</p>'
                     '<p class="f-nota gap32">Fonte: Escritório do Cuidado numa indústria, 1º sem. 2026</p>') + rod('Reel · 20 s'),
          label='Número suave com foto de conversa no topo')
sono = ''.join(f'<div class="col-b"><span style="height:{h}%"></span><span class="f-nota">{s}</span></div>'
               for h, s in ((61, 'S1'), (66, 'S2'), (72, 'S3'), (78, 'S4')))
P[10] = ab(PH('tenis', 0, 0, 1080, 1350, 62, 50) +
           BX(48, 48, 640, 420, 'tif') + etq('Como funciona o cuidado · 3/3') +
           A(96, 190, f'<p class="f-titulo">O cuidado não para quando a consulta {k("acaba")}.</p>', w=560) +
           A(392, 900, f'<div class="card baixo"><p class="f-nota card-head">Sono · 4 semanas · dados ilustrativos</p><div class="cols">{sono}</div></div>', w=592) + rod(cls='creme'),
           label='Carrossel com foto de pessoa amarrando o tênis, bloco tiffany e card de sono')
P[11] = ab(PH('consulta', 0, 0, 1080, 1350, 45, 50, duo=True) +
           BX(48, 640, 984, 662, 'creme') + etq('Origem', y=700) +
           A(96, 780, f'<p class="f-display">Tudo começou num {k("hospital")}.</p>') +
           A(96, 1000, '<div class="linha-t"><p class="f-titulo"><span class="k">2009</span></p><p class="f-corpo">Ouvir antes de propor.</p></div>'
                       '<div class="linha-t"><p class="f-titulo"><span class="k">Hoje</span></p><p class="f-corpo">Dentro da empresa.</p></div>'),
           label='Capa de reel de origem com foto em duotone e folha creme')
P[12] = ab('<div class="folha"></div>' + PH('maos', 640, 48, 392, 1254, 40, 50) + etq('Na imprensa') + A(96, 250, '<p class="aspas">«</p>') +
           A(96, 400, f'<p class="f-sub">Antes de perguntar apenas o que o trabalho está fazendo com a saúde mental das pessoas, deveríamos fazer uma {k("pergunta maior")}.</p>', w=500) +
           A(96, 1010, '<span class="fio-c"></span><p class="f-nota gap16">Do artigo “Riscos psicossociais no ambiente de trabalho e saúde”, RH Pra Você</p>', w=500) +
           '<div class="rod meia"><span>@fairhealth.br</span></div>',
           label='Citação com coluna de foto de mãos dadas')
P[13] = ab(PH('sono', 0, 0, 1080, 1350, 38, 50) +
           BX(0, 0, 1080, 420, 'tif') + etq('Pilares · Sono') +
           A(96, 200, f'<p class="f-display">Dormir não é tempo {k("perdido")}.</p>') +
           BX(48, 900, 620, 402, 'verde') + A(96, 950, '<p class="f-num creme">7 a 9 h</p><p class="f-sub claro">por noite, para adultos.</p>', w=540) + A(96, 1206, '<p class="f-nota claro">Fonte: RAND Europe, 2016</p>', w=540),
           label='Capa de reel do pilar sono com foto de pessoa dormindo')
P[14] = ab(PH('conversa3', 0, 0, 1080, 1350, 68, 50) +
           BX(48, 700, 700, 602, 'verde') + etq('Liderança', x=96, y=760, cls='claro') +
           A(96, 850, f'<p class="f-titulo creme">O que é {k("importante")} para você?</p>', w=600) +
           A(96, 1110, '<p class="f-leg claro">Uma pergunta que todo líder pode fazer.</p>', w=600) +
           RESP(600, 140, 400, 'Sair no horário.', 3) + RESP(560, 360, 440, 'Mais tempo com meus filhos.', -2),
           label='Capa de carrossel para líderes com foto, painel verde e cartões de resposta')
passos = ''.join(f'<div class="passo"><span class="f-titulo k">{n}</span><span class="f-corpo">{t}</span></div>'
                 for n, t in ((1, 'Diagnóstico gratuito'), (2, 'Proposta personalizada'), (3, 'Implantação e primeiros atendimentos')))
P[15] = ab(BX(672, 120, 344, 400, 'verde') + PH('maos-time', 640, 88, 344, 400, 50, 45) +
           etq('Como chega a uma empresa') + A(96, 220, f'<p class="f-titulo">Como o cuidado chega à sua {k("empresa")}.</p>', w=500) +
           A(96, 600, passos) + A(96, 1100, '<p class="f-sub">Comente <span class="k">CUIDADO</span>.</p>') + rod('Reel · 25 s'),
           label='Passos com foto de mãos unidas sobre bloco verde deslocado')
P[16] = ab(PH('escada', 0, 0, 1080, 720, 55, 60) +
           '<div class="folha-b"></div>' + etq('Ciência no cuidado', y=780) +
           A(96, 860, f'<p class="f-titulo">Estilo de vida também é tratamento {mt("sério")}.</p>') +
           A(96, 1100, '<span class="chip out">N Engl J Med · 2002</span>') + rod(),
           label='Capa de carrossel de ciência com foto de pés subindo escada')

CIENCIA3 = ab('<div class="folha"></div>' + etq('Ciência no cuidado · 3/6') +
              A(96, 280, f'<p class="f-titulo">Quem mudou a {k("rotina")}</p>') +
              A(96, 420, '<p class="f-num">58% menos</p><p class="f-sub">casos novos de diabetes tipo 2 do que o grupo placebo.</p><p class="f-leg gap32">Com medicamento, a redução foi de 31%.</p>') +
              PH('comida', 96, 790, 888, 220, 50, 50) +
              A(96, 1040, '<div class="ref"><p class="f-nota">Diabetes Prevention Program. N Engl J Med. 2002;346(6):393-403. Adultos com risco aumentado, 2,8 anos.</p></div>') + rod('3/6'),
              label='Slide de resultado de estudo com faixa de foto')
PILAR = ab(PH('respira', 540, 0, 540, 1350, 50, 40) + etq('Pilares da MEV · 4/6') + A(96, 250, icone('Manejo do estresse', 'ic-g')) +
           A(96, 420, f'<p class="f-display">Respirar {k("também")} é cuidado.</p>', w=420) +
           A(96, 900, '<p class="f-corpo">O estresse entra no plano a partir da sua rotina real.</p>', w=400) + rod(),
           label='Modelo de pilar com coluna de foto')

# carrossel panorâmico com fio contínuo (P2)
def fio(d):
    return f'<svg class="fio-svg" viewBox="0 0 1080 1350" preserveAspectRatio="none" aria-hidden="true"><path d="{d}"/></svg>'

CARR = [
    ab(PH('sorriso1', 560, 0, 520, 1350, 50, 30) + etq('Como funciona o cuidado') +
       A(96, 330, f'<p class="f-display">Aqui, o cuidado começa com uma {k("pergunta")}.</p>', w=520) +
       fio('M96 1100 H1080') + rod()),
    ab(PH('conversa1', 0, 0, 1080, 620, 30, 40) + fio('M0 1100 H300 V760 H1080') + etq('Como funciona · 2/6', y=680) +
       A(96, 860, f'<p class="f-titulo">Fica {k("dentro")} da empresa.</p>', w=640) + rod('2/6')),
    ab(fio('M0 760 H540 V420 H1080') + etq('Como funciona · 3/6') + A(96, 200, '<p class="f-etq">Passo 1</p>') +
       A(96, 480, f'<p class="f-display">A gente te {k("conhece")}.</p>', w=420) +
       PH('conversa2', 600, 520, 400, 560, 55, 40) + rod('3/6')),
    ab(fio('M0 420 H200 V1180 H1080') + etq('Como funciona · 4/6') + A(260, 200, f'<p class="f-titulo">O que é {k("importante")} para você?</p>', w=724) +
       A(260, 520, '<div class="card"><p class="f-nota card-head">Conversa · Escritório do Cuidado</p><p class="balao pro f-corpo">O que é importante para você hoje?</p>'
                   '<p class="balao pessoa f-corpo">Dormir melhor e ter energia.</p></div>', w=724)),
    ab(PH('maos', 0, 0, 1080, 1350, 45, 50, duo=True) + VEU + fio('M0 1180 H1080') +
       A(96, 380, f'<p class="f-display creme">O que você conta fica entre você e quem {mt("cuida")}.</p>') + rod('5/6', cls='on-esc')),
    ab(fio('M0 1180 H480') + etq('Como funciona · 6/6') + A(96, 240, f'<p class="f-display">E para você, o que é {k("importante")}?</p>') +
       A(96, 640, '<div class="card fino"><p class="f-leg">Comente aqui…</p></div>') +
       BX(744, 1014, 288, 288, 'verde') + f'<img class="logo-canto" src="{LOGO_C}" alt="">'),
]

REEL = [
    ab(PH('estresse', 0, 0, 1080, 1920, 50, 40, duo=True) + GR(420, 1500) + A(96, 760, f'<p class="f-titulo creme">Antes do afastamento, teve um {mt("atestado")}.</p>', w=844), 'reel', 'Cena 1 com foto em duotone'),
    ab(PH('cafe-notebook', 0, 0, 1080, 1920, 50, 50) + BX(48, 640, 984, 560, 'tif') +
       A(96, 760, f'<p class="f-titulo">Antes do atestado, uma semana {k("pesada")}.</p>', w=844), 'reel', 'Cena 2 com foto e faixa tiffany'),
    ab(A(96, 620, '<p class="f-corpo">Em 2024, no Brasil:</p><p class="f-num gap24">mais de 470 mil</p><p class="f-sub">licenças por saúde mental. Cada uma teve um <span class="k">antes</span>.</p><p class="f-nota gap48">Fonte: Ministério da Previdência Social</p>', w=844) +
       PH('industria2', 96, 1200, 888, 360, 30, 40), 'reel', 'Cena com número e foto'),
    ab('<div class="painel"></div>' + A(96, 760, f'<p class="f-display">Cuidar {k("antes")}.</p>', w=844, cls='creme') +
       f'<img class="logo-reel" src="{LOGO_C}" alt="">', 'reel', 'Cena final com logo'),
]

ERR = [
    ('Tudo tiffany, sem foto: some no feed.',
     ab(etq('Como funciona o cuidado') + A(96, 400, f'<p class="f-display">Aqui, o cuidado começa com uma {k("pergunta")}.</p>') + rod()),
     'Foto de gente, tiffany como acento.', P[2]),
    ('Banco posado: jaleco, braços cruzados, sorriso para a câmera.',
     ab(PH('evitar-pose', 0, 0, 1080, 1350, 50, 30) + A(96, 1000, '<p class="f-titulo">Conheça nossos especialistas</p>')),
     'Gente de verdade, em situação real.', P[1]),
    ('Inclinado demais, elementos demais.',
     ab(PH('conversa3', 0, 0, 1080, 1350, 68, 50) + RESP(100, 120, 520, 'Sair no horário.', -14) + RESP(420, 380, 560, 'Mais tempo com meus filhos.', 12) +
        RESP(160, 700, 600, 'Dormir melhor.', -9) + RESP(380, 980, 560, 'Comer sem pressa.', 15)),
     'No máximo ±3° e dois cartões.', P[14]),
    ('Texto sobre foto sem apoio: ilegível.',
     ab(PH('conversa1', 0, 0, 1080, 1350, 45, 40) + A(96, 900, f'<p class="f-titulo branco">Antes de qualquer exame, uma {k("conversa")}.</p>')),
     'Texto sempre sobre faixa, folha ou duotone.', P[1]),
]

# ---------------- CSS ----------------
CSS = r'''
/* Brand book v2: a foto é a protagonista, o tiffany é o acento, os elementos dão movimento. */
:root {
  --tif: #96C5BD; --verde: #1F3A36; --creme: #F0F0E9; --tesc: #5FA89A; --vlogo: #2F6B64;
  --tclaro: #BFE0D9; --gelo: #F6F8F7; --tinta: #141B1B; --ui: #FFFFFF; --ui-linha: #DBDBDB; --ui-texto: #262626;
  --erro: #A3342C; --branco: #FFFFFF;
  --f: "Raleway", "Helvetica Neue", Arial, sans-serif;
  color-scheme: light;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--gelo); color: var(--verde); font-family: var(--f); font-size: 16px; line-height: 1.5; }
p { margin: 0; }
.k { font-weight: 800; font-style: italic; }
:focus-visible { outline: 3px solid var(--vlogo); outline-offset: 2px; }
.nav { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 10; background: var(--verde); color: var(--creme); }
.nav-in { display: flex; align-items: center; gap: 24px; max-width: 1240px; margin: 0 auto; padding: 10px 24px; overflow-x: auto; scrollbar-width: none; }
.nav img { width: 32px; height: 32px; flex: none; }
.nav a { text-decoration: none; font-size: 12px; letter-spacing: .16em; text-transform: uppercase; white-space: nowrap; color: var(--tclaro); }
.nav a:hover { color: var(--creme); }
.nav .v { margin-left: auto; font-size: 11px; color: var(--tesc); white-space: nowrap; }
.faixa { padding-block: 72px; padding-inline: 24px; }
.wrap { max-width: 1240px; margin: 0 auto; display: grid; gap: 40px; }
.f-tif { background: var(--tif); } .f-cre { background: var(--creme); } .f-gelo { background: var(--gelo); }
.f-esc { background: var(--verde); color: var(--creme); }
.cab { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 24px; align-items: end; border-top: 2px solid currentColor; padding-top: 16px; }
.cab h2 { margin: 0; font-weight: 400; font-size: clamp(36px, 6vw, 72px); line-height: 1; letter-spacing: -0.01em; text-wrap: balance; }
.cab > p { font-size: 16px; max-width: 46ch; justify-self: end; }
.rot { font-size: 11px; letter-spacing: .2em; text-transform: uppercase; }
.leg { font-size: 13px; line-height: 18px; margin-top: 10px; }

/* hero: colagem em camadas */
.hero { background: var(--verde); color: var(--creme); padding-block: 56px 80px; padding-inline: 24px; overflow: hidden; }
.hero-in { max-width: 1240px; margin: 0 auto; display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 48px; align-items: center; }
.hero h1 { margin: 0; font-weight: 400; font-size: clamp(56px, 10vw, 128px); line-height: .9; letter-spacing: -0.02em; }
.hero .sub { font-size: clamp(22px, 2.6vw, 34px); line-height: 1.15; margin-top: 24px; text-wrap: balance; }
.hero .rot { color: var(--tclaro); }
.hero-pecas { position: relative; display: grid; grid-template-columns: repeat(12, minmax(0, 1fr)); grid-template-rows: auto; }
.hero-pecas > :nth-child(1) { grid-column: 1 / span 5; grid-row: 1; margin-top: 64px; transform: rotate(-2deg); }
.hero-pecas > :nth-child(2) { grid-column: 4 / span 5; grid-row: 1; z-index: 2; }
.hero-pecas > :nth-child(3) { grid-column: 8 / span 5; grid-row: 1; margin-top: 96px; transform: rotate(2deg); }

/* artboards */
.ab { container-type: inline-size; position: relative; width: 100%; max-width: 100%; aspect-ratio: 4 / 5; overflow: hidden; background: var(--tif); color: var(--verde); box-shadow: 0 12px 28px rgba(20, 27, 27, .16); }
.ab.reel { aspect-ratio: 9 / 16; }
.f-esc .ab, .hero .ab { box-shadow: 0 18px 40px rgba(0, 0, 0, .35); }
.ig-grade .ab, .tel .ab { box-shadow: none; }
.in { position: absolute; inset: 0; --u: calc(100cqw / 1080); font-family: var(--f); font-variant-numeric: lining-nums; }
.a, .ph, .bx, .resp { position: absolute; left: calc(var(--x) * var(--u)); top: calc(var(--y) * var(--u)); width: calc(var(--w) * var(--u)); }
.ph, .bx { height: calc(var(--h) * var(--u)); }
.ph { background-size: cover; background-position: var(--px) var(--py); background-color: var(--verde); }
.resp { background: var(--creme); padding: calc(28 * var(--u)) calc(36 * var(--u)); transform: rotate(var(--r)); box-shadow: 0 calc(16 * var(--u)) calc(32 * var(--u)) rgba(20, 27, 27, .22); }
.mt { background: linear-gradient(transparent 14%, var(--tif) 14%, var(--tif) 94%, transparent 94%); color: var(--verde); padding: 0 .08em; -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.f-display { font-size: calc(104 * var(--u)); line-height: calc(104 * var(--u)); letter-spacing: -0.01em; }
.f-titulo { font-size: calc(72 * var(--u)); line-height: calc(80 * var(--u)); letter-spacing: -0.005em; }
.f-sub { font-size: calc(44 * var(--u)); line-height: calc(56 * var(--u)); }
.f-corpo { font-size: calc(34 * var(--u)); line-height: calc(46 * var(--u)); }
.f-leg { font-size: calc(28 * var(--u)); line-height: calc(38 * var(--u)); }
.f-etq { font-size: calc(26 * var(--u)); line-height: calc(32 * var(--u)); letter-spacing: .2em; text-transform: uppercase; }
.f-nota { font-size: calc(24 * var(--u)); line-height: calc(32 * var(--u)); }
.f-num { font-size: calc(120 * var(--u)); line-height: calc(128 * var(--u)); letter-spacing: -0.01em; }
.gap16 { margin-top: calc(16 * var(--u)); } .gap24 { margin-top: calc(24 * var(--u)); } .gap32 { margin-top: calc(32 * var(--u)); } .gap48 { margin-top: calc(48 * var(--u)); }
.fio-c { display: block; width: calc(64 * var(--u)); height: calc(4 * var(--u)); background: currentColor; margin-top: calc(16 * var(--u)); }
.creme { color: var(--creme); } .claro { color: var(--tclaro); } .on-esc { color: var(--tclaro); } .branco { color: var(--branco); }
.sombra-t { text-shadow: 0 2px 18px rgba(0, 0, 0, .45); }
.rod { position: absolute; left: calc(96 * var(--u)); right: calc(96 * var(--u)); top: calc(1206 * var(--u)); height: calc(48 * var(--u)); border-top: calc(2 * var(--u)) solid currentColor; display: flex; justify-content: space-between; align-items: flex-end; font-size: calc(24 * var(--u)); line-height: calc(32 * var(--u)); }
.rod.on-esc, .rod.creme { color: var(--creme); }
.rod.meia { right: calc(540 * var(--u)); padding-right: calc(48 * var(--u)); }
.rod.meia-d { left: calc(600 * var(--u)); color: var(--creme); justify-content: flex-end; }
.arr { display: inline-flex; align-items: center; gap: calc(16 * var(--u)); }
.seta { width: calc(48 * var(--u)); height: calc(16 * var(--u)); }
.folha { position: absolute; inset: calc(48 * var(--u)); background: var(--creme); }
.folha-b { position: absolute; left: calc(48 * var(--u)); right: calc(48 * var(--u)); top: calc(680 * var(--u)); bottom: calc(48 * var(--u)); background: var(--creme); }
.painel { position: absolute; inset: calc(48 * var(--u)); background: var(--verde); }
.split { position: absolute; left: calc(540 * var(--u)); top: 0; right: 0; bottom: 0; background: var(--verde); }
.chip { display: inline-flex; align-items: center; height: calc(64 * var(--u)); padding: 0 calc(24 * var(--u)); border-radius: calc(8 * var(--u)); background: var(--creme); font-size: calc(28 * var(--u)); }
.chip.out { background: transparent; border: calc(2 * var(--u)) solid var(--vlogo); color: var(--vlogo); }
.card { background: var(--gelo); border-radius: calc(16 * var(--u)); padding: calc(40 * var(--u)) calc(48 * var(--u)); box-shadow: 0 calc(24 * var(--u)) calc(48 * var(--u)) rgba(20, 27, 27, .22); color: var(--verde); }
.card.fino { padding: calc(32 * var(--u)) calc(40 * var(--u)); color: var(--vlogo); }
.card-head { color: var(--vlogo); padding-bottom: calc(20 * var(--u)); border-bottom: calc(2 * var(--u)) solid var(--verde); margin-bottom: calc(24 * var(--u)); }
.chk { display: flex; align-items: center; gap: calc(24 * var(--u)); padding: calc(10 * var(--u)) 0; }
.box { width: calc(40 * var(--u)); height: calc(40 * var(--u)); border: calc(3 * var(--u)) solid var(--verde); border-radius: calc(6 * var(--u)); flex: none; }
.barra { display: grid; grid-template-columns: calc(300 * var(--u)) 1fr; align-items: center; gap: calc(24 * var(--u)); padding: calc(12 * var(--u)) 0; }
.trilho { display: block; height: calc(24 * var(--u)); background: var(--tclaro); }
.trilho span { display: block; height: 100%; background: var(--verde); }
.cols { display: flex; align-items: flex-end; gap: calc(40 * var(--u)); height: calc(150 * var(--u)); }
.col-b { display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: calc(8 * var(--u)); height: 100%; width: calc(90 * var(--u)); }
.col-b span:first-child { width: 100%; background: var(--verde); }
.linha-t { display: grid; grid-template-columns: calc(232 * var(--u)) 1fr; gap: calc(24 * var(--u)); align-items: baseline; border-top: calc(2 * var(--u)) solid var(--verde); padding: calc(16 * var(--u)) 0; }
.lista p { font-size: calc(34 * var(--u)); line-height: calc(46 * var(--u)); padding: calc(20 * var(--u)) 0; border-top: calc(2 * var(--u)) solid var(--verde); }
.lista.on-esc p { border-color: var(--tclaro); color: var(--creme); }
.passo { display: grid; grid-template-columns: calc(128 * var(--u)) 1fr; align-items: center; min-height: calc(150 * var(--u)); border-top: calc(2 * var(--u)) solid var(--verde); }
.passo:last-child { border-bottom: calc(2 * var(--u)) solid var(--verde); }
.icos { display: flex; gap: calc(40 * var(--u)); }
.ic { width: calc(72 * var(--u)); height: calc(72 * var(--u)); flex: none; fill: none; stroke: var(--verde); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
.ic-g { width: calc(112 * var(--u)); height: calc(112 * var(--u)); fill: none; stroke: var(--verde); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.aspas { font-size: calc(144 * var(--u)); line-height: calc(120 * var(--u)); font-weight: 800; font-style: italic; color: var(--vlogo); }
.ref { border-top: calc(2 * var(--u)) solid var(--verde); padding-top: calc(16 * var(--u)); }
.aviso { color: var(--vlogo); }
.balao { padding: calc(20 * var(--u)) calc(28 * var(--u)); border-radius: calc(16 * var(--u)); max-width: 85%; margin-bottom: calc(20 * var(--u)); }
.balao.pro { background: var(--verde); color: var(--creme); }
.balao.pessoa { background: var(--creme); margin-left: auto; }
.faixa-logo { position: absolute; left: 0; right: 0; top: calc(1000 * var(--u)); bottom: 0; background: var(--verde); display: flex; align-items: center; justify-content: flex-end; padding-right: calc(96 * var(--u)); }
.logo-canto { position: absolute; left: calc(808 * var(--u)); top: calc(1078 * var(--u)); width: calc(160 * var(--u)); height: auto; }
.faixa-logo img { width: calc(160 * var(--u)); height: auto; }
.logo-reel { position: absolute; left: calc(96 * var(--u)); top: calc(1380 * var(--u)); width: calc(160 * var(--u)); height: auto; }
.gr { position: absolute; left: 0; right: 0; top: calc(var(--y) * var(--u)); height: calc(var(--h) * var(--u)); background: linear-gradient(rgba(20, 35, 32, 0), rgba(20, 35, 32, .88) 55%); }
.veu { position: absolute; inset: 0; background: rgba(20, 35, 32, .42); }
.fio-svg { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
.fio-svg path { fill: none; stroke: var(--verde); stroke-width: 8; stroke-linejoin: miter; }

/* página */
.grade { display: grid; gap: 24px; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); }
.grade figure { margin: 0; min-width: 0; }
.modelo-nome { font-size: 15px; margin-top: 12px; }
.tira { display: grid; grid-template-columns: repeat(6, minmax(140px, 1fr)); gap: 0; overflow-x: auto; padding-bottom: 8px; }
.tira .ab { box-shadow: none; }
.tira-reel { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; max-width: 760px; }
.selo { display: inline-flex; align-items: center; gap: 6px; font-size: 11px; letter-spacing: .14em; text-transform: uppercase; font-weight: 800; padding: 4px 8px; }
.selo.sim { background: var(--verde); color: var(--creme); } .selo.nao { background: var(--erro); color: var(--branco); }
.f-esc .selo.sim { background: var(--creme); color: var(--verde); }
.prop { display: flex; height: 300px; }
.prop > div { padding: 16px; display: flex; flex-direction: column; justify-content: space-between; min-width: 0; background-size: cover; background-position: center; }
.prop .nm { font-size: clamp(18px, 2.4vw, 32px); line-height: 1.05; }
.prop .hx { font-size: 12px; letter-spacing: .1em; text-transform: uppercase; }
.fotos { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; }
.cat { display: grid; gap: 8px; grid-template-columns: repeat(2, minmax(0, 1fr)); align-content: start; }
.cat h3 { grid-column: 1 / -1; margin: 0 0 4px; font-weight: 400; font-size: 24px; line-height: 1.1; }
.cat h3 .k { display: inline; }
.foto { aspect-ratio: 4 / 5; max-width: 100%; background-size: cover; background-position: center; }
.foto.l { grid-column: 1 / -1; aspect-ratio: 4 / 3; }
.trat { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; }
.trat figure { margin: 0; position: relative; min-width: 0; }
.trat .foto { aspect-ratio: 4 / 5; }
.vida { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.vida figure { margin: 0; min-width: 0; }
.vida h3 { margin: 12px 0 2px; font-size: 18px; font-weight: 400; }
.vida h3 .k { font-weight: 800; }
.uso { display: grid; grid-template-columns: minmax(0, 420px) minmax(0, 420px); gap: 40px; justify-content: center; align-items: start; }
.tel { background: var(--ui); color: var(--ui-texto); border-radius: 28px; padding: 16px 0 0; box-shadow: 0 30px 60px rgba(0, 0, 0, .35); overflow: hidden; }
.perfil { display: grid; grid-template-columns: 76px 1fr; gap: 16px; align-items: center; padding: 8px 16px; }
.perfil img { width: 76px; height: 76px; border-radius: 50%; }
.perfil .user { font-weight: 800; font-size: 16px; }
.bio { padding: 4px 16px 12px; font-size: 13px; line-height: 18px; }
.bio b { font-weight: 800; } .bio .lk { color: #00376B; }
.botoes { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; padding: 0 16px 12px; }
.botoes span { background: #EFEFEF; border-radius: 8px; text-align: center; font-size: 13px; font-weight: 800; padding: 7px 0; }
.ig-grade { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; border-top: 1px solid var(--ui-linha); }
.crop3x4 { position: relative; aspect-ratio: 3 / 4; overflow: hidden; max-width: 100%; }
.crop3x4 .ab { position: absolute; top: 0; left: -3.333%; width: 106.667%; max-width: none; }
.post-h { display: flex; align-items: center; gap: 10px; padding: 0 12px 12px; font-size: 13px; }
.post-h img { width: 32px; height: 32px; border-radius: 50%; }
.post-h b { font-weight: 800; }
.acoes { display: flex; gap: 16px; padding: 12px; }
.acoes svg { width: 24px; height: 24px; fill: none; stroke: var(--ui-texto); stroke-width: 1.8; stroke-linejoin: round; stroke-linecap: round; }
.acoes .salvar { margin-left: auto; }
.cap { padding: 0 12px 16px; font-size: 13px; line-height: 18px; }
.cap b { font-weight: 800; } .cap .mais { color: #737373; }
.ce { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 32px 40px; }
.ce-par { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.ce-par figure { margin: 0; position: relative; min-width: 0; }
.ce-par .nao-ab { outline: 4px solid var(--erro); outline-offset: -4px; }
.logos { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; }
.lt { min-height: 240px; display: flex; flex-direction: column; justify-content: space-between; padding: 20px; }
.lt .alvo { flex: 1; display: flex; align-items: center; justify-content: center; padding-block: 20px; }
.lt-esc { background: var(--verde); color: var(--creme); } .lt-gelo { background: var(--gelo); border: 1px solid var(--tclaro); }
.lt-foto { background-size: cover; background-position: center; color: var(--creme); position: relative; }
.lt-foto::before { content: ""; position: absolute; inset: 0; background: linear-gradient(transparent 50%, rgba(20, 27, 27, .7)); }
.lt-foto > * { position: relative; }
.mood { display: grid; grid-template-columns: minmax(0, 3fr) minmax(0, 2fr); gap: 40px; align-items: end; }
.mood .frase { font-size: clamp(44px, 7vw, 96px); line-height: .95; letter-spacing: -0.02em; text-wrap: balance; }
.palavras { display: flex; flex-wrap: wrap; gap: 6px 22px; font-size: clamp(22px, 3vw, 34px); color: var(--tclaro); }
.palavras .k { color: var(--creme); }
.mosaico { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 8px; }
.mosaico .foto { aspect-ratio: 1; }
.rodape-pg { padding: 24px; text-align: center; font-size: 12px; background: var(--verde); color: var(--tclaro); }
@media (max-width: 900px) {
  .hero-in, .mood, .cab { grid-template-columns: minmax(0, 1fr); }
  .cab > p { justify-self: start; }
  .fotos, .trat, .logos { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .vida { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .ce, .uso { grid-template-columns: minmax(0, 1fr); }
  .mosaico { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
@media (max-width: 560px) {
  .faixa { padding-block: 48px; padding-inline: 16px; }
  .hero { padding-inline: 16px; }
  .fotos, .vida, .logos { grid-template-columns: minmax(0, 1fr); }
  .prop { height: 200px; } .prop .hx { display: none; }
  .tira-reel { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .grade { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }
}
'''


def fig(ab_html, nome, desc=''):
    return f'<figure>{ab_html}<figcaption class="modelo-nome">{nome}{"<br><span class=leg>" + desc + "</span>" if desc else ""}</figcaption></figure>'


def cab(titulo, sub, eyebrow):
    return f'<div class="cab"><div><p class="rot">{eyebrow}</p><h2>{titulo}</h2></div><p>{sub}</p></div>'


def crop(p):
    return f'<div class="crop3x4">{p}</div>'


def foto(n, cls='', style=''):
    USADAS.add(n)
    return f'<div class="foto f-{n} {cls}" style="{style}"></div>'


SELO_S = '<span class="selo sim">✓ Assim</span>'
SELO_N = '<span class="selo nao">✕ Evite</span>'
ICON_UI = {
    'curtir': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    'comentar': '<path d="M20 12a8 8 0 1 1-3.3-6.5A8 8 0 0 1 20 12l1 5-5-1.2"/>',
    'enviar': '<path d="M21 3L3 10l7 3 3 7 8-17z"/><path d="M10 13l11-10"/>',
    'salvar': '<path d="M6 3h12v18l-6-5-6 5z"/>',
}
acoes = ''.join(f'<svg class="{"salvar" if n == "salvar" else ""}" viewBox="0 0 24 24" aria-hidden="true">{d}</svg>' for n, d in ICON_UI.items())

h = []
h.append(f'''<meta charset="utf-8">
<title>Identidade Visual fairhealth</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,400;0,800;1,400;1,800&display=swap">
<style>{CSS}</style>
<style id="fotos">/*FOTOS*/</style>
<nav class="nav" aria-label="Seções"><div class="nav-in"><img src="{LOGO_C}" alt="fairhealth">
<a href="#fotografia">Fotografia</a><a href="#vida">Elementos</a><a href="#cor">Cor</a><a href="#modelos">Modelos</a><a href="#uso">Em uso</a><a href="#certo-errado">Certo e errado</a><a href="#marca">Marca</a><a href="#tipografia">Tipografia</a><a href="#mood">Mood</a><span class="v">v2 · mais gente, mais vida</span></div></nav>

<header class="hero"><div class="hero-in">
  <div><p class="rot">Identidade visual · redes sociais · v2 · outubro de 2026</p>
    <h1>fair<span class="k">health</span></h1>
    <p class="sub">Gente de verdade. Tiffany como <span class="k">acento</span>.</p></div>
  <div class="hero-pecas">{P[1]}{P[14]}{P[5]}</div>
</div></header>
''')

# FOTOGRAFIA
cats = [
    ('Gente no <span class="k">trabalho</span>', ['industria1', 'industria2', 'oculos', 'cafe-notebook', 'solda']),
    ('Conversa e <span class="k">cuidado</span>', ['conversa1', 'conversa2', 'maos', 'consulta', 'conversa3']),
    ('Hábitos do <span class="k">dia a dia</span>', ['sono', 'comida', 'tenis', 'respira', 'escada']),
    ('Vínculos e <span class="k">pausa</span>', ['amigos', 'cafe', 'maos-time', 'sorriso2', 'sorriso1']),
]
cat_html = ''.join(f'<div class="cat"><h3>{t}</h3>{foto(fs[0], "l")}{"".join(foto(f) for f in fs[1:])}</div>' for t, fs in cats)
trat = [
    (foto('conversa2'), f'{SELO_S} Natural, luz do dia', ''),
    (foto('conversa2-d'), f'{SELO_S} Duotone verde, para texto por cima', ''),
    (foto('conversa2', style='filter:grayscale(1)'), f'{SELO_N} Preto e branco', ''),
    (foto('conversa2', style='filter:saturate(2.2) contrast(1.3)'), f'{SELO_N} Saturada e contrastada', ''),
]
h.append(f'''<section class="faixa f-cre" id="fotografia"><div class="wrap">
{cab(f"Mais {k('gente')}", "A foto é a protagonista. Pessoas em situações reais, luz natural, tons quentes. Imagens de banco são ilustrativas: nunca apresentadas como o time ou como clientes.", "Fotografia")}
<div class="fotos">{cat_html}</div>
<div class="trat">{''.join(f'<figure>{f}<figcaption class="leg">{c}</figcaption></figure>' for f, c, _ in trat)}</div>
</div></section>
''')

# ELEMENTOS DE VIDA
def demo(inner, cls=''):
    return ab(inner, cls)

vida = [
    (demo(PH('conversa1', 0, 0, 1080, 1350, 45, 40) + BX(0, 860, 1080, 490, 'tif') + A(96, 960, f'<p class="f-titulo">Uma {k("conversa")}.</p>')),
     f'Faixa {k("tiffany")}', 'O tiffany entra como faixa sobre a foto, não como fundo inteiro.'),
    (demo(PH('conversa3', 0, 0, 1080, 1350, 68, 50) + RESP(120, 300, 520, 'Sair no horário.', 3) + RESP(400, 620, 600, 'Mais tempo com meus filhos.', -2)),
     f'Cartão de {k("resposta")}', 'Respostas ilustrativas a "o que é importante para você?". No máximo 2, inclinação até 3°.'),
    (demo(PH('estresse', 0, 0, 1080, 1350, 50, 40, duo=True) + GR(460, 890) + A(96, 780, f'<p class="f-display creme">Teve um {mt("sinal")}.</p>')),
     f'{k("Marca-texto")} tiffany', 'A palavra-chave ganha um bloco tiffany. Funciona sobre foto escura e sobre creme.'),
    (demo(PH('comida', 0, 0, 352, 1350, 50, 50) + PH('tenis', 364, 0, 352, 1350, 65, 50) + PH('sono', 728, 0, 352, 1350, 35, 50)),
     f'Tiras de {k("foto")}', 'Três recortes lado a lado dão ritmo. Para pilares, rotina e listas.'),
    (demo(BX(200, 260, 760, 900, 'verde') + PH('retrato', 136, 196, 760, 900, 50, 25)),
     f'Bloco {k("deslocado")}', 'Um plano verde ou tiffany atrás da foto, deslocado 64 px. Cria profundidade sem sombra pesada.'),
    (demo(PH('maos', 0, 0, 1080, 1350, 45, 50, duo=True) + VEU + A(96, 520, f'<p class="f-display creme">Entre você e quem {k("cuida")}.</p>')),
     f'{k("Duotone")} verde', 'Foto em verde-autoridade e tiffany-claro para receber texto grande em creme.'),
]
h.append(f'''<section class="faixa f-gelo" id="vida"><div class="wrap">
{cab(f"Elementos de {k('vida')}", "Seis recursos para dar movimento sem perder a seriedade. Use no máximo dois por peça.", "Elementos")}
<div class="vida">{''.join(f'<figure>{d}<h3>{t}</h3><p class="leg">{x}</p></figure>' for d, t, x in vida)}</div>
</div></section>
''')

# COR
USADAS.add('conversa1')
h.append(f'''<section class="faixa f-cre" id="cor"><div class="wrap">
{cab(f"Tiffany como {k('acento')}", "Nova proporção: a foto ocupa o maior espaço, o tiffany aparece em faixas, blocos e marca-texto, e o verde dá o contraste.", "Cor")}
<div class="prop" role="img" aria-label="Proporção: foto 40%, tiffany 30%, verde-autoridade 20%, creme 10%">
  <div class="f-conversa1" style="flex:40;color:var(--creme)"><span class="hx">40%</span><div><p class="nm">Foto</p><p class="hx">natural ou duotone</p></div></div>
  <div style="flex:30;background:var(--tif)"><span class="hx">30%</span><div><p class="nm">Tiffany</p><p class="hx">#96C5BD · faixas e acentos</p></div></div>
  <div style="flex:20;background:var(--verde);color:var(--creme)"><span class="hx">20%</span><div><p class="nm">Verde</p><p class="hx">#1F3A36</p></div></div>
  <div style="flex:10;background:var(--creme);outline:1px solid var(--tclaro);outline-offset:-1px"><span class="hx">10%</span><div><p class="nm">Creme</p></div></div>
</div>
</div></section>
''')

# MODELOS
modelos = [
    (P[1], 'Foto + faixa tiffany', 'Capa de reel ou carrossel.'),
    (P[2], 'Coluna de foto + resposta', 'Capa-pergunta com gente.'),
    (P[3], 'Duotone + marca-texto', 'Frase forte sobre foto.'),
    (P[14], 'Foto + painel + respostas', 'Conversa com líderes.'),
    (P[8], 'Bloco deslocado + card', 'Produto com personagem fictícia.'),
    (P[5], 'Tiras de foto', 'Pilares e rotina.'),
    (P[9], 'Foto no topo + número suave', 'Prova com cuidado.'),
    (P[10], 'Foto inteira + bloco + card', 'Acompanhamento.'),
    (P[11], 'Duotone + folha creme', 'História e origem.'),
    (P[12], 'Citação + coluna de foto', 'Artigos e frases.'),
    (PILAR, 'Pilar com coluna de foto', 'Um pilar por peça.'),
    (CIENCIA3, 'Ciência com faixa de foto', 'Resultado de estudo.'),
]
h.append(f'''<section class="faixa f-tif" id="modelos"><div class="wrap">
{cab(f"Os {k('modelos')}, com gente", "Desenhados com o conteúdo do Mês 1. Cada peça combina foto, uma cor de apoio e no máximo dois elementos.", "Modelos")}
<div class="grade">{''.join(fig(p, n, d) for p, n, d in modelos)}</div>
</div></section>
''')

# EM USO
grade_ig = ''.join(crop(P[i]) for i in range(16, 4, -1))
h.append(f'''<section class="faixa f-esc" id="uso"><div class="wrap">
{cab(f"Na {k('tela')}", "O Mês 1 no perfil: foto, tiffany e verde se alternam e a grade respira.", "Em uso")}
<div class="uso">
  <div class="tel" role="img" aria-label="Simulação do perfil @fairhealth.br com 12 posts do Mês 1">
    <div class="perfil"><img src="{LOGO_C}" alt=""><div><p class="user">fairhealth.br</p><p style="font-size:13px">Cuidado dentro da empresa</p></div></div>
    <p class="bio"><b>fairhealth</b><br>Cuidamos antes: médicos e psicólogos dentro da empresa, com Medicina do Estilo de Vida.<br>Ecossistema @fairjob<br><span class="lk">fairhealth.com.br</span></p>
    <div class="botoes"><span>Seguir</span><span>Mensagem</span></div>
    <div class="ig-grade">{grade_ig}</div>
  </div>
  <div class="tel" style="padding-top:12px" role="img" aria-label="Simulação de post no feed">
    <div class="post-h"><img src="{LOGO_C}" alt=""><span><b>fairhealth.br</b> e <b>fairjob</b></span></div>
    {P[14]}
    <div class="acoes">{acoes}</div>
    <p class="cap"><b>fairhealth.br</b> Líder, quando foi a última vez que você perguntou ao seu time o que é importante para eles? <span class="mais">… mais</span></p>
  </div>
</div>
<div><p class="rot" style="color:var(--tclaro)">Carrossel com fio contínuo · a linha passa de um slide para o outro e convida a arrastar</p></div>
<div class="tira">{''.join(CARR)}</div>
<div><p class="rot" style="color:var(--tclaro)">Reel · foto, faixa e número em cenas</p></div>
<div class="tira-reel">{''.join(REEL)}</div>
</div></section>
''')

# CERTO E ERRADO
ce = ''.join(f'''<div><div class="ce-par">
  <figure>{e_ab.replace('class="ab ', 'class="ab nao-ab ', 1)}<figcaption class="leg">{SELO_N} {e_txt}</figcaption></figure>
  <figure>{c_ab}<figcaption class="leg">{SELO_S} {c_txt}</figcaption></figure></div></div>''' for e_txt, e_ab, c_txt, c_ab in ERR)
h.append(f'''<section class="faixa f-gelo" id="certo-errado"><div class="wrap">
{cab(f"Certo e {k('errado')}", "Os erros mais comuns com foto e movimento.", "Certo e errado")}
<div class="ce">{ce}</div>
</div></section>
''')

# MARCA (resumo)
USADAS.update(['industria1', 'sono'])
h.append(f'''<section class="faixa f-cre" id="marca"><div class="wrap">
{cab(f"A {k('marca')} com foto", "Sobre foto, a logo vai num bloco verde. Nunca solta sobre a imagem.", "Marca")}
<div class="logos">
  <div class="lt lt-esc"><p class="rot">Círculo · sobre o verde</p><div class="alvo"><img src="{LOGO_C}" alt="Logo fairhealth em círculo" style="width:150px"></div><p class="leg">Institucional, dados, último slide.</p></div>
  <div class="lt lt-gelo"><p class="rot">Coração · momentos de pessoas</p><div class="alvo"><img src="{LOGO_H}" alt="Logo fairhealth em coração" style="width:150px"></div><p class="leg">Nunca com número.</p></div>
  <div class="lt lt-foto f-industria1"><span class="selo nao" style="align-self:flex-start">✕ Evite</span><div class="alvo"><img src="{LOGO_C}" alt="" style="width:110px"></div><p class="leg">Logo solta sobre a foto.</p></div>
  <div class="lt lt-foto f-sono" style="justify-content:flex-end"><span class="selo sim" style="align-self:flex-start;margin-bottom:auto">✓ Assim</span><div style="background:var(--verde);padding:16px;align-self:flex-start"><img src="{LOGO_C}" alt="" style="width:80px;display:block"></div><p class="leg">Num bloco verde, no canto.</p></div>
</div>
</div></section>
''')

# TIPOGRAFIA (resumo)
h.append(f'''<section class="faixa f-tif" id="tipografia"><div class="wrap">
{cab(f"Só Raleway. Um {k('destaque')}.", "Regular no texto, ExtraBold Itálico na palavra-chave. Sobre foto, sempre com faixa, folha ou duotone.", "Tipografia")}
<div class="grade" style="grid-template-columns:repeat(auto-fill,minmax(260px,1fr))">
  {fig(ab(A(96, 380, f'<p class="f-display">O que é {k("importante")} para você?</p>')), 'Display 104 + palavra-chave', '')}
  {fig(ab(PH('estresse', 0, 0, 1080, 1350, 50, 40, duo=True) + GR(400, 950) + A(96, 700, f'<p class="f-display creme">Teve um {mt("sinal")}.</p>')), 'Sobre duotone + marca-texto', '')}
  {fig(ab(PH('sono', 0, 0, 1080, 1350, 38, 50) + BX(0, 0, 1080, 420, 'tif') + A(96, 160, f'<p class="f-display">Dormir é {k("cuidado")}.</p>')), 'Sobre faixa tiffany', '')}
</div>
</div></section>
''')

# MOOD
mos = ['conversa1', 'industria2', 'sono', 'cafe', 'maos', 'oculos', 'amigos', 'comida', 'consulta', 'tenis', 'sorriso2', 'respira']
h.append(f'''<section class="faixa f-esc" id="mood"><div class="wrap">
<div class="mood"><p class="frase">Gente cuidando de {k('gente')}. Com rigor de laudo.</p>
<p class="palavras"><span>Humano</span><span>Calmo</span><span>Preciso</span><span>Vivo</span><span class="k">Antes</span></p></div>
<div class="mosaico">{''.join(foto(n) for n in mos)}</div>
</div></section>
<footer class="rodape-pg">fairhealth · identidade visual v2 · 09/10/2026 · fotos de banco Unsplash, ilustrativas · nunca nomes reais · personagens fictícias sinalizadas · números sempre com fonte</footer>
''')

pagina = '\n'.join(h)
# fotos: cada uma entra uma vez, como classe CSS
css_f = ''.join(f'.f-{n}{{background-image:url(data:image/jpeg;base64,{b64(os.path.join(FOTOS, n + ".jpg"))})}}' for n in sorted(USADAS))
pagina = pagina.replace('/*FOTOS*/', css_f)
pagina = pagina.replace(f'src="{LOGO_C}"', 'data-logo="c"').replace(f'src="{LOGO_H}"', 'data-logo="h"')
pagina += ('<script>(function(){var L={c:"' + LOGO_C + '",h:"' + LOGO_H + '"};'
           'document.querySelectorAll("img[data-logo]").forEach(function(i){i.src=L[i.dataset.logo];});})();</script>')
open(OUT, 'w').write(pagina)
print('ok', OUT, len(pagina) // 1024, 'KB', sorted(USADAS))
