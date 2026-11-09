# Identidade visual — fairhealth

Origem: `instagram/diretrizes-criativas.md` (08/10 a 09/10), `instagram/voice.md` e `instagram/marca/`.
A identidade vem da marca, não das referências.

## Cores
| Nome | Código | Uso no vídeo | Situação na marca |
|---|---|---|---|
| Tiffany | `#9FC5BD` | a cor de destaque: marca-texto da palavra-chave, número, pílula, detalhe | adotada |
| Verde-autoridade | `#1F3A36` | texto sobre creme, fundo dos cartões de dado | em teste |
| Creme | `#F0F0E9` | texto sobre o vídeo e sobre o verde, fundo de cartão claro | em teste |
| Verde-noite | `#0D1816` | fundo do cartão "Luz tiffany" (dados e ciência) | aprovado na série Luz tiffany |
| Verde-logo | `#2F6B64` | fios e ícones | em teste |

- **Uma cor de destaque só: o Tiffany.** As referências usam uma cor só (verde-limão na ref03, terracota na
  ref01); aqui ela é sempre o Tiffany.
- Sobre o creme, o Tiffany só entra como forma (marca-texto, sublinhado, pílula), nunca como cor de texto
  (contraste 1,67:1).
- Sem amarelo e sem roxo até a marca decidir (pendência do `voice.md`).
- **Atenção:** a diretriz diz `#9FC5BD`; o CSS da marca (`instagram/marca/identidade-visual-v4.html`) usa
  `#96C5BD`. Usar `#9FC5BD` até a Nina confirmar.

## Fontes
- **Nunito** (pedido da Nina, 09/11: "a fonte correta é o Nunito"). Vem do Google Fonts (`@import` no
  HTML de cada camada). Texto em 700–800; **palavra-chave em Nunito Black Itálico (900 itálico)**; números em 900.
- A diretriz da marca (`instagram/diretrizes-criativas.md`) ainda diz Raleway, marcada como pendente.
  Nos vídeos vale a Nunito.

## Bonecos (pictograma de pessoas)
- O ícone enviado pela Nina em 09/11: cabeça redonda, tronco com ombros arredondados e uma peça só nas pernas.
  Redesenhado em SVG (viewBox `420 150 415 955`): `<circle cx="624" cy="286" r="124"/>` e o caminho
  `M428,542 A110,110 0 0 1 538,432 L716,432 A110,110 0 0 1 826,542 L826,759 A28,28 0 0 1 798,787 L752,787
  L752,1057 A40,40 0 0 1 712,1097 L540,1097 A40,40 0 0 1 500,1057 L500,787 L456,787 A28,28 0 0 1 428,759 Z`.
  Aceso em Tiffany, apagado em `#D3D8D3`.

## Logo
- **Logo em círculo** (`instagram/marca/logo-circulo.png`) **só no fechamento** (Nina, 09/11: o logo fixo o vídeo
  todo foi testado e tirado). No "Contrate…" ele aparece no topo, centralizado (96 px, y 240), e se abre no selo
  creme com "@fairhealth.br" (o logo desliza para a esquerda e a pílula cresce a partir dele). **Logo em coração nunca junto de número.** Uma logo por vídeo.
- O PNG do círculo tem só 196 px: em 1080x1920, usar no máximo ~180 px de largura até existir a versão em
  alta (pendência da marca).
- Slogan, quando couber no fechamento: « Fazemos o certo pelos motivos certos ».

## Capa do reel (texto de título inicial)
- Padrão enviado pela Nina em 09/11: PNG 1080x1920 com o topo transparente e um degradê verde-noite `#0F1F1C`
  subindo de baixo (transparente até y 760, 72% em y 1060, 95% na base); "@FAIRHEALTH.BR" pequeno e espaçado;
  título branco em 3 linhas no máximo (Nunito 800, 104 px, margem 72 px) com a palavra-chave numa pílula Tiffany
  e texto verde; subtítulo de até 700 px com o trecho final em negrito branco. O título é o gancho da
  programação. Modelo: `video/ferramentas/modelos/capa-reel.html`; gerador: `scripts/capa.py`.

## Quadro e áreas seguras (9:16, 1080x1920)
- Saída das animações e das legendas em 1080x1920, mesmo com o bruto em 720x1280.
- Nada essencial nos ~220 px de cima nem nos ~420 px de baixo (nome, legenda e botões do Instagram), nem nos
  ~140 px da direita (botões). Ponto de partida; conferir no primeiro vídeo.
- Essencial dentro do centro 4:5 (diretriz da marca), para poder recortar.
- Títulos com 60 px ou mais; apoio com 32 px ou mais (diretriz da marca).

## Nunca usar
- Círculos e "bolas" decorativos, glassmorphism, elementos soltos (recusados pelo time).
- Arcos da Fair Edu.
- Ícones girando em volta da cabeça e o clima "tecnológico" escuro da ref02 (fora do tom B2B).
- Dado sem fonte visível. Promessa clínica. Preço.
- Colaboradores atendidos na imagem.
- "Fair Health" separado ou com maiúscula: sempre "fairhealth".
