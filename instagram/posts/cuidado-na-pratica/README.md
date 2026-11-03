# Carrossel 03/11: O cuidado que todo mundo queria ter no trabalho · 6 slides

**Terça, 03/11.** Semana 1 de novembro, bloco 3 (Produto). Pauta do PDF:
"Como funciona o cuidado na prática?", a jornada entre escuta, atendimento,
plano individualizado e acompanhamento. É a continuação do post de 30/10, que
fecha com "Na terça: como funciona o cuidado na prática".

Segue o guia `instagram/carrossel.md`, na versão curta (6 slides).

**Status:** texto e design para aprovação (v3, 03/11).

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

A v2 explicava o processo e ficou rasa (retorno de 03/11). Nesta versão, cada
slide parte de algo que todo mundo já viveu ou deseja e responde com o que o
Escritório do Cuidado faz. Os quatro pontos são as quatro etapas da jornada
do PDF:

| Etapa do PDF | O desejo | O que o Escritório do Cuidado faz |
|---|---|---|
| Escuta | Ser ouvido de verdade | A primeira consulta começa por "o que importa para você?" |
| Atendimento | Não perder meio dia por uma consulta | Médico, psicólogo e assistente social dentro da empresa |
| Plano individualizado | Um plano possível, não uma dieta impossível | Metas combinadas, do tamanho da rotina (MEV), com o depoimento A1 |
| Acompanhamento | Não começar do zero, e poder falar sem medo | Histórico e metas na plataforma, retorno, sigilo |

## Os três Cs deste post

- **Capa:** "O cuidado que todo mundo queria ter no trabalho." (9 palavras).
  Em cima, "Por dentro do Escritório do Cuidado", para a capa não ficar avulsa.
  Na pílula: "Como isso funciona na prática, em 4 pontos →".
- **CTA, no slide 3:** "Conhece quem cuida das pessoas na sua empresa? Mande
  este post: os 4 pontos estão aqui."
- **Convite, no slide 6:** "Quer esse cuidado para o seu time? Comente
  CUIDADO e enviamos na DM como funciona o diagnóstico gratuito."

## Os slides

Em itálico, o trecho em Instrument Serif, na cor de destaque.

| # | Fundo e layout | Rótulo | Título | Texto | Fecho |
|---|---|---|---|---|---|
| 1 | Foto colorida inteira, título no terço de baixo | Por dentro do Escritório do Cuidado | O cuidado que todo mundo *queria ter* no trabalho. | Pílula: Como isso funciona **na prática**, em 4 pontos → | |
| 2 | Claro, foto na metade de cima | 01 · Ser ouvido | Todo mundo quer ser *ouvido de verdade.* | Às vezes, o que tira o sono é o turno, a conta do mês ou a casa. Por isso, no Escritório do Cuidado, a primeira consulta começa por uma pergunta: **o que importa para você?** | Cuidado começa pela história, não pelo sintoma. |
| 3 | Escuro, foto numa faixa à direita | 02 · Cuidado por perto | Ninguém quer perder *meio dia por uma consulta.* | Por isso o cuidado fica dentro da empresa: médico, psicólogo e assistente social **a poucos passos de quem trabalha**, presencial ou remoto. + CTA | Sem trânsito e sem sala de espera. |
| 4 | Água (slide de virada), número grande e foto ao lado | 03 · Um plano possível | Quem nunca recebeu *uma dieta impossível?* | No Escritório do Cuidado, o plano é combinado com a pessoa e cabe na rotina real: **dormir meia hora mais cedo, almoçar longe da mesa.** A base é a Medicina do Estilo de Vida. | *"Não é aquela dieta impossível de fazer. É algo pra vida."* Colaboradora atendida pelo Escritório do Cuidado |
| 5 | Claro, foto saindo pela lateral | 04 · Continuidade | Ninguém quer *começar do zero* a cada consulta. | A equipe acompanha cada pessoa. Histórico e metas ficam na plataforma, e a cada retorno o plano é revisto. **Sigilo. Pode falar:** o que é conversado fica no atendimento. O RH recebe só indicadores do grupo, anonimizados. | O plano muda quando a vida muda. |
| 6 | Verde-escuro, sem foto | Convite | Quer esse cuidado *para o seu time?* | Comente **CUIDADO** e enviamos na DM como funciona o diagnóstico gratuito. | Na quarta: quatro frentes, um cuidado conectado. |

## O design

- **Série:** barra fixa no topo (@FAIRHEALTH.BR e 01/06), título em Raleway 800
  com um trecho em Instrument Serif itálico, fecho em serif na cor de
  destaque e a bolinha com o número de cada ponto, como no post de 30/10.
- **Uma foto por ponto, com layouts alternados** (guia, "O visual"): foto
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
| 4 | comida.jpg | Prato colorido sobre a mesa | https://images.unsplash.com/photo-1490645935967-10de6ba17061 |
| 5 | escada.jpg | Pés subindo uma escada | https://images.unsplash.com/photo-1476480862126-209bfaa8edc8 |

Quando a sessão de fotos acontecer (`instagram/sessao-de-fotos.md`), vale
trocar a capa por uma foto própria do Escritório do Cuidado, como pede o guia.

## Antes de publicar

- **[PENDENTE] Depoimento A1 (slide 4 e legenda):** é um trecho aprovado de
  `instagram/depoimentos.md`, com a assinatura padrão. O formato dos
  depoimentos ainda precisa do aval do Dr. Ronald. O de 19/11 usa outro
  trecho (A2).
- **Convite com CUIDADO:** os posts de 28/10 e 30/10 já usam "Comente
  CUIDADO". Até a resposta automática ficar pronta (prazo 13/11), alguém
  precisa responder as DMs no mesmo dia.
- **Plataforma (slide 5):** "histórico e metas ficam na plataforma" vem do
  Executive Summary (plataforma com prontuário, histórico e metas).
- **Dr. Ronald:** revisar o texto, porque o post fala de atendimento médico
  (CFM).
- **Sem dados de clientes** (decisão de 30/10): o post não cita nome nem
  número de cliente.

## Legenda

```
O cuidado que todo mundo queria ter no trabalho tem endereço: o Escritório do Cuidado.

Ser ouvido, não perder o dia, ter um plano possível e não precisar recomeçar do zero. Na prática, funciona assim.

Às vezes, o que tira o sono é o turno, a conta do mês ou a casa. Por isso a primeira consulta começa por uma pergunta: o que importa para você? A rotina e o que anda pesando vêm antes de qualquer conduta.

O atendimento fica a poucos passos de quem trabalha. Médico, psicólogo e assistente social dentro da empresa, presencial ou remoto, sem meio período perdido entre trânsito e sala de espera.

O plano é combinado com a pessoa, tem base na Medicina do Estilo de Vida e cabe na rotina real. Como disse uma colaboradora atendida: "Não é aquela dieta impossível de fazer. É algo pra vida."

E o cuidado continua. Histórico e metas ficam registrados na plataforma, e a cada retorno o plano é revisto. O que é conversado fica no atendimento. Para cuidar da saúde corporativa, o RH recebe só indicadores do grupo, anonimizados.

Quer esse cuidado para o seu time? Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #medicinadoestilodevida #cuidadocentradonapessoa #gestaodepessoas
```

**Alt text da capa:** Duas mulheres conversando num escritório, com o texto
"Por dentro do Escritório do Cuidado. O cuidado que todo mundo queria ter no
trabalho. Como isso funciona na prática, em 4 pontos."
