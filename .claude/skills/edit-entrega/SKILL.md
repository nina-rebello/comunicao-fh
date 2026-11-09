---
name: edit-entrega
description: "Monta a entrega final de um reel da fairhealth: o MP4 completo e as peças soltas para o CapCut, numa versão nova, e confere tudo antes de entregar. Use em /edit-entrega, depois da edit-som."
---

# edit-entrega

Junta tudo o que foi aprovado: o MP4 completo para postar ou acabar no CapCut, e as peças soltas para
retoques. Não muda nada criativo.

- **Lê:** os últimos arquivos aprovados de cada etapa (pelo estado), `validacao.md`.
- **Escreve:** `CE/V*deos Prontos/<video>/final_vNN/` e o bloco `entrega` no estado.
- **Próximo passo:** nenhum (o vídeo está pronto). Sugerir `/editar aprendizados` se houver linhas anotadas.

Se `som` não estiver `concluido` (ou `nao_precisa`), pare e sugira terminá-la.

## O que entra na pasta
- `<video>_final_vNN.mp4`: 1080x1920, fps do bruto, H.264, AAC 48 kHz, voz em torno de -14 LUFS (perfil),
  sem música.
- As peças soltas (regras comuns, seção 4), todas com a duração do vídeo e começando em 0:00.
- `LEIA.txt` curto: o que é cada arquivo e a ordem das faixas no CapCut (apresentadora embaixo, animações,
  legendas por cima; `sfx` abaixo da voz).

## Conferir antes de entregar
Resolução, fps e número de frames iguais em todas as peças; nenhum texto fora da área segura (3 quadros: no
gancho, no número principal e no fechamento); "fairhealth" minúsculo; todo número com a fonte na tela;
loudness. Mostrar os 3 quadros à Nina.

## Scripts
| Script | O que faz | Armadilhas |
|---|---|---|
| `entrega.py` | compõe o final, copia as peças, mede loudness e frames | nunca sobrescrever uma versão; caminhos com acento por glob |
Na primeira vez, escreva, teste e anote o uso aqui.

## Revisão e aprovação
A revisão final é no CapCut. Ajuste pedido aqui volta para a etapa dona dele (ex.: som → `edit-som`), que gera
versão nova; depois a entrega é refeita. Com o "ok", `concluido` e lembrar a legenda do post (skill
`ig-caption`, regra do projeto).

## Regras comuns
Antes de começar, leia `.claude/skills/editar/regras-comuns.md` (uma vez por sessão).
