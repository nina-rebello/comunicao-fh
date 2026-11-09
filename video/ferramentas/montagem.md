# Montagem do fluxo de edição

Fase atual: 6 (teste num clipe curto) · Atualizado em 09/11/2026

## Ambiente
- **Decisão (09/11):** a edição passa para o Claude Code instalado no computador da Nina, com os vídeos em
  pastas locais.
- Computador da Nina (conferido em 09/11): macOS 27, Apple M2, 8 GB de memória, Python 3.13.3, Node 23.11
  (npx 10.9), Git 2.39, Homebrew 7.0, FFmpeg 9.0.2 (instalado em 09/11 pelo Homebrew). Sem GPU NVIDIA: a transcrição local roda no chip M2
  (mais devagar, mas dá para reels de 30 a 90 s). Disco: 40 GB livres (91% cheio), atenção com renders.
- Até aqui a montagem foi na nuvem (Linux, Python 3.13, FFmpeg 6.1, Node 22, sem GPU), só para referência.
- Instalado nesta montagem: FFmpeg 9.0.2 (`brew install ffmpeg`, 09/11); ambiente Python em
  `video/ferramentas/.venv` (fora do git) com mlx-whisper 0.4.3 e o modelo `mlx-community/whisper-large-v3-turbo`
  (cerca de 1,6 GB, no cache do Hugging Face).

## Decisões
- Revisão: no CapCut. O CapCut não importa projeto de outro programa (ajuda do CapCut), então a entrega é
  o MP4 completo mais as peças soltas: o vídeo cortado sem animação, cada animação em MP4 com fundo verde
  (para o chroma key do CapCut) e os efeitos sonoros em áudio. Legendas: dinâmicas, geradas pelo fluxo (09/11) a partir
  dos tempos por palavra, no estilo da marca (Raleway, palavra falada em destaque Tiffany, "fairhealth" em
  minúsculas), entregues como camada separada como as animações e sem colidir com elas. Mesmo teste no CapCut.
  Na primeira vez, um arquivo de teste curto para conferir no CapCut.
- Tipo e formato: reels do Instagram, vertical 9:16, de 30 a 90 s, com alguém falando para a câmera (ex.: Dr.
  Ronald). Motion sem gravação fica para depois, como versão curta do fluxo. Taxa de quadros: 30 fps
  (medida no primeiro bruto, 09/11; conferir a cada vídeo novo).
- Pastas (09/11, mudou): `~/FairHealth/Comunicação/Calude Editing/`, fora do repositório, com `Vídeos Brutos/`,
  `Referências/`, `Vídeos Prontos/` e `_CLAUDE/`. A cópia antiga em `video/ferramentas/Calude Editing/` não é mais usada.
  O repositório é público: a pasta inteira está no `.gitignore` (09/11) e os vídeos nunca vão para o git.
  Primeiro bruto: `marilia_0911_calude.mp4` (54,6 s, 720x1280, HEVC, 30 fps constante, áudio AAC
  44,1 kHz estéreo). Três referências gravadas da tela do
  celular (22 a 26 s, 1170x2532).
  Ferramentas, perfil, estado de cada vídeo e este caderno ficam no repositório (`video/`).
- Transcrição (09/11): local, de graça, com **mlx-whisper** (Whisper para o chip M2), modelo
  `large-v3-turbo`, `language="pt"`, `word_timestamps=True`, `condition_on_previous_text=False`.
  Teste no bruto da Marília (54,6 s): 18,6 s para transcrever, texto certo em todas as frases.
  - Tempos por palavra: a maioria a menos de 0,15 s, mas alguns erram de 0,3 a 0,6 s (as bordas invadem as
    pausas). Por isso a etapa de preparar **ajusta as bordas das palavras às pausas** medidas pelo FFmpeg
    (`silencedetect`) antes de qualquer corte. Se isso não bastar, testar alinhamento forçado (ex.: WhisperX).
  - "fairhealth" sai como "Fair Health": corrigir depois, por uma lista de termos (não pelo `initial_prompt`,
    que pode fazer o Whisper inventar frases).
  - Hesitações: este take não tinha nenhuma, então não deu para avaliar. Conferir no primeiro bruto com
    erros; o Whisper costuma limpar os "ééé". Trechos com som e sem palavra: retranscrever.
- Notas faladas (09/11): deixadas para depois. Sugestão em aberto: abrir com "nota de edição" e fechar com
  "fim da nota", com uma pausa curta antes e depois.
- Cortes (09/11): quase nenhum. A Marília grava ensaiado, num take só. O fluxo apara o começo e o fim e
  não corta o meio; se aparecer um erro ou uma pausa estranha, marca para a Nina decidir, sem cortar.
  Roteiro: não é usado nos cortes.
- Animação (09/11): poucas e no branding da fairhealth. Só nos momentos fortes, começando pelos números
  (ex.: "8 em cada 10", "98%") e a marca no fim. Quase tudo em sobreposição sobre a apresentadora; tela cheia
  só no fechamento com a marca. Ferramenta: HyperFrames (HTML em vídeo, como os `slides.html` dos carrosséis),
  usando cores, Raleway e logos de `instagram/marca/` e as regras de `instagram/diretrizes-criativas.md`
  (Tiffany visível, número só com fonte, área segura do 9:16).
  - Teste antes de usar: o fundo verde para chroma key pode apagar o Tiffany (azul-esverdeado). Na primeira
    vez, gerar um clipe curto com fundo verde e outro com transparência e conferir os dois no CapCut.
- Câmera (09/11): pouca e discreta. Duas ou três aproximações lentas no vídeo, um punch só nas frases mais
  fortes e a câmera casada com a entrada dos números. Sem seguir o rosto. Zoom máximo de 10 a 15% enquanto o
  bruto vier em 720x1280 (mais, se vier em 1080x1920 ou maior). O movimento vai pronto dentro do vídeo da
  apresentadora (o CapCut não importa keyframes), por isso a câmera é feita depois das animações.
- Som (09/11): efeitos poucos e baixos, só nas entradas das animações e no fechamento (pop, whoosh, clique,
  impacto suave). Biblioteca pequena de sons gratuitos com licença clara para uso comercial (ex.: CC0 do
  Freesound), conferida som a som, organizada por tipo, na pasta de ferramentas. Entrega: áudios separados
  no tempo certo. Música de fundo: fica com a Nina, no CapCut ou no Instagram (conta comercial tem
  biblioteca restrita).
- Revisões (09/11): (1) plano das animações e das legendas aprovado pelo chat, antes de animar; (2) animações e
  legendas prontas, no CapCut; (3) câmera e som, no CapCut (revisão final). Cortes sem revisão própria: o fluxo
  só avisa se marcou algum trecho. Correções pelo chat, citando o tempo ("0:21 o 98% entra cedo"); o que vale
  para outros vídeos vai para o caderno de aprendizados.
- Nomes (09/11): skill mestra `/editar`; prefixo das etapas `edit-` (ex.: `/edit-preparar`).

## Perfil
- fairhealth: escrito em 09/11, em `video/ferramentas/perfis/fairhealth/` (identidade, motion, câmera, cortes,
  som, catálogo e a síntese das referências). Identidade vinda da marca; jeito de mover vindo das referências.
  Pendentes: fotos do espaço como imagem de apoio (sim ou não); Tiffany `#9FC5BD` × `#96C5BD`.
- Referências (09/11): três gravações de tela em `Calude Editing/Referências/` (ref01 podcast de bem-estar,
  ref02 cirurgião "NO Edit / FINAL", ref03 "Raw Video / Claude Edit"). Folhas de contato e quadros em
  `Calude Editing/_CLAUDE/referencias/`. Análise feita pela imagem (sem medir curvas: são gravações de tela,
  com o vídeo pequeno e a interface do Instagram por cima). Aguardando a Nina confirmar a síntese.

## Fluxo aprovado (09/11)
Skill mestra: **`/editar`**. Claude Code aberto na raiz de `comunicao-fh`.
1. `edit-preparar`: briefing, inventário, transcrição (mlx-whisper + bordas pelas pausas + termos), aparar
   começo e fim (junta iniciar, preparar e cortes).
2. `edit-plano`: animações, legendas e intenção de câmera numa lista; aprovação pelo chat.
3. `edit-motion`: animações e legendas no HyperFrames; teste verde × transparente no CapCut na primeira vez;
   revisão no CapCut. (A etapa de assets saiu: tudo vem de `instagram/marca/`.)
4. `edit-camera`: aproximações e punch aplicados no vídeo da apresentadora.
5. `edit-som`: efeitos sonoros numa faixa.
6. `edit-entrega`: MP4 final e peças soltas, conferidos; revisão final no CapCut.
Entrega no CapCut: prévia + peças com a duração do vídeo inteiro, começando em 0:00 (é só arrastar).

## Skills escritas (09/11)
No repositório (versionadas no git), não em `~/.claude/skills`: `.claude/skills/editar/` (com
`regras-comuns.md`), `edit-preparar`, `edit-plano`, `edit-motion`, `edit-camera`, `edit-som`, `edit-entrega`.
Apoio: `video/ferramentas/termos.md`, `validacao.md`, `scripts/` (vazia: os scripts nascem no teste).

## Próximo passo
Fase 6: rodar o fluxo inteiro no bruto da Marília (`marilia_0911_calude.mp4`) com `/editar`, etapa por
etapa, escrevendo e testando os scripts. Abrir o Claude Code na raiz de `comunicao-fh`. Instalar a skill globalmente não é preciso:
ela está no repositório, em `.claude/skills/fluxo-de-edicao`.
