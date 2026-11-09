---
name: edit-som
description: "Coloca os efeitos sonoros discretos de um reel da fairhealth (pop, whoosh, clique) no tempo das animações e da câmera, numa faixa de áudio para o CapCut. Use em /edit-som, depois da edit-camera."
---

# edit-som

O som entra por último, sobre animações e câmera travadas. Poucos efeitos e baixos. A música fica com a Nina.

- **Lê:** `eventos_som.json` (animações e câmera), loudness da voz; perfil (`estilo-som.md`); guia
  `.claude/skills/fluxo-de-edicao/guias/etapa-sfx.md`; índice da biblioteca `video/ferramentas/sons/indice.md`.
- **Escreve:** bloco `sfx` (`sfx01`…), `sfx_vNN.wav` com todos os efeitos (duração do vídeo inteiro) e a prévia.
- **Próximo passo:** `/edit-entrega`

Se `camera` não estiver `concluido` (ou `nao_precisa`), pare e sugira terminá-la.

## A biblioteca
Hoje os sons são **sintetizados** pelo `sfx.py` no FFmpeg (pop, tique, sino, whoosh), em
`video/ferramentas/sons/` (fora do git, recriáveis): sem download e sem licença de terceiros. As receitas
ficam no próprio script, com a duração e o tempo até o pico. Para sons de banco no futuro: só com licença clara
para uso comercial (ex.: CC0), conferida um a um, e baixar só com o "sim" da Nina, dizendo de onde e o quê.

## Ofício (do guia, no gosto do perfil)
- O som segue o que se vê: entrada de número, pílula, cartão, punch e fechamento. Legenda palavra por palavra
  não leva som.
- Uma camada por evento (o perfil é discreto: sem grave, riser ou cauda, salvo pedido).
- Sincronia: pop e clique começam no evento; o pico do whoosh cai na chegada.
- Nível bem abaixo da voz (ponto de partida do perfil), sem repetir o mesmo arquivo em ~20 s.

## Scripts
| Script | O que faz | Armadilhas |
|---|---|---|
| `indice_sons.py` | mede duração útil, tempo até o pico, brilho | pular o silêncio do começo |
| `sfx.py` | alinha, nivela pela voz e mixa numa faixa WAV da duração do vídeo; gera a prévia | fade de 1 frame em cada som; nada acima da voz |
Uso (testado em 09/11): grave `sfx.itens` [{id, tempo, som, alinhar: inicio|pico, db, nota}] e rode
`$PY sfx.py <video> <N>`: mede o pico da voz, põe cada efeito ~14 dB abaixo (mais o `db` do item) e grava
`renders/sfx_vNN.wav` com a duração do vídeo. O `previa.py` mistura essa faixa com a voz e copia o WAV para
a entrega.

## Resumo, revisão e aprovação
Lista curta (`sfx01` no tempo X, qual som), caminho da pasta; `aguardando_aprovacao`. Revisão por número
("sfx02 mais baixo" = 3 dB a menos, "sfx03 tira", "troca o sfx01", "sfx04 um frame antes"). Aprendizados no
caderno. Com o "ok", `concluido`, `/clear` e `/editar`.

## Regras comuns
Antes de começar, leia `.claude/skills/editar/regras-comuns.md` (uma vez por sessão).
