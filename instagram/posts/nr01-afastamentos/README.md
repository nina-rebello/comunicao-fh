# Carrossel 18/11: Recorde de afastamentos por saúde mental e a NR-01 · 8 slides

**Quarta, 18/11.** Semana 3 de novembro, bloco 5 (Atualidade), eixo Notícias + Mercado. É o N08 de
`marketing/ferramentas/conteudo_posts_novembro.py`. Vem depois do Reel do Novembro Azul (16/11) e antes
do depoimento de 19/11.

**Status:** texto aprovado pela Nina em 04/11 (com a capa mais específica: afastamentos do trabalho, no
Brasil, concedidos pelo INSS). Design v2 para aprovação (04/11).

- **Artes** (1080x1350): `png/n-01.png` … `n-08.png`, 8 imagens, nesta ordem. Prévia em `previa.png`.
- **Canva:** `canva.html` (autocontido, com fundos, texturas, fotos, fontes e logo embutidos; cerca de 24 MB,
  como o do carrossel de 11/11). Para importar, siga o passo a passo do `CLAUDE.md` (commit, push e endereço
  raw com o hash do commit). Também há o `nr01-afastamentos.pdf`.
- **Para regerar depois de editar o `slides.html`:**
  ```
  python3 instagram/posts/nr01-afastamentos/gerar.py
  node instagram/ferramentas/render.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/png
  node instagram/ferramentas/pdf.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/nr01-afastamentos.pdf
  node instagram/ferramentas/canva.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/canva.html
  ```
  O `gerar.py` refaz os fundos com granulado, as barras e a fita com textura, o recorte da NR-01 e a capa do
  guia (`recorte.html`, em PNG transparente) e os marca-textos: mede cada linha `data-mk` e acerta a posição da
  imagem `data-tx` correspondente. Usa `instagram/ferramentas/textura.py` e `medir-marcas.mjs`, trazidos do
  carrossel de 11/11.

## v2 (04/11): no padrão dos últimos carrosséis

A v1 ficou abaixo do padrão dos carrosséis de 28/10, 03/11 e 11/11 (retorno da Nina: "mais modernos,
complexos, bonitos, com menos cara de IA"). A v2 usa o que esses posts têm de melhor:

- **Método Vinci (`carrossel.md`, branch `claude/adoring-dirac-fmh66g`):** a capa não usa foto de banco; o
  visual muda a cada slide; o último slide retoma a capa. O balão "E agora, RH?" abre na capa e volta no
  convite, e a resposta é o próximo passo (Comente CUIDADO).
- **Do 11/11:** papel texturizado, creme com brilho Tiffany, marca-texto Tiffany com textura atrás das
  linhas-chave, gráfico desenhado com barras de textura, anotação à mão (seta, círculo, sublinhado) e recorte
  colado com fita.
- **Do 03/11:** interface como cena (a planilha, como a conversa com a IA), cartões claros sobre o Tiffany,
  bolinhas numeradas e o fim que espelha a capa.
- **Sem o quase-preto**, como pedido em 03/11.

## Os slides

| # | Fundo | Recurso visual | Texto |
|---|---|---|---|
| 1 | Creme com brilho Tiffany | Número gigante, marca-texto, fonte sublinhada à mão, balão "E agora, RH?" | Saúde mental no trabalho · **546,2 mil** afastamentos do trabalho ==por saúde mental== no Brasil em 2025, concedidos pelo INSS. Fonte: Ministério da Previdência Social. *E agora, RH?* |
| 2 | Tiffany | Planilha "Inventário de riscos · PGR" com os cinco riscos "Mapeado" e a coluna circulada à mão | O que a NR-01 pede *e por que a planilha sozinha não resolve.* |
| 3 | Papel | Gráfico: barras com textura (2024 em cinza, 2025 em Tiffany), seta e "+15,7%" circulado à mão | 546,2 mil licenças por transtornos mentais em 2025, ==o segundo recorde seguido.== Fonte completa no pé |
| 4 | Verde-escuro | "NR-01" gigante em menta e o recorte do item 1.5.3.1.4 colado com fita, com o trecho dos riscos psicossociais no marca-texto | Desde maio de 2026, a NR-01 pede que a empresa **identifique e gerencie os riscos psicossociais**, junto com os outros riscos ocupacionais. |
| 5 | Tiffany | Cinco cartões claros com ícone fino num círculo Tiffany | O que é *risco psicossocial*: sobrecarga, metas sem clareza, falta de apoio, conflitos e assédio, jornada sem pausa |
| 6 | Foto + papel | Foto de conversa no alto e a linha com três passos numerados | Mapear o risco *é o começo.* Reduzir o risco pede ==gente perto:== 01 Escuta · 02 Acompanhamento · 03 Encaminhamento |
| 7 | Papel | Folha de pauta colada com fita, caixas desenhadas à mão | Três perguntas para ==a próxima reunião de RH== (as três perguntas) |
| 8 | Creme com brilho Tiffany | O balão da capa de volta e a capa do guia de NR-01 | Comente ==CUIDADO== e receba o guia de NR-01. Precisa de ajuda agora? **CVV 188.** |

`==trecho==` = marca-texto Tiffany. Em itálico, o trecho em Instrument Serif.

**O que entrou além do texto aprovado (para a Nina confirmar):**

- slide 1: o rótulo "Saúde mental no trabalho" e "Arraste para o lado →";
- slide 2: a planilha (títulos "Inventário de riscos · PGR", "Risco psicossocial", "Status" e "Mapeado"), com
  os cinco riscos do slide 5;
- slide 3: o rótulo "O dado", o valor de 2024 (472,3 mil) e o aumento (+15,7%), os dois da mesma nota oficial;
- slide 4: o rótulo "A norma" e o recorte com o texto do item 1.5.3.1.4 da NR-01;
- slide 8: o balão "E agora, RH?" (o mesmo da capa) e a capa do guia ("Guia NR-01", logo e fairhealth).

## O design

- Mesma barra no topo dos outros carrosséis (@FAIRHEALTH.BR e 01/08). A numeração pode sair se a Nina
  preferir (o `CLAUDE.md` registra que ela tirou os números do carrossel de 21/10).
- Fundos que mudam a cada slide, nenhum vizinho igual: creme com brilho, Tiffany, papel, verde-escuro,
  Tiffany, foto e papel, papel, creme com brilho. O Tiffany `#9FC5BD` aparece como fundo nos slides 2 e 5.
- Fundos, marca-textos, barras, fita, recorte e capa do guia são imagens, para o Canva aceitar (granulado,
  textura e elementos girados não passam na conversão). Os textos continuam editáveis, cada um na sua caixa.
- Fonte em letra pequena em todo slide com dado (1, 3 e 4).
- Todo post de saúde mental termina com onde pedir ajuda: CVV 188 no slide 8.

## As imagens

- **Slide 6:** `fotos/conversa1.jpg`, do banco da marca (`instagram/marca/fotos-banco/`, licença Unsplash),
  ilustrativa: nunca apresentar como time, cliente ou colaborador atendido. Recorte em `fotos/n-06.jpg`. Se a
  Nina tiver uma foto própria de conversa no Escritório do Cuidado, ela entra no mesmo lugar (1080x600).
- **Fundos de creme com brilho e de papel:** os mesmos do carrossel de 11/11 (`fundo-capa.jpg` = `fundo-2`,
  `fundo-fim.jpg` = `fundo-3`, `fundo-papel.jpg`). Os fundos Tiffany e verde-escuro com granulado são gerados
  pelo `gerar.py`.

## Fontes

- **Afastamentos:** Ministério da Previdência Social, nota oficial na Agência Gov (jan/2026): 546.254
  benefícios por incapacidade temporária concedidos pelo INSS por transtornos mentais e
  comportamentais em 2025, 15,66% acima de 2024 (472.328).
  https://agenciagov.ebc.com.br/noticias/202601/previdencia-social-concede-546-254-beneficios-por-incapacidade-temporaria-por-transtornos-mentais-e-comportamentais
- O número conta benefícios concedidos, não pessoas. Por isso a capa diz "afastamentos" e não
  "trabalhadores".
- **NR-01:** item 1.5.3.1.4, na redação da Portaria MTE nº 1.419/2024 (riscos psicossociais no gerenciamento
  de riscos ocupacionais, GRO/PGR). A vigência foi adiada para 26/05/2026 pela Portaria MTE nº 765/2025. O
  texto do recorte foi conferido em reproduções do item (ABMES, Migalhas, Grupo GEN); falta conferir
  palavra por palavra no Diário Oficial antes de publicar.

## Pendências

- [ ] Aprovação do design pela Nina, incluindo o que entrou além do texto aprovado (lista acima) e a
      numeração no topo.
- [ ] Dr. Ronald: confirmar a vigência da NR-01 e o que ela exige (slide 4) e revisar o texto de saúde mental
      (CFM).
- [ ] Conferir o texto do item 1.5.3.1.4 no Diário Oficial (recorte do slide 4).
- [ ] Guia de NR-01 pronto e validado até 13/11 (é a entrega do CUIDADO no slide 8, e a capa do slide 8 pode
      ser trocada pela capa real), e alguém para responder as DMs.
- [ ] Legenda: o rascunho está no N08 de `marketing/ferramentas/conteudo_posts_novembro.py`. Ainda
      precisa passar pela skill ig-caption (com o `caption.py`) e pela ig-human.
- [ ] Métrica que decide se o post deu certo (método Vinci): comentários CUIDADO e salvamentos, comparados
      com o carrossel de 28/10 (também de dados para o RH).
