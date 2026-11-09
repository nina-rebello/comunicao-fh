# Montagem do fluxo de edição

Fase atual: 2 (entrevista) · Atualizado em 09/11/2026

## Ambiente
- **Decisão (09/11):** a edição passa para o Claude Code instalado no computador da Nina, com os vídeos em
  pastas locais.
- Computador da Nina (conferido em 09/11): macOS 27, Apple M2, 8 GB de memória, Python 3.13.3, Node 23.11
  (npx 10.9), Git 2.39, Homebrew 7.0. **Falta o FFmpeg.** Sem GPU NVIDIA: a transcrição local roda no chip M2
  (mais devagar, mas dá para reels de 30 a 90 s). Disco: 40 GB livres (91% cheio), atenção com renders.
- Até aqui a montagem foi na nuvem (Linux, Python 3.13, FFmpeg 6.1, Node 22, sem GPU), só para referência.
- Instalado nesta montagem: nada ainda.

## Decisões
- Revisão: no CapCut. O CapCut não importa projeto de outro programa (ajuda do CapCut), então a entrega é
  o MP4 completo mais as peças soltas: o vídeo cortado sem animação, cada animação em MP4 com fundo verde
  (para o chroma key do CapCut) e os efeitos sonoros em áudio. Legendas: as automáticas do CapCut.
  Na primeira vez, um arquivo de teste curto para conferir no CapCut.
- Tipo e formato: reels do Instagram, vertical 9:16, de 30 a 90 s, com alguém falando para a câmera (ex.: Dr.
  Ronald). Motion sem gravação fica para depois, como versão curta do fluxo. Taxa de quadros: medir no
  primeiro vídeo.
- Pastas: `video/ferramentas/Calude Editing/`, com `Vídeos Brutos/`, `Referências/` e `Vídeos Prontos/`.
  O repositório é público: os vídeos não podem ir para o git.
  Primeiro bruto: `marilia_0911_calude.mp4` (54,6 s, 720x1280, HEVC). Três referências gravadas da tela do
  celular (22 a 26 s, 1170x2532).
  Ferramentas, perfil, estado de cada vídeo e este caderno ficam no repositório (`video/`).
- Transcrição: (a decidir)
- Notas faladas: (a decidir)
- Animação: (a decidir)
- Câmera: (a decidir)
- Som: (a decidir)
- Revisões: (a decidir)
- Nomes: (a decidir)

## Perfil
- fairhealth: a criar na fase 3. Base visual em `instagram/diretrizes-criativas.md` e `instagram/marca/`.

## Fluxo aprovado
(fase 4)

## Skills escritas
(fase 5)

## Próximo passo
Proteger os vídeos do git (.gitignore), instalar o FFmpeg e seguir a entrevista pela decisão 4
(transcrição; sugestão: local, de graça, no chip M2). Instalar a skill globalmente não é preciso:
ela está no repositório, em `.claude/skills/fluxo-de-edicao`.
