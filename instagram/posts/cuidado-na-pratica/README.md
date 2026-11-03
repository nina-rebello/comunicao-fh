# Carrossel 03/11: Como funciona o cuidado na prática? · 6 slides

**Terça, 03/11.** Semana 1 de novembro, bloco 3 (Produto). É a continuação
do post de 30/10, que fecha com "Na terça: como funciona o cuidado na
prática". Mostra a jornada de quem é cuidado no Escritório do Cuidado, em
quatro etapas: escuta, atendimento, plano individualizado e acompanhamento.

Segue o guia `instagram/carrossel.md`, na versão curta (6 slides). O texto
aprovado em 02/11 tinha 9 slides e foi condensado para o guia: o slide 2
antigo e o resumo saíram, o sigilo entrou no slide do acompanhamento, e o
pedido de envio passou para o slide 3.

**Status:** design para aprovação (03/11).

- **Artes** (1080x1350): `png/c-01.png` … `c-06.png`, 6 imagens, nesta ordem.
  Prévia em `previa.png`.
- **Canva:** `canva.html` (autocontido, com fotos, fontes e logo embutidas).
  Para importar, siga o passo a passo do `CLAUDE.md`: commit, push e o
  endereço raw com o hash do commit. Também há o `cuidado-na-pratica.pdf`.
- **Para regerar depois de editar o `slides.html`:**
  ```
  python3 instagram/posts/cuidado-na-pratica/recortes.py
  node instagram/ferramentas/render.mjs instagram/posts/cuidado-na-pratica/slides.html instagram/posts/cuidado-na-pratica/png
  node instagram/ferramentas/canva.mjs instagram/posts/cuidado-na-pratica/slides.html instagram/posts/cuidado-na-pratica/canva.html
  ```

## Os três Cs deste post

- **Capa:** "Como funciona o cuidado na prática?" (6 palavras, título do PDF
  e o gancho do post de 30/10). Na pílula: "4 etapas, da primeira conversa ao
  retorno →".
- **CTA, no slide 3:** "Conhece quem cuida das pessoas na sua empresa? Mande
  este post: as 4 etapas estão aqui."
- **Convite, no slide 6:** "Na sua empresa, alguém escuta o colaborador antes
  do atestado? Comente CUIDADO e enviamos na DM como funciona o diagnóstico
  gratuito."

## Os slides

Em itálico, o trecho em Instrument Serif, na cor de destaque.

| # | Fundo e layout | Rótulo | Título | Texto | Fecho |
|---|---|---|---|---|---|
| 1 | Foto colorida inteira, título no terço de baixo | Capa | Como funciona o cuidado *na prática?* | Pílula: 4 etapas, da **primeira conversa ao retorno** → | |
| 2 | Claro, foto na metade de cima | 01 · Escuta | Antes de qualquer orientação, *a gente escuta.* | Tudo começa com uma pergunta: **o que importa para você?** Rotina, turno, família e objetivos mostram de onde cada pessoa parte. | Ninguém sai de lá com uma lista de regras. |
| 3 | Escuro, foto numa faixa à direita | 02 · Atendimento | Cuidado *perto de quem precisa.* | Médico, psicólogo e assistente social dentro da empresa, **sem perder meio dia de trabalho.** Na avaliação, entram hábitos, sono, estresse e bioimpedância. + CTA | |
| 4 | Água (slide de virada), número grande e foto ao lado | 03 · Plano individualizado | Um plano feito *com a pessoa,* não para ela. | Metas do tamanho da rotina real, como **dormir meia hora mais cedo** ou almoçar longe da mesa. A base é a Medicina do Estilo de Vida. | Meta boa é a que cabe na semana. |
| 5 | Claro, foto saindo pela lateral | 04 · Acompanhamento | O retorno faz *parte do plano.* | A cada retorno, as metas são revistas. Entre uma consulta e outra, a smartband acompanha a rotina. **Sigilo:** o que é conversado fica no atendimento. O RH recebe só **indicadores do grupo**, anonimizados. | O plano muda quando a vida muda. |
| 6 | Verde-escuro, sem foto | Convite | Na sua empresa, alguém escuta o colaborador *antes do atestado?* | Comente **CUIDADO** e enviamos na DM como funciona o diagnóstico gratuito. | Na quarta: quatro frentes, um cuidado conectado. |

## O design

- **Série:** barra fixa no topo (@FAIRHEALTH.BR e 01/06), título em Raleway 800
  com um trecho em Instrument Serif itálico, fecho em serif na cor de
  destaque e a bolinha com o número da etapa, como no post de 30/10.
- **Uma foto por etapa, com layouts alternados** (guia, "O visual"): foto
  inteira na capa, metade de cima no 2, faixa à direita no 3, foto ao lado do
  número grande no 4 e foto saindo pela lateral no 5. O convite fica sem foto.
- **Fundos alternados:** foto, off, tinta, água, off e verde-escuro.
- **Fotos coloridas também no miolo**, como decidido no post de 30/10.
- **Para o Canva:** tudo em posição fixa, as fotos em `<img>` já recortadas no
  tamanho da moldura (`recortes.py`, em 2x) e as quebras de linha dos títulos
  com `<br>`.

## As fotos

Todas são do banco de imagens da marca (licença Unsplash, uso comercial
gratuito, `instagram/marca/fotos-banco/` no branch `claude/eager-bell-tblhnh`).
São ilustrativas: nunca apresentar como time, cliente ou colaborador atendido.
Os originais estão em `fotos/`, e os recortes, em `fotos/c-0X.jpg`.

| Slide | Arquivo | Cena | Origem |
|---|---|---|---|
| 1 | conversa3.jpg | Duas mulheres conversando no escritório | https://images.unsplash.com/photo-1590650516494-0c8e4a4dd67e |
| 2 | maos.jpg | Mãos dadas, acolhimento | https://images.unsplash.com/photo-1584515933487-779824d29309 |
| 3 | industria2.jpg | Profissional de capacete no trabalho | https://images.unsplash.com/photo-1621905251189-08b45d6a269e |
| 4 | sono-limpa.jpg | Mulher dormindo (versão com a estampa do lençol retocada) | https://images.unsplash.com/photo-1520206183501-b80df61043c2 |
| 5 | escada.jpg | Pés subindo uma escada | https://images.unsplash.com/photo-1476480862126-209bfaa8edc8 |

Quando a sessão de fotos acontecer (`instagram/sessao-de-fotos.md`), vale
trocar a capa por uma foto própria do Escritório do Cuidado, como pede o guia.

## Antes de publicar

- **Convite com CUIDADO:** os posts de 28/10 e 30/10 já usam "Comente
  CUIDADO". Até a resposta automática ficar pronta (prazo 13/11), alguém
  precisa responder as DMs no mesmo dia.
- **[PENDENTE] Smartband (slide 5):** confirmar se todos os atendidos usam a
  pulseira. Se não for regra: "Entre uma consulta e outra, quem usa a
  smartband tem a rotina acompanhada."
- **Dr. Ronald:** revisar o texto, porque o post fala de atendimento médico
  (CFM).
- **Sem dados de clientes** (decisão de 30/10): o post não cita nome nem
  número de cliente.

## Legenda

```
O que acontece quando um colaborador entra no Escritório do Cuidado?

Ninguém sai de lá com uma lista de regras. A conversa começa com uma pergunta: o que importa para você? Rotina, turno, família, objetivos. É daí que a gente entende de onde cada pessoa parte.

Depois vem o atendimento. Médico, psicólogo e assistente social dentro da empresa, sem deslocamento e sem meio dia perdido para ir a uma consulta.

Dessa conversa sai um plano de cuidado individual, baseado na Medicina do Estilo de Vida, com metas combinadas com a pessoa. Às vezes é dormir meia hora mais cedo. Às vezes é almoçar longe da mesa.

E tem retorno. A cada consulta, as metas são revistas, porque o plano muda quando a vida muda.

O que é conversado fica no atendimento. Para a gestão da saúde corporativa, o RH recebe só indicadores do grupo, anonimizados.

É esse cuidado, da primeira conversa ao retorno, que a fairhealth leva para dentro das empresas.

Na sua empresa, alguém escuta o colaborador antes do atestado? Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #medicinadoestilodevida #cuidadocentradonapessoa #gestaodepessoas
```

Em relação ao texto aprovado, mudaram só o fim (o convite do slide 6 no lugar
do pedido de envio, que agora está no slide 3) e o nome da marca, em
minúsculas como no post de 30/10.

**Alt text da capa:** Duas mulheres conversando num escritório, com o texto
"Como funciona o cuidado na prática? 4 etapas, da primeira conversa ao
retorno."
