# Carrossel: O que é a fairhealth

> **Versão atual: v2 (11/10).** Texto em `texto.md`; arte em `slides-v2.html` → `png-v2/v01.png` …
> `v10.png`, nesta ordem (prévia: `previa-v2.jpg`). Para regerar:
> `node instagram/ferramentas/render.mjs instagram/posts/o-que-e-a-fairhealth/slides-v2.html instagram/posts/o-que-e-a-fairhealth/png-v2`
> A legenda da v2 está em `texto.md`. O conteúdo abaixo é da v1 (9 slides), guardada.
>
> **Elementos da v2:** trilha das três perguntas no topo de cada slide, empresa desenhada com o cuidado lá
> dentro (2), linha do tempo "a fairhealth entra aqui / o plano de saúde entra aqui" (3), os seis pilares em
> cartões com ícone (4), plantões alternados (5), quatro passos ligados por uma linha (6), pessoas em
> pictograma (7), quatro frentes em cartões com ícone (8) e o que a empresa recebe, com ícones (9).

Pedido do sócio (11/10): o post seguinte ao do Escritório do Cuidado apresenta a fairhealth, o que fazemos e
o que oferecemos, ligado ao post anterior ("Como funciona o Escritório do Cuidado"). Linha editorial:
institucional. Público: RH e colaboradores.

- **Artes** (1080 × 1350): `png/s01.png` … `png/s09.png`, nesta ordem. Prévia: `previa.jpg`.
- **Para regerar depois de editar:**
  `node instagram/ferramentas/render.mjs instagram/posts/o-que-e-a-fairhealth/slides.html instagram/posts/o-que-e-a-fairhealth/png`
- **Visual:** v1 com o tiffany no detalhe (fundos verde, creme e tiffany alternados) e três elementos gráficos
  da aba nova do livro da marca: cartões espiando nas bordas (ponte com o post anterior), Venn com o encontro
  cheio e pessoas em pictograma.
- **Correção de 11/10:** o slide 3 deixou de só citar o post anterior e passou a explicar o Escritório do
  Cuidado. O slide 7 deixou de tratar "medir, cuidar, conscientizar, comprovar" como método da fairhealth:
  são os quatro passos das quatro empresas da fairjob.

| Slide | Fundo | Conteúdo |
| --- | --- | --- |
| 1 | verde | Capa: "O que é a fairhealth?" + ponte com o último post |
| 2 | creme | Somos uma empresa de saúde corporativa (frase de quem somos) |
| 3 | tiffany | O Escritório do Cuidado é onde isso acontece: espaço dentro da empresa, médicos e psicólogos que se revezam, presencial ou remoto, a pergunta (cartão central) |
| 4 | verde | A gente trabalha no encontro (Venn: o que a empresa precisa × o que é importante para cada pessoa) |
| 5 | creme | O que oferecemos para quem é cuidado |
| 6 | tiffany | O que oferecemos para a empresa |
| 7 | creme | A fairhealth é o cuidar: os quatro passos do ecossistema fairjob (medir, cuidar, conscientizar, comprovar), um por empresa, com a fairhealth em destaque |
| 8 | verde | Prova: 8 em cada 10 pessoas voltaram para mais de um atendimento |
| 9 | creme | Logo, slogan e convite para falar pelo direct |

## Legenda

```
O Escritório do Cuidado você já conhece. Agora, o que é a fairhealth?

No último post, mostramos como o cuidado começa: com uma conversa e uma pergunta, "O que é importante para você?". A fairhealth é quem está por trás desse espaço.

Somos uma empresa de saúde corporativa e, no ecossistema fairjob, somos o cuidar. Levamos médicos e psicólogos para dentro da empresa, para cuidar das pessoas antes que o adoecimento vire afastamento.

Para quem é cuidado, isso significa atendimento perto, sigilo e um plano que cabe na rotina real, montado nos pilares da Medicina do Estilo de Vida. Para a empresa, significa um espaço de cuidado montado ali dentro e relatórios do grupo, anonimizados, para o RH decidir com evidência.

Numa indústria que atendemos, 8 em cada 10 pessoas voltaram para mais de um atendimento. Ninguém volta a um lugar onde não se sentiu cuidado.

Quer levar o Escritório do Cuidado para a sua empresa? Fale com a gente pelo direct.

Fazemos o certo pelos motivos certos.

#fairhealth #saudecorporativa #escritoriodocuidado #medicinadoestilodevida #gestaodepessoas
```

**Alt text da capa:** Fundo verde com o texto "O que é a fairhealth? No último post, você conheceu o
Escritório do Cuidado. Agora, quem está por trás dele."

**Checagem (caption.py):** tamanho, primeira linha, gancho, hashtags (5, começando por #fairhealth),
posição das tags, links, emoji e termos de busca passaram. O aviso "sem chamada" é falso: o verificador só
reconhece chamadas em inglês, e a legenda tem uma só ("Fale com a gente pelo direct").

## Validação antes de publicar

- **8 em cada 10:** dado liberado (indústria atendida, 1º semestre de 2026: 81,3% voltaram para 2 ou mais
  atendimentos), sem o nome da empresa.
- **Equipe:** o post fala em "médicos e psicólogos". Assistentes sociais ficaram de fora até a confirmação
  (pendência no `voice.md`).
- **NR-1:** "um aliado na prevenção dos riscos psicossociais", sem prometer conformidade.
- **Prazo do programa:** o post não cita os 12 meses (prazo de acompanhamento pede aval).
- **Pilares:** o post não diz quantos são, até a confirmação dos 6 pilares.
- **[CONFIRMAR] Verbo de cada empresa no slide 7:** cuidar = fairhealth está na essência. Os outros foram
  ligados pelo nome: medir = fairdata, conscientizar = fairedu, comprovar = fairtrust.
