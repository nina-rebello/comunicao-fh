# Comunicação fairhealth

Conteúdo do Instagram da fairhealth (@fairhealth.br).

## Git: uma branch só, a `main` (pedido da Nina, 03/11)

Todo o trabalho fica na branch `main`. Não crie branch nova e não deixe trabalho
numa branch `claude/...`. Esta é uma autorização permanente da Nina para fazer
commit e push direto na `main`, mesmo que o chat abra numa branch `claude/...`
ou indique outra branch.

- Antes de mexer em qualquer arquivo, troque para a `main` atualizada:
  `git fetch origin main && git checkout -B main origin/main`
- A cada entrega: commit e `git push -u origin main`.
- Se o push for recusado porque a `main` andou: `git pull --rebase origin main`
  e push de novo.

## O que ler antes de criar ou revisar um post

O índice dos materiais está em `instagram/README.md`. Além dele:

- `instagram/plan.md`: o cronograma atual (19/10 a 13/11). A fonte é
  `marketing/Programacao_Instagram_19-10_a_13-11.pdf`.
- `instagram/carrossel.md`: o método (três Cs) e o visual dos carrosséis. Onde
  discordar da skill `/ig-carousel`, vale o guia.
- `instagram/voice.md`: a voz, as palavras proibidas, o time e as regras do CFM.
- `instagram/referencias.md`: os números oficiais e os materiais de apoio.
- `instagram/essencia.md` e `instagram/diretrizes-criativas.md`: a história, as
  crenças e o visual da marca.
- `instagram/estrategia.md`: a estratégia de fundo (revisada em 08/10, com as três
  linhas editoriais). Ainda não foi alinhada ao cronograma atual.

A planilha `marketing/Cronograma_Conteudo_FairHealth_90dias.xlsx` tem
novembro atualizado (02/11) com a programação do PDF de novembro. As linhas de
outubro e de dezembro em diante estão desatualizadas: não use as datas delas.

Cada post fica em `instagram/posts/<nome>/`, com `slides.html`, `png/`,
`previa.png` e um `README.md` com a legenda e as pendências. Para gerar as
artes e o PDF para o Canva:

```
node instagram/ferramentas/render.mjs instagram/posts/<nome>/slides.html instagram/posts/<nome>/png
node instagram/ferramentas/pdf.mjs instagram/posts/<nome>/slides.html instagram/posts/<nome>/<nome>.pdf
```

## Planilhas de posts: sempre o modelo simples (pedido da Nina, 04/11)

Toda planilha com a programação ou o detalhamento dos posts segue o modelo de
`marketing/Cronograma_Posts_19-10_a_13-11_simples.xlsx`: uma aba só
("Programação"), uma linha por post e estas colunas, nesta ordem: Semana,
Data, Dia, Bloco, Formato, Título, Subtítulo, Roteiro (cena a cena ou slide a
slide) e Legenda. Arial 10, cabeçalho Tiffany, formato colorido (Reel, Carrossel,
Foto única). Não crie planilhas com várias abas, fichas ou pendências.

Para gerar: escreva o conteúdo num `marketing/ferramentas/conteudo_posts_<período>.py`
(mesma estrutura de `conteudo_posts_novembro.py`) e rode
`python3 marketing/ferramentas/gerar_cronograma_simples.py marketing/Cronograma_Posts_<período>.xlsx marketing/ferramentas/conteudo_posts_<período>.py`.
Novembro está em `marketing/Cronograma_Posts_03-11_a_30-11.xlsx`.

## Legendas (pedido da Nina, 20/10)

- Toda legenda é escrita com a skill **ig-caption** (`.claude/skills/ig-caption`), rodando o verificador
  `caption.py` com as palavras de busca do post.
- Antes de entregar, o texto passa pela skill **ig-human**.
- Quando a skill e a marca discordam, vale a marca: 5 hashtags, a primeira #fairhealth; "fairhealth" em minúsculas;
  comunicação B2B; sem travessão; números só com fonte; sem promessa clínica; sem preço.
- O verificador não reconhece chamadas em português ("link da bio"); o aviso de "sem chamada" nesse caso é falso.

## Carrosséis (pedido da Nina, 20/10)

- Todo carrossel começa pela skill **ig-carousel** (`.claude/skills/ig-carousel`) para a estrutura e o texto: capa
  curta, uma ideia por slide, chamada única no final.
- O design continua com os geradores do projeto (HTML renderizado em PNG, `instagram/ferramentas/render.mjs`) e o
  Canva, no estilo da marca (`instagram/diretrizes-criativas.md` e `instagram/carrossel.md`).
- Quando a skill e a marca discordam, vale a marca:
  - de 5 a 8 slides, nunca mais que 8 (a skill pede de 6 a 10);
  - sem numerar os slides (a Nina tirou os números do carrossel de 21/10);
  - nada de slide-resumo que diga a mensagem de forma explícita demais; a conclusão aparece nos fatos (retorno da
    Nina sobre o conteúdo v7 de 21/10);
  - comunicação B2B, sem frases de acolhimento direto ao leitor.
- No Canva, antes de alterar um slide, duplicar a versão antiga daquele slide no mesmo design.

## Levar um post para o Canva

O Canva importa HTML por URL pública. O repositório é público, então:

1. Gere um `canva.html` autocontido a partir do `slides.html` com
   `node instagram/ferramentas/canva.mjs <slides.html> <canva.html>`. Ele embute
   CSS, fontes e logo e liga o bloco `<style media="canva">` do post, se houver.
   Por trás, o que o Canva precisa: CSS, fontes e
   logo embutidos em base64 (o GitHub serve CSS e fontes como texto puro, e o
   Canva ignora). Também é preciso marcar cada `<section class="slide">` com
   `data-document-role="page"` e trocar as molduras de foto por formas lisas,
   sem filtro nem retícula.
2. Faça commit e push, e importe pelo endereço raw com o hash do commit (não
   com o nome do branch, que fica em cache):
   `https://raw.githubusercontent.com/nina-rebello/comunicao-fh/<commit>/instagram/posts/<nome>/canva.html`
3. Confira as miniaturas no Canva. O que o Canva não respeita na conversão:
   `display:flex` com `gap` (use posição absoluta), `padding` dentro de texto
   com fundo (use `&nbsp;`), `box-decoration-break` (uma pílula por linha) e
   `border-left` em texto (use uma `div` separada como barra).
   Também (post de 30/10): duas fontes na mesma caixa de texto (o trecho em
   serif vira outra caixa), `inline-block` lado a lado (use posição absoluta),
   SVG com posição absoluta (ponha o SVG dentro de um `div` posicionado),
   `line-height` para centrar texto numa forma (calcule o `top`), texto em
   degradê e elementos girados. Quebre as linhas dos títulos com `<br>` e deixe
   folga na largura: no Canva o texto sai um pouco mais largo.
