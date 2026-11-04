# Gera marketing/Detalhamento_Posts_Novembro_2026.xlsx a partir de conteudo_posts_novembro.py.
# Uso: python3 marketing/ferramentas/gerar_detalhamento_novembro.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
from conteudo_posts_novembro import POSTS, PENDENCIAS, DATAS

SAIDA = os.path.join(os.path.dirname(__file__), '..', 'Detalhamento_Posts_Novembro_2026.xlsx')
ESCURO, VERDE, TIFFANY, FUNDO = '1F3B36', '2F6B64', '9CC5BC', 'EFF0EB'
COR_FMT = {'Reel': 'D7EBE6', 'Carrossel': 'E3E8DF', 'Foto única': 'FFFFFF'}
F = lambda **k: Font(name='Arial', **k)
fino = Side(style='thin', color='A9CFC6')
BORDA = Border(left=fino, right=fino, top=fino, bottom=fino)
TOPO = Alignment(wrap_text=True, vertical='top')
STATUS = ['Pauta proposta (calendário de novembro)', 'Roteiro proposto', 'Roteiro aprovado', 'Em produção',
          'Arte em rascunho (faltam fotos; reduzir de 9 para 8 slides)', 'Arte para aprovação', 'Aprovado',
          'Agendado', 'Publicado', 'Adiado']

wb = Workbook()


def titulo(ws, texto, sub):
    ws['A1'] = texto
    ws['A1'].font = F(bold=True, size=16, color=ESCURO)
    ws['A2'] = sub
    ws['A2'].font = F(italic=True, size=10, color=VERDE)


def cabecalho(ws, linha, nomes, larguras):
    for i, (n, w) in enumerate(zip(nomes, larguras), 1):
        c = ws.cell(row=linha, column=i, value=n)
        c.font = F(bold=True, color='FFFFFF')
        c.fill = PatternFill('solid', fgColor=ESCURO)
        c.alignment = Alignment(wrap_text=True, vertical='center')
        c.border = BORDA
        ws.column_dimensions[get_column_letter(i)].width = w
    ws.freeze_panes = ws.cell(row=linha + 1, column=3)
    ws.auto_filter.ref = f'A{linha}:{get_column_letter(len(nomes))}{linha}'


def celula(ws, r, c, v, fmt=None, fill=None, bold=False):
    x = ws.cell(row=r, column=c, value=v)
    x.font = F(size=10, bold=bold)
    x.alignment = TOPO
    x.border = BORDA
    if fmt:
        x.number_format = fmt
    if fill:
        x.fill = PatternFill('solid', fgColor=fill)
    return x


DIA = '=CHOOSE(WEEKDAY(B{r},2),"seg","ter","qua","qui","sex","sáb","dom")'

# ---------- Como usar
ws = wb.active
ws.title = 'Como usar'
ws.column_dimensions['A'].width = 120
linhas = [
    ('Detalhamento dos posts de novembro de 2026 · fairhealth (@fairhealth.br)', 'h1'),
    ('Versão de 04/11/2026. 13 posts de 03/11 a 30/11: 5 reels, 7 carrosséis e 1 foto única. Gerada por marketing/ferramentas/gerar_detalhamento_novembro.py a partir de conteudo_posts_novembro.py (edite o conteúdo lá e rode o gerador de novo).', ''),
    ('', ''),
    ('Abas', 'h2'),
    ('Calendário: a lista dos 13 posts com data, formato, bloco, eixo, chamada, status, responsável e pasta no repositório. Status tem lista suspensa.', ''),
    ('Fichas: a ficha completa de cada post: gancho, objetivo, o que estamos dizendo por trás, persona, fio da história, direção visual, material, chamada, stories de apoio, fontes e o que validar.', ''),
    ('Roteiros: cada reel cena por cena (tempo, texto na tela, fala e visual) e cada carrossel slide por slide.', ''),
    ('Legendas: a legenda completa de cada post, com a contagem de caracteres (o Instagram corta em 125 no feed e aceita até 2.200).', ''),
    ('Pendências: o que precisa de aval antes de publicar, com quem confirma e a situação.', ''),
    ('Datas: feriados e datas especiais do mês.', ''),
    ('', ''),
    ('De onde vem o conteúdo', 'h2'),
    ('03 a 13/11: instagram/plan.md (fonte: Programacao_Instagram_19-10_a_13-11.pdf), com os roteiros de 14/10 revistos. O 03/11 é o post pronto em instagram/posts/cuidado-na-pratica.', ''),
    ('16 a 30/11: calendário de novembro (marketing/calendario-novembro) e instagram/carrossel-de-tendencia.md. O 25/11 já tem rascunho em instagram/posts/geracao-z. As demais pautas desta faixa são propostas novas: roteiro e legenda são rascunhos para aprovação.', ''),
    ('', ''),
    ('Regras de texto e arte (instagram/voice.md, CLAUDE.md)', 'h2'),
    ('"fairhealth" em minúsculas · comunicação B2B · sem travessão · número só com fonte · sem promessa clínica · sem preço · 5 hashtags, a primeira #fairhealth · carrossel de 5 a 8 slides, sem numeração e com uma chamada só · post de saúde mental termina com "onde pedir ajuda" (CVV 188).', ''),
    ('Toda legenda passa pela skill ig-caption (verificador caption.py) e pela ig-human antes de publicar. As legendas desta planilha passaram pelo caption.py em 04/11; o aviso de "sem chamada" é falso para chamadas em português.', ''),
    ('Marcadores {{...}} indicam dado que ainda falta, com a fonte a confirmar. Nada com {{...}} vai ao ar.', ''),
]
for i, (t, k) in enumerate(linhas, 1):
    c = ws.cell(row=i, column=1, value=t)
    c.alignment = Alignment(wrap_text=True, vertical='top')
    c.font = F(bold=True, size=16, color=ESCURO) if k == 'h1' else F(bold=True, size=12, color=VERDE) if k == 'h2' else F(size=10)

# ---------- Calendário
ws = wb.create_sheet('Calendário')
titulo(ws, 'Calendário de novembro · 13 posts', 'Mude a data na coluna B: o dia da semana acompanha. Status tem lista suspensa. Cor da linha = formato.')
cols = ['ID', 'Data', 'Dia', 'Semana', 'Bloco', 'Eixo', 'Formato', 'Título', 'Chamada (CTA)', 'Status', 'Responsável', 'Pasta no repositório']
cabecalho(ws, 4, cols, [6, 11, 6, 8, 16, 18, 11, 46, 34, 26, 30, 44])
for i, p in enumerate(POSTS):
    r = 5 + i
    cor = COR_FMT[p['fmt']]
    vals = [p['id'], p['data'], DIA.format(r=r), p['semana'], p['bloco'], p['eixo'], p['fmt'], p['titulo'],
            p['cta'], p['status'], p['resp'], p['arquivos']]
    for c, v in enumerate(vals, 1):
        celula(ws, r, c, v, fmt='dd/mm' if c == 2 else None, fill=cor, bold=(c == 8))
fim = 4 + len(POSTS)
dv = DataValidation(type='list', formula1='=Listas!$A$1:$A$%d' % len(STATUS), allow_blank=True)
ws.add_data_validation(dv)
dv.add(f'J5:J{fim}')
r = fim + 2
ws.cell(row=r, column=7, value='Totais').font = F(bold=True)
for j, fm in enumerate(['Reel', 'Carrossel', 'Foto única']):
    ws.cell(row=r + 1 + j, column=7, value=fm).font = F(size=10)
    ws.cell(row=r + 1 + j, column=8, value=f'=COUNTIF($G$5:$G${fim},G{r + 1 + j})').font = F(size=10)
ws.cell(row=r + 4, column=7, value='Total').font = F(bold=True, size=10)
ws.cell(row=r + 4, column=8, value=f'=SUM(H{r + 1}:H{r + 3})').font = F(bold=True, size=10)
ws.cell(row=r + 5, column=7, value='Publicados').font = F(size=10)
ws.cell(row=r + 5, column=8, value=f'=COUNTIF($J$5:$J${fim},"Publicado")').font = F(size=10)
for j in range(5):
    ws.cell(row=r + 1 + j, column=8).alignment = Alignment(horizontal='left')

# ---------- Fichas
ws = wb.create_sheet('Fichas')
titulo(ws, 'Ficha de cada post', 'Data, dia, formato e título vêm da aba Calendário. Uma linha por post.')
campos = [('Gancho / capa', 'gancho', 40), ('Objetivo', 'objetivo', 40), ('O que estamos dizendo por trás', 'portras', 36),
          ('Persona', 'persona', 18), ('Fio da história', 'fio', 34), ('Especificação', 'espec', 30),
          ('Direção visual', 'visual', 44), ('Material e quem aparece', 'material', 32), ('Chamada (CTA)', 'cta', 26),
          ('Stories de apoio', 'stories', 32), ('Fontes e números', 'fonte', 44), ('Validar antes de publicar', 'validar', 48)]
cabecalho(ws, 4, ['ID', 'Data', 'Dia', 'Formato', 'Título'] + [c[0] for c in campos],
          [6, 9, 6, 11, 30] + [c[2] for c in campos])
for i, p in enumerate(POSTS):
    r, lc = 5 + i, 5 + i
    cor = COR_FMT[p['fmt']]
    celula(ws, r, 1, p['id'], fill=cor)
    celula(ws, r, 2, f'=Calendário!B{lc}', fmt='dd/mm', fill=cor)
    celula(ws, r, 3, f'=Calendário!C{lc}', fill=cor)
    celula(ws, r, 4, f'=Calendário!G{lc}', fill=cor)
    celula(ws, r, 5, f'=Calendário!H{lc}', fill=cor, bold=True)
    for c, (_, k, _) in enumerate(campos, 6):
        celula(ws, r, c, p[k])
    ws.row_dimensions[r].height = 190

# ---------- Roteiros
ws = wb.create_sheet('Roteiros')
titulo(ws, 'Roteiros: cena por cena (reels) e slide por slide (carrosséis)', 'Título, formato e data vêm da aba Calendário.')
cabecalho(ws, 4, ['ID', 'Post', 'Formato', 'Data', 'Parte', 'Texto na tela / no slide', 'Fala (reels)', 'Visual e direção', 'Observação'],
          [6, 30, 11, 8, 22, 60, 44, 40, 34])
r = 5
for i, p in enumerate(POSTS):
    lc = 5 + i
    cor = COR_FMT[p['fmt']]
    for parte in p['roteiro']:
        celula(ws, r, 1, p['id'], fill=cor)
        celula(ws, r, 2, f'=Calendário!H{lc}', fill=cor)
        celula(ws, r, 3, f'=Calendário!G{lc}', fill=cor)
        celula(ws, r, 4, f'=Calendário!B{lc}', fmt='dd/mm', fill=cor)
        for c, v in enumerate(parte, 5):
            celula(ws, r, c, v or None, bold=(c == 5))
        r += 1

# ---------- Legendas
ws = wb.create_sheet('Legendas')
titulo(ws, 'Legendas prontas para revisão', 'Copie a célula da coluna E. Caracteres: o feed corta em 125; o limite é 2.200.')
cabecalho(ws, 4, ['ID', 'Data', 'Título', 'Chamada (CTA)', 'Legenda', 'Caracteres', 'Dentro do limite?'], [6, 9, 30, 28, 90, 11, 12])
for i, p in enumerate(POSTS):
    r, lc = 5 + i, 5 + i
    cor = COR_FMT[p['fmt']]
    celula(ws, r, 1, p['id'], fill=cor)
    celula(ws, r, 2, f'=Calendário!B{lc}', fmt='dd/mm', fill=cor)
    celula(ws, r, 3, f'=Calendário!H{lc}', fill=cor, bold=True)
    celula(ws, r, 4, p['cta'])
    celula(ws, r, 5, p['legenda'])
    celula(ws, r, 6, f'=LEN(E{r})')
    celula(ws, r, 7, f'=IF(F{r}<=2200,"sim","não")')
    ws.row_dimensions[r].height = 15 * (p['legenda'].count('\n') + 2 + len(p['legenda']) // 110)

# ---------- Pendências
ws = wb.create_sheet('Pendências')
titulo(ws, 'O que validar antes de publicar', 'Mude a situação para "Resolvida" quando estiver confirmado.')
cabecalho(ws, 4, ['#', 'Posts', 'O que validar', 'Quem confirma', 'Situação'], [5, 14, 90, 26, 12])
for i, (posts, oque, quem, sit) in enumerate(PENDENCIAS):
    r = 5 + i
    for c, v in enumerate([i + 1, posts, oque, quem, sit], 1):
        celula(ws, r, c, v, fill='FCE4D6' if sit == 'Urgente' else None)
dv2 = DataValidation(type='list', formula1='"Urgente,Aberta,Resolvida"', allow_blank=True)
ws.add_data_validation(dv2)
dv2.add(f'E5:E{4 + len(PENDENCIAS)}')

# ---------- Datas
ws = wb.create_sheet('Datas')
titulo(ws, 'Feriados e datas especiais de novembro', '')
cabecalho(ws, 4, ['Data', 'Dia', 'O que é'], [11, 6, 80])
for i, (d, t) in enumerate(DATAS):
    r = 5 + i
    celula(ws, r, 1, d, fmt='dd/mm')
    celula(ws, r, 2, DIA.replace('B{r}', 'A{r}').format(r=r))
    celula(ws, r, 3, t)

# ---------- Listas
ws = wb.create_sheet('Listas')
for i, s in enumerate(STATUS, 1):
    ws.cell(row=i, column=1, value=s).font = F(size=10)
ws.sheet_state = 'hidden'

for s in wb.worksheets:
    s.sheet_view.zoomScale = 100
wb.save(SAIDA)
print('ok', os.path.abspath(SAIDA))
