---
name: editar
description: "Ponto de entrada da edição dos reels da fairhealth: mostra onde cada vídeo está (etapas, pendências, aprendizados anotados) e abre a skill da etapa certa. Também aplica os aprendizados (/editar aprendizados). Use em /editar, ao começar ou retomar um vídeo, depois de um /clear, ou quando a Nina perguntar em que pé está um vídeo."
---

# editar

Fluxo: `edit-preparar` → `edit-plano` → `edit-motion` → `edit-camera` → `edit-som` → `edit-entrega`

Antes de tudo, leia `regras-comuns.md` (nesta pasta), uma vez por sessão.

## /editar
1. **Qual vídeo:** liste os brutos em `video/ferramentas/Calude Editing/V*deos Brutos/` e, para cada um, se já
   tem `_CLAUDE/<video>/projeto.json`. Se a Nina disse qual, use esse; se só um está em andamento, proponha
   esse; senão pergunte.
2. **Vídeo novo** (sem `projeto.json`): diga que ele ainda não foi iniciado e ofereça a `edit-preparar`.
3. **Status:** rode `video/ferramentas/.venv/bin/python video/ferramentas/scripts/estado.py <video> status`
   e mostre de forma curta: etapas, pendências, alertas e quantos aprendizados estão anotados.
4. **Próximo passo:** diga qual é e pergunte se segue. Com o "sim", abra a skill da etapa e siga as
   instruções dela.
   - Etapa aguardando revisão: o próximo passo é continuar essa mesma etapa, nunca pular.
   - Alerta de algo desatualizado: mostre primeiro e espere a decisão.
   - A Nina pediu outra etapa: abra essa.
5. **Uma etapa por vez.** Não encadear etapas sozinho e não dar `/clear` (isso é sempre da Nina).
6. **Modelo:** lembre, numa linha, o modelo sugerido para a etapa (regras comuns, seção 8).

## /editar aprendizados
Siga a seção 7 das regras comuns.

## Regras
- Não editar vídeo nem rodar scripts de etapa: isso é das skills de cada etapa.
- Nunca mover, renomear ou apagar arquivos da Nina.
- Mudar o próprio fluxo (etapas, regras): é com `/fluxo-de-edicao`.
