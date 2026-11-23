# Carrossel: Geração Z e desconexão · 7 slides (25/11)

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
| 5 | Técnico | As causas da desconexão e a NR-01 |
| 6 | **Produto** | "O que importa para você?" no Escritório do Cuidado (foto do espaço): profissionais, bioimpedância e smartwatches, plano pela Medicina do Estilo de Vida; o RH recebe dados anonimizados e agregados |
| 7 | **Salvamento + chamada** | Para o líder: três perguntas no lugar do rótulo. Comente CUIDADO. Fonte completa. |

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

## Fotos escolhidas (16/11)

A Nina mandou opções e escolheu, para as quatro vagas (teste de composição feito só no chat; as fotos não entram no
repositório, que é público, até os direitos estarem confirmados):

| Slide | Foto escolhida | Observação |
|---|---|---|
| 1 · capa | Moça olhando para cima num escritório, colegas desfocados dos lados, luz de filme (vertical) | Rosto no alto, título embaixo |
| 2 | Grupo de jovens almoçando numa mesa, luz natural, janelas ao fundo (vertical, recortada na faixa horizontal) | Parece ensaio de marca de roupa: conferir antes de usar |
| 3 | Moça no celular entre pilhas de livros, luz quente (vertical, na faixa estreita ao lado do 46,7%) | Tem tela de app de música visível |
| 4 | Rapaz no metrô, fone, cabeça para trás e olhos fechados, janela com movimento (vertical 4:5) | Escolhida no lugar da foto do ônibus: o rosto fica no alto e o texto na parte escura |

Descartadas: a do ônibus (o rapaz ficava atrás do texto), a mulher com post-its no rosto (texto em cirílico, cena
carregada) e a mulher na janela com chuva (parece imagem de IA).

**Antes de publicar:** achar a origem de cada uma pelo Google Lens, baixar o original (Unsplash, Pexels ou banco pago,
com pelo menos 1080 px de largura) e salvar em `fotos/`. As cópias recebidas têm de 736 a 1200 px e vêm do Pinterest.

## Slide 7 com a foto do Escritório (16/11)

A Nina não gostou do render do espaço no slide 7. Entrou a foto real do Escritório do Cuidado (a mesma do post de 06/11,
`instagram/posts/historia-2009/fotos/espaco-nina-original.jpg`, foto da marca), numa faixa de 1080 × 640 no alto
(`fotos/gz-07-faixa.jpg`), com o texto em fundo escuro embaixo. Em tela cheia, as poltronas ficavam atrás do texto.

## Tipografia (16/11)

Pedido da Nina: menos Instrument Serif; o padrão é Raleway e a serif fica só para detalhes. Todos os textos e títulos
que estavam em serif passaram a Raleway (tamanhos reduzidos, porque a Raleway é mais larga), e os destaques em itálico
viraram cor ou negrito. A serif ficou só na pergunta "o que importa para você?" (slide 7 e item 3 do slide 8). Regra
registrada no `CLAUDE.md`.

## Cores (16/11)

A Nina testou a versão em branco e Tiffany e preferiu a versão escura anterior. Ficou assim: capa e slide 4 em foto;
2 e 5 em papel (creme); 3, 6 e 7 no fundo "noite" (`#14201E`); 8 no verde-escuro da marca `#2F6B64`. O logo do
último slide voltou sem o anel branco. A versão branca e Tiffany fica no histórico do git (commit anterior a este).
Atenção: o fundo "noite" contraria a regra de cores do `CLAUDE.md` (16/11); falta a Nina dizer se a regra muda ou se
este post é exceção.

## Revisão de 23/11 (pedido da Nina)

- **Saiu o slide do meme** ("A desconexão virou meme", Gen Z stare e task masking): não condiz com a linguagem técnica, intelectual e
  médica da marca. O carrossel passou a **7 slides** e os ids foram renumerados (`gz-01` a `gz-07`). A legenda perdeu a frase do meme, e o
  cronograma de novembro (`conteudo_posts_novembro.py` e a planilha) foi atualizado.
- Continuam pendentes: as fotos dos slides 1 a 4, a conferência dos números no material original, o que o relatório do RH mostra e a revisão
  do Dr. Ronald.
- **Canva (23/11):** `canva-fotos.py` gera o `canva.html` a partir do `slides.html`, com tudo em posição absoluta (achatado por
  `instagram/ferramentas/achatar.mjs`, que mede o slide no navegador e escreve cada texto numa caixa própria, com as quebras de linha
  do navegador). As vagas de foto viram quadros lisos (`fotos-canva/vaga-*.png`) e os degradês viram camadas PNG por cima. As fotos
  escolhidas não entram no repositório: vão direto para o Canva por upload e entram no lugar dos quadros.
- No slide 6, a pergunta "o que importa para você?" passou para uma linha própria, abaixo de "mesma pergunta:", porque o Canva não
  aceita duas fontes na mesma caixa de texto.
- **No Canva (23/11):** design `DAHbvhptIK0` ("25/11 Geração Z e desconexão (carrossel)"), 7 páginas, com as quatro fotos já nos
  quadros e todos os textos editáveis. Link de edição: https://www.canva.com/d/XbGWPpCX_jdAcmw

## Versão Tiffany (23/11)

Retorno da Nina: os slides estavam escuros demais ("mórbido"); pediu o Tiffany no lugar do azul escuro onde fosse possível, num link
do Canva separado para não perder o anterior.

- Slides 3, 5 e 6 saíram do fundo "noite" para o Tiffany `#9FC5BD` (acento `#24564F`). O slide 7 continua no verde-escuro da marca
  `#2F6B64`, como o único slide de contraste; o 2 continua em papel.
- O degradê por cima das fotos (capa e slide 4) saiu do quase preto e foi para o verde da marca `#2F6B64`, mais leve no alto.
- A versão escura fica em `slides-v2-escura.html`, `png-v2-escura/` e `previa-v2-escura.png`, e no Canva em `DAHbvhptIK0`.
- **No Canva (23/11):** design separado `DAHbvqgIZ0k` ("25/11 Geração Z e desconexão (versão Tiffany)"), 7 páginas, com as fotos nos
  quadros. Link de edição: https://www.canva.com/d/BPeePZuDoGUUSJ3

