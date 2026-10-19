# Post de qua 21/10: Por que a fairhealth existe? · acolhimento forte

## Testes de design, rodada 2 (19/10)

Mais três referências, no mesmo formato da rodada 1.

**Arquivos:**
- imagem única: `testes-design-2.jpg`, montada a partir de `testes-design-2.html`;
- gerador: `gerar_testes_design_2.py`;
- slides: `testes-design-2-slides.html` → `png-testes-2/`;
- conteúdo compartilhado: `conteudo_v6.py`.

**As três faixas:**
- **F · Jornada** ("Jornada de conteúdo imobiliário"):
  - fundo verde-escuro, com blocos Tiffany na capa;
  - o coração da marca como objeto grande, na capa e no final;
  - número do slide em cima e título em Tiffany;
  - medidor em meia-lua (1/6 a 6/6, o avanço da história);
  - listas com ícones nos slides 4 e 6;
  - foto em cartão arredondado;
  - final com a frase e os ícones do Instagram.
- **G · caixa alta e papel rasgado** ("Toda empresa começa com uma história"):
  - caixa alta enorme e uma etiqueta inclinada ("2009 → hoje");
  - ícones grandes em traço fino no lugar das ilustrações, sem personagens;
  - itálico centralizado e texto pequeno em caixa alta;
  - trechos sublinhados no slide escuro;
  - no slide 4, o render do espaço com borda de papel rasgado e um bilhete.
- **H · Polina:**
  - papel creme com textura;
  - linha fina em verde, com dois laços;
  - números de 01 a 07 nas bolinhas;
  - texto grande e anotações curtas;
  - cabeçalho e rodapé em Tiffany;
  - final alinhado à direita, com a linha chegando ao logo.

**Imagens:** são fotos do banco Unsplash, a smartband e o render do Escritório do Cuidado. O render ainda está marcado
como **[PENDENTE]** em `referencias.md`. Tudo isso é só para testar.

## Testes de design (19/10)

Pedido da Nina: "vamos testar designs. Em uma imagem só, crie vários carrosséis em uma única sequência (largura
única e grande com todos os slides juntos). Faça uma versão para cada design que vou enviar."

**Arquivos:**
- imagem única: `testes-design.jpg`, montada a partir de `testes-design.html`;
- gerador: `gerar_testes_design.py`;
- slides: `testes-design-slides.html` → `png-testes/`.

Cada faixa é um carrossel inteiro, com o conteúdo final (v6) e os 8 slides lado a lado.

**As cinco faixas:**
- **A · caminho largo** (Eleken): é a arte v7.
- **B · editorial com capítulos** (template "Why We Started Our Business"):
  - capítulos no cabeçalho;
  - foto em moldura na capa;
  - caixa de citação;
  - quadro "2009 | Hoje";
  - lista numerada;
  - final escuro.
- **C · linha do tempo com hastes** ("Life of a video editor"): fundo verde-escuro e uma linha fina com brilho. Nos
  marcos, bolinha e haste até o rótulo. O slide 6 tem três hastes, uma por item.
- **D · frase forte e linha reta** ("founders"): fundo quase preto e frase grande. A linha nasce numa bolinha Tiffany
  na capa e atravessa todos os slides até o logo.
- **E · palavra gigante e curva** ("O poder da sua pausa"): creme, com uma palavra enorme em caixa alta. Embaixo, a
  curva Tiffany com patamares, um por slide, até o logo.

**Fotos:** as fotos da B são do banco Unsplash, só para testar.

## Arte v7 (19/10), o caminho largo (referência Eleken)

A partir das novas referências da Nina. A principal é o carrossel "Customer Journey Map", da Eleken.

**Arquivos:**
- gerador: `gerar_slides_v7.py`;
- saída: `slides-v7.html` e `png-v7/` (v01 a v08);
- prévia: `previa-v7.jpg`.

**Como ficou:**
- **O caminho:** uma faixa larga em creme, sempre da mesma espessura, com curvas lisas e abertas. Serpenteia de um
  slide para o outro, sem tremido e sem canto quadrado.
  - Na capa, nasce numa bolinha verde e sobe pela direita.
  - No slide 3, sobe pela direita.
  - No slide 4, passa por cima.
  - No slide 5, desce pela esquerda.
  - No final, chega ao logo.
- **Bolinhas verdes:** marcam cada etapa no caminho.
- **Títulos:** curtos e fortes, como na referência:
  - "2009" e "hoje" em número grande;
  - "No hospital", "O acolhimento", "O que levamos", "Perto" e "O propósito".
  Embaixo de cada um vem o texto aprovado (conteúdo v6), grande.
- **Slide 6:** os três itens ficam num cartão claro com marcadores, como os cartões da referência.
- **Detalhes:**
  - em cima, o nome fairhealth (capa) e a página numa pílula (1/8 a 8/8);
  - embaixo, fairhealth e uma barra de progresso;
  - fundo Tiffany com textura leve.

As versões anteriores ficam guardadas.

## Direção para a próxima arte (19/10), antes de refazer

A Nina explicou: "reta eu não quis dizer quadrada, só não queria aquele aspecto de rabisco torto". Ela mandou mais
referências e vai mandar outras no próximo chat. A arte só será refeita depois disso. As imagens das referências não
entram no repositório.

**O que tirar de cada referência:**
- **"Life of a video editor":** uma linha horizontal fina atravessa o slide. Nos marcos, uma bolinha e uma haste
  vertical fina sobem até o rótulo. Serve para "2009" e "hoje".
- **Silvio Santos (Grids):** a linha é reta, mas vira com cantos bem arredondados (raio grande) e contorna o bloco de
  texto. Nada de canto quadrado.
- **"The process that founders never talk about":** uma bolinha grande abre a linha, que sai pela borda do slide e
  continua no próximo.
- **"O poder da sua pausa" (nosso):** curva lisa e regular, com espessura constante e geometria limpa.
- **Polina (processo de trabalho):** a linha contínua entre os slides e as anotações curtas.

**Para a linha:** trechos retos ligados por curvas de raio grande, ou curvas geométricas regulares, sempre com a
mesma espessura e sem tremido. Nos marcos, bolinha e haste.

## Arte v6 (19/10), linhas retas

Pedido da Nina sobre a v5: "essas linhas, faça elas sem parecer rabisco, faça linhas retas".

**Arquivos:**
- gerador: `gerar_slides_v6.py`, duplicado da v5, que fica guardada;
- saída: `slides-v6.html` e `png-v6/`;
- prévia: `previa-v6.jpg`.

**O que mudou:**
- **A linha:** passou a ser só de trechos retos, horizontais e verticais, com cantos levemente arredondados. Ela
  desce e sobe em degraus entre os slides, sem laços.
- **O resto:** o conteúdo, o fundo, as bolinhas, o "2009", o "hoje" e as anotações continuam iguais à v5. Só a
  posição de alguns elementos mudou, para acompanhar a linha nova.

## Conteúdo v6 (19/10), o final da Nina

A Nina reescreveu os três primeiros slides. O resto ficou igual à v5. São 8 slides.

| Slide | Título | Apoio |
| --- | --- | --- |
| 1 · capa | Antes de chegar às empresas, nossa história começou *em um hospital*. | 2009 → hoje (cabeçalho: por que a fairhealth existe?) |
| 2 | Há quase 20 anos, percebemos que os pacientes estavam *cada vez mais distantes do centro do cuidado*. | Era preciso mudar essa realidade. |
| 3 | Assim, dentro de um hospital, desenvolvemos o *Escritório do Paciente* para mudar essa realidade. | Com o tempo, levamos esse conceito para as empresas. |
| 4 | Assim, desenvolvemos o *Escritório do Cuidado*. | Um espaço de acolhimento e de medicina preventiva dentro da empresa, que fortalece o cuidado centrado na pessoa. |
| 5 | Tudo começa com uma pergunta: *o que é importante para você?* | Antes de qualquer exame, vem uma conversa: um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado. |
| 6 | Levamos ao *coração da sua empresa*: | atendimento médico e psicológico · planos de cuidado individualizados, baseados na Medicina do Estilo de Vida · tecnologia, humanização e cuidado verdadeiro |
| 7 | Porque, quando o cuidado está perto, *ele acontece*. | A maior barreira ao cuidado é tempo e acesso. Por isso, o Escritório do Cuidado fica dentro da empresa, perto da rotina de quem trabalha. |
| 8 · final | Nosso propósito é promover *qualidade de vida, engajamento e um ambiente de trabalho mais saudável*. | Com resultados demonstrados por indicadores. Faça o certo pelos motivos certos. / Conheça a fairhealth no link da bio. |

A legenda é a da v5.

**Para a Nina ver:**
- "mudar essa realidade" aparece nos slides 2 e 3, um logo depois do outro.
- O "Assim" abre os slides 3 e 4.

Ficou como ela escreveu. Para variar, uma opção seria tirar "para mudar essa realidade" do slide 3.

## Arte v5 (19/10), no estilo da v4, com o conteúdo v6

**Arquivos:**
- gerador: `gerar_slides_v5.py`, duplicado da v4, que fica guardada;
- saída: `slides-v5.html` e `png-v5/` (u01 a u08);
- prévia: `previa-v5.jpg`.

**Como ficou:**
- **Estilo:** igual ao da v4. Fundo Tiffany com textura de papel, linha fina e verde atravessando os 8 slides e
  textos grandes.
- **Laços:** um na capa e outro no slide da conversa (slide 5).
- **Números em creme:** "2009" no slide 2 e "hoje" no slide 4, que é o do Escritório do Cuidado.
- **Slide 6:** os três itens do que levamos ficam em três bolinhas ao longo da linha.
- **Slide 8:** o texto fica alinhado à direita e a linha termina no logo.
- **Anotações:**
  - "2009 → hoje";
  - "nas empresas";
  - "dentro da empresa";
  - "faça o certo pelos motivos certos";
  - "conheça a fairhealth no link da bio".
- **Cabeçalho:** @fairhealth.br e "por que a fairhealth existe?".

## Conteúdo v5 (19/10), substituído pela v6

Resposta da Nina à v4: "não vamos focar na criação do Escritório do Paciente e sim no Escritório do Cuidado". O
Escritório do Paciente aparece só como contexto, numa linha do slide 2.

O que continua da v4:
- "desenvolvemos" no lugar de "surgiu";
- a linha do reel do Dr. Ronald, sem o nome;
- o acolhimento forte, tema do dia no calendário.

| Slide | Etiqueta | Título | Apoio |
| --- | --- | --- | --- |
| 1 · capa | Nossa história | Por que a fairhealth *existe*? | a resposta começa com uma pergunta |
| 2 | O porquê | Há quase 20 anos, percebemos que os pacientes estavam *cada vez mais distantes do centro do cuidado*. | Dentro de um hospital, desenvolvemos o Escritório do Paciente para mudar essa realidade. Com o tempo, levamos esse conceito para as empresas. |
| 3 | Nas empresas | Assim, desenvolvemos o *Escritório do Cuidado*. | Um espaço de acolhimento e de medicina preventiva dentro da empresa, que fortalece o cuidado centrado na pessoa. |
| 4 | O acolhimento | Tudo começa com uma pergunta: *o que é importante para você?* | Antes de qualquer exame, vem uma conversa: um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado. |
| 5 | O que levamos | Levamos ao *coração da sua empresa*: | atendimento médico e psicológico · planos de cuidado individualizados, baseados na Medicina do Estilo de Vida · tecnologia, humanização e cuidado verdadeiro |
| 6 | Perto | Porque, quando o cuidado está perto, *ele acontece*. | A maior barreira ao cuidado é tempo e acesso. Por isso, o Escritório do Cuidado fica dentro da empresa, perto da rotina de quem trabalha. |
| 7 · final | O propósito | Nosso propósito é promover *qualidade de vida, engajamento e um ambiente de trabalho mais saudável*. | Com resultados demonstrados por indicadores. Faça o certo pelos motivos certos. / Conheça a fairhealth no link da bio. |

**De onde vem cada slide:**
- **Slide 1:** título do calendário ("Por que a FairHealth existe?"). A anotação vem de "Tudo começa com uma
  pergunta", tema do Mês 1 no posicionamento.
- **Slides 2, 3, 5 e 7:** roteiro do reel do Dr. Ronald, com "desenvolvemos". O "espaço de acolhimento e de
  medicina preventiva" do slide 3 vem da essência ("Em uma frase").
- **Slide 4:** a pergunta-assinatura e a dinâmica das consultas, na essência (a conversa vem antes dos exames). O
  apoio é o do conteúdo aprovado da v3.
- **Slide 6:**
  - "Proximidade gera adesão. A maior barreira ao cuidado é tempo e acesso; por isso o espaço fica dentro da
    empresa" (essência);
  - "quando o cuidado está perto, ele acontece" (v3).

**Legenda v5:**

```
A fairhealth existe para colocar as pessoas de volta no centro do cuidado.

Há quase 20 anos, percebemos que os pacientes estavam cada vez mais distantes desse centro. Com o tempo, levamos esse conceito para as empresas e desenvolvemos o Escritório do Cuidado: um espaço de acolhimento e de medicina preventiva dentro da empresa, onde tudo começa com uma pergunta, "O que é importante para você?".

Porque, quando o cuidado está perto, ele acontece.

Faça o certo pelos motivos certos. Conheça a fairhealth no link da bio.

#fairhealth #saudecorporativa #medicinapreventiva #cuidadohumanizado #escritoriodocuidado
```

**Validar:**
- "com resultados demonstrados por indicadores" é fala do reel, sem número.
- A arte v4 (fundo Tiffany e linha fina) ainda está com o conteúdo v3. Ajustar depois que a v5 for aprovada.

## Conteúdo v4 (19/10), substituído pela v5

Dois feedbacks sobre a v3:
- "Eu daria mais peso na autoria do Ronald. 'Surgiu' poderia dar impressão que aconteceu em algum lugar e imitamos."
- "Poderíamos seguir mais ou menos o roteiro do reels que gravarei hoje. Não precisa colocar nome, só escrever que
  desenvolvemos."

Então:
- **Sai o "surgiu", entra "desenvolvemos"** nos dois projetos.
- **A ordem segue o roteiro do reel:** percebemos o problema, desenvolvemos o Escritório do Paciente, levamos o
  conceito para as empresas com o Escritório do Cuidado, o que levamos e o propósito.
- **O acolhimento continua** no slide 4.
- **O fechamento** é a frase do reel: "Faça o certo pelos motivos certos."

| Slide | Etiqueta | Título | Apoio |
| --- | --- | --- | --- |
| 1 · capa | Nossa história | Antes de chegar às empresas, nossa história começou *em um hospital*. | de 2009 até hoje |
| 2 | 2009 | Há quase 20 anos, percebemos que os pacientes estavam *cada vez mais distantes do centro do cuidado*. | Era preciso mudar essa realidade. |
| 3 | No hospital | Assim, desenvolvemos o *Escritório do Paciente*. | Um modelo de cuidado inspirado nos princípios do Triple Aim, para trazer o paciente de volta ao centro, com a escuta, o acolhimento e as necessidades de cada pessoa em primeiro lugar. |
| 4 | A essência | Por trás de cada atendimento, existe *uma pessoa*. | Por isso, antes de qualquer exame, vem uma conversa: um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado. |
| 5 | Nas empresas | Com o tempo, levamos esse conceito para as empresas e desenvolvemos o *Escritório do Cuidado*. | Um projeto novo, inspirado no Escritório do Paciente, que fortalece o cuidado centrado na pessoa. |
| 6 | Hoje | Levamos ao *coração da sua empresa*: | atendimento médico e psicológico · planos de cuidado individualizados, baseados na Medicina do Estilo de Vida · tecnologia, humanização e cuidado verdadeiro |
| 7 | O propósito | Os lugares mudaram. *A essência do cuidado permanece.* | Nosso propósito é promover qualidade de vida, engajamento e um ambiente de trabalho mais saudável, com resultados demonstrados por indicadores. |
| 8 · final | | Faça o certo *pelos motivos certos*. | Dê esse presente para o seu time. Chame a fairhealth: link na bio. |

**De onde vem cada slide:**
- **Roteiro do reel do Dr. Ronald (19/10), sem o nome:** slides 2, 3, 5, 6, 7 (o propósito) e 8.
- **Conteúdo aprovado da v3:**
  - capa;
  - a escuta e o acolhimento (slide 3);
  - slide 4 inteiro;
  - "um projeto novo, inspirado no Escritório do Paciente" (slide 5);
  - "Os lugares mudaram. A essência do cuidado permanece." (slide 7).

**Legenda v4** (mais curta, na linha do reel):

```
Há quase 20 anos, percebemos que os pacientes estavam cada vez mais distantes do centro do cuidado. Era preciso mudar essa realidade.

Foi assim que desenvolvemos o Escritório do Paciente, dentro de um hospital. Com o tempo, levamos esse conceito para as empresas e desenvolvemos o Escritório do Cuidado: atendimento médico e psicológico e planos de cuidado individualizados, perto da rotina de quem trabalha.

Os lugares mudaram. A essência do cuidado permanece.

Faça o certo pelos motivos certos. Conheça a fairhealth no link da bio.

#fairhealth #saudecorporativa #medicinapreventiva #cuidadohumanizado #escritoriodocuidado
```

**Validar:**
- **Triple Aim:** entra só como no reel ("inspirado nos princípios do Triple Aim"), sem explicação. Se quiserem
  explicar, a definição oficial do IHI é melhorar a experiência do cuidado, melhorar a saúde da população e reduzir
  o custo per capita. A `essencia.md` resume como "qualidade, acesso, custo": vale conferir antes de usar.
- **2009 e "há quase 20 anos":** a arte usa o "2009" grande e o texto usa "há quase 20 anos", a fala do reel.
  2009 dá 17 anos, o que cabe no "quase 20".
- **"Dê esse presente para o seu time":** frase do reel; é opcional no carrossel.
- **A arte v4** ainda está com o conteúdo v3 (7 slides). Ajustar depois que o conteúdo v4 for aprovado.

## Arte v4 (19/10), recomeço: chique, elegante e Tiffany

Pedido da Nina: "vamos começar do início, tire todos esses personagens, faça algo mais chique e elegante, foque mais
no Tiffany que no creme". A inspiração é o carrossel de processo de trabalho que ela mandou.

**Arquivos:**
- gerador: `gerar_slides_v4.py`;
- saída: `slides-v4.html` e `png-v4/` (t01 a t07);
- prévia: `previa-v4.jpg`.

**Como ficou:**
- **Fundo:** Tiffany em todos os slides, com textura de papel.
- **A linha:** fina, lisa e verde. Atravessa os sete slides, faz um laço na capa e outro na conversa (slide 4) e
  termina no logo.
- **Marcos:** bolinhas na linha. "2009" e "hoje" aparecem grandes, em creme, com uma anotação ao lado. Os outros
  marcos levam uma etiqueta: a essência, o acolhimento e a evolução.
- **Textos:** grandes e soltos, de um lado da linha. No final, ficam alinhados à direita, como na referência.
- **Anotações:** curtas, em Raleway itálico, todas do material base:
  - "de 2009 até hoje";
  - "onde tudo começou";
  - "o que é importante para você?";
  - "perto da rotina das pessoas";
  - "a gente tá aqui pra te ouvir".
- **Cabeçalho e rodapé (em creme):**
  - cabeçalho: @fairhealth.br e "nossa história";
  - rodapé: "fairhealth | o cuidado começa pela pessoa", com uma seta fina.
- **Desenhos e personagens:** nenhum.

As versões v1 a v3 ficam guardadas.

## Arte v3 (19/10), desenhada sutilmente

O que a Nina disse sobre a v2: "menos rabiscado e mais desenhado sutilmente". Ela gostou da linha que atravessa
todos os slides, mas achou os bonequinhos toscos.

**Arquivos:**
- gerador: `gerar_slides_v3.py`;
- saída: `slides-v3.html` e `png-v3/`;
- prévia: `previa-v3.jpg`.

**O que mudou:**
- **A linha que atravessa os slides:** igual à da v2.
- **Pessoas:** os bonequinhos saíram. Entraram pessoas ilustradas em traço fino, do Open Peeps (CC0), no verde da
  marca e com preenchimento branco. Os arquivos estão em `../../marca/peeps/`, com a origem e a licença.
  - Capa: alguém caminhando na linha.
  - Slide 3: uma pessoa no centro, com as setas para a história, os hábitos, as necessidades e as prioridades.
  - Slide 4: quem pergunta "O que é importante para você?" e quem responde com um coração.
  - Slide 5: alguém a caminho do trabalho.
  - Final: alguém apontando para o logo.
- **Os outros desenhos (hospital, prédio, balões, setas, brilhos):** traço mais fino e firme, sem hachura.
- **Marca-texto:** virou uma faixa lisa em Tiffany atrás da palavra, e em creme nos slides Tiffany.

A v2 fica guardada.

## Arte v2 (19/10), rabiscada

Pedido da Nina: "algo totalmente diferente" da arte v1, "mais rabiscado, com elementos mais divertidos que humanizam
os slides". As referências dela foram:
- um carrossel de processo de trabalho, com papel com textura, um fio fino que faz curvas e laços e anotações à mão;
- uma linha do tempo com pessoinhas caminhando.

**Arquivos:**
- gerador: `gerar_slides_v2.py`;
- saída: `slides-v2.html` e `png-v2/` (r01 a r07);
- prévia: `previa-v2.jpg`.

**Como ficou:**
- **Papel com textura:** Tiffany na capa e no final, creme nos slides 2 a 6.
- **O fio:** um fio verde desenhado à mão atravessa os sete slides. Ele nasce na capa, marca 2009 e hoje com uma
  bolinha, faz um laço na conversa (slide 4) e termina no logo.
- **Desenhos à mão (rough.js, licença MIT):**
  - pessoinhas;
  - o hospital (2009) e o prédio da empresa, que no slide 6 ganha um coração;
  - balões de fala, com a pergunta "O que é importante para você?";
  - setas, brilhos e marca-texto Tiffany nas palavras de destaque.
- **Anotações:** em Raleway itálico, inclinadas. Não usei fonte manuscrita, por causa da regra de só usar Raleway.
- **De onde vêm as anotações:**
  - "há quase 20 anos": roteiro do reel do Dr. Ronald;
  - "sem pressa e sem julgamento" e "a gente tá aqui pra te ouvir": vídeo de acolhimento
    (`primeiros-posts-acolhimento.md`);
  - "dentro da empresa": essência;
  - "a sua história", "seus hábitos", "suas necessidades" e "suas prioridades": o texto do slide 3, que virou
    setas em volta da pessoinha.
- **No Canva:** os textos entram editáveis. Os desenhos e o fio entram como imagem, uma camada por slide.

A arte v1 fica guardada.

## Arte v1 (19/10)

- **Base:** a arte do post da origem que a Nina aprovou (`../nossa-historia/`, v2). O gerador foi duplicado de
  `gerar_slides_v2.py`; o original fica intacto.
  - Gerador: `gerar_slides.py`.
  - Saída: `slides.html` e `png/` (e01 a e07).
  - Prévia: `previa.jpg`.
- **O que se mantém:** capa de luz, fio creme contínuo de 2009 até o logo, "2009" grande e Tiffany como cor
  principal.
- **O que muda:**
  - 7 slides, com fundos luz, Tiffany, verde, Tiffany, verde, Tiffany e verde;
  - slide 4 (acolhimento): o fio passa por uma foto em círculo (`maos.jpg`, Unsplash, 75% de saturação);
  - slide 6: "Hoje" grande, no mesmo modelo do "2009", para marcar que são dois projetos, cada um no seu tempo;
  - etiquetas "No hospital" (slide 2) e "Nas empresas" (slide 6).

> **v3 (19/10), a versão que vale.** Igual à v2, com um ponto corrigido a pedido da Nina: **o Escritório do Paciente
> e o Escritório do Cuidado são projetos diferentes.** O primeiro nasceu no hospital; o segundo é um projeto novo,
> inspirado nele e pensado para as empresas. Sai o "virou". Inspiração sutil: o roteiro que o Dr. Ronald usou no
> reel ("os pacientes estavam cada vez mais distantes do centro do cuidado"; "trouxemos esse conceito para as
> empresas e assim surgiu o Escritório do Cuidado, fortalecendo o cuidado centrado na pessoa").
>
> | Slide | Etiqueta | Título | Apoio | O que mudou da v2 |
> | --- | --- | --- | --- | --- |
> | 1 · capa | Nossa história | Antes de chegar às empresas, nossa história começou *em um hospital*. | 2009 → hoje | igual |
> | 2 | 2009 · No hospital | Dentro de um hospital, surgiu o *Escritório do Paciente*. | Um modelo de cuidado criado para trazer o paciente de volta ao centro, com a escuta, o acolhimento e as necessidades de cada pessoa em primeiro lugar. | o motivo do projeto (roteiro do Dr. Ronald) |
> | 3 | A essência | Por trás de cada atendimento, existe *uma pessoa*. | Com a sua própria história, hábitos, necessidades e prioridades. Por isso, escutar sempre foi parte essencial da nossa maneira de cuidar. | igual |
> | 4 | O acolhimento | Antes de qualquer exame, *uma conversa*. | Um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado. | igual |
> | 5 | Evolução | Com o tempo, essa forma de cuidar *evoluiu*. | E o conceito chegou a um lugar que faz parte da rotina das pessoas: o trabalho. Porque, quando o cuidado está perto, ele acontece. | "o conceito chegou" |
> | 6 | Hoje · Nas empresas | Assim surgiu o *Escritório do Cuidado*, da fairhealth. | Um projeto novo, inspirado no Escritório do Paciente e pensado para as empresas: um espaço de acolhimento e de medicina preventiva, com cuidado individualizado e acompanhamento. | dois projetos, sem "virou" |
> | 7 | O propósito | Os lugares mudaram. *A essência do cuidado permanece.* | Do hospital às empresas, seguimos com um mesmo princípio: o cuidado começa pela pessoa. | "Do hospital às empresas" |
>
> As etiquetas "2009 · No hospital" (slide 2) e "Hoje · Nas empresas" (slide 6) marcam na arte que são dois
> projetos, cada um no seu lugar e no seu tempo.
>
> **Legenda:**
>
> ```
> A história por trás da fairhealth começou muito antes de chegarmos às empresas.
>
> Em 2009, dentro de um hospital, nascia o Escritório do Paciente, para trazer as pessoas de volta ao centro do cuidado: um modelo que tinha a escuta, o acolhimento e as necessidades de cada pessoa como ponto de partida.
>
> Com o tempo, levamos esse conceito para as empresas, e assim surgiu um novo projeto: o Escritório do Cuidado. Um espaço de acolhimento e de medicina preventiva, perto da rotina das pessoas, onde antes de qualquer exame vem uma conversa.
>
> Porque, para nós, cuidar não é apenas olhar para a saúde. É olhar para quem está por trás dela.
>
> O cuidado começa pela pessoa.
>
> #fairhealth #saudecorporativa #medicinapreventiva #cuidadohumanizado #escritoriodocuidado
> ```
>
> **Fica para outro post:** o Triple Aim e os outros "Aims" vão para a linha do tempo do post 10 (10/11).
> **Validar:** 2009 (o roteiro do Dr. Ronald diz "há quase 20 anos", o que bate). Sem o nome do hospital.

---

## v2 (19/10), guardada

> **v2 (19/10).** A Nina prefere o roteiro original do post 02 (`instagram/posts/nossa-historia/`,
> v2). A base continua aquela, só com mais acolhimento. São 7 slides (o ideal é de 5 a 8). Nada novo foi criado do
> zero: cada acréscimo vem do material base.
>
> **De onde vem cada acréscimo:**
> - "um espaço de acolhimento e de medicina preventiva" (`essencia.md`, "Em uma frase");
> - "Antes de qualquer exame, uma conversa" (`essencia.md`, dinâmica das consultas: a conversa e a pergunta vêm
>   antes da bioimpedância e da smartband; é o gancho do Reel de boas-vindas em `primeiros-posts-acolhimento.md`);
> - "acolhimento, confidencialidade" (o que o colaborador precisa ouvir) e "escuta, autonomia, decisão
>   compartilhada, acolhimento, confidencialidade" (território "Cuidado centrado na pessoa"), no
>   `Plano_Marketing_Fairhealth_Consolidado.docx`;
> - "Proximidade gera adesão" (`essencia.md`, "Em que a gente acredita"), o que o RH quer ouvir.
>
> | Slide | Etiqueta | Título | Apoio | O que mudou |
> | --- | --- | --- | --- | --- |
> | 1 · capa | Nossa história | Antes de chegar às empresas, nossa história começou *em um hospital*. | 2009 → hoje | igual |
> | 2 | O início | 2009 · Dentro de um hospital, surgiu o *Escritório do Paciente*. | Um modelo de cuidado que colocava a escuta, o acolhimento e as necessidades de cada pessoa no centro da atenção. | + "o acolhimento" |
> | 3 | A essência | Por trás de cada atendimento, existe *uma pessoa*. | Com a sua própria história, hábitos, necessidades e prioridades. Por isso, escutar sempre foi parte essencial da nossa maneira de cuidar. | igual |
> | 4 | O acolhimento | Antes de qualquer exame, *uma conversa*. | Um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado. | **novo** |
> | 5 | Evolução | Com o tempo, essa forma de cuidar *evoluiu*. | E chegou a um lugar que faz parte da rotina das pessoas: o trabalho. Porque, quando o cuidado está perto, ele acontece. | + a frase da proximidade |
> | 6 | Hoje | Hoje, essa filosofia está presente na *fairhealth*. | Levamos para dentro das empresas um espaço de acolhimento e de medicina preventiva, com cuidado individualizado e acompanhamento. O Escritório do Paciente virou o Escritório do Cuidado. | + "espaço de acolhimento" |
> | 7 | O propósito | Os lugares mudaram. *A essência do cuidado permanece.* | Da experiência hospitalar ao ambiente corporativo, seguimos com um mesmo princípio: o cuidado começa pela pessoa. | igual |
>
> **Legenda (a original, com o acolhimento em dois parágrafos):**
>
> ```
> A história por trás da fairhealth começou muito antes de chegarmos às empresas.
>
> Em 2009, dentro de um hospital, nascia o Escritório do Paciente: um modelo de cuidado que tinha a escuta, o acolhimento e as necessidades de cada pessoa como ponto de partida.
>
> Ao longo do tempo, essa forma de cuidar evoluiu e encontrou novos espaços. O Escritório do Paciente virou o Escritório do Cuidado.
>
> Hoje, na fairhealth, levamos essa filosofia para dentro das empresas: um espaço de acolhimento e de medicina preventiva, perto da rotina das pessoas. Antes de qualquer exame, uma conversa.
>
> Porque, para nós, cuidar não é apenas olhar para a saúde. É olhar para quem está por trás dela.
>
> O cuidado começa pela pessoa.
>
> #fairhealth #saudecorporativa #medicinapreventiva #cuidadohumanizado #escritoriodocuidado
> ```
>
> **Validar:** 2009 e a passagem do Escritório do Paciente para o Escritório do Cuidado (pendente desde o post 02).
> Sem o nome do hospital.

---

## v1 (19/10), guardada: rascunho com roteiro novo

> **Rascunho de conteúdo (19/10), para alinhar antes da arte.** Parte do post 02 já pronto
> (`instagram/posts/nossa-historia/`, v2), que fica guardado. Esta versão põe o **acolhimento** no centro, como
> pede a nota da Nina ("acolhimento forte").

- **Bloco:** 1 (Reconhecimento). **Formato:** carrossel 1080 × 1350, 7 slides.
- **Objetivo:** explicar o porquê da marca pela origem. Existimos porque, por trás de cada atendimento, existe uma
  pessoa, e o acolhimento é o nosso método.
- **Público:** todos (colaboradores, RH, lideranças). Constrói confiança e conexão.
- **Fio da história:** vem do reel do Dr. Ronald (19/10). Leva para o 23/10: se o acolhimento é o método, é ele que
  permite cuidar antes.

## Argumentos

1. **Origem com credibilidade:** o modelo nasceu em 2009, num hospital, como Escritório do Paciente, criado pelo
   Dr. Ronald Maia Filho (`essencia.md`).
2. **A descoberta:** por trás de cada atendimento existe uma pessoa, com história, rotina e prioridades.
3. **Acolhimento como método, não como gentileza:** ouvir sem pressa, entender a história antes de propor o plano,
   caminhar junto.
4. **Continuidade:** a mesma forma de cuidar saiu do hospital e chegou ao trabalho. O Escritório do Paciente virou
   o Escritório do Cuidado.
5. **O porquê:** para que ninguém seja só mais um no cuidado.

## Roteiro

| Slide | Etiqueta | Título | Apoio |
| --- | --- | --- | --- |
| 1 · capa | Por que existimos | Por que a *fairhealth* existe? | A resposta começa em 2009, dentro de um hospital. |
| 2 | 2009 · O início | Dentro de um hospital, nasceu o *Escritório do Paciente*. | Criado pelo Dr. Ronald Maia Filho, com uma ideia simples: colocar a pessoa, de verdade, no centro do cuidado. |
| 3 | A descoberta | Por trás de cada atendimento, existe *uma pessoa*. | Com história, rotina, medos e prioridades que nenhum exame mostra sozinho. |
| 4 | Acolhimento | Acolher não é gentileza. *É método.* | Ouvir sem pressa. Entender a história antes de propor o plano. Caminhar junto, do começo ao fim. |
| 5 | A evolução | Essa forma de cuidar saiu do hospital e chegou *ao trabalho*. | Onde as pessoas passam boa parte do dia. O Escritório do Paciente virou o Escritório do Cuidado. |
| 6 | Por que existimos | A fairhealth existe para que ninguém seja *só mais um* no cuidado. | Cada pessoa ouvida, acolhida e acompanhada. |
| 7 · final | | O cuidado começa pela pessoa. | Salve e compartilhe. Logo. |

## Legenda (rascunho)

```
A história da fairhealth começou em 2009, dentro de um hospital.

Foi lá que o Dr. Ronald Maia Filho criou o Escritório do Paciente, um jeito de cuidar que começa pelo acolhimento: ouvir sem pressa, entender a história de cada pessoa e caminhar junto.

Com o tempo, essa forma de cuidar ganhou um novo endereço, o trabalho. O Escritório do Paciente virou o Escritório do Cuidado, e é ele que a fairhealth leva para dentro das empresas.

Existimos para que ninguém seja só mais um no cuidado.

#fairhealth #saudecorporativa #cuidadohumanizado #escritoriodocuidado #acolhimento
```

## Validar antes de publicar

- **[CONFIRMAR]** 2009 e a passagem do Escritório do Paciente para o Escritório do Cuidado. Sem o nome do hospital.
- **[CONFIRMAR]** Citar o Dr. Ronald como criador do Escritório do Paciente (fonte: stories "Conheça nosso time").
- Não repetir a pergunta "O que é importante para você?" em destaque: ela acabou de ser o centro do slide 2 do
  post "Gestão de pessoas que começa pela saúde".
