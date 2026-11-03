# Carrossel 03/11: 7 em cada 10 brasileiros consideram desabafar com uma IA · 7 slides

**Terça, 03/11.** Semana 1 de novembro, bloco 3 (Produto). Pauta do PDF:
"Como funciona o cuidado na prática?", a jornada entre escuta, atendimento,
plano individualizado e acompanhamento. É a continuação do post de 30/10, que
fecha com "Na terça: como funciona o cuidado na prática".

Segue o guia `instagram/carrossel.md` (método Vinci). Tem 7 slides, e não 6,
porque a médica pediu para ampliar o post (03/11).

**Status:** texto e design para aprovação (v5, 03/11, com o feedback da
médica).

- **Artes** (1080x1350): `png/c-01.png` … `c-07.png`, 7 imagens, nesta ordem.
  Prévia em `previa.png`.
- **Canva:** `canva.html` (autocontido, com fotos, fontes e logo embutidas).
  Para importar, siga o passo a passo do `CLAUDE.md` (commit, push e endereço
  raw com o hash do commit). Também há o `cuidado-na-pratica.pdf`.
- **Para regerar depois de editar o `slides.html`:**
  ```
  python3 instagram/posts/cuidado-na-pratica/recortes.py
  node instagram/ferramentas/render.mjs instagram/posts/cuidado-na-pratica/slides.html instagram/posts/cuidado-na-pratica/png
  node instagram/ferramentas/canva.mjs instagram/posts/cuidado-na-pratica/slides.html instagram/posts/cuidado-na-pratica/canva.html
  ```

## Feedback da médica (03/11)

> Eu gosto bastante! Não só desabafar mas se consultar tbm. Acho que poderia
> ampliar. Usam a IA pra conferir sintomas. Isso aumenta iatrogenia. Que nós
> diminuímos nas empresas. E consequentemente o absenteísmo.

Como entrou no post:

- **Capa:** o segundo balão deixou de ser "o que eu faço?" e passou a ser
  "posso tomar alguma coisa pra dormir?". A conversa começa como desabafo e já
  vira consulta.
- **Slide 3 (novo):** "A IA também virou consultório". Mostra os dados de
  sintomas e remédios, explica a iatrogenia em uma frase e liga ao trabalho
  ("No trabalho, ele vira atestado e falta").
- **Slide 5:** fecha com "A dúvida chega ao médico antes de virar remédio".
- **Slide 6:** "sem remédio a mais nem exame à toa", com a prova de
  absenteísmo (−28%, Harvard Business Review, 2022, o número oficial do
  `voice.md`). O depoimento A1 saiu do slide para dar lugar a essa prova.
- **Slide 7:** o ponto de virada responde à nova pergunta da capa.

**Sobre a afirmação "nós diminuímos a iatrogenia nas empresas":** não temos um
número próprio para isso, e o post não promete resultado. Ele mostra o
mecanismo (a dúvida chega ao profissional, o cuidado é na medida certa) e usa
o número oficial de absenteísmo. Se a médica ou o Dr. Ronald tiverem um dado
de atendimento (sempre agregado e sem nome de cliente), ele pode entrar no
slide 6.

## A ideia (método Vinci)

- **Caçador de referências:** junta uma dor real (não ter com quem falar, nem
  tempo, nem coragem) a um assunto do momento, fora do nicho: as pessoas estão
  desabafando e se consultando com IA.
- **Abordagem única:** todo mundo debate se a IA substitui o psicólogo ou o
  médico. A nossa ótica é outra: o que esse dado mostra sobre o cuidado que
  falta perto das pessoas, no trabalho, e quanto isso custa em faltas.
- **Funil:** a capa é o trailer (atenção), os slides 2 a 6 levam do dado à
  prática (retenção), e o slide 7 é o ponto de virada.
- **Curiosidade:** a capa mostra uma conversa de madrugada com uma IA, que
  ainda está "digitando". A resposta não vem.
- **Conflito:** por que as pessoas recorrem à IA (slide 2), e o que isso custa
  quando vira consulta: iatrogenia, atestado e falta (slide 3).
- **Inversão:** numa crise forte de ansiedade, só 4% recorreriam primeiro à
  IA. "Na hora que pesa, a gente quer gente."
- **Resolução, sempre no Escritório do Cuidado:**
  - a escuta responde à vergonha (slide 4);
  - o cuidado por perto responde à disponibilidade e à iatrogenia (slide 5);
  - o plano com retorno é o que uma resposta pronta não dá (slide 6).

  São as etapas da pauta do PDF.
- **Ponto de virada:** o slide 7 volta ao balão da capa e responde: "Quando
  alguém do seu time perguntar isso, que a resposta venha de gente."

## Os três Cs deste post

- **Capa:** "7 em cada 10 brasileiros consideram desabafar com uma IA."
  (9 palavras, com a fonte no slide). Na pílula: "O que isso diz sobre o
  cuidado no trabalho →".
- **CTA, no slide 4:** "Conhece quem cuida das pessoas na sua empresa? Mande
  este post para essa pessoa."
- **Convite, no slide 7:** "Quando alguém do seu time perguntar isso [posso
  tomar alguma coisa pra dormir?], que a resposta venha de gente." Depois:
  "Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito."

## Os slides

Em itálico, o trecho em Instrument Serif, na cor de destaque.

| # | Fundo e layout | Rótulo | Título | Texto | Fecho |
|---|---|---|---|---|---|
| 1 | Tinta, conversa com balões (sem foto) | Capa | *7 em cada 10* brasileiros consideram desabafar com uma IA. | Balões: "não tô dormindo direito, tô brigando em casa e não consigo focar no trabalho" · "posso tomar alguma coisa pra dormir?" · assistente de IA digitando. Fonte: Doctoralia, pesquisa com 3.903 usuários (2026). Pílula: O que isso diz sobre **o cuidado no trabalho** → | |
| 2 | Off com dados, painel verde-escuro embaixo | Por que uma IA? | Ela está lá quando *ninguém mais está.* | 31,2% porque está disponível a qualquer hora · 26,2% pelo custo · 14% por vergonha de falar com outra pessoa. Painel: Mas, numa crise forte de ansiedade, só **4%** recorreriam primeiro a uma IA. | Na hora que pesa, a gente quer gente. |
| 3 | Tinta com dados, caixa menta | E não é só desabafo | A IA também virou *consultório.* | 71% usaram IA para tirar dúvidas sobre sintomas ou doenças no último ano · 49% pesquisaram remédios com a IA · 37% dos psiquiatras já atenderam pacientes pedindo ajuste de remédio sugerido por IA. Caixa: Remédio sem indicação e exame sem necessidade fazem mal. Na medicina, esse dano tem nome: **iatrogenia**. | No trabalho, ele vira atestado e falta. |
| 4 | Off, foto na metade de cima | 01 · Escuta | Todo mundo quer ser *ouvido de verdade.* | No Escritório do Cuidado, a primeira consulta começa por uma pergunta: **o que importa para você?** Turno, casa, sono e a conta do mês entram na conversa. Sem julgamento, e com sigilo. + CTA | |
| 5 | Tinta, foto numa faixa à direita | 02 · Por perto | Ninguém quer perder *meio dia por uma consulta.* | Médico, psicólogo e assistente social ficam dentro da empresa, **a poucos passos de quem trabalha**, presencial ou remoto. Na avaliação, entram hábitos, sono, estresse e bioimpedância. | A dúvida chega ao médico antes de virar remédio. |
| 6 | Água, número grande e foto ao lado | 03 · Plano e retorno | Uma resposta *não é um plano.* | No Escritório do Cuidado, o plano é combinado com a pessoa, tem base na Medicina do Estilo de Vida e é revisto a cada retorno. **Cada um recebe o cuidado de que precisa: sem remédio a mais nem exame à toa.** Prova: −28% de absenteísmo com programas de saúde preventiva (Harvard Business Review, 2022). | |
| 7 | Verde-escuro, o balão da capa no alto | Ponto de virada e convite | Balão: "posso tomar alguma coisa pra dormir?". Quando alguém do seu time perguntar isso, *que a resposta venha de gente.* | Escuta, cuidado por perto e um plano com retorno: é isso que o **Escritório do Cuidado** leva para dentro da empresa. Comente **CUIDADO** e enviamos na DM como funciona o diagnóstico gratuito. | Na quarta: quatro frentes, um cuidado conectado. |

## Os dados

Não achamos os relatórios originais, só reportagens. **[PENDENTE]** Antes de
publicar, conferir na fonte original (pedir os relatórios à Doctoralia e à Olá
Doutor, ou achar os releases).

- **Doctoralia (2026), 3.903 usuários:** 70% consideram usar IA para questões
  emocionais; motivos: 31,2% disponibilidade, 26,2% custo, 14% vergonha; numa
  crise forte de ansiedade, só 4% recorreriam primeiro à IA.
  [Viva, 19/09/2026](https://viva.com.br/saude-e-bem-estar/brasileiro-usaria-ia-para-desabafar-mas-em-crises-prefere-atendimento-humano.html) ·
  [Consumidor Moderno, 05/10/2026](https://consumidormoderno.com.br/ia-saude-mental-chatbots-ansiedade-depressao-profissionais/)
- **Doctoralia (2026), mais de 1.700 psicólogos e psiquiatras:** 37% dos
  psiquiatras tiveram pacientes pedindo ajuste de medicação com base em
  sugestão de IA.
  [Consumidor Moderno, 05/10/2026](https://consumidormoderno.com.br/ia-saude-mental-chatbots-ansiedade-depressao-profissionais/)
- **Olá Doutor (2026), 500 pessoas, margem de 3,3 pontos:** 71% usaram IA no
  último ano para tirar dúvidas sobre sintomas ou doenças; 49% pesquisaram
  remédios.
  [Medicina S/A, 23/03/2026](https://medicinasa.com.br/duvidas-saude-ia/)
- **Absenteísmo:** −28% (Harvard Business Review, 2022), número oficial de
  `voice.md` e do Executive Summary. Confirmar com o Dr. Ronald se
  "programas de saúde preventiva" é a descrição certa do estudo.
- **Iatrogenia:** dano ao paciente causado por intervenção de saúde,
  incluindo o excesso de medicamentos e exames. O slide usa a versão simples:
  "Remédio sem indicação e exame sem necessidade fazem mal."

## As fotos

Do banco de imagens da marca (licença Unsplash, uso comercial gratuito,
`instagram/marca/fotos-banco/` no branch `claude/eager-bell-tblhnh`). São
ilustrativas: nunca apresentar como time, cliente ou colaborador atendido.
Os originais estão em `fotos/`, e os recortes, em `fotos/c-0X.jpg`. A capa e
os slides 2, 3 e 7 não têm foto.

| Slide | Arquivo | Cena | Origem |
|---|---|---|---|
| 4 | maos.jpg | Mãos dadas, acolhimento | https://images.unsplash.com/photo-1584515933487-779824d29309 |
| 5 | industria2.jpg | Profissional de capacete no trabalho | https://images.unsplash.com/photo-1621905251189-08b45d6a269e |
| 6 | comida.jpg | Prato colorido sobre a mesa | https://images.unsplash.com/photo-1490645935967-10de6ba17061 |

## Resultado visível: como saber se deu certo

- **Objetivo do post:** desejo pelo Escritório do Cuidado e conversa com o RH.
- **Métricas, em 7 dias:** envios a cada 100 visualizações (o CTA do slide 4),
  comentários CUIDADO e alcance em não seguidores (o tema do momento deve
  levar o post para fora da base).
- **Deu certo se:** os três números ficarem acima dos posts de 28/10 e 30/10,
  que têm o mesmo convite. Registrar os números na reunião semanal de
  métricas.

## Antes de publicar

- **[PENDENTE] Dados da Doctoralia e da Olá Doutor:** conferir na fonte
  original (ver acima).
- **Dr. Ronald e a médica:** revisar o texto (CFM), principalmente os slides 2
  e 3 (crise de ansiedade, remédio, iatrogenia) e a descrição do −28%.
- **Tom sobre a IA:** o post não ataca a IA nem quem a usa. Ele entende por
  que as pessoas recorrem a ela e mostra o que o cuidado com gente oferece.
  Não citar marca de assistente.
- **Opcional, se for confirmado:** se o atendimento não custa nada para o
  colaborador, dá para responder também ao motivo "custo" no slide 5 ("e sem
  custo para o colaborador").
- **Convite com CUIDADO:** até a resposta automática ficar pronta (prazo
  13/11), alguém precisa responder as DMs no mesmo dia.
- **Sem dados de clientes** (decisão de 30/10).

## Legenda

```
7 em cada 10 brasileiros consideram desabafar com uma IA. E isso diz muito sobre o cuidado que está faltando.

Numa pesquisa da Doctoralia com 3.903 pessoas, os motivos aparecem claros: a IA está disponível a qualquer hora (31,2%), pesa menos no bolso (26,2%) e não dá vergonha (14%). Mas, numa crise forte de ansiedade, só 4% recorreriam primeiro a ela.

E não é só desabafo. No último ano, 71% dos brasileiros usaram IA para tirar dúvidas sobre sintomas ou doenças, e 49% pesquisaram remédios (Olá Doutor, 2026). Remédio sem indicação e exame sem necessidade fazem mal. Na medicina, esse dano tem nome: iatrogenia. No trabalho, ele vira atestado e falta.

Em saúde mental, como em qualquer dúvida de saúde, na hora que pesa a gente quer gente. É isso que o Escritório do Cuidado leva para dentro da empresa.

A escuta vem primeiro. A consulta começa por "o que importa para você?", e turno, casa, sono e a conta do mês entram na conversa, sem julgamento e com sigilo.

O cuidado fica perto. Médico, psicólogo e assistente social a poucos passos de quem trabalha, e a dúvida chega a um profissional antes de virar remédio por conta própria.

E a resposta vira um plano, combinado com a pessoa, com base na Medicina do Estilo de Vida e revisto a cada retorno. Cada um recebe o cuidado de que precisa. Para a saúde corporativa, isso aparece na conta: programas de saúde preventiva reduzem o absenteísmo em 28% (Harvard Business Review, 2022).

Quando alguém do seu time perguntar "posso tomar alguma coisa pra dormir?", que a resposta venha de gente. Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #saudemental #absenteismo #gestaodepessoas
```

**Alt text da capa:** Conversa de madrugada num aplicativo de mensagens: a
pessoa escreve "não tô dormindo direito, tô brigando em casa e não consigo
focar no trabalho" e "posso tomar alguma coisa pra dormir?", e um assistente
de IA está digitando. Embaixo, o texto "7 em cada 10 brasileiros consideram
desabafar com uma IA".

## Versões anteriores

- v4.1 (commit `9f93a26`): 6 slides, só desabafo, com o depoimento A1 no
  slide do plano.
- v3 (commit `5f7c72f`): "O cuidado que todo mundo queria ter no trabalho",
  com foto de banco na capa.
- v2 (commit `8559242`): "Como funciona o cuidado na prática?", em 6 slides
  com fotos.
