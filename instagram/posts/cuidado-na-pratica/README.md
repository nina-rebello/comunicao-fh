# Carrossel 03/11: 7 em cada 10 brasileiros já perguntaram a uma IA sobre a própria saúde · 6 slides

**Terça, 03/11.** Semana 1 de novembro, bloco 3 (Produto). Pauta do PDF:
"Como funciona o cuidado na prática?", a jornada entre escuta, atendimento,
plano individualizado e acompanhamento. É a continuação do post de 30/10, que
fecha com "Na terça: como funciona o cuidado na prática".

Segue o guia `instagram/carrossel.md` (versão curta e método Vinci).

**Status:** texto e design para aprovação (v8, 03/11: capa com a imagem do celular e Tiffany oficial `#9FC5BD` no post todo). É a v4.1 com o feedback
da médica distribuído nos mesmos 6 slides e com os ajustes da Nina de 03/11:
balão "o que eu faço?" de volta, dados do slide 2 mais visuais, capa clara no
verde-água (tiffany) e molduras com a descrição da foto ideal no lugar das
fotos de banco.

- **Artes** (1080x1350): `png/c-01.png` … `c-06.png`, 6 imagens, nesta ordem.
  Prévia em `previa.png`.
- **Canva:** `canva.html` (autocontido, com fotos, fontes e logo embutidas).
  Para importar, siga o passo a passo do `CLAUDE.md` (commit, push e endereço
  raw com o hash do commit). Também há o `cuidado-na-pratica.pdf`.
- **Para regerar depois de editar o `slides.html`:**
  ```
  node instagram/ferramentas/render.mjs instagram/posts/cuidado-na-pratica/slides.html instagram/posts/cuidado-na-pratica/png
  node instagram/ferramentas/canva.mjs instagram/posts/cuidado-na-pratica/slides.html instagram/posts/cuidado-na-pratica/canva.html
  ```

## Feedback da médica (03/11)

> Eu gosto bastante! Não só desabafar mas se consultar tbm. Acho que poderia
> ampliar. Usam a IA pra conferir sintomas. Isso aumenta iatrogenia. Que nós
> diminuímos nas empresas. E consequentemente o absenteísmo.

Como entrou, sem mudar o número de slides:

- **Capa:** o título passou de "7 em cada 10 brasileiros consideram desabafar
  com uma IA" para "**7 em cada 10 brasileiros já perguntaram a uma IA sobre a
  própria saúde**" (Olá Doutor: 71% usaram IA para tirar dúvidas sobre
  sintomas ou doenças). Os balões continuam "não tô dormindo direito, tô
  brigando em casa..." e "o que eu faço?" (a Nina preferiu manter este, 03/11).
- **Slide 4 (por perto):** "A dúvida chega a um profissional antes de virar
  remédio", e uma caixa explica a iatrogenia e o que ela custa ("No trabalho,
  ele vira atestado e falta").
- **Slide 5 (plano):** "sem remédio a mais nem exame à toa", com a prova de
  absenteísmo (−28%, Harvard Business Review, 2022, o número oficial do
  `voice.md`). O depoimento A1 saiu do slide para dar lugar a essa prova.
- **Slide 6:** o ponto de virada responde à pergunta da capa.

**Sobre "nós diminuímos a iatrogenia nas empresas":** não temos um número
próprio para isso, e o post não promete resultado. Ele mostra o mecanismo (a
dúvida chega ao profissional, o cuidado é na medida certa) e usa o número
oficial de absenteísmo. Se a médica ou o Dr. Ronald tiverem um dado de
atendimento (sempre agregado e sem nome de cliente), ele pode entrar no
slide 5.

## A ideia (método Vinci)

- **Caçador de referências:** junta uma dor real (não ter com quem falar, nem
  tempo, nem coragem) a um assunto do momento, fora do nicho: as pessoas estão
  desabafando e se consultando com IA.
- **Abordagem única:** todo mundo debate se a IA substitui o psicólogo ou o
  médico. A nossa ótica é outra: o que esse dado mostra sobre o cuidado que
  falta perto das pessoas, no trabalho, e quanto isso custa em faltas.
- **Funil:** a capa é o trailer (atenção), os slides 2 a 5 levam do dado à
  prática (retenção), e o slide 6 é o ponto de virada.
- **Curiosidade:** a capa mostra uma conversa de madrugada com uma IA, que
  ainda está "digitando". A resposta não vem.
- **Conflito:** por que as pessoas recorrem à IA (slide 2), e o que isso custa
  quando a dúvida vira remédio por conta própria (slide 4).
- **Inversão:** numa crise forte de ansiedade, só 4% recorreriam primeiro à
  IA. "Na hora que pesa, a gente quer gente."
- **Resolução, sempre no Escritório do Cuidado:**
  - a escuta responde à vergonha (slide 3);
  - o cuidado por perto responde à disponibilidade e à iatrogenia (slide 4);
  - o plano com retorno é o que uma resposta pronta não dá (slide 5).

  São as etapas da pauta do PDF.
- **Ponto de virada:** o slide 6 volta ao balão da capa e responde: "Quando
  alguém do seu time perguntar isso, que a resposta venha de gente."

## Os três Cs deste post

- **Capa:** "7 em cada 10 brasileiros já perguntaram a uma IA sobre a própria
  saúde." (12 palavras, com a fonte no slide). Na pílula: "O que isso diz
  sobre o cuidado no trabalho →".
- **CTA, no slide 3:** "Conhece quem cuida das pessoas na sua empresa? Mande
  este post para essa pessoa."
- **Convite, no slide 6:** "Quando alguém do seu time perguntar isso [o que
  eu faço?], que a resposta venha de gente." Depois:
  "Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito."

## Os slides

Em itálico, o trecho em Instrument Serif, na cor de destaque.

| # | Fundo e layout | Rótulo | Título | Texto | Fecho |
|---|---|---|---|---|---|
| 1 | Verde-água (tiffany) liso, conversa numa tela off-white com balões em tiffany (sem foto) | Capa | *7 em cada 10* brasileiros já perguntaram a uma IA sobre a própria saúde. | Balões: "não tô dormindo direito, tô brigando em casa e não consigo focar no trabalho" · "o que eu faço?" · assistente de IA digitando. Fonte: Olá Doutor, pesquisa com 500 pessoas (2026). Pílula: O que isso diz sobre **o cuidado no trabalho** → | |
| 2 | Off com três cartões, painel verde-escuro embaixo | Por que uma IA? | Ela está lá quando *ninguém mais está.* | Cartões, cada um com o número, um rótulo curto e uma barra do tamanho do percentual: 31,2% Está lá a qualquer hora · 26,2% Custa menos · 14% Não dá vergonha (motivos de quem usa IA para questões emocionais, Doctoralia). Painel: Mas, numa crise forte de ansiedade, só **4%** recorreriam primeiro a uma IA, com uma grade de 100 pontos e 4 acesos. | Na hora que pesa, a gente quer gente. |
| 3 | Verde-água, foto na metade de cima | 01 · Escuta | Todo mundo quer ser *ouvido de verdade.* | No Escritório do Cuidado, a primeira consulta começa por uma pergunta: **o que importa para você?** Turno, casa, sono e a conta do mês entram na conversa. Sem julgamento, e com sigilo. + CTA | |
| 4 | Verde-escuro, foto numa faixa à direita, caixa menta embaixo | 02 · Por perto | Ninguém quer perder *meio dia por uma consulta.* | Médico, psicólogo e assistente social ficam dentro da empresa, **a poucos passos de quem trabalha**, presencial ou remoto. *A dúvida chega a um profissional antes de virar remédio.* Caixa: Remédio sem indicação e exame sem necessidade fazem mal. Na medicina, esse dano tem nome: **iatrogenia**. No trabalho, ele vira atestado e falta. | |
| 5 | Off, número grande e foto ao lado | 03 · Plano e retorno | Uma resposta *não é um plano.* | No Escritório do Cuidado, o plano é combinado com a pessoa, tem base na Medicina do Estilo de Vida e é revisto a cada retorno. **Cada um recebe o cuidado de que precisa: sem remédio a mais nem exame à toa.** Prova: −28% de absenteísmo com programas de saúde preventiva (Harvard Business Review, 2022). | |
| 6 | Verde-água como a capa, o balão da capa no alto | Ponto de virada e convite | Balão: "o que eu faço?". Quando alguém do seu time perguntar isso, *que a resposta venha de gente.* | Escuta, cuidado por perto e um plano com retorno: é isso que o **Escritório do Cuidado** leva para dentro da empresa. Comente **CUIDADO** e enviamos na DM como funciona o diagnóstico gratuito. | Na quarta: quatro frentes, um cuidado conectado. |

## Os dados

Não achamos os relatórios originais, só reportagens. **[PENDENTE]** Antes de
publicar, conferir na fonte original (pedir os relatórios à Olá Doutor e à
Doctoralia, ou achar os releases).

- **Olá Doutor (2026), 500 pessoas, margem de 3,3 pontos (capa e legenda):**
  71% usaram IA no último ano para tirar dúvidas sobre sintomas ou doenças;
  49% pesquisaram remédios.
  [Medicina S/A, 23/03/2026](https://medicinasa.com.br/duvidas-saude-ia/)
- **Doctoralia (2026), 3.903 usuários (slide 2):** motivos de quem usa IA para
  questões emocionais: 31,2% disponibilidade, 26,2% custo, 14% vergonha; numa
  crise forte de ansiedade, só 4% recorreriam primeiro à IA.
  [Viva, 19/09/2026](https://viva.com.br/saude-e-bem-estar/brasileiro-usaria-ia-para-desabafar-mas-em-crises-prefere-atendimento-humano.html) ·
  [Consumidor Moderno, 05/10/2026](https://consumidormoderno.com.br/ia-saude-mental-chatbots-ansiedade-depressao-profissionais/)
- **Absenteísmo (slide 5):** −28% (Harvard Business Review, 2022), número
  oficial de `voice.md` e do Executive Summary. Confirmar com o Dr. Ronald se
  "programas de saúde preventiva" é a descrição certa do estudo.
- **Iatrogenia (slide 4):** dano ao paciente causado por intervenção de saúde,
  incluindo o excesso de medicamentos e exames. O slide usa a versão simples:
  "Remédio sem indicação e exame sem necessidade fazem mal."

Mais dados das mesmas pesquisas estão em `instagram/referencias.md`.

## O visual

- **Capa clara e elegante, no tiffany** (pedidos de 03/11): fundo verde-água
  liso, sem degradê. A conversa fica numa "tela" off-white de cantos
  arredondados, com os balões enviados em tiffany e texto escuro. A pílula é
  sólida, em verde-escuro com texto branco. O slide 6 usa o mesmo fundo, com o
  balão "o que eu faço?" numa telinha igual e a pílula "Comente CUIDADO"
  sólida, para o fim espelhar a capa.
- **Sem o quase-preto:** os fundos alternam verde-água, off e verde-escuro
  (água, off, água, verde-escuro, off, água).
- **Slide 2 mais fácil de ler:** os motivos viraram três cartões, com o número
  grande, um rótulo de três palavras e uma barra proporcional ao percentual. O
  4% ganhou uma grade de 100 pontos, com 4 acesos.
- **Logo no slide 6:** como o círculo da logo tem a mesma cor do verde-água,
  ela ganhou um anel branco.

## As imagens: a Nina escolhe e coloca

Cada slide tem uma moldura tracejada com a descrição da imagem ideal. No
Canva, é só apagar a moldura e o texto e pôr a foto no mesmo lugar e tamanho.
De preferência fotos próprias (`instagram/sessao-de-fotos.md`). Nenhum
colaborador atendido aparece com o rosto.

| Slide | Moldura (px) | Imagem ideal |
|---|---|---|
| 3 · Escuta | 1080x480, horizontal, encostada no topo | Conversa de escuta no Escritório do Cuidado: alguém do time de frente, atento, ouvindo; a outra pessoa de costas ou só as mãos. Luz natural, tons claros. Deixar o alto da foto mais limpo, porque o @ e o 03/06 ficam por cima. |
| 4 · Por perto | 368x520, vertical | Colaborador no posto de trabalho (fábrica, linha de produção ou escritório), em plano médio, sem logo de empresa. Se for alguém atendido, de costas ou de perfil, sem rosto identificável. Alternativa: a porta do Escritório do Cuidado aberta, dentro da empresa. |
| 5 · Plano e retorno | 448x360, horizontal | Rotina possível: um prato simples e colorido, ou uma agenda com metas escritas à mão ao lado de uma caneca. Tons claros. Nada de dieta da moda, balança ou fita métrica. |

**Capa (v8, simulação de 03/11):** usa a imagem enviada pela Nina, a mão
segurando o celular com a conversa (`fotos/capa-celular.jpg`, parece gerada por
IA). O fundo azulado da foto foi recolorido para o Tiffany `#9FC5BD`, sem
mexer na mão e no celular (`capa-recolorir.py`). Ela vai até o pé do slide e
se funde num degradê para o creme `#F0F0E9` atrás do título, que está em
Tiffany. O creme e o título em Tiffany seguem o pedido da Nina de 03/11
(o creme ainda está "em teste" nas diretrizes). A barra "Pergunte algo para a IA" foi
apagada da tela para não brigar com o texto (`fotos/c-01.jpg`). Por cima, no HTML, ficaram o "Hoje" no lugar de "Today" e
o balão da IA digitando. Antes de publicar, conferir se a mão e os dedos não
têm defeito.

Os slides 2 e 6 não têm foto.

## Resultado visível: como saber se deu certo

- **Objetivo do post:** desejo pelo Escritório do Cuidado e conversa com o RH.
- **Métricas, em 7 dias:** envios a cada 100 visualizações (o CTA do slide 3),
  comentários CUIDADO e alcance em não seguidores (o tema do momento deve
  levar o post para fora da base).
- **Deu certo se:** os três números ficarem acima dos posts de 28/10 e 30/10,
  que têm o mesmo convite. Registrar os números na reunião semanal de
  métricas.

## Antes de publicar

- **[PENDENTE] Dados da Olá Doutor e da Doctoralia:** conferir na fonte
  original (ver acima).
- **Dr. Ronald e a médica:** revisar o texto (CFM), principalmente os slides 2,
  4 e 5 (crise de ansiedade, remédio, iatrogenia e a descrição do −28%).
- **Tom sobre a IA:** o post não ataca a IA nem quem a usa. Ele entende por
  que as pessoas recorrem a ela e mostra o que o cuidado com gente oferece.
  Não citar marca de assistente.
- **Opcional, se for confirmado:** se o atendimento não custa nada para o
  colaborador, dá para responder também ao motivo "custo" no slide 4 ("e sem
  custo para o colaborador").
- **Convite com CUIDADO:** até a resposta automática ficar pronta (prazo
  13/11), alguém precisa responder as DMs no mesmo dia.
- **Sem dados de clientes** (decisão de 30/10).

## Legenda

```
7 em cada 10 brasileiros já perguntaram a uma IA sobre a própria saúde. E isso diz muito sobre o cuidado que está faltando.

Na pesquisa da Olá Doutor, 71% usaram IA no último ano para tirar dúvidas sobre sintomas ou doenças, e 49% pesquisaram remédios. Para desabafar, os motivos aparecem numa pesquisa da Doctoralia com 3.903 pessoas: a IA está disponível a qualquer hora (31,2%), pesa menos no bolso (26,2%) e não dá vergonha (14%).

Mas, numa crise forte de ansiedade, só 4% recorreriam primeiro a ela. Em saúde mental, como em qualquer dúvida de saúde, na hora que pesa a gente quer gente. É isso que o Escritório do Cuidado leva para dentro da empresa.

A escuta vem primeiro. A consulta começa por "o que importa para você?", e turno, casa, sono e a conta do mês entram na conversa, sem julgamento e com sigilo.

O cuidado fica perto. Médico, psicólogo e assistente social a poucos passos de quem trabalha, e a dúvida chega a um profissional antes de virar remédio por conta própria. Remédio sem indicação e exame sem necessidade fazem mal. Na medicina, esse dano tem nome: iatrogenia. No trabalho, ele vira atestado e falta.

E a resposta vira um plano, combinado com a pessoa, com base na Medicina do Estilo de Vida e revisto a cada retorno. Cada um recebe o cuidado de que precisa. Para a saúde corporativa, isso aparece na conta: programas de saúde preventiva reduzem o absenteísmo em 28% (Harvard Business Review, 2022).

Quando alguém do seu time perguntar "o que eu faço?", que a resposta venha de gente. Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #saudemental #absenteismo #gestaodepessoas
```

**Alt text da capa:** Conversa de madrugada num aplicativo de mensagens: a
pessoa escreve "não tô dormindo direito, tô brigando em casa e não consigo
focar no trabalho" e "o que eu faço?", e um assistente de IA está digitando. Embaixo, o texto "7 em cada 10 brasileiros já
perguntaram a uma IA sobre a própria saúde".

## Versões anteriores

- v7 (commit `1bc3c11`): capa no verde-água com degradê branco, balões em
  verde-escuro e pílula só com contorno.
- v6 (commit `999eccf`): mesmos 6 slides, capa escura, balão "posso tomar
  alguma coisa pra dormir?" e fotos de banco.
- v5 (commit `d816e02`): o mesmo conteúdo em 7 slides, com um slide só para
  "A IA também virou consultório". Descartada: o pedido era ajustar os slides
  que já existiam.
- v4.1 (commit `9f93a26`): 6 slides, só desabafo, com o depoimento A1 no
  slide do plano.
- v3 (commit `5f7c72f`): "O cuidado que todo mundo queria ter no trabalho",
  com foto de banco na capa.
