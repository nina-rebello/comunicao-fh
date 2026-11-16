# Foto única 19/11: Depoimentos

**Quinta, 19/11** (sexta, 20/11, é feriado da Consciência Negra). Semana 3, bloco 5, eixo Cases. É o N09 de
`marketing/ferramentas/conteudo_posts_novembro.py`. Vem depois do carrossel da NR-01 (18/11) e antes do Reel
"Quem cuida do RH?" (23/11).

**Status:** arte v2 para aprovação (16/11), mais limpa. A v1 fica em `slides-v1.html`, `png-v1/`, `previa-v1.png`.

- **Arte** (1080x1350): `png/d-01.png` (também em `previa.png`).
- **Canva:** `canva.html` (autocontido). Para importar, siga o `CLAUDE.md` (commit, push e endereço raw com o
  hash do commit).
- **Para regerar:**
  ```
  python3 instagram/posts/depoimentos/gerar.py
  node instagram/ferramentas/render.mjs instagram/posts/depoimentos/slides.html instagram/posts/depoimentos/png
  node instagram/ferramentas/canva.mjs instagram/posts/depoimentos/slides.html instagram/posts/depoimentos/canva.html
  ```
  O `gerar.py` faz o fundo (Tiffany com grade fina, brilho creme e granulado) como imagem.

## A ideia

Referência enviada pela Nina em 04/11: depoimentos em balões de conversa sobre um fundo de cor com grade, título
"Depoimentos", uma frase de fecho e um rodapé com a marca. Nos nossos tons:

- fundo Tiffany `#9FC5BD` com grade branca fina e brilho creme no canto de baixo;
- título "Depoimentos" em Raleway 800, com o rótulo "Escritório do Cuidado";
- três balões, um por fonte, alternando a margem como na referência:
  - **colaboradora (vídeo):** "Os meus hábitos mudaram, e não foi um sacrifício. [...] Não é aquela dieta
    impossível de fazer. É algo pra vida." (A2 + A1);
  - **colaboradora (e-mail):** "Agradeço por me ajudar a olhar para as minhas conquistas com mais gentileza e
    reconhecer que o processo não precisa ser perfeito para estar funcionando." (B2 + B1);
  - **equipe (WhatsApp), balão verde com o logo:** "Ficamos bem felizes ao ouvir de uma paciente o quanto o que
    estamos fazendo mudou a cultura da empresa. [...] Todos estão se alimentando mais saudável, se movimentando
    mais e fazendo melhores escolhas." (C1 + C2);
- fecho em Instrument Serif: "O que é bom a gente tem que compartilhar." (A5);
- rodapé branco com o logo, @fairhealth.br e o slogan "Fazemos o certo pelos motivos certos.";
- letra miúda: "Trechos de depoimentos e de relato da equipe, publicados com autorização e sem nomes. Cortes marcados
  com [...]."

## Como as regras de depoimento foram seguidas (`instagram/depoimentos.md` e `voice.md`)

- **Sem rosto:** a referência usa fotos de pessoas; aqui os avatares são pictogramas (colaboradoras) e o logo
  (equipe). Foto de banco no avatar faria parecer que aquela pessoa deu o depoimento.
- **Sem nome e sem condição de saúde:** o e-mail entra sem o nome e sem a parte do joelho; o relato da equipe
  entra sem o nome da médica.
- **Sem resultado clínico:** do WhatsApp ficaram de fora o número de pacientes, exames, receitas, bioimpedância,
  "recomposição corporal" e "vendo resultado nos colegas". Ficaram cultura e hábito.
- **Cortes marcados com [...]** e limpeza mínima de transcrição ("Também agradeço" virou "Agradeço"; "o que
  estamos fazendo lá" virou "o que estamos fazendo"; "Que todos estão" virou "Todos estão").
- **Sem hora falsa:** a referência mostra "15:30" em cada balão; aqui só o "lido" (✓✓), porque os trechos não são
  mensagens daquele horário.

## Pendências

- [ ] Aprovação da arte pela Nina.
- [ ] **Autorização por escrito** da colaboradora do e-mail para publicar o trecho, mesmo sem nome, e ok da
      Dra. Marília para o relato. A letra miúda diz "publicados com autorização": só publicar com as duas.
- [ ] Dr. Ronald: formato dos depoimentos (CFM), a mesma pendência do post de 03/11.
- [x] Legenda (16/11): em `legenda.txt`, com os três trechos, o Escritório como no site (profissionais, bioimpedância
      e smartwatches, plano pela Medicina do Estilo de Vida) e o Comente CUIDADO; conferida com `caption.py` e `detect.py`.
- [ ] Texto alternativo: "Fundo verde-água com grade. Título: Depoimentos. Três balões de conversa com trechos de
      depoimentos de colaboradoras e da equipe do Escritório do Cuidado, e a frase: O que é bom a gente tem que
      compartilhar."

## Revisão de 16/11 (regras de 12 e 13/11)

A arte não precisou mudar: é uma imagem só (sem numeração), sem diagnóstico gratuito, sem prazo de programa e sem
descrever o serviço. A legenda nova (`legenda.txt`) é que cita bioimpedância e smartwatches e a Medicina do Estilo de
Vida dentro do Escritório. As autorizações por escrito continuam pendentes.

## v2 (16/11): mais elegante, menos formas

Pedido da Nina: sem foto de perfil e com algo mais elegante, sem formas que deixem o post infantil. Referências:
balões de mensagem do iOS e um "Feedback de Cliente" em fundo verde chapado com balões brancos.

- **Fundo verde-escuro liso** (`#2A625B`), sem grade nem brilho.
- **Título centrado:** "Escritório do Cuidado" (menta, caixa alta espaçada) e "Depoimentos" em Raleway 800 branco.
- **Três balões de mensagem com rabicho**, sem avatar e sem os tiques de lido: as duas colaboradoras em branco, à
  esquerda; a equipe em Tiffany, à direita, como resposta. A assinatura fica dentro do balão, em caixa alta pequena
  ("Colaboradora atendida", "Equipe do Escritório do Cuidado").
- **Pé:** a frase "O que é bom a gente tem que compartilhar." em serif itálico menta, o logo com @fairhealth.br e a
  letra miúda. Saíram o cartão branco do rodapé, o slogan e o traço do título.
- Os balões são SVG dentro de `div` posicionado (regra do Canva). O `slides.html` é gerado por `gerar_v2.py`.
- O texto dos depoimentos não mudou.
