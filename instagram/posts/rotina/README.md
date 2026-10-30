# Carrossel 30/10: Como transformar a prevenção em parte da rotina de uma empresa? · 6 slides

Semana 2, bloco 2 (Relevância). Último post do bloco: sai do "por que prevenir"
(23 e 28/10) e chega ao "como fazer isso durar", com o modelo de cuidado da
fairhealth (acolhimento e encaminhamento) como resposta. Não compara com a
medicina do trabalho nem com o plano de saúde. Fala com o RH; o médico do
trabalho chega pelo CTA de envio.

Segue o guia `instagram/carrossel.md`, na versão curta. O texto de cada slide
está em `slides.html`, as artes em `png/` e a prévia em `previa.png`.

**Status:** rascunho para aprovação. As fotos ainda são molduras com a
descrição da cena.

## No Canva

**Design editável:** [Prevenção na rotina (30/10) · carrossel 6 slides ·
final](https://www.canva.com/d/TChp2LNpPUSKzPC) (id `DAHZbxCNgZw`). Foi importado de `canva.html`, gerado com
`node instagram/ferramentas/canva.mjs instagram/posts/rotina/slides.html instagram/posts/rotina/canva.html`.
Na versão do Canva, as molduras de foto são retas e lisas e o número do cartão
é em cor sólida (o Canva não converte rotação nem texto em degradê).

## Os três Cs deste post

- **Capa:** "Como transformar a prevenção em parte da rotina de uma empresa?" (11
  palavras, o título do PDF). Na pílula: "4 passos para o cuidado sair da
  campanha →".
- **CTA, no slide 3:** "Conhece quem cuida da saúde do time na sua empresa?
  Envie este post para essa pessoa."
- **Convite, no slide 6:** "Na sua empresa, a prevenção já faz parte da
  rotina? Comente CUIDADO e enviamos na DM como funciona o diagnóstico
  gratuito."

## Os slides

| # | Rótulo | Título | Texto | Fecho |
|---|---|---|---|---|
| 1 | Capa | Como transformar a prevenção em parte da *rotina* de uma empresa? | Pílula: 4 passos para o cuidado sair da campanha → | |
| 2 | 01 · Levar o cuidado para perto | O cuidado chega tarde quando fica *longe*. | É preciso marcar, sair do trabalho, esperar. Médico, psicólogo e assistente social dentro da empresa. Tudo começa pelo **acolhimento**: alguém escuta a pessoa antes de qualquer conduta. | Quando o cuidado está perto, ele cabe no dia. |
| 3 | 02 · Dar dia e hora | Campanha tem fim. *Plantão tem dia marcado.* | Na Chemitec, em 6 meses: 161 atendimentos, 48 colaboradores atendidos, 98% de adesão. No Escritório do Cuidado, médicos e psicólogos fazem **plantões alternados** dentro da empresa. O colaborador sabe quando vai encontrar alguém. + CTA | Menos barreira, mais adesão. |
| 4 | 03 · Encaminhar e acompanhar | O cuidado não termina no *primeiro encontro*. | Quando é preciso mais, a equipe faz o **encaminhamento** para o especialista certo e continua junto: plano individual, retorno marcado e smartband entre um encontro e outro. 81,3% voltaram para 2 ou mais atendimentos (Chemitec, 1º semestre de 2026). | Quem encaminha continua junto. |
| 5 | 04 · Medir o que muda | O RH vê *o que muda*. | O RH recebe indicadores do time, sempre anonimizados e agregados: adesão, retornos, fatores de risco. | Da intenção à evidência. |
| 6 | Convite | Na sua empresa, a prevenção já faz parte da *rotina*? | Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito. | Na terça: como funciona o cuidado na prática. |

Em itálico no título, o trecho em Instrument Serif, na cor de destaque.

## O design

Referências enviadas em 29/10: linha do tempo com cartões numerados (Pikscore),
título que mistura fonte reta e serifada em itálico (9 Yards), foto de conversa
de cuidado com título grande e pílula por cima (anima psicólogos).

- **Capa:** foto colorida inteira de uma conversa de cuidado, título centrado
  em cima (a pessoa fica na metade de baixo), "rotina" grande em Instrument
  Serif itálico na cor menta e a pílula com contorno no pé.
- **Slides 2 a 5:** fundo claro com grade fina. Uma trilha vertical em degradê
  (água para verde-escuro) atravessa os slides, com o ponto do passo atual
  ligado ao cartão branco do passo: número em degradê ("01."), ícone no canto,
  título em caixa alta, texto e barra de progresso de 4 partes.
- **Fotos do miolo:** coloridas, como recorte com borda branca e leve
  inclinação. Muda o preto e branco com retícula do guia, que deixava a série
  pesada para um post sobre cuidado.
- **Slide 3:** sem foto. O visual é a grade de caixas com os números da
  Chemitec (161 atendimentos, 48 colaboradores, 98% de adesão), recurso de
  leitura do guia de carrossel.
- **Slide 6:** fundo verde-escuro, a trilha termina no ponto menta do convite.

As referências servem de estilo e de cena. As fotos delas não entram no post:
são de banco de imagem ou geradas por IA, e uma já está num anúncio de outra
marca.

## As fotos

| Slide | Cena | Da sessão de fotos |
|---|---|---|
| 1 | Conversa de cuidado no Escritório do Cuidado: profissional e pessoa sentadas, luz natural, sem rosto de colaborador atendido (só o time de frente, ou a pessoa de costas) | A4 ou C2 |
| 2 | Porta ou sala do Escritório, com alguém do time recebendo | B1, B2 |
| 4 | Pulso com smartband sobre a mesa, ao lado de uma agenda aberta | A1, A7 |
| 5 | Mãos sobre um relatório com gráfico genérico | A5 |

Para trocar a moldura, coloque `style="background-image:url(fotos/nome.jpg)"`
na `div` com classe `img` e apague o `aviso`. Depois rode:
`node instagram/ferramentas/render.mjs instagram/posts/rotina/slides.html instagram/posts/rotina/png`

## Confirmar antes de publicar

- **Slide 3, de onde vem cada coisa:** "campanha tem fim" retoma a abertura
  da legenda e a pílula da capa; os plantões alternados vêm do Executive
  Summary; "menos barreira, mais adesão" está nas palavras do `voice.md`; os
  números da Chemitec estão liberados no `voice.md`.
- **[PENDENTE] Base do 98% de adesão** (dos colaboradores elegíveis? dos
  convidados?) e **frequência dos plantões**, para o "dia marcado" valer em
  qualquer empresa.
- **[PENDENTE] Como funciona o encaminhamento** na prática: para quem a pessoa
  é encaminhada e como o acompanhamento continua depois.
- **A smartband** mede de fato sono e atividade? A legenda não cita; o slide 4
  fala só em "smartband entre um encontro e outro".
- **Os números da Chemitec** (slides 3 e 4) estão liberados no `voice.md`. Se
  ficarem guardados para o Reel de 09/11, os slides 3 e 4 e a legenda saem sem
  eles.
- **Quem responde as DMs do "CUIDADO"** no mesmo dia.
- **O Dr. Ronald aprova o texto** (menção médica, CFM).
- **Canva:** o número em degradê e o recorte inclinado podem não converter. No
  `canva.html`, trocar por cor sólida e foto reta.

## Legenda

```
Campanha de saúde tem data para acabar. Prevenção que funciona, não.

Toda empresa conhece o ciclo: a palestra do mês temático, o check-up anual, a semana da saúde. Na segunda-feira seguinte, a rotina volta a ser a mesma, e o cuidado fica para quando algo der errado. Aí ele chega tarde, longe do trabalho e sem continuidade.

Para a prevenção fazer parte do dia a dia, o cuidado precisa estar perto, ter dia e hora, acompanhar cada pessoa ao longo do tempo e mostrar ao RH o que está mudando.

É assim que funciona o modelo de cuidado da fairhealth. Começa pelo acolhimento: médicos, psicólogos e assistentes sociais dentro da empresa, em plantões, escutando cada pessoa antes de qualquer conduta. Segue pelo encaminhamento: quando é preciso mais, a equipe leva a pessoa até o cuidado certo e continua acompanhando, com plano individual e indicadores anonimizados para o RH. Na Chemitec, 81,3% dos colaboradores atendidos voltaram para dois ou mais atendimentos no primeiro semestre de 2026.

Na fairhealth, acreditamos que cuidar antes é rotina, não evento.

Na sua empresa, a prevenção já faz parte da rotina? Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #saudepreventiva #gestaodepessoas #rhestrategico
```

**Alt text da capa:** Profissional de saúde conversando com uma pessoa numa
sala de atendimento, com o texto "Como transformar a prevenção em parte da
rotina de uma empresa?"
