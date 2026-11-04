# Carrossel 18/11: Recorde de afastamentos por saúde mental e a NR-01 · 8 slides

**Quarta, 18/11.** Semana 3 de novembro, bloco 5 (Atualidade), eixo Notícias + Mercado. É o N08 de
`marketing/ferramentas/conteudo_posts_novembro.py`. Vem depois do Reel do Novembro Azul (16/11) e antes
do depoimento de 19/11.

**Status:** texto aprovado pela Nina em 04/11 (com a capa mais específica: afastamentos do trabalho, no
Brasil, concedidos pelo INSS). Design v1 para aprovação (04/11).

- **Artes** (1080x1350): `png/n-01.png` … `n-08.png`, 8 imagens, nesta ordem. Prévia em `previa.png`.
- **Canva:** `canva.html` (autocontido, com fotos, fontes e logo embutidas). Para importar, siga o passo a
  passo do `CLAUDE.md` (commit, push e endereço raw com o hash do commit). Também há o
  `nr01-afastamentos.pdf`.
- **Para regerar depois de editar o `slides.html`:**
  ```
  python3 instagram/posts/nr01-afastamentos/recortes.py
  node instagram/ferramentas/render.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/png
  node instagram/ferramentas/pdf.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/nr01-afastamentos.pdf
  node instagram/ferramentas/canva.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/canva.html
  ```

## Os slides

Em itálico, o trecho em Instrument Serif, na cor de destaque.

| # | Fundo e layout | Texto |
|---|---|---|
| 1 | Foto de ambiente de trabalho no alto, escurecendo para o tinta; número grande | **546,2 mil** afastamentos do trabalho por saúde mental / no Brasil em 2025, concedidos pelo INSS. / *E agora, RH?* · Fonte: Ministério da Previdência Social |
| 2 | Claro, foto na metade de cima | O que a NR-01 pede *e por que a planilha sozinha não resolve.* → |
| 3 | Verde, gráfico de duas barras (2024 e 2025, mesma escala e base zero) | 546,2 mil licenças por transtornos mentais em 2025, *o segundo recorde seguido.* · 472,3 mil (2024) e 546,2 mil (2025) · Fonte: Ministério da Previdência Social |
| 4 | Água, "NR-01" grande e foto saindo pela lateral direita | Desde maio de 2026, a NR-01 pede que a empresa **identifique e gerencie os riscos psicossociais**, junto com os outros riscos ocupacionais. · Fonte: NR-01, Ministério do Trabalho e Emprego |
| 5 | Tinta, lista com ícones finos e fios | O que é *risco psicossocial*: sobrecarga, metas sem clareza, falta de apoio, conflitos e assédio, jornada sem pausa |
| 6 | Água, texto em cima e foto de conversa embaixo | Mapear o risco *é o começo.* Reduzir o risco pede **gente perto:** → escuta → acompanhamento → encaminhamento |
| 7 | Claro, checklist | Três perguntas para *a próxima reunião de RH*: Onde a sobrecarga aparece primeiro? A quem o colaborador recorre quando não está bem? Que indicador mostra se melhorou? |
| 8 | Verde-escuro, logo | Comente **CUIDADO** *e receba o guia* de NR-01. · Precisa de ajuda agora? **CVV 188.** |

## O design

- Mesmo sistema do carrossel de 03/11 (`instagram/carrossel.md`): barra fixa no topo (@FAIRHEALTH.BR e
  01/08), título em Raleway 800 com um trecho em Instrument Serif itálico e fundos alternados (tinta,
  off, verde, água, tinta, água, off e verde-escuro). O Tiffany aparece como fundo nos slides 4 e 6
  (decisão de 13/10).
- Estilo institucional, como pede a pauta: número grande e calmo na capa ("mil" menor, na base) e o dado
  do slide 3 em gráfico. As barras usam os números da nota oficial (472.328 e 546.254), com a mesma
  escala e base zero.
- Fonte em letra pequena em todo slide com dado (1, 3 e 4).
- Todo post de saúde mental termina com onde pedir ajuda: CVV 188 no slide 8.
- Para o Canva: tudo em posição fixa, fotos em `<img>` já recortadas no tamanho da moldura
  (`recortes.py`, em 2x), ícones SVG dentro de `div` posicionada e quebras dos títulos com `<br>` ou em
  caixas separadas. "de NR-01." no slide 8 fica em Raleway, porque os algarismos da Instrument Serif
  deixam "01" com cara de "0l".

## As fotos

Todas são do banco de imagens da marca (`instagram/marca/fotos-banco/`, licença Unsplash). São
ilustrativas: nunca apresentar como time, cliente ou colaborador atendido. Nenhuma mostra rosto em
sofrimento. Os originais estão em `fotos/` e os recortes em `fotos/n-0X.jpg`.

| Slide | Foto | Por quê |
|---|---|---|
| 1 | `industria1.jpg` | Ambiente de trabalho real, sem sofrimento |
| 2 | `cafe-notebook.jpg` | Alguém no computador: a "planilha" |
| 4 | `oculos.jpg` | Óculos de proteção: segurança do trabalho (SST) |
| 6 | `conversa1.jpg` | Gente perto, conversando |

Nenhuma repete as do carrossel de 03/11.

## Fontes

- **Afastamentos:** Ministério da Previdência Social, nota oficial na Agência Gov (jan/2026): 546.254
  benefícios por incapacidade temporária concedidos pelo INSS por transtornos mentais e
  comportamentais em 2025, 15,66% acima de 2024 (472.328).
  https://agenciagov.ebc.com.br/noticias/202601/previdencia-social-concede-546-254-beneficios-por-incapacidade-temporaria-por-transtornos-mentais-e-comportamentais
- O número conta benefícios concedidos, não pessoas. Por isso a capa diz "afastamentos" e não
  "trabalhadores".
- **NR-01:** gerenciamento de riscos psicossociais no GRO/PGR, exigido desde maio de 2026.

## Pendências

- [ ] Aprovação do design pela Nina.
- [ ] Dr. Ronald: confirmar a vigência da NR-01 (maio de 2026) e o que ela exige (slide 4), e revisar o
      texto de saúde mental (CFM).
- [ ] Guia de NR-01 pronto e validado até 13/11 (é a entrega do CUIDADO no slide 8), e alguém para
      responder as DMs.
- [ ] Legenda: o rascunho está no N08 de `marketing/ferramentas/conteudo_posts_novembro.py`. Ainda
      precisa passar pela skill ig-caption (com o `caption.py`) e pela ig-human.
