# Carrossel: Geração Z e desconexão · 8 slides (25/11)

Primeiro teste no tom editorial da @brandsdecoded_: manchete sem serifa,
texto em serifa (Instrument Serif), dado com nome da pesquisa e da autora,
foto em tela cheia. As cores e a logo são da fairhealth. Série "Cuidado em
números".

O texto de cada slide está em `slides.html`, as artes em `png/` e a prévia em
`previa.png`. Para regerar:
`node instagram/ferramentas/render.mjs instagram/posts/geracao-z/slides.html instagram/posts/geracao-z/png`

| Slide | Função | Conteúdo |
| --- | --- | --- |
| 1 | Capa | Por que a Geração Z está tão desconectada do trabalho? Não é preguiça. A desconexão tem causa. |
| 2 | Promessa | A pesquisa: 33% dos jovens muito satisfeitos, contra 47,9% |
| 3 | Dado | 46,7% dizem que o trabalho os deixa mais infelizes (20,5% nas outras idades) |
| 4 | Dado | Mais de 1 em cada 5 não tem com quem contar; 27% preocupados; 71,1% tristes com as redes |
| 5 | Tendência | Gen Z stare e task masking: o meme descreve um sintoma |
| 6 | Técnico | As causas da desconexão e a NR-01 |
| 7 | **Produto** | "O que importa para você?" no Escritório do Cuidado (foto do espaço): profissionais, bioimpedância e smartwatches, plano pela Medicina do Estilo de Vida; o RH recebe dados anonimizados e agregados |
| 8 | **Salvamento + chamada** | Para o líder: três perguntas no lugar do rótulo. Comente CUIDADO. Fonte completa. |

## Fotos que faltam (slides 1, 2, 3 e 4)

As áreas listradas são vagas de foto, com a cena descrita em cada uma. O tom
depende delas: foto real, luz natural, gente comum, nada de banco de imagem com
cara de anúncio.

- Usar banco de imagem com licença comercial (Unsplash, Pexels ou pago) ou a
  sessão de fotos. Nunca colaborador atendido.
- Para trocar: salvar em `instagram/posts/geracao-z/fotos/`, tirar a classe
  `vaga` (e o aviso) e pôr `style="background-image:url(fotos/arquivo.jpg)"`
  na seção ou no bloco.

## Confirmar antes de publicar

- Os números são do Mapa da Felicidade Real dos Brasileiros 2026 (Renata
  Rivetti e Instituto Ideia; 1.500 entrevistas; 20/02 a 01/03/2026; margem de
  2,5 pontos), conforme Metrópoles e Grupo Amanhã. Conferir no material
  original. "Mais de 1 em cada 5" vem de 79% que dizem ter com quem contar.
- O que o relatório para o RH mostra de fato (slide 8).
- Revisão do Dr. Ronald (saúde mental, NR-01).
- A @brandsdecoded_ já publicou um carrossel com esses mesmos dados. O nosso
  se diferencia pelo que vem depois do dado: o que a empresa faz e o
  Escritório do Cuidado.

## Legenda

Em `legenda.txt` (revisada em 16/11).

## Revisão de 16/11 (regras de 12 e 13/11)

- **8 slides** (o máximo da marca): o antigo slide 8 (RH + três perguntas) e o 9 (chamada) foram reorganizados.
  A parte do RH entrou no slide 7; as três perguntas para o líder foram para o último slide, com o Comente CUIDADO
  e a fonte. Saiu o "Geração Z não é o problema. Falta de cuidado é.", que dizia a mensagem de forma explícita
  demais (regra do `CLAUDE.md`), e o segundo pedido ("mande para um líder"), para ficar uma chamada só.
- **Slide 7:** como o site descreve o Escritório: médicos, psicólogos, assistentes sociais e felicitologistas;
  medições com bioimpedância e smartwatches; plano individual com base na Medicina do Estilo de Vida (dentro do
  Escritório); o RH recebe dados anonimizados e agregados.
- **Legenda** atualizada no mesmo sentido, conferida com `caption.py` e `detect.py`.
- A v1 de 9 slides fica em `slides-v1-9slides.html` e `png-v1-9slides/`.
- **Continua pendente:** as fotos dos slides 1 a 4 (vagas listradas), a conferência dos números no material
  original do Mapa da Felicidade e a revisão do Dr. Ronald.

## Capa nova (16/11)

Pedido da Nina: deixar claras a pergunta "Por que a Geração Z está tão desconectada do trabalho?" e a ideia "não é
preguiça, a desconexão tem causa". A capa passou a ter a pergunta como título, em Raleway 800 (pedido dela), e
"*Não é preguiça.* A desconexão tem causa." como subtítulo em serif. O "olhar vazio na reunião" continua no slide 5
(o meme), e o slide 6 ("Desconexão tem causa. E nenhuma delas é a idade.") responde à capa. A primeira linha da
legenda virou a mesma pergunta; o termo de busca "saúde mental no trabalho" foi para o parágrafo da NR-01.
