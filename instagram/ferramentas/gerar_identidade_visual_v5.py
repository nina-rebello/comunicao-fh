# Gera o brand book visual da fairhealth v1.3 (instagram/marca/identidade-visual-v5.html): a v1.2 com a série
# Luz tiffany (aprovada em 09/10) e a grade mista. Base anterior: a v1.1, com o tiffany
# deixando de ser o fundo de todos os posts. Em cada linha da grade, no máximo um post com fundo tiffany;
# nos outros, fundo verde ou creme e o tiffany num detalhe.
# As peças são desenhadas em unidades da arte de 1080 px (--u) e escalam com o container.
# Uso: python3 instagram/ferramentas/gerar_identidade_visual_v5.py <logo-circulo.png> <logo-coracao.png> <saida.html> <pasta-fotos-web>
import base64
import io
import os
import sys
from PIL import Image

LOGO_C = 'data:image/png;base64,' + base64.b64encode(open(sys.argv[1], 'rb').read()).decode()
LOGO_H = 'data:image/png;base64,' + base64.b64encode(open(sys.argv[2], 'rb').read()).decode()
OUT = sys.argv[3]
FOTOS = sys.argv[4]
USADAS = set()


def PH(nome, x, y, w, h, px=50, py=50):
    USADAS.add(nome)
    return f'<div class="ph f-{nome}" style="--x:{x};--y:{y};--w:{w};--h:{h};--px:{px}%;--py:{py}%"></div>'


def k(t):
    return f'<span class="k">{t}</span>'


def A(x, y, html, w=888, cls='', style=''):
    return f'<div class="a {cls}" style="--x:{x};--y:{y};--w:{w};{style}">{html}</div>'


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


# ---------------- as peças do Mês 1 ----------------
P = {}
P[1] = ab(etq('Boas-vindas') + A(96, 420, f'<p class="f-display">Antes de qualquer exame, uma {k("conversa")}.</p>') +
          A(96, 900, '<p class="f-corpo">O cuidado que começa por uma pergunta.</p>', w=592) + rod('Reel · 30 s'),
          label='Capa de reel: Antes de qualquer exame, uma conversa')
P[2] = ab(etq('Como funciona o cuidado') + A(96, 400, f'<p class="f-display">Aqui, o cuidado começa com uma {k("pergunta")}.</p>') +
          A(96, 900, '<p class="f-corpo">Antes de exame, antes de número: o que é importante para você?</p>', w=640) + rod(),
          label='Capa de carrossel: Aqui, o cuidado começa com uma pergunta')
P[3] = ab('<div class="painel"></div>' + etq('Cuidar antes', cls='on-esc') +
          A(96, 420, f'<p class="f-display">Antes do afastamento, teve um {k("sinal")}.</p>', cls='creme') + rod('Reel · 20 s', cls='on-esc'),
          label='Capa de reel tipográfico: Antes do afastamento, teve um sinal')
P[4] = ab('<div class="folha"></div>' + etq('Na imprensa') +
          A(96, 300, f'<p class="f-titulo">O trabalho pode adoecer. Mas não é o único {k("vilão")}.</p>') +
          A(96, 720, '<p class="f-corpo">Um artigo sobre riscos psicossociais e responsabilidade compartilhada.</p>', w=640) +
          A(96, 940, '<span class="chip out">RH Pra Você · 25/09/2026</span>') + rod(),
          label='Carrossel de artigo: O trabalho pode adoecer. Mas não é o único vilão')
pil = ''.join(f'<div class="pil">{icone(n)}<span class="f-leg">{n}</span></div>' for n in ICON)
P[5] = ab(etq('Pilares da MEV') + A(96, 280, f'<p class="f-display">Medicina do Estilo de Vida em 1 {k("minuto")}.</p>') +
          A(96, 780, f'<div class="pils">{pil}</div>') + rod('Reel · 60 s'),
          label='Capa de reel: Medicina do Estilo de Vida em 1 minuto, com os 6 pilares')
P[6] = ab('<div class="split"></div>' + etq('O que acreditamos') +
          A(96, 330, f'<p class="f-titulo">Não é {k("benefício")}.</p>', w=400) +
          A(600, 330, f'<p class="f-titulo">É infraestrutura de {k("cuidado")}.</p>', w=400, cls='creme') +
          A(96, 760, '<div class="lista"><p>Usa se lembrar</p><p>Espera o problema</p><p>É um cartão</p></div>', w=380) +
          A(600, 760, '<div class="lista on-esc"><p>Está lá todo dia</p><p>Começa antes</p><p>Gente acompanhando</p></div>', w=380) +
          '<div class="rod meia"><span>@fairhealth.br</span></div><div class="rod meia-d"><span class="arr">Arraste ' + SETA + '</span></div>',
          label='Comparativo: Não é benefício. É infraestrutura de cuidado')
barras = ''.join(f'<div class="barra"><span class="f-leg">{n}</span><span class="trilho"><span style="width:{v}%"></span></span></div>'
                 for n, v in (('Adesão', 82), ('Retornos', 68), ('Procura por sono', 44)))
P[7] = ab(etq('Entregas para o RH') + A(96, 220, f'<p class="f-titulo">O que o RH {k("vê")}. E o que não vê.</p>') +
          A(96, 500, f'<div class="card"><p class="f-nota card-head">Painel do Escritório do Cuidado · dados ilustrativos</p>{barras}'
                     '<p class="f-leg cad">Conversas individuais: ficam no atendimento</p></div>') + rod('Reel · 30 s'),
          label='Capa de reel: O que o RH vê, com painel de dados ilustrativos')
itens = ''.join(f'<div class="chk"><span class="box"></span><span class="f-corpo">{t}</span></div>'
                for t in ('Dormir 30 min mais cedo', 'Caminhar 10 min no almoço', 'Conversa quinzenal com a psicóloga'))
P[8] = ab(etq('Como funciona o cuidado · 2/3') + A(96, 200, f'<p class="f-display">O plano é {k("seu")}.</p>') +
          A(96, 400, f'<div class="card"><p class="f-nota card-head">Plano de cuidado · Clara, 41 anos</p>'
                     f'<p class="f-sub fala">“Quero voltar a ter energia para brincar com meu filho.”</p>{itens}</div>') +
          A(96, 1130, '<p class="f-nota aviso">História ilustrativa. Personagem fictícia.</p>') + rod(),
          label='Carrossel com card de plano de uma personagem fictícia')
P[9] = ab(etq('Da intenção à evidência') +
          A(96, 300, f'<p class="f-titulo">Ninguém volta a um lugar onde não se sentiu {k("cuidado")}.</p>') +
          A(96, 640, '<p class="f-num">8 em cada 10</p><p class="f-sub">voltaram para mais de um atendimento.</p>'
                     '<p class="f-leg gap32">A adesão chegou a 98%.</p><p class="f-nota gap48">Fonte: Escritório do Cuidado numa indústria, 1º sem. 2026</p>') + rod('Reel · 20 s'),
          label='Número suave: 8 em cada 10 voltaram para mais de um atendimento')
sono = ''.join(f'<div class="col-b"><span style="height:{h}%"></span><span class="f-nota">{s}</span></div>'
               for h, s in ((61, 'S1'), (66, 'S2'), (72, 'S3'), (78, 'S4')))
P[10] = ab(etq('Como funciona o cuidado · 3/3') + A(96, 260, f'<p class="f-display">O cuidado não para quando a consulta {k("acaba")}.</p>') +
           A(96, 800, f'<div class="card baixo"><p class="f-nota card-head">Sono nas últimas 4 semanas · dados ilustrativos</p><div class="cols">{sono}</div></div>') + rod(),
           label='Carrossel de acompanhamento com gráfico ilustrativo de sono')
P[11] = ab(etq('Origem') + A(96, 260, f'<p class="f-display">Tudo começou num {k("hospital")}.</p>') +
           A(96, 760, '<div class="linha-t"><p class="f-titulo"><span class="k">2009</span></p><p class="f-corpo">Escritório do Paciente: ouvir antes de propor.</p></div>'
                      '<div class="linha-t"><p class="f-titulo"><span class="k">Hoje</span></p><p class="f-corpo">Escritório do Cuidado, dentro da empresa.</p></div>') + rod('Reel · 30 s'),
           label='Capa de reel: Tudo começou num hospital, com linha do tempo')
P[12] = ab('<div class="folha"></div>' + etq('Na imprensa') + A(96, 250, '<p class="aspas">«</p>') +
           A(96, 400, f'<p class="f-sub">Antes de perguntar apenas o que o trabalho está fazendo com a saúde mental das pessoas, deveríamos fazer uma {k("pergunta maior")}: o que a nossa forma de viver em sociedade está fazendo com a saúde mental das pessoas?</p>') +
           A(96, 1010, '<span class="fio-c"></span><p class="f-nota gap16">Do artigo “Riscos psicossociais no ambiente de trabalho e saúde”, RH Pra Você</p>') + rod('Citação'),
           label='Citação do artigo da RH Pra Você')
P[13] = ab(etq('Pilares · Sono') + A(96, 280, f'<p class="f-display">Dormir não é tempo {k("perdido")}.</p>') +
           A(96, 760, '<p class="f-num">7 a 9 h</p><p class="f-sub">por noite: a faixa saudável para adultos.</p><p class="f-nota gap48">Fonte: RAND Europe, 2016</p>') + rod('Reel · 25 s'),
           label='Capa de reel do pilar sono: 7 a 9 horas')
P[14] = ab('<div class="painel"></div>' + etq('Liderança', cls='on-esc') +
           A(96, 380, f'<p class="f-display">O que é {k("importante")} para você?</p>', cls='creme') +
           A(96, 860, '<p class="f-corpo">Uma pergunta que todo líder pode fazer. A OMS recomenda preparar as lideranças para acolher.</p><p class="f-nota gap32">Fonte: OMS, 2022</p>', w=700, cls='claro') +
           rod(cls='on-esc'), label='Capa de carrossel: O que é importante para você, para líderes')
passos = ''.join(f'<div class="passo"><span class="f-titulo k">{n}</span><span class="f-corpo">{t}</span></div>'
                 for n, t in ((1, 'Diagnóstico gratuito'), (2, 'Proposta personalizada'), (3, 'Implantação e primeiros atendimentos')))
P[15] = ab(etq('Como chega a uma empresa') + A(96, 200, f'<p class="f-titulo">Como o cuidado chega à sua {k("empresa")}.</p>') +
           A(96, 520, passos) + A(96, 1060, '<p class="f-sub">Comente <span class="k">CUIDADO</span>.</p>') + rod('Reel · 25 s'),
           label='Passos: como o cuidado chega à sua empresa')
P[16] = ab(etq('Ciência no cuidado') + A(96, 400, f'<p class="f-display">Estilo de vida também é tratamento {k("sério")}.</p>') +
           A(96, 900, '<p class="f-corpo">Um estudo que mudou a forma de cuidar.</p>', w=592) + rod(),
           label='Capa de carrossel de ciência: Estilo de vida também é tratamento sério')


# ---------------- v1.2: tiffany no detalhe ----------------
P_ORIG = dict(P)
SETA_G = '<svg viewBox="0 0 48 16" aria-hidden="true"><path d="M0 8H46M38 1l8 7-8 7" fill="none" stroke="currentColor" stroke-width="2"/></svg>'
CANTO = f'<div class="canto">{SETA_G}</div>'


def rodc(direita=''):
    return f'<div class="rod curto"><span>@fairhealth.br</span><span>{direita}</span></div>'


def etqv(t, x=96, y=96):
    return A(x, y, f'<p class="f-etq">{t}</p><span class="fio-c"></span>', w=888)


# P16 · creme com etiqueta tiffany, sublinhado e canto
P[16] = ab(A(96, 96, '<span class="chip t">Ciência no cuidado</span>') +
           A(96, 400, f'<p class="f-display">Estilo de vida também é tratamento <span class="k sub-t">sério</span>.</p>') +
           A(96, 900, '<p class="f-corpo">Um estudo que mudou a forma de cuidar.</p>', w=592) + CANTO + rodc(), 'c',
           'Capa de ciência em fundo creme com etiqueta, sublinhado e canto tiffany')
# P14 · painel verde recuado na moldura tiffany, eco da palavra-chave e recorte
eco = ''.join(A(26, y, '<p class="eco it">importante</p>') for y in (150, 286))
P[14] = ab('<div class="pn">' + A(32, 64, '<p class="f-titulo creme">O que é</p>') + eco +
           A(26, 422, '<p class="cheio it tf">importante</p>') + A(32, 584, '<p class="f-titulo creme">para você?</p>') +
           A(32, 740, '<p class="f-corpo claro">Uma pergunta que todo líder pode fazer.</p>', w=420) +
           f'<img class="logo-pn" src="{LOGO_C}" alt=""></div>' +
           '<div class="rc rc-mulher" style="--x:540;--y:640;--w:560;--h:716"></div>', '',
           'Pergunta em painel verde com eco da palavra importante em tiffany e recorte de mulher sentada')
# P13 · verde com número tiffany
P[13] = ab(etqv('Pilares · Sono') + A(96, 280, f'<p class="f-display">Dormir não é tempo {k("perdido")}.</p>') +
           A(96, 760, '<p class="f-num tf">7 a 9 h</p><p class="f-sub">por noite: a faixa saudável para adultos.</p><p class="f-nota gap48 claro">Fonte: RAND Europe, 2016</p>') + rod('Reel · 25 s'), 'v',
           'Pilar sono em fundo verde com número tiffany')
# P12 · creme com sublinhado e etiqueta tiffany
P[12] = ab(A(96, 96, '<span class="chip t">Na imprensa</span>') + A(96, 250, '<p class="aspas">«</p>') +
           A(96, 400, f'<p class="f-sub">Antes de perguntar apenas o que o trabalho está fazendo com a saúde mental das pessoas, deveríamos fazer uma <span class="k sub-t">pergunta maior</span>: o que a nossa forma de viver em sociedade está fazendo com a saúde mental das pessoas?</p>') +
           A(96, 1010, '<span class="fio-c"></span><p class="f-nota gap16">Do artigo “Riscos psicossociais no ambiente de trabalho e saúde”, RH Pra Você</p>') + rod('Citação'), 'c',
           'Citação em fundo creme com etiqueta e sublinhado tiffany')
# P9 · verde com número tiffany
P[9] = ab(etqv('Da intenção à evidência') +
          A(96, 300, f'<p class="f-titulo">Ninguém volta a um lugar onde não se sentiu {k("cuidado")}.</p>') +
          A(96, 640, '<p class="f-num tf">8 em cada 10</p><p class="f-sub">voltaram para mais de um atendimento.</p>'
                     '<p class="f-leg gap32 claro">A adesão chegou a 98%.</p><p class="f-nota gap48 claro">Fonte: Escritório do Cuidado numa indústria, 1º sem. 2026</p>') + rod('Reel · 20 s'), 'v',
          'Número suave em fundo verde com número tiffany')
# P8 · creme com etiqueta tiffany, sublinhado e canto
itens8 = ''.join(f'<div class="chk"><span class="box"></span><span class="f-corpo">{t}</span></div>'
                 for t in ('Dormir 30 min mais cedo', 'Caminhar 10 min no almoço', 'Conversa quinzenal com a psicóloga'))
P[8] = ab(A(96, 96, '<span class="chip t">Como funciona o cuidado · 2/3</span>') + A(96, 200, f'<p class="f-display">O plano é <span class="k sub-t">seu</span>.</p>') +
          A(96, 400, f'<div class="card"><p class="f-nota card-head">Plano de cuidado · Clara, 41 anos</p>'
                     f'<p class="f-sub fala">“Quero voltar a ter energia para brincar com meu filho.”</p>{itens8}</div>') +
          A(96, 1090, '<p class="f-nota aviso">História ilustrativa. Personagem fictícia.</p>', w=600) + CANTO + rodc(), 'c',
          'Carrossel do plano em fundo creme com detalhes tiffany')
# P7 · creme com barras tiffany e canto
barras7 = ''.join(f'<div class="barra"><span class="f-leg">{n}</span><span class="trilho t"><span style="width:{v}%"></span></span></div>'
                  for n, v in (('Adesão', 82), ('Retornos', 68), ('Procura por sono', 44)))
P[7] = ab(A(96, 96, '<span class="chip t">Entregas para o RH</span>') + A(96, 220, f'<p class="f-titulo">O que o RH <span class="k sub-t">vê</span>. E o que não vê.</p>') +
          A(96, 500, f'<div class="card"><p class="f-nota card-head">Painel do Escritório do Cuidado · dados ilustrativos</p>{barras7}'
                     '<p class="f-leg cad">Conversas individuais: ficam no atendimento</p></div>') + rodc('Reel · 30 s'), 'c',
          'Painel do RH em fundo creme com barras tiffany')
# P5 · verde com ícones tiffany
pil5 = ''.join(f'<div class="pil">{icone(n)}<span class="f-leg">{n}</span></div>' for n in ICON)
P[5] = ab(etqv('Pilares da MEV') + A(96, 280, f'<p class="f-display">Medicina do Estilo de Vida em 1 {k("minuto")}.</p>') +
          A(96, 780, f'<div class="pils">{pil5}</div>') + rod('Reel · 60 s'), 'v',
          'Reel da MEV em fundo verde com ícones tiffany')


# ---------------- v1.3: Luz tiffany e eco, a partir dos PNG renderizados ----------------
PNG_DIR = 'instagram/posts/exploracoes/png'
PNGS = {}


def abimg(nome, label=''):
    PNGS[nome] = True
    aria = f' role="img" aria-label="{label}"' if label else ''
    return f'<div class="ab abimg pi-{nome}"{aria}></div>'


LUZ = [
    (abimg('luz-1-tarde', 'O cuidado chega tarde, com feixes de luz tiffany'), 'Feixes de luz', 'Manifestos e dores. Título embaixo, etiqueta em contorno no topo.'),
    (abimg('luz-2-diagrama', 'O que o exame não vê, com os 6 pilares num círculo tracejado'), 'Diagrama', 'Círculo tracejado com pontos tiffany. Só quando explica algo.'),
    (abimg('luz-3-plano', 'Um plano feito para você, com etiquetas em contorno'), 'Etiquetas em contorno', 'Listas curtas em etiquetas arredondadas, só com contorno.'),
    (abimg('luz-4-sono', 'Dormir não é tempo perdido, foto escurecida com luz tiffany'), 'Foto com luz', 'Foto escurecida, tom tiffany e grão. Única série com foto inteira.'),
]

# os seis jeitos de pôr o tiffany no detalhe
DET = [
    (ab(etqv('Liderança') + A(96, 420, f'<p class="f-display">O que é {k("importante")} para você?</p>'), 'v'), 'Palavra-chave tiffany', 'Sobre o verde (6,4:1).'),
    (ab(A(96, 420, '<p class="f-num tf" style="font-size:calc(170*var(--u));line-height:calc(170*var(--u))">8 em cada 10</p><p class="f-sub">voltaram para mais de um atendimento.</p>'), 'v'), 'Número tiffany', 'Sobre o verde, com a fonte embaixo.'),
    (ab(A(96, 96, '<span class="chip t">Ciência no cuidado</span>') + A(96, 420, f'<p class="f-display">Um estudo, uma {k("ideia")}.</p>'), 'c'), 'Etiqueta tiffany', 'Chip tiffany com texto verde.'),
    (ab(A(96, 420, f'<p class="f-display">Arraste para ver {k("como")}.</p>') + CANTO + rodc(), 'c'), 'Canto tiffany', 'Quadrado no canto, com a seta de arrastar.'),
    (ab(A(96, 420, f'<p class="f-display">O plano é <span class="k sub-t">seu</span>.</p>'), 'c'), 'Sublinhado tiffany', 'Só na palavra-chave, sobre o creme.'),
    (ab('<div class="pn"></div>' + A(96, 420, '<p class="f-display creme">Painel na moldura.</p>'), ''), 'Moldura tiffany', 'Painel recuado: o tiffany vira a borda.'),
]

# peças de modelo que não estão no mês
CIENCIA3 = ab('<div class="folha"></div>' + etq('Ciência no cuidado · 3/6') +
              A(96, 280, f'<p class="f-titulo">Quem mudou a {k("rotina")}</p>') +
              A(96, 420, '<p class="f-num">58% menos</p><p class="f-sub">casos novos de diabetes tipo 2 do que o grupo placebo.</p><p class="f-leg gap32">Com medicamento, a redução foi de 31%.</p>') +
              PH('comida', 96, 790, 888, 220, 50, 50) +
              A(96, 1040, '<div class="ref"><p class="f-nota">Diabetes Prevention Program. N Engl J Med. 2002;346(6):393-403. Adultos com risco aumentado, 2,8 anos.</p></div>') + rod('3/6'),
              label='Slide de resultado de estudo, em folha creme com faixa de foto e referência')
PILAR = ab(etq('Pilares da MEV · 3/6') + A(96, 250, icone('Sono', 'ic-g')) +
           A(96, 420, f'<p class="f-display">Sono {k("é cuidado")}.</p>') +
           A(96, 660, '<p class="f-corpo">Dormir bem entra no plano a partir da sua rotina real, não de uma regra pronta.</p>', w=640) +
           A(96, 940, '<span class="chip">Medicina do Estilo de Vida</span>') + rod(),
           label='Modelo de pilar: Sono é cuidado')

# carrossel completo (P2)
CARR = [
    P[2],
    ab('<div class="folha"></div>' + etq('Como funciona · 2/6') + A(96, 300, f'<p class="f-display">Fica {k("dentro")} da empresa.</p>') +
       A(96, 760, '<p class="f-corpo">Perto de onde você já está, com médicos e psicólogos.</p>', w=640) + rod('2/6')),
    ab(etq('Como funciona · 3/6') + A(96, 300, '<p class="f-etq">Passo 1</p>') + A(96, 380, f'<p class="f-display">A gente te {k("conhece")}.</p>') +
       A(96, 820, '<p class="f-corpo">Sua rotina, seu trabalho, o que anda pesando.</p>', w=640) + rod('3/6')),
    ab(etq('Como funciona · 4/6') + A(96, 200, f'<p class="f-titulo">O que é {k("importante")} para você?</p>') +
       A(96, 520, '<div class="card"><p class="f-nota card-head">Conversa · Escritório do Cuidado</p><p class="balao pro f-corpo">O que é importante para você hoje?</p>'
                  '<p class="balao pessoa f-corpo">Dormir melhor e ter energia no fim do dia.</p></div>') + rod('4/6')),
    ab('<div class="painel"></div>' + etq('Como funciona · 5/6', cls='on-esc') +
       A(96, 420, f'<p class="f-display">O que você conta fica entre você e quem {k("cuida")}.</p>', cls='creme') + rod('5/6', cls='on-esc')),
    ab(etq('Como funciona · 6/6') + A(96, 240, f'<p class="f-display">E para você, o que é {k("importante")}?</p>') +
       A(96, 640, '<div class="card fino"><p class="f-leg">Comente aqui…</p></div>') +
       f'<div class="faixa-logo"><img src="{LOGO_C}" alt=""></div>'),
]

# reel tipográfico 9:16
REEL = [
    ab(A(96, 760, f'<p class="f-titulo">Antes do afastamento, teve um {k("atestado")}.</p>', w=844), 'reel', 'Cena 1'),
    ab(A(96, 760, f'<p class="f-titulo">Antes do atestado, uma semana {k("pesada")}.</p>', w=844), 'reel', 'Cena 2'),
    ab(A(96, 620, '<p class="f-corpo">Em 2024, no Brasil:</p><p class="f-num gap24">mais de 470 mil</p><p class="f-sub">licenças por saúde mental. Cada uma teve um <span class="k">antes</span>.</p><p class="f-nota gap48">Fonte: Ministério da Previdência Social</p>', w=844), 'reel', 'Cena com número'),
    ab('<div class="painel"></div>' + A(96, 760, f'<p class="f-display">Cuidar {k("antes")}.</p>', w=844, cls='creme') +
       f'<img class="logo-reel" src="{LOGO_C}" alt="">', 'reel', 'Cena final com logo'),
]

# ---------------- certo e errado ----------------
ERR = [
    ('Texto branco some no tiffany (1,9:1).',
     ab(A(96, 420, f'<p class="f-display branco">O que é {k("importante")} para você?</p>')),
     'Texto sempre em verde-autoridade.',
     ab(A(96, 420, f'<p class="f-display">O que é {k("importante")} para você?</p>'))),
    ('Três destaques não destacam nada.',
     ab(A(96, 380, f'<p class="f-titulo">{k("Como")} o {k("cuidado")} chega à {k("sua empresa")}.</p>')),
     'Uma palavra-chave por título.',
     ab(A(96, 380, f'<p class="f-titulo">Como o cuidado chega à sua {k("empresa")}.</p>'))),
    ('Número como alarme.',
     ab(A(96, 300, '<p class="alarme">↑ 472.328</p><p class="f-titulo alarme-t">RECORDE de afastamentos!!</p>')),
     'Cuidado primeiro, número depois, com fonte.',
     ab(A(96, 300, f'<p class="f-titulo">Cada licença teve um {k("antes")}.</p>') +
        A(96, 620, '<p class="f-num">mais de 470 mil</p><p class="f-sub">licenças por saúde mental em 2024.</p><p class="f-nota gap48">Fonte: Ministério da Previdência Social</p>'))),
    ('Amarelo, bolas decorativas, pílula e emoji.',
     ab('<span class="bola b1"></span><span class="bola b2"></span><span class="bola b3"></span>' +
        A(96, 460, '<p class="f-titulo">Cuide-se! 💚</p>') + A(96, 760, '<span class="pilula">Saiba mais</span>')),
     'Planos retos, uma ideia por peça.',
     P[6]),
]

# ---------------- HTML ----------------
CSS = r'''
/* Brand book em faixas de cor; as próprias peças são as ilustrações. */
:root {
  --tif: #96C5BD; --verde: #1F3A36; --creme: #F0F0E9; --tesc: #5FA89A; --vlogo: #2F6B64;
  --tclaro: #BFE0D9; --gelo: #F6F8F7; --tinta: #141B1B; --ui: #FFFFFF; --ui-linha: #DBDBDB; --ui-texto: #262626;
  --erro: #A3342C; --amarelo: #F2C94C; --branco: #FFFFFF;
  --f: "Raleway", "Helvetica Neue", Arial, sans-serif;
  color-scheme: light;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--gelo); color: var(--verde); font-family: var(--f); font-size: 16px; line-height: 1.5; }
p { margin: 0; }
.k { font-weight: 800; font-style: italic; }
a { color: inherit; }
:focus-visible { outline: 3px solid var(--vlogo); outline-offset: 2px; }

/* navegação */
.nav { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 10; background: var(--verde); color: var(--creme); }
.nav-in { display: flex; align-items: center; gap: 24px; max-width: 1240px; margin: 0 auto; padding: 10px 24px; overflow-x: auto; scrollbar-width: none; }
.nav img { width: 32px; height: 32px; flex: none; }
.nav a { text-decoration: none; font-size: 12px; letter-spacing: .16em; text-transform: uppercase; white-space: nowrap; color: var(--tclaro); }
.nav a:hover { color: var(--creme); }

/* faixas */
.faixa { padding-block: 72px; padding-inline: 24px; }
.wrap { max-width: 1240px; margin: 0 auto; display: grid; gap: 40px; }
.f-tif { background: var(--tif); } .f-cre { background: var(--creme); } .f-gelo { background: var(--gelo); }
.f-esc { background: var(--verde); color: var(--creme); }
.cab { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 24px; align-items: end; border-top: 2px solid currentColor; padding-top: 16px; }
.cab h2 { margin: 0; font-weight: 400; font-size: clamp(36px, 6vw, 72px); line-height: 1; letter-spacing: -0.01em; text-wrap: balance; }
.cab > p { font-size: 16px; max-width: 46ch; justify-self: end; }
.rot { font-size: 11px; letter-spacing: .2em; text-transform: uppercase; }
.leg { font-size: 13px; line-height: 18px; margin-top: 10px; }
.leg b { font-weight: 800; }

/* hero */
.hero { background: var(--tif); padding-block: 56px 72px; padding-inline: 24px; }
.hero-in { max-width: 1240px; margin: 0 auto; display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 48px; align-items: end; }
.hero h1 { margin: 0; font-weight: 400; font-size: clamp(56px, 10vw, 128px); line-height: .9; letter-spacing: -0.02em; }
.hero .sub { font-size: clamp(22px, 2.6vw, 34px); line-height: 1.15; margin-top: 24px; text-wrap: balance; }
.hero .meta { margin-top: 32px; display: grid; gap: 6px; }
.hero-pecas { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; align-items: end; }
.hero-pecas > :nth-child(2) { transform: translateY(-32px); }

/* artboards: 1 unidade = 1 px da arte de 1080 */
.ab { container-type: inline-size; position: relative; width: 100%; max-width: 100%; aspect-ratio: 4 / 5; overflow: hidden; background: var(--tif); color: var(--verde); box-shadow: 0 12px 28px rgba(20, 27, 27, .14); }
.f-tif .ab, .hero .ab { outline: 1px solid rgba(31, 58, 54, .22); }
.f-esc .ab { outline: 1px solid rgba(191, 224, 217, .45); box-shadow: none; }
.ig-grade .ab, .tel .ab { box-shadow: none; outline: 0; }
.ab.reel { aspect-ratio: 9 / 16; }
.in { position: absolute; inset: 0; --u: calc(100cqw / 1080); font-family: var(--f); font-variant-numeric: lining-nums; }
.a { position: absolute; left: calc(var(--x) * var(--u)); top: calc(var(--y) * var(--u)); width: calc(var(--w) * var(--u)); }
.f-display { font-size: calc(104 * var(--u)); line-height: calc(104 * var(--u)); letter-spacing: -0.01em; }
.f-titulo { font-size: calc(72 * var(--u)); line-height: calc(80 * var(--u)); letter-spacing: -0.005em; }
.f-sub { font-size: calc(44 * var(--u)); line-height: calc(56 * var(--u)); }
.f-corpo { font-size: calc(34 * var(--u)); line-height: calc(46 * var(--u)); }
.f-leg { font-size: calc(28 * var(--u)); line-height: calc(38 * var(--u)); }
.f-etq { font-size: calc(26 * var(--u)); line-height: calc(32 * var(--u)); letter-spacing: .2em; text-transform: uppercase; }
.f-nota { font-size: calc(24 * var(--u)); line-height: calc(32 * var(--u)); }
.f-num { font-size: calc(120 * var(--u)); line-height: calc(128 * var(--u)); letter-spacing: -0.01em; }
.ph { position: absolute; left: calc(var(--x) * var(--u)); top: calc(var(--y) * var(--u)); width: calc(var(--w) * var(--u)); height: calc(var(--h) * var(--u)); background-size: cover; background-position: var(--px) var(--py); }
.gap16 { margin-top: calc(16 * var(--u)); } .gap24 { margin-top: calc(24 * var(--u)); } .gap32 { margin-top: calc(32 * var(--u)); } .gap48 { margin-top: calc(48 * var(--u)); }
.fio-c { display: block; width: calc(64 * var(--u)); height: calc(4 * var(--u)); background: currentColor; margin-top: calc(16 * var(--u)); }
.creme { color: var(--creme); } .claro { color: var(--tclaro); } .on-esc { color: var(--tclaro); }
.rod { position: absolute; left: calc(96 * var(--u)); right: calc(96 * var(--u)); top: calc(1206 * var(--u)); height: calc(48 * var(--u)); border-top: calc(2 * var(--u)) solid currentColor; display: flex; justify-content: space-between; align-items: flex-end; font-size: calc(24 * var(--u)); line-height: calc(32 * var(--u)); }
.rod.on-esc { color: var(--creme); }
.rod.meia { right: calc(540 * var(--u)); padding-right: calc(48 * var(--u)); }
.rod.meia-d { left: calc(600 * var(--u)); color: var(--creme); justify-content: flex-end; }
.arr { display: inline-flex; align-items: center; gap: calc(16 * var(--u)); }
.seta { width: calc(48 * var(--u)); height: calc(16 * var(--u)); }
.folha { position: absolute; inset: calc(48 * var(--u)); background: var(--creme); }
.painel { position: absolute; inset: calc(48 * var(--u)); background: var(--verde); }
.split { position: absolute; left: calc(540 * var(--u)); top: 0; right: 0; bottom: 0; background: var(--verde); }
.chip { display: inline-flex; align-items: center; height: calc(64 * var(--u)); padding: 0 calc(24 * var(--u)); border-radius: calc(8 * var(--u)); background: var(--creme); font-size: calc(28 * var(--u)); }
.chip.out { background: transparent; border: calc(2 * var(--u)) solid var(--vlogo); color: var(--vlogo); }
.card { background: var(--gelo); border-radius: calc(16 * var(--u)); padding: calc(48 * var(--u)); box-shadow: 0 calc(24 * var(--u)) calc(48 * var(--u)) rgba(20, 27, 27, .18); }
.card.fino { padding: calc(32 * var(--u)) calc(40 * var(--u)); color: var(--vlogo); }
.card-head { color: var(--vlogo); padding-bottom: calc(24 * var(--u)); border-bottom: calc(2 * var(--u)) solid var(--verde); margin-bottom: calc(32 * var(--u)); }
.fala { margin-bottom: calc(32 * var(--u)); }
.chk { display: flex; align-items: center; gap: calc(24 * var(--u)); padding: calc(12 * var(--u)) 0; }
.box { width: calc(40 * var(--u)); height: calc(40 * var(--u)); border: calc(3 * var(--u)) solid var(--verde); border-radius: calc(6 * var(--u)); flex: none; }
.barra { display: grid; grid-template-columns: calc(300 * var(--u)) 1fr; align-items: center; gap: calc(24 * var(--u)); padding: calc(14 * var(--u)) 0; }
.trilho { display: block; height: calc(24 * var(--u)); background: var(--tclaro); }
.trilho span { display: block; height: 100%; background: var(--verde); }
.cad { margin-top: calc(28 * var(--u)); padding-top: calc(24 * var(--u)); border-top: calc(2 * var(--u)) solid var(--tclaro); color: var(--vlogo); }
.cols { display: flex; align-items: flex-end; gap: calc(48 * var(--u)); height: calc(150 * var(--u)); }
.col-b { display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: calc(8 * var(--u)); height: 100%; width: calc(120 * var(--u)); }
.col-b span:first-child { width: 100%; background: var(--verde); }
.linha-t { display: grid; grid-template-columns: calc(232 * var(--u)) 1fr; gap: calc(24 * var(--u)); align-items: baseline; border-top: calc(2 * var(--u)) solid var(--verde); padding: calc(24 * var(--u)) 0; }
.lista p { font-size: calc(34 * var(--u)); line-height: calc(46 * var(--u)); padding: calc(20 * var(--u)) 0; border-top: calc(2 * var(--u)) solid var(--verde); }
.lista.on-esc p { border-color: var(--tclaro); color: var(--creme); }
.passo { display: grid; grid-template-columns: calc(128 * var(--u)) 1fr; align-items: center; min-height: calc(160 * var(--u)); border-top: calc(2 * var(--u)) solid var(--verde); }
.passo:last-child { border-bottom: calc(2 * var(--u)) solid var(--verde); }
.pils { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: calc(32 * var(--u)) calc(24 * var(--u)); }
.pil { display: flex; align-items: center; gap: calc(16 * var(--u)); }
.ic { width: calc(64 * var(--u)); height: calc(64 * var(--u)); flex: none; fill: none; stroke: var(--verde); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
.ic-g { width: calc(112 * var(--u)); height: calc(112 * var(--u)); fill: none; stroke: var(--verde); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.aspas { font-size: calc(144 * var(--u)); line-height: calc(120 * var(--u)); font-weight: 800; font-style: italic; color: var(--vlogo); }
.ref { border-top: calc(2 * var(--u)) solid var(--verde); padding-top: calc(16 * var(--u)); }
.aviso { color: var(--vlogo); }
.balao { padding: calc(24 * var(--u)) calc(32 * var(--u)); border-radius: calc(16 * var(--u)); max-width: 80%; margin-bottom: calc(24 * var(--u)); }
.balao.pro { background: var(--verde); color: var(--creme); }
.balao.pessoa { background: var(--creme); margin-left: auto; }
.faixa-logo { position: absolute; left: 0; right: 0; top: calc(1000 * var(--u)); bottom: 0; background: var(--verde); display: flex; align-items: center; padding-left: calc(96 * var(--u)); }
.faixa-logo img { width: calc(160 * var(--u)); height: auto; }
.logo-reel { position: absolute; left: calc(96 * var(--u)); top: calc(1380 * var(--u)); width: calc(160 * var(--u)); height: auto; }
.branco { color: var(--branco); }
.alarme { font-size: calc(220 * var(--u)); line-height: calc(200 * var(--u)); font-weight: 800; color: var(--erro); letter-spacing: -0.02em; }
.alarme-t { color: var(--erro); font-weight: 800; margin-top: calc(32 * var(--u)); }
.bola { position: absolute; border-radius: 50%; background: var(--amarelo); }
.b1 { width: calc(360 * var(--u)); height: calc(360 * var(--u)); left: calc(700 * var(--u)); top: calc(-80 * var(--u)); }
.b2 { width: calc(180 * var(--u)); height: calc(180 * var(--u)); left: calc(-40 * var(--u)); top: calc(1100 * var(--u)); background: var(--tclaro); }
.b3 { width: calc(120 * var(--u)); height: calc(120 * var(--u)); left: calc(820 * var(--u)); top: calc(980 * var(--u)); }
.pilula { display: inline-block; padding: calc(24 * var(--u)) calc(56 * var(--u)); border-radius: 999px; background: var(--amarelo); font-size: calc(34 * var(--u)); font-weight: 800; }

/* grades de exemplo */
.grade { display: grid; gap: 24px; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); }
.grade figure { margin: 0; min-width: 0; }
.modelo-nome { font-size: 15px; margin-top: 12px; } .modelo-nome b { font-weight: 800; font-style: italic; }
.par { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }
.tira { display: grid; grid-auto-flow: column; grid-auto-columns: minmax(160px, 1fr); gap: 16px; overflow-x: auto; padding-bottom: 8px; }
.tira-reel { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; max-width: 760px; }

/* marca */
.logos { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; }
.lt { min-height: 260px; display: flex; flex-direction: column; justify-content: space-between; padding: 20px; }
.lt .alvo { flex: 1; display: flex; align-items: center; justify-content: center; padding-block: 24px; }
.lt-esc { background: var(--verde); color: var(--creme); } .lt-cre { background: var(--creme); } .lt-tif { background: var(--tif); } .lt-gelo { background: var(--gelo); border: 1px solid var(--tclaro); }
.lt-2 { grid-column: span 2; }
.area { position: relative; padding: 48px; outline: 1.5px dashed var(--tclaro); outline-offset: -1px; }
.area::after { content: "½ logo"; position: absolute; top: 6px; left: 8px; font-size: 10px; letter-spacing: .15em; text-transform: uppercase; color: var(--tclaro); }
.marca-x { position: relative; }
.selo { display: inline-flex; align-items: center; gap: 6px; font-size: 11px; letter-spacing: .14em; text-transform: uppercase; font-weight: 800; padding: 4px 8px; }
.selo.sim { background: var(--verde); color: var(--creme); } .selo.nao { background: var(--erro); color: var(--branco); }
.sobre-selo { position: absolute; top: 10px; left: 10px; z-index: 2; }

/* cor */
.prop { display: flex; height: 320px; }
.prop > div { padding: 16px; display: flex; flex-direction: column; justify-content: space-between; min-width: 0; }
.prop .nm { font-size: clamp(18px, 2.4vw, 32px); line-height: 1.05; }
.prop .hx { font-size: 12px; letter-spacing: .1em; text-transform: uppercase; }
.apoio { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px; }
.sw { height: 120px; padding: 12px; display: flex; flex-direction: column; justify-content: flex-end; font-size: 12px; line-height: 16px; }
.combos { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px; }
.cb { position: relative; height: 150px; padding: 14px; display: flex; flex-direction: column; justify-content: space-between; }
.cb .aa { font-size: 44px; line-height: 1; }
.cb .rz { font-size: 12px; }

/* tipografia */
.esp { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 24px; }
.esp .big { font-size: clamp(120px, 22vw, 280px); line-height: .85; letter-spacing: -0.03em; }
.abc { font-size: clamp(20px, 2.6vw, 30px); line-height: 1.35; overflow-wrap: anywhere; }
.escala { display: grid; border-top: 2px solid var(--verde); }
.escala > div { display: grid; grid-template-columns: 150px minmax(0, 1fr); gap: 16px; align-items: baseline; padding-block: 14px; border-bottom: 1px solid var(--tesc); }
.escala .nm { font-size: 11px; letter-spacing: .16em; text-transform: uppercase; }
.escala .nm small { display: block; letter-spacing: .04em; text-transform: none; font-size: 12px; color: var(--vlogo); }
.escala .s { min-width: 0; overflow-wrap: anywhere; }

/* elementos */
.elems { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; }
.el { background: var(--tif); padding: 24px; min-height: 220px; display: flex; flex-direction: column; justify-content: space-between; gap: 20px; min-width: 0; }
.el.esc { background: var(--verde); color: var(--creme); }
.el .demo { flex: 1; display: flex; align-items: center; }
.el .demo > * { width: 100%; }
.mini-ab { container-type: inline-size; position: relative; width: 100%; }
.mini-ab .in { position: relative; inset: auto; --u: calc(100cqw / 888); }
.icones { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px; }
.icones div { display: grid; justify-items: center; gap: 8px; text-align: center; font-size: 11px; line-height: 14px; }
.icones svg { width: 40px; height: 40px; fill: none; stroke: var(--verde); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }

/* grid */
.grid-demo { display: grid; grid-template-columns: minmax(0, 4fr) minmax(0, 3fr) minmax(0, 4fr); gap: 32px; align-items: start; }
.ov { position: absolute; inset: 0; }
.ov .m { position: absolute; background: rgba(163, 52, 44, .14); }
.ov .c { position: absolute; top: calc(96 * var(--u)); bottom: calc(96 * var(--u)); width: calc(128 * var(--u)); background: rgba(31, 58, 54, .12); }
.ov .t { position: absolute; font-size: calc(26 * var(--u)); letter-spacing: .1em; text-transform: uppercase; color: var(--erro); }
.ov .seg { position: absolute; left: calc(96 * var(--u)); right: calc(140 * var(--u)); top: calc(220 * var(--u)); bottom: calc(420 * var(--u)); outline: calc(4 * var(--u)) dashed var(--verde); }
.ov .ui { position: absolute; background: rgba(20, 27, 27, .28); }
.crop3x4 { position: relative; aspect-ratio: 3 / 4; overflow: hidden; outline: 2px solid var(--verde); max-width: 100%; }
.crop3x4 .ab { position: absolute; top: 0; left: -3.333%; width: 106.667%; max-width: none; }

/* em uso: perfil e post */
.uso { display: grid; grid-template-columns: minmax(0, 420px) minmax(0, 420px); gap: 40px; justify-content: center; align-items: start; }
.tel { background: var(--ui); color: var(--ui-texto); border-radius: 28px; padding: 16px 0 0; box-shadow: 0 30px 60px rgba(0, 0, 0, .28); overflow: hidden; }
.perfil { display: grid; grid-template-columns: 76px 1fr; gap: 16px; align-items: center; padding: 8px 16px; }
.perfil img { width: 76px; height: 76px; border-radius: 50%; }
.perfil .user { font-weight: 800; font-size: 16px; }
.bio { padding: 4px 16px 12px; font-size: 13px; line-height: 18px; }
.bio b { font-weight: 800; } .bio .lk { color: #00376B; }
.botoes { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; padding: 0 16px 12px; }
.botoes span { background: #EFEFEF; border-radius: 8px; text-align: center; font-size: 13px; font-weight: 800; padding: 7px 0; }
.ig-grade { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2px; border-top: 1px solid var(--ui-linha); }
.ig-grade .crop3x4 { outline: 0; }
.post-h { display: flex; align-items: center; gap: 10px; padding: 0 12px 12px; font-size: 13px; }
.post-h img { width: 32px; height: 32px; border-radius: 50%; }
.post-h b { font-weight: 800; }
.acoes { display: flex; gap: 16px; padding: 12px; }
.acoes svg { width: 24px; height: 24px; fill: none; stroke: var(--ui-texto); stroke-width: 1.8; stroke-linejoin: round; stroke-linecap: round; }
.acoes .salvar { margin-left: auto; }
.cap { padding: 0 12px 16px; font-size: 13px; line-height: 18px; }
.cap b { font-weight: 800; } .cap .mais { color: #737373; }

/* certo e errado */
.ce { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 32px 40px; }
.ce-par { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.ce-par figure { margin: 0; position: relative; min-width: 0; }
.ce-par .nao-ab, .grade .nao-ab { outline: 4px solid var(--erro); outline-offset: -4px; }

/* mood */
.mood { display: grid; grid-template-columns: minmax(0, 3fr) minmax(0, 2fr); gap: 40px; align-items: end; }
.mood .frase { font-size: clamp(44px, 7vw, 96px); line-height: .95; letter-spacing: -0.02em; text-wrap: balance; }
.palavras { display: flex; flex-wrap: wrap; gap: 6px 22px; font-size: clamp(22px, 3vw, 34px); color: var(--tclaro); }
.palavras .k { color: var(--creme); }
.refs { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 0; border-top: 1px solid var(--tclaro); }
.refs div { padding: 16px 16px 0 0; font-size: 14px; color: var(--tclaro); }
.refs div b { display: block; font-weight: 400; color: var(--creme); font-size: 20px; margin-bottom: 4px; }
.rodape-pg { padding: 24px; text-align: center; font-size: 12px; background: var(--verde); color: var(--tclaro); }

@media (max-width: 900px) {
  .hero-in, .mood, .esp, .grid-demo, .cab { grid-template-columns: minmax(0, 1fr); }
  .cab > p { justify-self: start; }
  .logos, .elems { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .combos { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .apoio { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .ce, .uso { grid-template-columns: minmax(0, 1fr); }
  .refs { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 560px) {
  .faixa { padding-block: 48px; padding-inline: 16px; }
  .hero { padding-inline: 16px; }
  .logos, .elems { grid-template-columns: minmax(0, 1fr); }
  .lt-2 { grid-column: auto; }
  .prop { height: 220px; } .prop .hx { display: none; }
  .tira-reel { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .escala > div { grid-template-columns: minmax(0, 1fr); gap: 4px; }
  .grade { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; }
}
@media (prefers-reduced-motion: no-preference) {
  .nav a { transition: color .15s; }
}
'''


CSS += '\n/* v1.3: Luz tiffany */\n.f-noite { background: #0D1816; color: var(--creme); }\n.f-noite .rot, .f-noite .leg { color: var(--tclaro); }\n.abimg { background-size: cover; background-position: center; }\n.luz { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 24px; }\n.luz figure { margin: 0; min-width: 0; }\n.regras { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; border-top: 1px solid var(--tesc); padding-top: 24px; }\n.regras p { font-size: 15px; line-height: 22px; color: var(--tclaro); }\n.regras b { display: block; color: var(--creme); font-weight: 400; font-size: 20px; margin-bottom: 4px; }\n@media (max-width: 900px) { .luz { grid-template-columns: repeat(2, minmax(0, 1fr)); } .regras { grid-template-columns: minmax(0, 1fr); } }\n'
CSS += '\n/* v1.2: fundos verde e creme, tiffany no detalhe */\n.ab.v { background: var(--verde); color: var(--creme); }\n.ab.v .k { color: var(--tif); }\n.ab.v .fio-c { background: var(--tif); }\n.ab.v .f-etq { color: var(--tif); }\n.ab.v .rod { color: var(--tclaro); }\n.ab.v .ic { stroke: var(--tif); }\n.ab.c { background: var(--creme); }\n.tf { color: var(--tif); }\n.chip.t { background: var(--tif); color: var(--verde); font-size: calc(26 * var(--u)); letter-spacing: .14em; text-transform: uppercase; }\n.sub-t { text-decoration: underline; text-decoration-color: var(--tif); text-decoration-thickness: calc(14 * var(--u)); text-underline-offset: calc(8 * var(--u)); text-decoration-skip-ink: none; }\n.canto { position: absolute; right: 0; bottom: 0; width: calc(216 * var(--u)); height: calc(216 * var(--u)); background: var(--tif); color: var(--verde); display: flex; align-items: center; justify-content: center; }\n.canto svg { width: calc(96 * var(--u)); height: calc(32 * var(--u)); }\n.rod.curto { right: calc(264 * var(--u)); }\n.trilho.t { background: var(--tif); }\n.pn { position: absolute; left: calc(64 * var(--u)); top: calc(64 * var(--u)); width: calc(952 * var(--u)); height: calc(1116 * var(--u)); background: var(--verde); overflow: hidden; }\n.eco, .cheio { font-size: calc(150 * var(--u)); line-height: calc(136 * var(--u)); font-weight: 800; letter-spacing: -0.02em; white-space: nowrap; }\n.eco { color: transparent; -webkit-text-stroke: calc(2.5 * var(--u)) var(--tif); opacity: .7; }\n.it { font-style: italic; }\n.logo-pn { position: absolute; left: calc(32 * var(--u)); top: calc(980 * var(--u)); width: calc(96 * var(--u)); height: auto; }\n.rc { position: absolute; left: calc(var(--x) * var(--u)); top: calc(var(--y) * var(--u)); width: calc(var(--w) * var(--u)); height: calc(var(--h) * var(--u)); background-size: contain; background-repeat: no-repeat; background-position: bottom center; }\n.det { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 16px; }\n.det figure { margin: 0; min-width: 0; }\n.antes-depois { display: grid; grid-template-columns: repeat(2, minmax(0, 360px)); gap: 40px; justify-content: center; }\n.antes-depois .ig-grade { border: 0; }\n.antes-depois .rot { margin-bottom: 10px; color: var(--tclaro); }\n@media (max-width: 900px) { .det { grid-template-columns: repeat(3, minmax(0, 1fr)); } }\n@media (max-width: 560px) { .det { grid-template-columns: repeat(2, minmax(0, 1fr)); } .antes-depois { grid-template-columns: minmax(0, 1fr); } }\n'

def fig(ab_html, nome, desc=''):
    return f'<figure>{ab_html}<figcaption class="modelo-nome">{nome}{"<br><span class=leg>" + desc + "</span>" if desc else ""}</figcaption></figure>'


def cab(titulo, sub, eyebrow):
    return f'<div class="cab"><div><p class="rot">{eyebrow}</p><h2>{titulo}</h2></div><p>{sub}</p></div>'


def crop(p):
    return f'<div class="crop3x4">{p}</div>'


SELO_S = '<span class="selo sim">✓ Assim</span>'
SELO_N = '<span class="selo nao">✕ Evite</span>'

ICON_UI = {
    'curtir': '<path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/>',
    'comentar': '<path d="M20 12a8 8 0 1 1-3.3-6.5A8 8 0 0 1 20 12l1 5-5-1.2"/>',
    'enviar': '<path d="M21 3L3 10l7 3 3 7 8-17z"/><path d="M10 13l11-10"/>',
    'salvar': '<path d="M6 3h12v18l-6-5-6 5z"/>',
}
acoes = ''.join(f'<svg class="{"salvar" if n == "salvar" else ""}" viewBox="0 0 24 24" aria-hidden="true">{d}</svg>' for n, d in ICON_UI.items())

html = []
html.append(f'''<meta charset="utf-8">
<title>Identidade Visual fairhealth</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,400;0,800;1,400;1,800&display=swap">
<style>{CSS}</style>
<style>/*FOTOS*/</style>
<nav class="nav" aria-label="Seções"><div class="nav-in"><img src="{LOGO_C}" alt="fairhealth">
<a href="#marca">Marca</a><a href="#cor">Cor</a><a href="#detalhe">Tiffany no detalhe</a><a href="#luz">Luz tiffany</a><a href="#tipografia">Tipografia</a><a href="#elementos">Elementos</a><a href="#grid">Grid</a><a href="#modelos">Modelos</a><a href="#imagem">Imagem</a><a href="#uso">Em uso</a><a href="#certo-errado">Certo e errado</a><a href="#mood">Mood</a></div></nav>

<header class="hero"><div class="hero-in">
  <div><p class="rot">Identidade visual · redes sociais · v1.3 · outubro de 2026</p>
    <h1>fair<span class="k">health</span></h1>
    <p class="sub">Cuidado com rigor de <span class="k">laudo</span>.</p>
    <div class="meta"><p class="leg">Instagram @fairhealth.br em collab com a FairJob · LinkedIn pela FairJob</p></div></div>
  <div class="hero-pecas">{P[2]}{P[9]}{P[16]}</div>
</div></header>
''')

# MARCA
erros_logo = [
    ('lt-tif', f'<img src="{LOGO_C}" alt="" style="width:110px">', 'Sobre o tiffany: o círculo some'),
    ('lt-esc', f'<img src="{LOGO_C}" alt="" style="width:150px;height:90px">', 'Esticada ou achatada'),
    ('lt-esc', f'<img src="{LOGO_C}" alt="" style="width:110px;filter:hue-rotate(150deg) saturate(2)">', 'Recolorida'),
    ('lt-gelo', f'<img src="{LOGO_H}" alt="" style="width:120px"><span style="font-size:22px;margin-left:12px">98%</span>', 'Coração junto de número'),
]
html.append(f'''<section class="faixa f-cre" id="marca"><div class="wrap">
{cab(f"A {k('marca')}", "Duas logos, um uso para cada. Uma única logo por peça, sempre no último slide.", "Marca")}
<div class="logos">
  <div class="lt lt-esc lt-2"><p class="rot">Principal · círculo sobre o painel verde</p><div class="alvo"><img src="{LOGO_C}" alt="Logo fairhealth em círculo" style="width:180px"></div><p class="leg">Institucional, dados, NR-1, oferta, último slide.</p></div>
  <div class="lt lt-gelo"><p class="rot">Coração · momentos de pessoas</p><div class="alvo"><img src="{LOGO_H}" alt="Logo fairhealth em coração" style="width:170px"></div><p class="leg">Bastidores, agradecimentos. Nunca com número.</p></div>
  <div class="lt lt-esc"><p class="rot">Área livre</p><div class="alvo"><div class="area"><img src="{LOGO_C}" alt="" style="width:96px;display:block"></div></div><p class="leg">Metade da altura da logo em volta.</p></div>
  <div class="lt lt-esc"><p class="rot">Tamanhos na arte de 1080</p><div class="alvo" style="gap:24px;align-items:flex-end"><img src="{LOGO_C}" alt="" style="width:80px"><img src="{LOGO_C}" alt="" style="width:48px"></div><p class="leg">160 px no último slide · 96 px na capa de reels.</p></div>
  {''.join(f'<div class="lt {c} marca-x"><span class="sobre-selo">{SELO_N}</span><div class="alvo">{img}</div><p class="leg">{t}</p></div>' for c, img, t in erros_logo[:3])}
</div>
<div class="logos">{''.join(f'<div class="lt {c} marca-x"><span class="sobre-selo">{SELO_N}</span><div class="alvo">{img}</div><p class="leg">{t}</p></div>' for c, img, t in erros_logo[3:])}
  <div class="lt lt-tif marca-x"><span class="sobre-selo">{SELO_N}</span><div class="alvo"><span style="font-size:30px;font-weight:800">fair health</span></div><p class="leg">Redesenhada ou digitada</p></div>
  <div class="lt lt-esc marca-x"><span class="sobre-selo">{SELO_N}</span><div class="alvo"><img src="{LOGO_C}" alt="" style="width:110px;filter:drop-shadow(0 10px 8px rgba(0,0,0,.6))"></div><p class="leg">Com sombra ou efeito</p></div>
  <div class="lt lt-gelo marca-x"><span class="sobre-selo">{SELO_N}</span><div class="alvo" style="gap:16px"><img src="{LOGO_C}" alt="" style="width:80px"><img src="{LOGO_H}" alt="" style="width:90px"></div><p class="leg">Duas logos na mesma peça</p></div>
</div>
</div></section>
''')

# COR
combos = [
    ('var(--tif)', 'var(--verde)', 'Verde no tiffany', '6,4:1', True),
    ('var(--tif)', 'var(--tinta)', 'Tinta no tiffany', '9,2:1', True),
    ('var(--verde)', 'var(--creme)', 'Creme no verde', '10,7:1', True),
    ('var(--creme)', 'var(--verde)', 'Verde no creme', '10,7:1', True),
    ('var(--tif)', 'var(--branco)', 'Branco no tiffany', '1,9:1', False),
    ('var(--creme)', 'var(--tesc)', 'Tiffany-escuro no creme', '2,4:1', False),
]
html.append(f'''<section class="faixa f-gelo" id="cor"><div class="wrap">
{cab(f"Muito tiffany, {k('pouco')} resto", "Proporção aproximada em cada peça. O fundo tiffany é sempre a última camada.", "Cor")}
<div class="prop" role="img" aria-label="Proporção: tiffany 60%, verde-autoridade 25%, creme 10%, acento 5%">
  <div style="flex:60;background:var(--tif)"><span class="hx">60%</span><div><p class="nm">Tiffany</p><p class="hx">#96C5BD · fundo</p></div></div>
  <div style="flex:25;background:var(--verde);color:var(--creme)"><span class="hx">25%</span><div><p class="nm">Verde-autoridade</p><p class="hx">#1F3A36 · texto e painel</p></div></div>
  <div style="flex:10;background:var(--creme);outline:1px solid var(--tclaro);outline-offset:-1px"><span class="hx">10%</span><div><p class="nm">Creme</p><p class="hx">#F0F0E9</p></div></div>
  <div style="flex:5;background:var(--vlogo);color:var(--creme)"><span class="hx">5%</span></div>
</div>
<div class="apoio">
  <div class="sw" style="background:var(--tesc);color:var(--verde)">Tiffany-escuro<br>#5FA89A · só sobre o verde</div>
  <div class="sw" style="background:var(--vlogo);color:var(--creme)">Verde-logo<br>#2F6B64 · fios e ícones</div>
  <div class="sw" style="background:var(--tclaro)">Tiffany-claro<br>#BFE0D9 · texto no verde</div>
  <div class="sw" style="background:var(--ui);outline:1px solid var(--tclaro);outline-offset:-1px">Gelo<br>#F6F8F7 · cartão de interface</div>
  <div class="sw" style="background:var(--tinta);color:var(--creme)">Tinta<br>#141B1B · contraste máximo</div>
</div>
<div class="combos">{''.join(f'<div class="cb" style="background:{bg};color:{fg}"><span class="sobre-selo" style="position:static">{SELO_S if ok else SELO_N}</span><p class="aa">Aa <span class="k">Aa</span></p><p class="rz">{n} · {r}</p></div>' for bg, fg, n, r, ok in combos)}</div>
</div></section>
''')

# TIFFANY NO DETALHE
html.append(f'''<section class="faixa f-esc" id="detalhe"><div class="wrap">
{cab(f"Tiffany no {k('detalhe')}", "Em cada linha da grade, no máximo um post com fundo tiffany. Nos outros, o fundo é verde ou creme e o tiffany aparece num destes seis detalhes.", "Tiffany no detalhe")}
<div class="det">{''.join(f'<figure>{a}<figcaption class="modelo-nome">{n}<br><span class="leg">{d}</span></figcaption></figure>' for a, n, d in DET)}</div>
</div></section>
''')

# LUZ TIFFANY
html.append(f"""<section class="faixa f-noite" id="luz"><div class="wrap">
{cab(f"Luz {k('tiffany')}", "Série para manifestos, ciência, dados e tecnologia, uma ou duas vezes por semana. O fundo é verde quase preto e o tiffany entra como luz.", "Série aprovada em 09/10")}
<div class="luz">{''.join(f'<figure>{a}<figcaption class="modelo-nome">{n}<br><span class="leg">{d}</span></figcaption></figure>' for a, n, d in LUZ)}</div>
<div class="regras">
  <p><b>Cor</b>Fundo #0D1816 (verde-noite). Luz, brilho e pontos em tiffany. Texto em creme, palavra-chave em tiffany.</p>
  <p><b>Atmosfera</b>Feixes e brilho desfocados, grão de filme leve, vinheta nas bordas. Sem arco-íris, sem arcos, sem vidro.</p>
  <p><b>Tipografia</b>Raleway. Palavra-chave em ExtraBold Itálico tiffany, ou itálico leve em títulos mais elegantes.</p>
  <p><b>Etiquetas</b>Arredondadas, só com contorno creme ou tiffany-claro. Nunca preenchidas.</p>
  <p><b>Foto</b>Só nesta série a foto ocupa a peça inteira: escurecida, com tom tiffany e grão, título sobre o degradê escuro.</p>
  <p><b>Na grade</b>No máximo uma peça Luz tiffany por linha, ao lado de uma tiffany e de uma creme ou eco.</p>
</div>
</div></section>
""")

# TIPOGRAFIA
escala = [('Display', '104 px', 'f-display', f'O que é {k("importante")}'), ('Título', '72 px', 'f-titulo', f'Como o cuidado {k("chega")}'),
          ('Número suave', '120 px', 'f-num', '8 em cada 10'), ('Subtítulo', '44 px', 'f-sub', 'Médicos e psicólogos dentro da empresa'),
          ('Corpo', '34 px', 'f-corpo', 'Atendimento presencial ou remoto, perto de quem trabalha.'), ('Legenda', '28 px', 'f-leg', 'Plano Individualizado de Cuidado'),
          ('Etiqueta', '26 px', 'f-etq', 'Ciência no cuidado'), ('Fonte', '24 px', 'f-nota', 'Fonte: OMS, 2022')]
esc_rows = ''.join(f'<div><p class="nm">{n}<small>{px} na arte</small></p><div class="mini-ab"><div class="in"><p class="{c} s">{s}</p></div></div></div>' for n, px, c, s in escala)
html.append(f'''<section class="faixa f-tif" id="tipografia"><div class="wrap">
{cab(f"Só Raleway. Um {k('destaque')} por título.", "Regular no texto. ExtraBold Itálico só na palavra-chave, na mesma linha.", "Tipografia")}
<div class="esp"><div><p class="big">Aa</p><p class="rot" style="margin-top:12px">Raleway Regular 400</p></div><div><p class="big k">Aa</p><p class="rot" style="margin-top:12px">Raleway ExtraBold Itálico 800</p></div></div>
<p class="abc">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz<br>0123456789 · áéíóú ãõ ç · « » → %</p>
<div class="escala">{esc_rows}</div>
<div class="ce-par" style="max-width:820px">
  <figure>{ab(A(96, 380, f'<p class="f-titulo">Como o cuidado chega à sua {k("empresa")}.</p>'))}<figcaption class="leg">{SELO_S} Uma palavra-chave</figcaption></figure>
  <figure>{ab(A(96, 380, f'<p class="f-titulo">{k("Como")} o {k("cuidado")} chega à {k("sua empresa")}.</p>'), 'nao-ab')}<figcaption class="leg">{SELO_N} Três destaques</figcaption></figure>
</div>
</div></section>
''')

# ELEMENTOS
html.append(f'''<section class="faixa f-cre" id="elementos"><div class="wrap">
{cab(f"Peças de {k('montar')}", "Cada bloco é um elemento separado e editável no Canva. Nada achatado numa imagem.", "Elementos")}
<div class="elems">
  <div class="el"><p class="rot">Etiqueta de série</p><div class="demo"><div class="mini-ab"><div class="in"><p class="f-etq" style="font-size:calc(40*var(--u));line-height:calc(48*var(--u))">Como funciona o cuidado</p><span class="fio-c" style="width:calc(96*var(--u));height:calc(6*var(--u))"></span></div></div></div></div>
  <div class="el"><p class="rot">Chips · cantos de 8 px</p><div class="demo"><div class="mini-ab"><div class="in" style="display:flex;flex-wrap:wrap;gap:calc(20*var(--u))"><span class="chip" style="font-size:calc(40*var(--u));height:calc(88*var(--u))">Sono</span><span class="chip" style="font-size:calc(40*var(--u));height:calc(88*var(--u))">Alimentação</span><span class="chip out" style="font-size:calc(40*var(--u));height:calc(88*var(--u))">Medicina do Estilo de Vida</span></div></div></div></div>
  <div class="el esc"><p class="rot">Ficha · fios de laudo</p><div class="demo"><div class="mini-ab"><div class="in"><div class="lista on-esc"><p style="font-size:calc(44*var(--u));line-height:calc(56*var(--u))">Medicina do Estilo de Vida</p><p style="font-size:calc(44*var(--u));line-height:calc(56*var(--u))">Escritório do Cuidado</p><p style="font-size:calc(44*var(--u));line-height:calc(56*var(--u))">Dados agregados, nunca individuais</p></div></div></div></div></div>
  <div class="el"><p class="rot">Cartão de interface · sombra suave</p><div class="demo"><div class="mini-ab"><div class="in"><div class="card"><p class="f-nota card-head" style="font-size:calc(36*var(--u));line-height:calc(44*var(--u))">Plano de cuidado</p>{''.join(f'<div class="chk"><span class="box" style="width:calc(56*var(--u));height:calc(56*var(--u))"></span><span style="font-size:calc(44*var(--u))">{t}</span></div>' for t in ('Dormir 30 min mais cedo', 'Caminhar 10 min'))}</div></div></div></div></div>
  <div class="el"><p class="rot">Número suave</p><div class="demo"><div class="mini-ab"><div class="in"><p class="f-titulo" style="font-size:calc(56*var(--u));line-height:calc(64*var(--u))">Ninguém volta a um lugar onde não se sentiu {k('cuidado')}.</p><p class="f-num gap24" style="font-size:calc(150*var(--u));line-height:calc(150*var(--u))">8 em cada 10</p><p class="f-nota gap16" style="font-size:calc(32*var(--u));line-height:calc(40*var(--u))">Fonte: Escritório do Cuidado numa indústria, 2026</p></div></div></div></div>
  <div class="el"><p class="rot">Rodapé e arraste</p><div class="demo"><div class="mini-ab"><div class="in" style="height:calc(120*var(--u))"><div class="rod" style="left:0;right:0;top:calc(40*var(--u));font-size:calc(40*var(--u));height:calc(72*var(--u));border-top-width:calc(3*var(--u))"><span>@fairhealth.br</span><span class="arr">Arraste para o lado <svg class="seta" style="width:calc(72*var(--u));height:calc(24*var(--u))" viewBox="0 0 48 16" aria-hidden="true"><path d="M0 8H46M38 1l8 7-8 7" fill="none" stroke="currentColor" stroke-width="2"/></svg></span></div></div></div></div></div>
</div>
<div class="el" style="min-height:0"><p class="rot">Ícones dos 6 pilares · traço fino, uma cor</p><div class="icones">{''.join(f'<div>{icone(n, "")}<span>{n}</span></div>' for n in ICON)}</div></div>
</div></section>
''')

# GRID
ov4x5 = ('<div class="ov">'
         '<span class="m" style="left:0;top:0;bottom:0;width:calc(96*var(--u))"></span><span class="m" style="right:0;top:0;bottom:0;width:calc(96*var(--u))"></span>'
         '<span class="m" style="left:calc(96*var(--u));right:calc(96*var(--u));top:0;height:calc(96*var(--u))"></span><span class="m" style="left:calc(96*var(--u));right:calc(96*var(--u));bottom:0;height:calc(96*var(--u))"></span>'
         + ''.join(f'<span class="c" style="left:calc({96 + i * 152}*var(--u))"></span>' for i in range(6)) +
         '<span class="t" style="left:calc(110*var(--u));top:calc(40*var(--u))">96 px</span><span class="t" style="left:calc(110*var(--u));bottom:calc(36*var(--u))">6 colunas · 128 px · gutter 24</span></div>')
ovreel = ('<div class="ov"><span class="ui" style="left:0;right:0;top:0;height:calc(220*var(--u))"></span><span class="ui" style="left:0;right:0;bottom:0;height:calc(420*var(--u))"></span>'
          '<span class="ui" style="right:0;top:calc(220*var(--u));bottom:calc(420*var(--u));width:calc(140*var(--u))"></span><span class="seg"></span>'
          '<span class="t" style="left:calc(120*var(--u));top:calc(250*var(--u));color:var(--verde)">Área segura</span></div>')
html.append(f'''<section class="faixa f-gelo" id="grid"><div class="wrap">
{cab(f"Margem de 96 px, {k('sempre')}", "Feed 1080 × 1350. Reels 1080 × 1920. Na grade do perfil, a peça aparece em 3:4.", "Grid")}
<div class="grid-demo">
  <figure style="margin:0">{ab(ov4x5 + etq('Como funciona o cuidado') + A(96, 400, f'<p class="f-display">Aqui, o cuidado começa com uma {k("pergunta")}.</p>') + rod())}<figcaption class="leg">Feed 4:5 · margens e 6 colunas</figcaption></figure>
  <figure style="margin:0">{ab(ovreel + A(96, 760, f'<p class="f-titulo">Antes do afastamento, teve um {k("atestado")}.</p>', w=844), 'reel')}<figcaption class="leg">Reels 9:16 · a interface cobre topo, base e direita</figcaption></figure>
  <figure style="margin:0">{crop(P[2])}<figcaption class="leg">Grade do perfil 3:4 · perde cerca de 34 px de cada lado</figcaption></figure>
</div>
</div></section>
''')

# MODELOS
modelos = [
    (P[2], 'M1 · Capa-pergunta', 'Abre o carrossel com uma pergunta do RH.'),
    (P[15], 'M2 · Passos', 'Processo em 3 a 5 passos, separados por fios.'),
    (P[8], 'M3 · Cartão de interface', 'Mostra o produto sem expor ninguém.'),
    (PILAR, 'M5 · Pilar', 'Um dos 6 pilares por peça, com ícone.'),
    (P[9], 'M6 · Número suave', 'Cuidado primeiro, número depois.'),
    (P[6], 'Autoridade · divisão', 'Tiffany e verde lado a lado. Uso pontual.'),
    (P[12], 'M8 · Citação', 'Folha creme, crédito ao artigo.'),
    (P[3], 'M9 · Capa de reel', 'Painel verde com moldura tiffany.'),
    (CIENCIA3, 'M10 · Ciência', 'Um estudo, o resultado e a referência.'),
    (P[4], 'Variação C · folha creme', 'Texto longo, cara de documento.'),
]
html.append(f'''<section class="faixa f-cre" id="modelos"><div class="wrap">
{cab(f"Os {k('modelos')}", "Desenhados com o conteúdo real do Mês 1. Mesma família, ritmos diferentes.", "Modelos")}
<div class="grade">{''.join(fig(p, n, d) for p, n, d in modelos)}</div>
</div></section>
''')

# IMAGEM: foto em faixa, dentro da folha
SONO_F = ab('<div class="folha"></div>' + etq('Pilares da MEV · Sono') +
            A(96, 280, f'<p class="f-titulo">Dormir não é tempo {k("perdido")}.</p>') +
            A(96, 480, '<p class="f-num">7 a 9 h</p><p class="f-sub">por noite: a faixa saudável para adultos.</p>') +
            PH('sono', 96, 790, 888, 220, 40, 45) +
            A(96, 1040, '<div class="ref"><p class="f-nota">Fonte: RAND Europe, Why sleep matters, 2016.</p></div>') + rod('2/5'),
            label='Slide do pilar sono em folha creme com faixa de foto')
ART_F = ab('<div class="folha"></div>' + etq('Na imprensa') +
           A(96, 280, f'<p class="f-titulo">O trabalho pode adoecer. Mas não é o único {k("vilão")}.</p>') +
           A(96, 560, '<p class="f-corpo">A empresa responde pelo ambiente que constrói, mas não controla todas as variáveis.</p>', w=760) +
           PH('industria1', 96, 790, 888, 220, 40, 40) +
           A(96, 1040, '<div class="ref"><p class="f-nota">Do artigo “Riscos psicossociais no ambiente de trabalho e saúde”, RH Pra Você, 25/09/2026.</p></div>') + rod('2/8'),
           label='Slide de artigo em folha creme com faixa de foto')
ERRADA_F = ab(PH('conversa1', 0, 0, 1080, 1350, 45, 40) +
              A(96, 980, f'<p class="f-titulo branco">Antes de qualquer exame, uma {k("conversa")}.</p>'))
ERRADA_F2 = ab(PH('comida', 0, 0, 1080, 700, 50, 50) + etq('Ciência no cuidado', y=760) +
               A(96, 860, f'<p class="f-titulo">Quem mudou a {k("rotina")}</p>'))
html.append(f'''<section class="faixa f-gelo" id="imagem"><div class="wrap">
{cab(f"Foto em {k('faixa')}", "A foto entra como uma faixa dentro da folha creme, na largura das margens (888 × 220 px na arte), entre o conteúdo e a referência. Uma faixa por slide.", "Imagem")}
<div class="grade">
  {fig(CIENCIA3, 'Ciência · resultado', 'O modelo de referência.')}
  {fig(SONO_F, 'Pilar · sono', 'Mesma faixa, outro tema.')}
  {fig(ART_F, 'Na imprensa · artigo', 'Foto de contexto, sem pessoa identificável em destaque.')}
  <figure>{ERRADA_F.replace('class="ab ', 'class="ab nao-ab ', 1)}<figcaption class="leg">{SELO_N} Foto ocupando a peça inteira</figcaption></figure>
  <figure>{ERRADA_F2.replace('class="ab ', 'class="ab nao-ab ', 1)}<figcaption class="leg">{SELO_N} Foto sangrando a borda</figcaption></figure>
</div>
</div></section>
''')

# EM USO
GRADE = [abimg('luz-1-tarde'), P[15], abimg('eco-2-voltaram'), P[16], abimg('luz-2-diagrama'), abimg('eco-3-importante'),
         abimg('luz-4-sono'), P[11], abimg('eco-4-ciencia'), P[8], abimg('luz-3-plano'), P[10]]
grade_ig = ''.join(crop(g) for g in GRADE)
grade_antes = ''.join(crop(P_ORIG[i]) for i in range(16, 4, -1))
html.append(f'''<section class="faixa f-esc" id="uso"><div class="wrap">
{cab(f"Na {k('tela')}", "O Mês 1 no perfil: em cada linha, uma peça Luz tiffany, uma tiffany e uma creme ou eco. O tiffany aparece como fundo, como detalhe e como luz.", "Em uso")}
<div class="uso">
  <div class="tel" role="img" aria-label="Simulação do perfil @fairhealth.br com 12 posts do Mês 1">
    <div class="perfil"><img src="{LOGO_C}" alt=""><div><p class="user">fairhealth.br</p><p style="font-size:13px">Cuidado dentro da empresa</p></div></div>
    <p class="bio"><b>fairhealth</b><br>Cuidamos antes: médicos e psicólogos dentro da empresa, com Medicina do Estilo de Vida.<br>Ecossistema @fairjob<br><span class="lk">fairhealth.com.br</span></p>
    <div class="botoes"><span>Seguir</span><span>Mensagem</span></div>
    <div class="ig-grade">{grade_ig}</div>
  </div>
  <div class="tel" style="padding-top:12px" role="img" aria-label="Simulação de post no feed">
    <div class="post-h"><img src="{LOGO_C}" alt=""><span><b>fairhealth.br</b> e <b>fairjob</b></span></div>
    {abimg('luz-2-diagrama')}
    <div class="acoes">{acoes}</div>
    <p class="cap"><b>fairhealth.br</b> O check-up mostra números. A rotina mostra o resto: sono, alimentação, estresse, relações. <span class="mais">… mais</span></p>
  </div>
</div>
<div class="antes-depois"><div><p class="rot">Antes · tudo tiffany</p><div class="ig-grade">{grade_antes}</div></div><div><p class="rot">Agora · tiffany, creme, eco e Luz tiffany</p><div class="ig-grade">{grade_ig}</div></div></div>
<div><p class="rot" style="color:var(--tclaro)">Carrossel completo · Aqui, o cuidado começa com uma pergunta</p></div>
<div class="tira">{''.join(CARR)}</div>
<div><p class="rot" style="color:var(--tclaro)">Reel tipográfico · frase a frase, corte seco</p></div>
<div class="tira-reel">{''.join(REEL)}</div>
</div></section>
''')

# CERTO E ERRADO
ce = ''.join(f'''<div><div class="ce-par">
  <figure>{e_ab.replace('class="ab ', 'class="ab nao-ab ', 1)}<figcaption class="leg">{SELO_N} {e_txt}</figcaption></figure>
  <figure>{c_ab}<figcaption class="leg">{SELO_S} {c_txt}</figcaption></figure></div></div>''' for e_txt, e_ab, c_txt, c_ab in ERR)
html.append(f'''<section class="faixa f-gelo" id="certo-errado"><div class="wrap">
{cab(f"Certo e {k('errado')}", "Os erros que mais aparecem, lado a lado com a versão certa.", "Certo e errado")}
<div class="ce">{ce}</div>
</div></section>
''')

# MOOD
html.append(f'''<section class="faixa f-esc" id="mood"><div class="wrap">
<div class="mood"><p class="frase">A calma de quem cuida. A precisão de quem {k('mede')}.</p>
<p class="palavras"><span>Calmo</span><span>Preciso</span><span>Sério</span><span>Humano</span><span class="k">Antes</span></p></div>
<div class="refs"><div><b>Laudo</b>fios finos, campos alinhados</div><div><b>Revista científica</b>referência no rodapé</div><div><b>Relatório anual</b>um número por página</div><div><b>Sinalização hospitalar</b>poucas palavras, contraste alto</div></div>
</div></section>
<footer class="rodape-pg">fairhealth · identidade visual v1 · 09/10/2026 · sem nomes reais nas peças, personagens fictícias sinalizadas, números sempre com fonte</footer>
''')

# cada logo entra uma vez só, num script, em vez de repetir o data URI em toda peça
css_f = ''.join(f'.f-{n}{{background-image:url(data:image/jpeg;base64,{base64.b64encode(open(os.path.join(FOTOS, n + ".jpg"), "rb").read()).decode()})}}' for n in sorted(USADAS))
pagina = '\n'.join(html).replace(f'src="{LOGO_C}"', 'data-logo="c"').replace(f'src="{LOGO_H}"', 'data-logo="h"')
_rc = Image.open(os.path.join(os.path.dirname(FOTOS.rstrip('/')) if False else 'instagram/marca/recortes', 'mulher-sentada.png'))
_rc.thumbnail((700, 900))
_buf = io.BytesIO(); _rc.save(_buf, 'WEBP', quality=80)
css_f += '.rc-mulher{background-image:url(data:image/webp;base64,' + base64.b64encode(_buf.getvalue()).decode() + ')}'
for _n in sorted(PNGS):
    _im = Image.open(os.path.join(PNG_DIR, _n + '.png')).convert('RGB'); _im.thumbnail((760, 950))
    _b = io.BytesIO(); _im.save(_b, 'WEBP', quality=82)
    css_f += '.pi-' + _n + '{background-image:url(data:image/webp;base64,' + base64.b64encode(_b.getvalue()).decode() + ')}'
pagina = pagina.replace('/*FOTOS*/', css_f, 1)
pagina += ('<script>(function(){var L={c:"' + LOGO_C + '",h:"' + LOGO_H + '"};'
           'document.querySelectorAll("img[data-logo]").forEach(function(i){i.src=L[i.dataset.logo];});})();</script>')
open(OUT, 'w').write(pagina)
print('ok', OUT, len(pagina) // 1024, 'KB')
