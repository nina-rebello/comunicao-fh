# Carrossel 18/11: Recorde de afastamentos por saúde mental e a NR-01 · 6 slides

**Quarta, 18/11.** Semana 3 de novembro, bloco 5 (Atualidade), eixo Notícias + Mercado. É o N08 de
`marketing/ferramentas/conteudo_posts_novembro.py`. Vem depois do Reel do Novembro Azul (16/11) e antes
do depoimento de 19/11.

**Status:** v4 para aprovação (04/11): a v3 com o convite trocado (sem "Comente CUIDADO").

- **Artes** (1080x1350): `png/n-01.png` … `n-06.png`, nesta ordem. Prévia em `previa.png`.
- **Alternativas** (`alternativas.html`, imagens em `png-alternativas/`, Canva em `canva-alternativas.html`):
  - slide 3 com o recorte digitado da v2, com o texto já corrigido pelo oficial (`n-03-recorte.png`);
  - slide 6 com o convite de contato: "Fale com a gente pelo link da bio e leve o Escritório do Cuidado para a sua
    empresa." (`n-06-contato.png`).
- **Canva:** `canva.html` (autocontido, cerca de 20 MB, como o de 11/11). Para importar, siga o `CLAUDE.md`
  (commit, push e endereço raw com o hash do commit). Também há o `nr01-afastamentos.pdf`.
- **Para regerar depois de editar:**
  ```
  python3 instagram/posts/nr01-afastamentos/gerar.py
  node instagram/ferramentas/render.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/png
  node instagram/ferramentas/render.mjs instagram/posts/nr01-afastamentos/alternativas.html instagram/posts/nr01-afastamentos/png-alternativas
  node instagram/ferramentas/pdf.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/nr01-afastamentos.pdf
  node instagram/ferramentas/canva.mjs instagram/posts/nr01-afastamentos/slides.html instagram/posts/nr01-afastamentos/canva.html
  node instagram/ferramentas/canva.mjs instagram/posts/nr01-afastamentos/alternativas.html instagram/posts/nr01-afastamentos/canva-alternativas.html
  ```
  O `gerar.py` refaz os fundos com granulado, as barras e a fita com textura, os recortes do PDF oficial da NR-01
  (`fotos/nr-01-atualizada-2025.pdf`, precisa do `pdftoppm`), as composições de `recorte.html` (print colado e
  recorte digitado, em PNG transparente), a foto do slide 5 e os marca-textos dos dois HTML (mede cada linha
  `data-mk` e acerta a imagem `data-tx`). Usa `instagram/ferramentas/textura.py` e `medir-marcas.mjs`, do carrossel
  de 11/11. O CSS fica em `estilo.css`, comum a `slides.html` e `alternativas.html`.

## v4 (04/11): o convite

A Nina pediu um convite sem "Comente CUIDADO": curtir, comentar e compartilhar, ou entrar em contato. O slide 6
mantém o balão "E agora, RH?" da capa e responde com "Curta, comente e compartilhe com quem cuida das pessoas na
sua empresa.", com os ícones das três ações. A versão de contato ("Fale com a gente pelo link da bio e leve o
Escritório do Cuidado para a sua empresa.", no modelo de chamadas anteriores) fica nas alternativas. A capa do
guia de NR-01 saiu: ela era a entrega da palavra CUIDADO.

## v3 (04/11): o que mudou e por quê

Pedidos da Nina sobre a v2:

1. **Conflito com a fairdata.** A fairdata faz o diagnóstico de riscos psicossociais para o PGR, então "a
   planilha sozinha não resolve" e "mapear o risco é só o começo" desvalorizavam um produto do próprio
   ecossistema. **Saída:** a própria NR-01 (item 1.5.3.2) pede os dois lados, e cada um tem quem faça:
   **medir** (identificar, avaliar e classificar os riscos) com a fairdata, e **cuidar** (implementar medidas de
   prevenção e acompanhar o controle dos riscos) com o Escritório do Cuidado. São os verbos do ecossistema
   (`voice.md`, decisões de 11/10: a fairdata é o "medir", a fairhealth o "cuidar"). Saíram o slide 2 da v2
   (promessa com a planilha) e o "Mapear o risco é o começo".
2. **Slide da norma com o texto real.** Print do PDF oficial do MTE: o quadro de vigência (pág. 4) e os itens
   1.5.3.1.4 e 1.5.3.2 (pág. 5), colados com fita, com o trecho dos riscos psicossociais no marca-texto. A versão
   da v2 (recorte digitado) fica como alternativa.
3. **Lista de riscos do guia do MTE**, com a fonte. A lista anterior vinha do roteiro, sem fonte, e dois itens
   ("metas sem clareza" e "jornada sem pausa") não estão no guia.
4. **Saiu o slide das três perguntas para o RH**, e o carrossel ficou com 6 slides.

## Os slides

| # | Fundo | Recurso visual | Texto |
|---|---|---|---|
| 1 | Creme com brilho Tiffany | Número gigante, marca-texto, fonte sublinhada à mão, balão | Saúde mental no trabalho · **546,2 mil** afastamentos do trabalho ==por saúde mental== no Brasil em 2025, concedidos pelo INSS. Fonte: Ministério da Previdência Social. Balão: E agora, RH? |
| 2 | Papel | Barras com textura (2024 cinza, 2025 Tiffany), seta e "+15,7%" à mão | O dado · 546,2 mil licenças por transtornos mentais em 2025, ==o segundo recorde seguido.== Fonte completa no pé |
| 3 | Verde-escuro | "NR-01" gigante e o print do texto oficial colado com fita | Desde maio de 2026, a NR-01 pede que a empresa **identifique e gerencie os riscos psicossociais**, junto com os outros riscos ocupacionais. |
| 4 | Tiffany | Folha com a lista numerada | O que é *risco psicossocial* · Exemplos da lista do Ministério do Trabalho e Emprego: os 13 fatores do guia. Fonte: guia do MTE (2025), lista exemplificativa |
| 5 | Foto + papel | Dois cartões, claro (Medir) e verde (Cuidar), com as alíneas da norma | Medir e cuidar: *a norma pede os dois.* Medir: b) identificar os perigos, c) avaliar os riscos, d) classificar os riscos. Com a **fairdata**: o diagnóstico dos riscos do grupo. Cuidar: e) implementar medidas de prevenção, f) acompanhar o controle dos riscos. Com o **Escritório do Cuidado**: escuta, acompanhamento e encaminhamento. Fonte: NR-01, item 1.5.3.2 |
| 6 | Creme com brilho Tiffany | O balão da capa de volta e os ícones de curtir, comentar e compartilhar | Curta, comente ==e compartilhe== com quem cuida das pessoas na sua empresa. Precisa de ajuda agora? **CVV 188.** |

`==trecho==` = marca-texto Tiffany. Em itálico, o trecho em Instrument Serif.

**Texto novo, para a Nina aprovar:** slide 5 inteiro ("Medir e cuidar: a norma pede os dois." e os dois
cartões), a frase "Exemplos da lista do Ministério do Trabalho e Emprego:" no slide 4 e os rótulos curtos
("Saúde mental no trabalho", "O dado", "A norma"). Os itens dos cartões do slide 5 são as alíneas da norma,
resumidas ("identificar os perigos e possíveis lesões ou agravos à saúde" virou "identificar os perigos").

## O design

- Barra no topo dos outros carrosséis (@FAIRHEALTH.BR e 01/06). A numeração pode sair se a Nina preferir (o
  `CLAUDE.md` registra que ela tirou os números do carrossel de 21/10).
- Fundos que mudam a cada slide, nenhum vizinho igual: creme com brilho, papel, verde-escuro, Tiffany, foto e
  papel, creme com brilho. O Tiffany `#9FC5BD` é fundo no slide 4 e cor dos destaques em todos.
- O balão "E agora, RH?" abre na capa e volta no último slide (ponto de virada do método Vinci).
- Fundos, marca-textos, barras, prints e fita são imagens, para o Canva aceitar. Os textos
  continuam editáveis, cada um na sua caixa.
- Fonte em letra pequena em todo slide com dado ou norma (1 a 5). CVV 188 no último slide.
- "NR-01" nunca vai em Instrument Serif: os algarismos dela deixam o "01" com cara de "0l".

## As imagens

- **Slide 3:** recortes do PDF oficial (`fotos/nr-01-atualizada-2025.pdf`, baixado do gov.br em 04/11). O
  marca-texto Tiffany é aplicado sobre o texto como caneta (multiplicação), sem mudar o documento. O amarelo em
  "Entra em vigor em 26 de maio de 2026" é do próprio PDF.
- **Slide 5:** `fotos/conversa1.jpg`, do banco da marca (licença Unsplash), ilustrativa: nunca apresentar como
  time, cliente ou colaborador atendido. Se houver foto própria de conversa no Escritório do Cuidado, ela entra
  no mesmo lugar (1080x420).
- **Fundos:** creme com brilho e papel do carrossel de 11/11 (`fundo-capa.jpg` = `fundo-2`, `fundo-fim.jpg` =
  `fundo-3`, `fundo-papel.jpg`); Tiffany e verde-escuro com granulado gerados pelo `gerar.py`.

## Fontes

- **Afastamentos:** Ministério da Previdência Social, nota oficial na Agência Gov (jan/2026): 546.254
  benefícios por incapacidade temporária concedidos pelo INSS por transtornos mentais e comportamentais em 2025,
  15,66% acima de 2024 (472.328). O número conta benefícios, não pessoas: a capa diz "afastamentos", não
  "trabalhadores".
  https://agenciagov.ebc.com.br/noticias/202601/previdencia-social-concede-546-254-beneficios-por-incapacidade-temporaria-por-transtornos-mentais-e-comportamentais
- **NR-01:** texto atualizado publicado pelo MTE no gov.br, itens 1.5.3.1.4 e 1.5.3.2, na redação da Portaria MTE
  nº 1.419/2024; em vigor desde 26/05/2026 (Portaria MTE nº 765/2025). Conferido palavra por palavra no PDF
  oficial e na Portaria nº 1.419/2024 (PDF do gov.br) em 04/11.
  https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/nr-01-atualizada-2025-i.pdf
- **Fatores de risco psicossociais:** Guia de informações sobre os fatores de riscos psicossociais relacionados
  ao trabalho (MTE, 2025), "listagem exemplificativa" com 13 fatores (pág. 7 a 8). Copiados na ordem do guia; o
  item "Más relacionamentos" do guia entrou como "Maus relacionamentos".
  https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/guia-nr-01-revisado.pdf

## Pendências

- [ ] Aprovação da v4 pela Nina: texto novo do slide 5 (com a fairdata), slide 3 com print ou com recorte
      digitado, slide 6 com curtir/comentar/compartilhar ou com contato, numeração no topo.
- [ ] Dr. Ronald: revisar o texto de saúde mental (CFM) e a leitura da NR-01.
- [ ] Legenda: o rascunho do N08 foi ajustado à v4 (lista do MTE, medir e cuidar, convite novo). Ainda precisa
      passar pela skill ig-caption (com o `caption.py`) e pela ig-human.
- [ ] Métrica que decide se o post deu certo (método Vinci): compartilhamentos, comentários e salvamentos (ou, na
      versão de contato, cliques no link da bio), comparados com o carrossel de 28/10 (também de dados para o RH).
