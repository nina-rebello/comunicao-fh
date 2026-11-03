# Carrossel 03/11: 7 em cada 10 brasileiros consideram desabafar com uma IA · 6 slides

**Terça, 03/11.** Semana 1 de novembro, bloco 3 (Produto). Pauta do PDF:
"Como funciona o cuidado na prática?", a jornada entre escuta, atendimento,
plano individualizado e acompanhamento. É a continuação do post de 30/10, que
fecha com "Na terça: como funciona o cuidado na prática".

Segue o guia `instagram/carrossel.md` (versão curta e método Vinci).

**Status:** texto e design para aprovação (v4, 03/11).

- **Artes** (1080x1350): `png/c-01.png` … `c-06.png`, 6 imagens, nesta ordem.
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

## A ideia

A v3 ("O cuidado que todo mundo queria ter no trabalho") falava dos desejos
certos, mas a capa não abria nenhuma curiosidade nem conflito. A v4 aplica o
método Vinci:

- **Caçador de referências:** junta uma dor real (não ter com quem falar, nem
  tempo, nem coragem) a um assunto do momento, fora do nicho: as pessoas estão
  desabafando com IA.
- **Abordagem única:** todo mundo debate se a IA substitui o psicólogo. A
  nossa ótica é outra: o que esse dado mostra sobre o cuidado que falta perto
  das pessoas, no trabalho.
- **Curiosidade:** a capa mostra uma conversa de madrugada com uma IA, que
  ainda está "digitando". A resposta não vem.
- **Conflito:** o slide 2 mostra por que as pessoas recorrem à IA: ela está
  disponível a qualquer hora, custa menos e não dá vergonha.
- **Inversão:** numa crise forte de ansiedade, só 4% recorreriam primeiro à
  IA. "Na hora que pesa, a gente quer gente."
- **Resolução, sempre no Escritório do Cuidado:** a escuta responde à
  vergonha (slide 3), o cuidado por perto responde à disponibilidade
  (slide 4), e o plano com retorno é o que uma resposta pronta não dá
  (slide 5). Essas são as etapas da pauta do PDF.
- **Visual atraente:** a capa é uma cena montada com balões, e não uma foto de
  banco. Cada slide muda de fundo e de layout.

## Os três Cs deste post

- **Capa:** "7 em cada 10 brasileiros consideram desabafar com uma IA."
  (9 palavras, com a fonte no slide). Na pílula: "O que isso diz sobre o
  cuidado no trabalho →".
- **CTA, no slide 3:** "Conhece quem cuida das pessoas na sua empresa? Mande
  este post para essa pessoa."
- **Convite, no slide 6:** "Seu time tem com quem conversar antes da crise?
  Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito."

## Os slides

Em itálico, o trecho em Instrument Serif, na cor de destaque.

| # | Fundo e layout | Rótulo | Título | Texto | Fecho |
|---|---|---|---|---|---|
| 1 | Tinta, conversa com balões (sem foto) | Capa | *7 em cada 10* brasileiros consideram desabafar com uma IA. | Balões: "não tô dormindo direito, tô brigando em casa e não consigo focar no trabalho" · "o que eu faço?" · assistente de IA digitando. Fonte: Doctoralia, pesquisa com 3.903 usuários (2026). Pílula: O que isso diz sobre **o cuidado no trabalho** → | |
| 2 | Off com dados, painel verde-escuro embaixo | Por que uma IA? | Ela está lá quando *ninguém mais está.* | 31,2% porque está disponível a qualquer hora · 26,2% pelo custo · 14% por vergonha de falar com outra pessoa. Painel: Mas, numa crise forte de ansiedade, só **4%** recorreriam primeiro a uma IA. | Na hora que pesa, a gente quer gente. |
| 3 | Off, foto na metade de cima | 01 · Escuta | Todo mundo quer ser *ouvido de verdade.* | No Escritório do Cuidado, a primeira consulta começa por uma pergunta: **o que importa para você?** Turno, casa, sono e a conta do mês entram na conversa. Sem julgamento, e com sigilo. + CTA | |
| 4 | Tinta, foto numa faixa à direita | 02 · Por perto | Ninguém quer perder *meio dia por uma consulta.* | Médico, psicólogo e assistente social ficam dentro da empresa, **a poucos passos de quem trabalha**, presencial ou remoto. Na avaliação, entram hábitos, sono, estresse e bioimpedância. | Sem trânsito e sem sala de espera. |
| 5 | Água, número grande e foto ao lado | 03 · Plano e retorno | Uma resposta *não é um plano.* | No Escritório do Cuidado, o plano é combinado com a pessoa, tem base na Medicina do Estilo de Vida e cabe na rotina real. **A cada retorno, as metas são revistas.** | *"Não é aquela dieta impossível de fazer. É algo pra vida."* Colaboradora atendida pelo Escritório do Cuidado |
| 6 | Verde-escuro, sem foto | Convite | Seu time tem com quem conversar *antes da crise?* | Comente **CUIDADO** e enviamos na DM como funciona o diagnóstico gratuito. | Na quarta: quatro frentes, um cuidado conectado. |

## Os dados

Todos vêm da pesquisa da Doctoralia com 3.903 usuários da plataforma,
divulgada entre setembro e outubro de 2026. Não achamos o relatório original,
só reportagens:

- [Viva (19/09/2026)](https://viva.com.br/saude-e-bem-estar/brasileiro-usaria-ia-para-desabafar-mas-em-crises-prefere-atendimento-humano.html):
  "cerca de 70% dos brasileiros consideram usar aplicativos ou chatbots de
  inteligência artificial para questões emocionais", e "apenas 4% recorreriam
  a essas ferramentas em uma crise de ansiedade severa".
- [Consumidor Moderno (05/10/2026)](https://consumidormoderno.com.br/ia-saude-mental-chatbots-ansiedade-depressao-profissionais/):
  70% já usaram ou consideram usar; 4% recorreriam primeiro à IA numa crise
  forte de ansiedade; motivos de uso: 31,2% disponibilidade 24 horas, 26,2%
  custo, 14% vergonha de conversar com outra pessoa.

**[PENDENTE]** Antes de publicar, pedir o relatório à Doctoralia ou achar o
release original, para conferir os números e a pergunta exata.

## As fotos

Do banco de imagens da marca (licença Unsplash, uso comercial gratuito,
`instagram/marca/fotos-banco/` no branch `claude/eager-bell-tblhnh`). São
ilustrativas: nunca apresentar como time, cliente ou colaborador atendido.
Os originais estão em `fotos/`, e os recortes, em `fotos/c-0X.jpg`. A capa
não tem foto.

| Slide | Arquivo | Cena | Origem |
|---|---|---|---|
| 3 | maos.jpg | Mãos dadas, acolhimento | https://images.unsplash.com/photo-1584515933487-779824d29309 |
| 4 | industria2.jpg | Profissional de capacete no trabalho | https://images.unsplash.com/photo-1621905251189-08b45d6a269e |
| 5 | comida.jpg | Prato colorido sobre a mesa | https://images.unsplash.com/photo-1490645935967-10de6ba17061 |

## Resultado visível: como saber se deu certo

- **Objetivo do post:** desejo pelo Escritório do Cuidado e conversa com o RH.
- **Métricas, em 7 dias:** envios a cada 100 visualizações (o CTA do slide 3),
  comentários CUIDADO e alcance em não seguidores (o tema do momento deve
  levar o post para fora da base).
- **Deu certo se:** os três números ficarem acima dos posts de 28/10 e 30/10,
  que têm o mesmo convite. Registrar os números na reunião semanal de
  métricas.

## Antes de publicar

- **[PENDENTE] Dados da Doctoralia:** conferir na fonte original (ver acima).
- **[PENDENTE] Depoimento A1 (slide 5 e legenda):** é um trecho aprovado de
  `instagram/depoimentos.md`, com a assinatura padrão. O formato dos
  depoimentos ainda precisa do aval do Dr. Ronald.
- **Tom sobre a IA:** o post não ataca a IA nem quem a usa. Ele entende por
  que as pessoas recorrem a ela e mostra o que o cuidado com gente oferece.
  Não citar marca de assistente.
- **Opcional, se for confirmado:** se o atendimento não custa nada para o
  colaborador, dá para responder também ao motivo "custo" no slide 4 ("e sem
  custo para o colaborador").
- **Convite com CUIDADO:** até a resposta automática ficar pronta (prazo
  13/11), alguém precisa responder as DMs no mesmo dia.
- **Dr. Ronald:** revisar o texto (CFM), principalmente o slide 2, que fala de
  crise de ansiedade.
- **Sem dados de clientes** (decisão de 30/10).

## Legenda

```
7 em cada 10 brasileiros consideram desabafar com uma IA. E isso diz muito sobre o cuidado que está faltando.

Numa pesquisa da Doctoralia com 3.903 pessoas, os motivos aparecem claros: a IA está disponível a qualquer hora (31,2%), pesa menos no bolso (26,2%) e não dá vergonha (14%). Mas, numa crise forte de ansiedade, só 4% recorreriam primeiro a ela.

Em saúde mental, na hora que pesa, a gente quer gente. É isso que o Escritório do Cuidado leva para dentro da empresa.

A escuta vem primeiro. A consulta começa por "o que importa para você?", e turno, casa, sono e a conta do mês entram na conversa, sem julgamento e com sigilo. Para a gestão da saúde corporativa, o RH recebe só indicadores do grupo, anonimizados.

O cuidado fica perto. Médico, psicólogo e assistente social a poucos passos de quem trabalha, sem meio dia perdido entre trânsito e sala de espera.

E a resposta vira um plano. Ele é combinado com a pessoa, tem base na Medicina do Estilo de Vida e é revisto a cada retorno. Como disse uma colaboradora atendida: "Não é aquela dieta impossível de fazer. É algo pra vida."

Seu time tem com quem conversar antes da crise? Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #saudemental #medicinadoestilodevida #gestaodepessoas
```

**Alt text da capa:** Conversa de madrugada num aplicativo de mensagens: a
pessoa escreve "não tô dormindo direito, tô brigando em casa e não consigo
focar no trabalho. O que eu faço?" e um assistente de IA está digitando. Embaixo,
o texto "7 em cada 10 brasileiros consideram desabafar com uma IA".

## Versões anteriores

- v3 (commit `5f7c72f`): "O cuidado que todo mundo queria ter no trabalho",
  com foto de banco na capa.
- v2 (commit `8559242`): "Como funciona o cuidado na prática?", em 6 slides
  com fotos.
