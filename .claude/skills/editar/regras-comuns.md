# Regras comuns das skills edit-*

Lidas uma vez por sessão por todas as skills de edição. Mudou uma regra geral? Mude aqui, não em cada skill.

## 0. Onde fica cada coisa
O Claude Code é aberto na raiz do repositório `comunicao-fh`. Caminhos a partir dela:

| O quê | Onde | No git? |
|---|---|---|
| Pasta da edição | `video/ferramentas/Calude Editing/` (abaixo: `CE/`) | não |
| Brutos | `CE/Vídeos Brutos/` | não |
| Referências de estilo | `CE/Referências/` | não |
| Trabalho do Claude, por vídeo | `CE/_CLAUDE/<video>/` (estado, transcrição, animações, renders) | não |
| Entregas, por vídeo | `CE/Vídeos Prontos/<video>/` | não |
| Scripts | `video/ferramentas/scripts/` | sim |
| Python | `video/ferramentas/.venv/bin/python` (mlx-whisper instalado) | não |
| Perfil | `video/ferramentas/perfis/<perfil>/` (hoje só `fairhealth`) | sim |
| Lista de termos | `video/ferramentas/termos.md` | sim |
| Formatos já validados no CapCut | `video/ferramentas/validacao.md` | sim |
| Biblioteca de sons | `video/ferramentas/sons/` (áudios fora do git, índice no git) | só o índice |
| Caderno da montagem | `video/ferramentas/montagem.md` | sim |

`<video>` é o nome do bruto sem extensão (ex.: `marilia_0911_calude`). A pasta tem caracteres acentuados
gravados pelo macOS em outra forma Unicode: nos comandos, use glob (`Refer*`, `V*deos Brutos`) em vez de
digitar o acento.

**O repositório é público.** Vídeo, áudio, quadro extraído e render nunca vão para o git. Antes de qualquer
commit, conferir `git status` e só adicionar scripts, perfil e textos.

## 1. Conversa e segurança
- Falar com a Nina em português, frases curtas, sem jargão sem explicar.
- Nunca mover, renomear ou apagar arquivos da Nina (brutos, referências, entregas antigas). Tudo o que o Claude
  gera fica em `CE/_CLAUDE/<video>/` ou em `CE/Vídeos Prontos/<video>/`.
- Nunca sobrescrever um arquivo entregue: versão nova (`_v01`, `_v02`…).
- Apagar, quando precisar, é mover para `CE/_CLAUDE/<video>/_lixeira/` e deixar a Nina apagar.
- Marca: "fairhealth" em minúsculas, número só com fonte, sem promessa clínica, sem preço
  (`instagram/voice.md`).

## 2. Estado do vídeo sem ler inteiro
Cada vídeo tem `CE/_CLAUDE/<video>/projeto.json` (esqueleto em
`.claude/skills/fluxo-de-edicao/modelos/estado-do-video.md`). Ler e mudar sempre pelo script de estado
`video/ferramentas/scripts/estado.py` (escrito na primeira vez que a `edit-preparar` rodar):
- `estado.py <video> status`: onde o vídeo está, pendências e alertas;
- `estado.py <video> <bloco>`: resumo de um bloco (`--json` para o bloco inteiro), `--item <id>`;
- `--set <caminho> <valor>`, `--etapa <etapa>=<status>`;
- `--pendencia <etapa> "<texto>"` e `--resolver <id>`.

Etapas, na ordem: `preparar`, `plano`, `motion`, `camera`, `som`, `entrega`. Status: `pendente`,
`em_andamento`, `aguardando_aprovacao`, `concluido`, `nao_precisa`.
Ids estáveis por item: `mo01` (animação), `lg01` (bloco de legenda), `cam01` (câmera), `sfx01` (som),
`mk01` (marcador). É por eles que a Nina pede ajustes.

## 3. Tempo e formato
- Taxa de quadros real do bruto (medir sempre; o primeiro era 30 fps constante). Toda conversão de segundos
  para frames passa por uma função só, nos scripts.
- Tempos guardados no tempo do arquivo bruto. O vídeo final começa no início aparado; os scripts convertem.
- Saída sempre em **1080x1920**, 9:16, mesmo com bruto menor.

## 4. Entrega no CapCut (vale para todas as etapas que entregam)
O CapCut não importa projeto de outro programa. Então cada entrega é:
- **`<video>_previa_vNN.mp4`**: tudo junto, para assistir.
- **Peças soltas, todas com a duração do vídeo inteiro e começando em 0:00**: assim a Nina arrasta cada uma
  para uma faixa no começo da linha do tempo e tudo fica no lugar, sem posicionar nada.
  - `apresentadora_vNN.mp4` (o vídeo aparado, com a câmera quando já existir, sem animação);
  - `animacoes_vNN` e `legendas_vNN` (no formato validado em `validacao.md`: fundo verde para chroma key ou
    transparência);
  - `sfx_vNN.wav` (todos os efeitos numa faixa só, no nível certo).
- Nomes fixos e uma pasta por versão: `CE/Vídeos Prontos/<video>/vNN/`.
- **Formato novo, teste primeiro:** antes de usar um formato pela primeira vez, gerar um teste curto (3 a 5 s),
  a Nina abre no CapCut e confirma. Anotar em `validacao.md` (data, formato, o que foi confirmado). Só depois
  usar de verdade.

## 5. Caderno de aprendizados (`CE/_CLAUDE/<video>/aprendizados.md`)
Durante a revisão de qualquer etapa, anotar na hora toda correção, elogio ou preferência que vale para outros
vídeos:
- "legenda mais alta", "esse pop ficou ótimo": **anota**;
- "tira essa frase": **não anota** (é só deste vídeo);
- na dúvida, anota com "(talvez só deste vídeo)".

Formato: `- [ ] <etapa> · <o que foi pedido, com contexto> · <dd/mm>`. Aplicado: `- [x] … → <onde entrou>`;
só daquele vídeo: `- [-] …`. Nunca apagar linhas. Anotar não é mudar: as skills e o perfil só mudam quando a
Nina pedir (seção 7).

## 6. Ponto salvo e fechar uma etapa
- **Ponto salvo:** etapa terminada, revisões aplicadas, entrega gerada. Só aí sugerir `/clear` e `/editar`.
- **Pendência:** pedido ainda não aplicado é anotado na hora pelo script de estado.
- **Fechar a etapa** (aprovada): marcar `concluido`, dizer quantos aprendizados ficaram anotados, sugerir
  `/clear` e `/editar`.
- Algo aprovado mudou depois (ex.: o plano mudou depois das animações)? Avisar o que precisa ser refeito.
- Scripts novos ou alterados: commit e push na `main` (só scripts e textos, ver seção 0).

## 7. Aplicar os aprendizados (quando a Nina pedir: `/editar aprendizados`)
1. Ler as linhas `- [ ]` dos cadernos de todos os vídeos.
2. Propor onde cada uma entra: gosto vai para o perfil (`estilo-*.md`, `identidade.md`, `catalogo.md`);
   ofício (vale para qualquer vídeo) vai para a skill da etapa; o que vale para todas vai para este arquivo.
3. A Nina filtra. Gravar só o aprovado, mostrando antes o texto das mudanças maiores. Marcar cada linha.
   Commit e push.

## 8. Economia
- `/clear` entre as etapas. Ler a transcrição por frase e o estado pelo script, nunca arquivos inteiros.
- Render e transcrição em segundo plano.
- Modelo sugerido: `/editar` e `edit-entrega` com o mais leve; `edit-preparar` intermediário; `edit-plano`,
  `edit-motion` e `edit-camera` com o mais capaz; `edit-som` com o mais capaz em esforço médio.
