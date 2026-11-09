---
name: edit-preparar
description: "Abre um reel novo da fairhealth: anota o briefing, mede o bruto, transcreve com o tempo de cada palavra, corrige os termos e apara o começo e o fim. Use em /edit-preparar, quando um bruto novo entrou em Vídeos Brutos."
---

# edit-preparar

Transforma o bruto em algo que o Claude consegue ler: briefing, inventário, transcrição com tempo por palavra
e o corte (só as pontas, porque a apresentadora grava ensaiado). Não planeja animação.

- **Lê:** o bruto em `CE/V*deos Brutos/`, o perfil (`estilo-cortes.md`), `video/ferramentas/termos.md`.
- **Escreve:** `CE/_CLAUDE/<video>/projeto.json` (blocos `briefing`, `midia`, `transcricao`, `cortes`,
  `marcadores`), `transcricao_palavras.json`, `transcricao_frases.txt`, `aprendizados.md` vazio.
- **Próximo passo:** `/edit-plano`

## 1. Começar
- Se `projeto.json` já existe: não sobrescreva; mostre o status e pergunte se é para atualizar algo.
- Crie `CE/_CLAUDE/<video>/` e o estado com `perfil: "fairhealth"`.
- **Briefing**, numa mensagem curta: "Me conta sobre esse vídeo: quem fala, o assunto, de onde vêm os números
  e qualquer direcionamento." Organize sem inventar (preserve as palavras dela). **A fonte de cada número é
  obrigatória** (regra da marca); se faltar, anote como pendência do plano.
- Roteiro, se a Nina tiver: só para conferir a grafia, nunca para trocar o que foi falado.

## 2. Inventário (ffprobe)
Duração, resolução, fps (real e médio: alerta se for variável), codec, áudio (taxa, canais), rotação.
Alertas: sem áudio, fps variável, resolução abaixo de 1080x1920 (limita o zoom da câmera, ver perfil).

## 3. Transcrição
- Áudio extraído em WAV 16 kHz mono para `_CLAUDE/<video>/audio.wav`.
- mlx-whisper, modelo `mlx-community/whisper-large-v3-turbo`, `language="pt"`, `word_timestamps=True`,
  `condition_on_previous_text=False`, **sem** `initial_prompt` (faz o Whisper inventar frases). Em segundo
  plano. Referência: 54 s de vídeo em ~19 s no M2.
- **Ajuste das bordas:** os tempos do Whisper às vezes invadem as pausas em 0,3 a 0,6 s (medido em 09/11).
  O script mede as pausas com `silencedetect` (ponto de partida: -35 dB, 0,25 s) e puxa o fim da palavra para
  o começo da pausa e o começo da seguinte para o fim dela.
- **O que foi engolido:** trechos com som e sem palavra (fora das pausas) são retranscritos sozinhos; se
  ainda assim sobrar, viram marcador.
- **Hesitações:** o Whisper costuma apagar os "ééé". Ainda não foi testado num take com erros: no primeiro,
  confira e anote o que aconteceu em `video/ferramentas/montagem.md`.
- **Termos:** aplique `termos.md` ("Fair Health" → "fairhealth" etc.) e mostre o que trocou.
- Saída para o Claude ler: `transcricao_frases.txt`, uma frase por linha, com tempo e pausas marcadas.

## 4. Corte
Siga o perfil (`estilo-cortes.md`): apara o começo e o fim com a folga do perfil e **não corta o meio**.
Erro, recomeço, take repetido ou pausa estranha: marcador com o tempo (`mk01`…), sem cortar. Se houver take
repetido, diga quais e qual sugere manter, e espere a Nina.

## Scripts (em `video/ferramentas/scripts/`)
| Script | O que faz | Armadilhas |
|---|---|---|
| `estado.py` | lê e muda o estado (regras comuns, seção 2) | escrever na primeira vez; nunca imprimir o arquivo inteiro |
| `inventario.py` | ffprobe do bruto para o bloco `midia` | fps real × médio; rotação no metadado |
| `transcrever.py` | áudio, mlx-whisper, ajuste das bordas pelas pausas, termos, frases | sem `initial_prompt`; retranscrever trechos com som e sem palavra |
| `aparar.py` | início e fim do corte com a folga do perfil, em frames | arredondar para frame numa função só |

Uso (escritos e testados em 09/11, no `marilia_0911_calude`), com `PY=video/ferramentas/.venv/bin/python`
e a partir de `video/ferramentas/scripts/`:
1. `$PY inventario.py <video>`: cria o estado (se não existir) e o bloco `midia`, com os alertas.
2. `$PY transcrever.py <video>`: ~20 s para 55 s de vídeo; imprime as frases, as bordas ajustadas, os termos
   trocados, as palavras de baixa confiança e os marcadores.
3. `$PY aparar.py <video> [folga_inicio] [folga_fim]`: grava o bloco `cortes`.
4. `$PY estado.py <video> status` e `--etapa preparar=aguardando_aprovacao`.
`comum.py` tem os caminhos (acha as pastas acentuadas sem depender da forma Unicode), a conversão única de
segundos para frame, o ffprobe e o silencedetect. Palavra de baixa confiança (< 0,5) vira marcador
`palavra_duvidosa` para a Nina conferir ouvindo.

## Resumo no chat
Duração do bruto → duração aparada, fps, resolução (com alerta se for baixa), a transcrição por frase (curta,
é um reel), termos trocados, marcadores. Nenhuma entrega no CapCut nesta etapa. Marque
`aguardando_aprovacao`.

## Revisão e aprovação
A Nina corrige palavras ou pontas pelo chat. Aplicar, anotar aprendizados (regras comuns, seção 5). Com o
"ok", marque `concluido` e sugira `/clear` e `/editar`.

## Regras comuns
Antes de começar, leia `.claude/skills/editar/regras-comuns.md` (uma vez por sessão).
