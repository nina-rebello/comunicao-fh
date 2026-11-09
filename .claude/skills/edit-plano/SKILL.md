---
name: edit-plano
description: "Planeja as animações, as legendas dinâmicas e a câmera de um reel da fairhealth, numa lista numerada para a Nina aprovar pelo chat, sem animar nada. Use em /edit-plano, depois da edit-preparar."
---

# edit-plano

A etapa que mais decide a qualidade do reel. Propõe onde entram números, pílulas, cartões e a palavra-chave da
legenda, e a intenção da câmera em volta. **Não anima nada.** Mudar aqui é barato; depois do render, custa uma
rodada.

- **Lê:** `transcricao_frases.txt`, briefing, marcadores; o perfil inteiro (`identidade.md`,
  `estilo-motion.md`, `estilo-camera.md`, `catalogo.md`); `.claude/skills/fluxo-de-edicao/guias/oficio-motion.md`.
- **Escreve:** blocos `plano.motions` (`mo01`…), `plano.legendas` (`lg01`…), `plano.camera` (intenções).
- **Próximo passo:** `/edit-motion`

Se `preparar` não estiver `concluido`, pare e sugira terminá-la.

## Ofício
- **O conteúdo decide a animação.** Para cada ideia, a forma que explica melhor aquela ideia. O catálogo é
  repertório, nunca obrigação.
- **Densidade do perfil:** pouca animação, só nos momentos fortes (números, listas curtas, a marca no fim).
  Na dúvida, não anima: a apresentadora e a legenda se sustentam.
- **Gancho primeiro** (os primeiros 3 a 5 s): é o que segura no feed. Planeje com mais cuidado.
- **Uma protagonista por vez:** quando um número ou cartão entra, a legenda dá lugar.
- **Número só com fonte.** Cada número planejado leva a fonte que vai aparecer na tela. Sem fonte, pergunte à
  Nina antes de planejar; sem resposta, não anima o número.
- Releia antes de mostrar: o conceito nasce desta fala? Estou repetindo a mesma entrada em tudo?

## O plano
1. **Legendas (`lg`):** blocos de 2 a 5 palavras, troca na pausa da frase, uma palavra-chave por frase
   (a que carrega o sentido). Mostre só as palavras-chave escolhidas, não todos os blocos.
2. **Animações (`mo`):** uma linha cada: tempo, formato (sobreposição, pílulas ou cartão em tela cheia),
   palavra-gatilho com o tempo exato, o que aparece (texto exato da tela, fonte do dado), lado do rosto.
   Duração: do gatilho até ~1 a 1,5 s depois da última palavra que ele ilustra.
3. **Câmera (intenção em palavras):** as 2 ou 3 aproximações lentas, o punch (1 ou 2) e o que a câmera faz
   quando um número entra ao lado do rosto. Valores e curvas são da `edit-camera`.
4. **Fechamento:** cartão com a logo em círculo (nunca o coração junto de número).

## Resumo no chat
O plano numerado, curto, com a pergunta "Aprova, muda ou risca algum?". Marque `aguardando_aprovacao`.

## Revisão e aprovação
Por número: "mo02 tira", "lg04 a palavra-chave é cuidado", "mo03 do outro lado". Ao gravar de novo, preserve
o status do que já foi aprovado. Aprendizados no caderno. Com o "ok", `concluido`, `/clear` e `/editar`.

## Regras comuns
Antes de começar, leia `.claude/skills/editar/regras-comuns.md` (uma vez por sessão).
