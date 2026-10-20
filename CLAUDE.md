# Instruções para o Claude

Conteúdo do Instagram da fairhealth (@fairhealth.br). O índice dos materiais está em `instagram/README.md`. As
regras da marca estão em `instagram/voice.md`, `instagram/essencia.md` e `instagram/diretrizes-criativas.md`.

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
  Canva, no estilo da marca (`instagram/diretrizes-criativas.md`).
- Quando a skill e a marca discordam, vale a marca:
  - de 5 a 8 slides (a skill pede de 6 a 10);
  - sem numerar os slides (a Nina tirou os números do carrossel de 21/10);
  - nada de slide-resumo que diga a mensagem de forma explícita demais; a conclusão aparece nos fatos (retorno da
    Nina sobre o conteúdo v7 de 21/10);
  - comunicação B2B, sem frases de acolhimento direto ao leitor.
- No Canva, antes de alterar um slide, duplicar a versão antiga daquele slide no mesmo design.
