# 27/11 · Foto única "Como ler o relatório do Escritório do Cuidado" (case de adesão)

Cronograma: `N12` em `marketing/ferramentas/conteudo_posts_novembro.py`.

## v2 (23/11): post único em forma de relatório

Pedido da Nina: no lugar do carrossel, um post único "como se fosse um relatório", com todos os dados explicados (o que
significa e como levar ao CFO e ao RH), numa estética clean e moderna, sem o visual do painel original.

- Dados: o relatório real do Escritório do Cuidado (print da Nina, 23/11), de 01/01 a 03/09/2026, modelo Quintuple Aim (IHI).
  Substituem os números do 1º semestre do `voice.md` (161 atendimentos, 98% de adesão, 81,3% de retorno).
  - 48 colaboradores atendidos, adesão de 94,1% (de 51 ativos); 189 atendimentos (quase 4 por pessoa); 46 smartbands
    (nos posts, "smartwatch"); retorno de 93,8% (45 de 48 com 2 ou mais atendimentos).
  - Formato: 181 presenciais (95,8%), 8 online (4,2%). Tipo: médico 75,7%, psicológico 17,5%, felicitológico 4,2%, serviço
    social 2,6%.
  - Quem: mulheres 50% (24), homens 35,4% (17), outros 14,6% (7); 18–24 16,7%, 25–34 27,1%, 35–49 39,6%, 50+ 16,7%.
- `slides.html` → `png/relatorio.png` (= `previa.png`). Papel, cartões brancos sem borda, números no verde da marca, barras
  em verde, Tiffany e menta. Quatro números com "Significa" e "Para o CFO e o RH"; três painéis com uma leitura cada.
- `canva-src.html` e `canva.html`: versão achatada para o Canva (conferida: igual ao PNG). Ainda não importada.
- `legenda.txt`: ig-caption (`caption.py` com "programa de saúde, adesão, indicadores": 3/3) e ig-human (`detect.py` 60,2,
  REVIEW só pelo VOICE, como nos outros posts).
- **Sem o nome do cliente** ("uma indústria atendida") até os sócios liberarem (decisão de 30/10). Sexta de Black Friday: sem
  linguagem de promoção.

Texto alternativo: "Relatório do Escritório do Cuidado de uma indústria atendida, de janeiro a setembro de 2026: adesão de
94,1%, retorno de 93,8%, 189 atendimentos, 46 smartwatches, 95,8% presencial, tipos de atendimento e perfil por idade e gênero,
cada número com o que significa para o CFO e o RH."

## v1: carrossel de 8 slides

`slides-v1-carrossel.html`, `png-v1-carrossel/`, `previa-v1-carrossel.png`, `legenda-v1-carrossel.txt`, `canva-v1-carrossel.html`
(números do 1º semestre). A capa usava `fotos/capa.jpg` (`gerar.py`).

## Pendências

- Sócios: o case sai? Com ou sem o nome Chemitec?
