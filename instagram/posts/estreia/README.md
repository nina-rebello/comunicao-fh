# Estreia: 3 posts (segunda, 28/09, 7:30)

Existem **duas versões**:
- **Versão humana (recomendada):** `slides-humano.html` → `png-humano/` (h1, h2,
  h3). As legendas estão no fim deste arquivo.
- **Versão fairedu:** `slides.html` → `png/` (p1, p2, p3), mais sóbria.

Ordem de publicação: **#3 → #2 → #1**, para o #1 ficar no topo da grade.
Fixar o #1.

- **Artes prontas** (1080x1350) em `png/`. O texto de cada slide está em
  `slides.html`.
- **Para regerar depois de editar:**
  `node instagram/ferramentas/render.mjs instagram/posts/estreia/slides.html instagram/posts/estreia/png`
- **Estilo:** modelo @fairedu.br (Raleway, negrito itálico nas palavras-chave,
  sublinhado e caixa de destaque) com a paleta da fairhealth.
- **[PENDENTE]** As fotos de fundo são renders do espaço. Confirmar se podem
  ser usadas.

| Post | Arquivos | Upload |
| --- | --- | --- |
| #1 Carrossel: Por que a fairhealth existe | `png/p1-01.png` … `p1-09.png` | 9 imagens, nesta ordem |
| #2 Foto: Manifesto | `png/p2-manifesto.png` | 1 imagem |
| #3 Carrossel: Cuidado tem método | `png/p3-01.png` … `p3-08.png` | 8 imagens, nesta ordem |

---

## #1 Legenda

```
E se o afastamento começar muito antes do atestado?

Sono ruim, estresse acumulado, um hábito que escorrega, uma dor que ninguém trata. Nada disso aparece em relatório. Quando chega ao RH, já virou atestado, afastamento ou sinistro no plano de saúde.

Isso não significa que o RH chegou atrasado por descuido. Significa que o cuidado, do jeito que costuma ser oferecido, fica longe demais de quem precisa.

A fairhealth nasceu para mudar essa ordem na saúde corporativa: levar médicos, psicólogos e assistentes sociais para dentro da empresa e cuidar antes que o adoecimento vire afastamento.

E, porque cuidado sem dado é só intenção, comprovar o resultado com evidência.

#fairhealth #saudecorporativa #saudedotrabalhador #gestaodepessoas #rh
```

**Alt text da capa:** Sala de espera do Escritório do Cuidado com o texto "O
afastamento não começa no atestado. Por que a fairhealth existe."

## #2 Legenda

```
Cuidar antes que o adoecimento vire afastamento. E comprovar com dados.

Essa é a frase que orienta tudo o que fazemos.

Saúde corporativa não pode depender só do plano de saúde e do atestado. Os dois chegam quando o problema já está instalado.

Por isso a fairhealth, do ecossistema fairjob, leva o cuidado para dentro da empresa: atendimento médico, psicológico e social, perto de quem precisa, com menos barreira e mais adesão.

Fazemos o certo pelos motivos certos.

#fairhealth #fairjob #saudecorporativa #prevencao #gestaodepessoas
```

**Alt text:** Sala de atendimento com o texto "Cuidar antes que o adoecimento
vire afastamento. E comprovar com dados." e a logo da fairhealth.

## #3 Legenda

```
Cuidado também precisa de método.

Sem ele, programa de saúde corporativa vira evento: todo mundo participa uma vez, e nada muda.

O nosso cabe em quatro palavras. Medir, para entender de onde cada pessoa parte. Cuidar, com atendimento médico, psicológico e social baseado na Medicina do Estilo de Vida. Conscientizar, porque hábito só muda quando a pessoa entende o porquê. Comprovar, porque o RH precisa decidir com evidência, não com intenção.

É esse caminho que a fairhealth leva para dentro das empresas: da intenção à evidência.

#fairhealth #saudecorporativa #medicinadoestilodevida #gestaodepessoas #nr1
```

**Alt text da capa:** Card verde com o texto "Cuidado tem método. Quatro
etapas, do primeiro dado à evidência."

---

## Checagem (caption.py)

Tamanho, primeira linha, hashtags (5, começando por #fairhealth) e termos de
busca: todos passaram.

As legendas seguem o estilo do @fairedu.br e fecham com a marca, sem pedir
nada. A chamada ("Siga", "Salve") fica no último slide. Nenhuma legenda usa
emoji ou travessão.

---

# Versão humana: legendas

## #1 Antes do atestado, tem uma pessoa (`png-humano/h1-01` … `h1-09`)

```
Antes de todo atestado, tem uma pessoa.

Alguém que anda dormindo mal. Que sente um cansaço que não passa. Que tem uma dor que foi ficando, porque marcar consulta, se deslocar e perder meio dia de trabalho nunca cabe na semana.

Quando essa história chega ao RH, ela já virou atestado, afastamento ou sinistro no plano. Mas ela começou muito antes, e quase sempre dava para cuidar mais cedo.

Foi por isso que a fairhealth nasceu. A gente leva médicos, psicólogos e assistentes sociais para dentro da empresa, perto de quem precisa, para o cuidado deixar de ficar para depois.

E mostra ao RH o que mudou, com relatórios anonimizados. O que é conversado no atendimento fica no atendimento.

Prazer, somos a fairhealth. Que bom ter você por aqui.

#fairhealth #saudecorporativa #cuidado #gestaodepessoas #rh
```

## #2 Manifesto (`png-humano/h2-manifesto`)

```
Cuidar das pessoas antes que o adoecimento vire afastamento.

É isso que move a gente todos os dias.

Saúde no trabalho não deveria aparecer só no atestado ou na fatura do plano. Ela está no sono, no estresse, na rotina, nas conversas que ninguém teve tempo de ter.

Por isso a fairhealth, do ecossistema fairjob, leva o cuidado para perto: atendimento médico, psicológico e social dentro da empresa, com menos barreira e mais gente se cuidando de verdade.

Fazemos o certo pelos motivos certos.

#fairhealth #fairjob #saudecorporativa #cuidado #prevencao
```

## #3 Cuidar tem jeito (`png-humano/h3-01` … `h3-08`)

```
Cuidar tem jeito. O nosso começa escutando.

Primeiro, a gente conhece a pessoa: rotina, sono, estresse, hábitos. Só depois orienta.

Aí vem o cuidado de verdade, com um plano feito para ela, e não um protocolo igual para todo mundo. Atendimento médico, psicológico e social, com base na Medicina do Estilo de Vida.

A gente também explica o porquê de cada mudança, porque hábito que faz sentido é hábito que fica.

E, no fim, mostra ao RH o que mudou no grupo, sem expor ninguém.

Medir, cuidar, conscientizar, comprovar. Tudo isso perto de quem precisa.

#fairhealth #saudecorporativa #medicinadoestilodevida #cuidado #gestaodepessoas
```
