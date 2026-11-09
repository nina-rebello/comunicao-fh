---
name: edit-camera
description: "Desenha os movimentos de câmera discretos (aproximações lentas, punch) no vídeo da apresentadora, casados com as animações já aprovadas, e aplica no vídeo. Use em /edit-camera, depois da edit-motion."
---

# edit-camera

O movimento digital da câmera sobre a apresentadora, feito **depois** das animações prontas. Como o CapCut
não importa keyframes, o movimento é aplicado no próprio vídeo (`apresentadora_vNN.mp4`).

- **Lê:** blocos `plano.camera`, `motions` (tempos e lados), transcrição por palavra; perfil
  (`estilo-camera.md`); guia `.claude/skills/fluxo-de-edicao/guias/etapa-camera.md` (§2 a §4) e
  `oficio-motion.md` (§2 e §3).
- **Escreve:** bloco `camera` (`cam01`…), eventos de câmera para o som, nova `apresentadora_vNN.mp4` e prévia.
- **Próximo passo:** `/edit-som`

Se `motion` não estiver `concluido`, pare e sugira terminá-la.

## Ofício (adaptado: sem cortes no meio, então não há alternância de planos)
- Uma aproximação lenta por baixo, em camada própria; as 2 ou 3 aproximações do plano emendam nela sem a
  velocidade chegar a zero.
- Punch na palavra de ápice: sobe ~5–7% e assenta em ~0,3 s (`power2.out`).
- Número ao lado do rosto: o rosto vai um pouco para o lado oposto enquanto ele está na tela e volta
  (`power2.inOut`, ~0,7 s).
- **Zoom máximo do perfil** (10 a 15% com bruto 720x1280). Nunca mostrar a borda. Olhos a ~35% da altura no
  plano mais fechado.
- Todo movimento parte de onde a câmera está. Nada de salto de escala no meio do vídeo.

## Scripts
| Script | O que faz | Armadilhas |
|---|---|---|
| `camera.py` | calcula escala e posição por frame (curvas do ofício) e aplica com FFmpeg, junto com a escala para 1080x1920 | um só reescalonamento (evita perder nitidez duas vezes); conferir que a borda nunca aparece; mesmo número de frames |
Uso (testado em 09/11, `marilia_0911_calude`): grave `camera.ancora` [x, y] (o rosto, em 1080x1920) e
`camera.movimentos` [{id, inicio, fim, de, para, curva, nota}] no estado e rode `$PY camera.py <video> <N>`.
- Curvas: `linear`, `power2.out`, `power2.inOut`, `sine.inOut`, `expo.out`. Cada movimento parte de onde o
  anterior terminou (o script recusa o contrário). Escala abaixo de 1,0 é recusada.
- Zoom pelo filtro `perspective` do FFmpeg (subpixel, cúbico): `crop` arredonda e o zoom lento treme.
  A escala vira soma de trechos com `clip()` (`if` aninhado estoura o analisador do FFmpeg; o quadro é `in`).
- ~3,5 min para 55 s no M2. Grava em arquivo temporário e só renomeia no fim.
- **Recortes:** onde há um elemento atrás da apresentadora (recorte), a escala tem de ser 1,00 naquele trecho,
  senão o recorte desalinha. Saltos de escala só escondidos sob tela cheia.

## Passo a passo
1. Rascunho numerado (`cam01`…): o quê, onde (palavra e tempo), duração, curva, de quanto a quanto. Mostrar
   e ajustar com a Nina antes de aplicar.
2. Aplicar, gerar a prévia com as camadas da `edit-motion` e a nova `apresentadora_vNN.mp4` na pasta `vNN`.
3. Anotar os eventos de câmera visíveis (punch, aproximação mais rápida) para o som.

## Resumo, revisão e aprovação
Resumo curto e caminho da pasta; `aguardando_aprovacao`. Revisão no CapCut, por número ("cam02 mais sutil",
"cam03 tira"). Ajuste manual no CapCut não volta para o plano: peça por número. Aprendizados no caderno.
Com o "ok", `concluido`, `/clear` e `/editar`.

## Regras comuns
Antes de começar, leia `.claude/skills/editar/regras-comuns.md` (uma vez por sessão).
