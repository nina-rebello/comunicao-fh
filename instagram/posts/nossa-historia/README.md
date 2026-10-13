# Post 02: nossa história começou em um hospital

Post 02 do calendário de 12 posts (bloco 01, Reconhecimento). O roteiro é a proposta da Nina de 13/10,
com os ajustes listados abaixo. Calendário de referência: `marketing/calendario-12-posts.md`.

- **Formato:** carrossel de 6 slides, 1080 × 1350.
- **Objetivo:** contar a origem do modelo e criar conexão com o propósito.
- **Arte:** `slides.html` → `png/h01.png` … `h06.png` (prévia em `previa.jpg`), gerada por `gerar_slides.py`.
- **Para regerar:**
  `python3 gerar_slides.py slides.html && node ../../ferramentas/render.mjs slides.html png`

## Direção visual

- **Fio contínuo:** um único fio atravessa os seis slides. Ele é a trajetória de 2009 até hoje:
  - nasce num ponto na capa;
  - marca "2009" no slide 2 e "hoje" no slide 5;
  - sobe no slide da evolução;
  - termina no logo, no último slide.
- **Capa:** fundo de luz, como a capa do "O que é a fairhealth", para os dois posts conversarem na grade.
- **Fundos:** verde e creme se alternam. Só Raleway, sem amarelo.

## Roteiro

| Slide | Etiqueta | Título | Texto |
| --- | --- | --- | --- |
| 1 | Nossa história | Antes de chegar às empresas, nossa história começou *em um hospital*. | 2009 → hoje |
| 2 | O início | 2009 · Dentro de um hospital, surgiu o *Escritório do Paciente*. | Um modelo de cuidado que colocava a escuta e as necessidades de cada pessoa no centro da atenção. |
| 3 | A essência | Por trás de cada atendimento, existe *uma pessoa*. | Com a sua própria história, hábitos, necessidades e prioridades. Por isso, escutar sempre foi parte essencial da nossa maneira de cuidar. |
| 4 | Evolução | Com o tempo, essa forma de cuidar *evoluiu*. | E surgiu a possibilidade de aproximar o cuidado preventivo de um lugar que faz parte da rotina das pessoas: o trabalho. |
| 5 | Hoje | Hoje, essa filosofia está presente na *fairhealth*. | Levamos cuidado individualizado, prevenção e acompanhamento para dentro das empresas, conectando profissionais de saúde, conhecimento e tecnologia. Nota: o Escritório do Paciente virou o Escritório do Cuidado. |
| 6 | O propósito | Os lugares mudaram. *A essência do cuidado permanece.* | Da experiência hospitalar ao ambiente corporativo, seguimos com um mesmo princípio: o cuidado começa pela pessoa. Logo no fim do fio. |

## Ajustes na proposta (13/10)

1. **"Milhões de pessoas" saiu do slide 4.** Virou "um lugar que faz parte da rotina das pessoas". É um
   número sem fonte, e a regra é número só com fonte.
2. **O nome "Escritório do Cuidado" entrou no slide 5**, numa nota pequena. Liga a origem ao post do
   Escritório, que já foi publicado, e mostra que o nome do hospital continua vivo.
3. **Nome da marca em minúsculas (fairhealth)**, como no `voice.md` e no "O que é a fairhealth" publicado.
4. **Hashtags sem acento e em minúsculas**, 5, começando por #fairhealth (`voice.md`).
5. **Assinatura:** a legenda fecha com "O cuidado começa pela pessoa." sem repetir o nome da marca. O
   slogan oficial ("Fazemos o certo pelos motivos certos.") fica para os posts de convite.

## Legenda

```
A história por trás da fairhealth começou muito antes de chegarmos às empresas.

Em 2009, dentro de um hospital, nascia o Escritório do Paciente: um modelo de cuidado que tinha a escuta e as necessidades de cada pessoa como ponto de partida.

Ao longo do tempo, essa forma de cuidar evoluiu e encontrou novos espaços. O Escritório do Paciente virou o Escritório do Cuidado.

Hoje, na fairhealth, levamos essa filosofia para dentro das empresas, aproximando o cuidado preventivo da rotina das pessoas.

Porque, para nós, cuidar não é apenas olhar para a saúde. É olhar para quem está por trás dela.

O cuidado começa pela pessoa.

#fairhealth #saudecorporativa #medicinapreventiva #cuidadohumanizado #escritoriodocuidado
```

**Alt text da capa:** Fundo escuro com luz verde-água e o texto "Antes de chegar às empresas, nossa história
começou em um hospital". Um fio verde-água nasce num ponto, com a legenda "2009 → hoje".

## Validar antes de publicar

- **[CONFIRMAR]** O ano de 2009 e a passagem do Escritório do Paciente para o Escritório do Cuidado
  (`essencia.md`: 2009 no hospital; Escritório do Cuidado em 2024 e 2025). Sem o nome do hospital nem de
  pessoas.
- **[CONFIRMAR]** "Validado no SUS" fica de fora até a fonte ser confirmada.
