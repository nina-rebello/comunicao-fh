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

**Versão limpa (30/10):** `slides-limpo.html`, com artes em `png-limpo/`, prévia
em `previa-limpo.png` e importação em `canva-limpo.html`. Mesmo texto, com o
miolo sem cartões, ícones, barra de progresso nem grade: o número do passo vai
na bolinha da trilha, o nome do passo no rótulo, e cada slide fica com título,
foto, um parágrafo e no máximo uma prova. No slide 4, o texto ficou mais curto
(sem a smartband).

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
| 3 | 02 · Dar dia e hora | Cuidado com *dia e hora marcados*. | Cartão de cima: *Sem tirar ninguém da rotina:* → Dentro da empresa · → No horário de trabalho · → Presencial ou remoto. Cartão 02: Plantões alternados de médicos e psicólogos. O colaborador sabe quando vai encontrar alguém. + CTA | |
| 4 | 03 · Encaminhar e acompanhar | O cuidado não termina no *primeiro encontro*. | Quando é preciso mais, a equipe faz o **encaminhamento** para o especialista certo e continua junto: plano individual, retorno marcado e smartband entre um encontro e outro. 93,8% voltaram para 2 ou mais atendimentos (Fonte: Cliente, 1º semestre de 2026). | Quem encaminha continua junto. |
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
- **Slide 3:** sem foto. O cartão de cima lista, com setas, como o cuidado
  entra na rotina (dentro da empresa, no horário de trabalho, presencial ou
  remoto). Sem dias da semana: não oferecemos plantão diário.
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

- **Sem dados de clientes (decisão de 30/10):** nada de nome de cliente nem dos
  números da Chemitec no post. O slide 4 usa o número que a Nina pôs no Canva
  (93,8%, "Fonte: Cliente, 1º semestre de 2026"); a legenda não cita número.
- **Slide 3:** "No horário de trabalho" é dedução (o atendimento acontece na
  empresa), não está escrito nos materiais. Confirmar.
- **[PENDENTE] Frequência dos plantões**, para o "dia e hora marcados" valer em
  qualquer empresa.
- **[PENDENTE] Como funciona o encaminhamento** na prática: para quem a pessoa
  é encaminhada e como o acompanhamento continua depois.
- **A smartband** mede de fato sono e atividade? A legenda não cita; o slide 4
  fala só em "smartband entre um encontro e outro".
- **Quem responde as DMs do "CUIDADO"** no mesmo dia.
- **O Dr. Ronald aprova o texto** (menção médica, CFM).
- **Canva:** o número em degradê e o recorte inclinado podem não converter. No
  `canva.html`, trocar por cor sólida e foto reta.

## Legenda

```
Campanha de saúde tem data para acabar. Prevenção que funciona, não.

Toda empresa conhece o ciclo: a palestra do mês temático, o check-up anual, a semana da saúde. Na segunda-feira seguinte, a rotina volta a ser a mesma, e o cuidado fica para quando algo der errado. Aí ele chega tarde, longe do trabalho e sem continuidade.

Para a prevenção fazer parte do dia a dia, o cuidado precisa estar perto, ter dia e hora, acompanhar cada pessoa ao longo do tempo e mostrar ao RH o que está mudando.

É assim que funciona o modelo de cuidado da fairhealth. Começa pelo acolhimento: médicos, psicólogos e assistentes sociais dentro da empresa, em plantões, escutando cada pessoa antes de qualquer conduta. Segue pelo encaminhamento: quando é preciso mais, a equipe leva a pessoa até o cuidado certo e continua acompanhando, com plano individual e indicadores anonimizados para o RH.

Na fairhealth, acreditamos que cuidar antes é rotina, não evento.

Na sua empresa, a prevenção já faz parte da rotina? Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #saudepreventiva #gestaodepessoas #rhestrategico
```

**Alt text da capa:** Profissional de saúde conversando com uma pessoa numa
sala de atendimento, com o texto "Como transformar a prevenção em parte da
rotina de uma empresa?"
