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
