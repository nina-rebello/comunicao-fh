---
name: edit-motion
description: "Constrói e renderiza as animações e as legendas dinâmicas aprovadas no plano de um reel da fairhealth, no HyperFrames, e entrega para revisão no CapCut. Use em /edit-motion, depois da edit-plano."
---

# edit-motion

Constrói cada item aprovado (`mo` e `lg`) no HyperFrames e entrega a prévia e as camadas para a Nina revisar
no CapCut. É a etapa mais longa e a que mais depende do ofício.

- **Lê:** blocos `plano.*`, transcrição por palavra (só o trecho de cada item); perfil (`identidade.md`,
  `estilo-motion.md`, peças-base quando existirem); guias `oficio-motion.md`, `hyperframes.md` e
  `etapa-motion-render.md` em `.claude/skills/fluxo-de-edicao/guias/`.
- **Escreve:** projetos em `CE/_CLAUDE/<video>/motion/`, renders versionados, `eventos_som.json`, bloco
  `motions` no estado; entrega em `CE/V*deos Prontos/<video>/vNN/`.
- **Próximo passo:** `/edit-camera`

Se `plano` não estiver `concluido`, pare e sugira terminá-lo.

## Antes da primeira vez de todas
- **HyperFrames:** confira a versão atual (`npx --yes hyperframes@latest --version`), fixe essa versão no
  estado do vídeo e use `npx --yes hyperframes@<versão>` em todos os comandos.
- **Teste no CapCut** (se `validacao.md` ainda não tiver o formato): um clipe de 3 a 5 s com uma pílula
  Tiffany e uma linha de legenda, em duas saídas: (a) MP4 com fundo verde `#00FF00` para chroma key e
  (b) MOV ProRes 4444 com transparência. A Nina abre as duas sobre um vídeo no CapCut e diz qual fica certa
  (o verde pode apagar o Tiffany, que é azul-esverdeado). Anotar em `validacao.md` e só então seguir.

## Construir
- Fontes da marca embutidas (Raleway de `instagram/marca/fontes/`, em base64 ou caminho local), cores do
  perfil, logo de `instagram/marca/logo-circulo.png`.
- Composição em 1080x1920 na taxa do vídeo. **Áreas seguras do perfil** (topo, base e lado direito livres).
- **Uma camada de animações e uma de legendas, cada uma com a duração do vídeo inteiro** (regras comuns,
  seção 4), no formato validado. Os itens ficam no tempo deles dentro da camada.
- Legenda palavra por palavra no tempo da transcrição, recentralizando a cada palavra (ofício §5); a
  palavra-chave em Raleway ExtraBold Itálico com marca-texto Tiffany e punch leve na hora em que é dita.
- Número contando até o valor, com a fonte pequena embaixo. Pílulas em cascata. Cartão em tela cheia e
  fechamento como no perfil.
- Anotar os **eventos para o som** ao construir (o que chega, sai, conta, revela; tempo, força, descrição).
- Ciclo por item: `check`, snapshots nos momentos-chave (olhar: legível, dentro da área segura, nada sobre o
  rosto), render em segundo plano, conferir resolução, fps, número de frames e um quadro composto sobre o
  vídeo.

## Scripts
| Script | O que faz | Armadilhas |
|---|---|---|
| `legendas.py` | blocos e tempos das legendas a partir da transcrição | troca de bloco na pausa; "fairhealth" minúsculo |
| `previa.py` | compõe bruto aparado + camadas numa prévia MP4 1080x1920 | escalar o bruto para 1080x1920; mesmo fps; chroma ou alpha conforme `validacao.md` |
Uso (testados em 09/11, `marilia_0911_calude`), a partir de `video/ferramentas/scripts/`:
1. `$PY legendas.py <video>`: gera `motion/legendas/index.html` a partir de `plano.legendas`
   (`palavras_chave` por tempo de início, `ocultar` [[ini, fim]], `correcoes` {"tempo": "palavra"}).
2. Animações: `motion/animacoes/index.html` escrito à mão por vídeo (uma composição com todos os `mo`, fundo
   transparente, duração `(frames − 0,5)/fps`). Fontes e logo copiados para dentro do projeto.
3. `npx --yes hyperframes@<versão> check` e `snapshot --at …`; compor o snapshot sobre o quadro do bruto
   escalado para conferir.
4. Render: `npx --yes hyperframes@<versão> render motion/<camada> --format mov --fps 30 -o renders/<camada>_vNN.mov`
   (ProRes 4444 com alfa; ~2 min para 55 s de animações, um pouco mais para as legendas).
5. `$PY previa.py <video> <N>`: prévia, apresentadora e camadas no formato de `validacao.md`;
   `$PY previa.py <video> <N> --teste-capcut INI FIM`: o teste dos dois formatos.
Os avisos `line_unread` do check nas legendas são esperados (a legenda segue a fala).

## Entrega e resumo
Pasta `vNN` com a prévia, `apresentadora_vNN.mp4` (aparada, escalada), `animacoes_vNN`, `legendas_vNN`
(regras comuns, seção 4). No chat: o que foi feito por item, o que não deu para fazer como no plano, o caminho
da pasta e "arraste cada peça para uma faixa no começo da linha do tempo do CapCut". Marque
`aguardando_aprovacao`.

## Revisão
- Por número ou por tempo: "mo02 mais lento", "0:21 o 98% entra cedo", "lg05 palavra-chave errada". Ajustar
  só o citado, renderizar versão nova, nova pasta `vNN`.
- Retorno geral ("sem vida", "básico") pede refazer, não retocar: releia as referências
  (`perfis/fairhealth/analises/sintese.md`), diga a nova direção em uma frase e construa de novo.
- Aprendizados no caderno. Na aprovação, o padrão que deu certo vira item do `catalogo.md` (com o "sim" da
  Nina). `concluido`, `/clear` e `/editar`.

## Regras comuns
Antes de começar, leia `.claude/skills/editar/regras-comuns.md` (uma vez por sessão).
