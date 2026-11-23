# 27/11 · Foto única "Como ler o relatório do Escritório do Cuidado" (case de adesão)

**Post final (aprovado pela Nina em 23/11):** `png/relatorio.png` e `legenda.txt`, sem o nome do cliente ("uma indústria
química atendida").

Cronograma: `N12` em `marketing/ferramentas/conteudo_posts_novembro.py`.

## v2 (23/11): post único em forma de relatório

Pedido da Nina: no lugar do carrossel, um post único "como se fosse um relatório", com todos os dados explicados (o que
significa e como levar ao CFO e ao RH), numa estética clean e moderna, sem o visual do painel original.

- Dados: o relatório real do Escritório do Cuidado de 01/01 a 23/11/2026 (PDF da Nina, 23/11), modelo Quintuple Aim (IHI).
  Substituem os do print de jan a set e os do 1º semestre do `voice.md`.
  - 51 colaboradores atendidos, adesão de 92,7% (de 55 ativos); 210 atendimentos (mais de 4 por pessoa); 48 smartbands
    (nos posts, "smartwatch"); retorno de 96,1% (49 de 51 com 2 ou mais atendimentos).
  - Formato: 198 presenciais (94,3%), 12 online (5,7%). Tipo: médico 75,2%, psicológico 18,6%, felicitológico 3,8%, serviço
    social 2,4%.
  - Idade: 18–24 15,7% (8), 25–34 23,5% (12), 35–49 45,1% (23), 50+ 15,7% (8). O gênero veio vazio nesse relatório (0% e 0%,
    "outros" 100%) e saiu do post; vale avisar quem gera o relatório.
- `slides.html` → `png/relatorio.png` (= `previa.png`). Papel, cartões brancos sem borda, números no verde da marca, barras
  em verde, Tiffany e menta. Quatro números com "Significa" e "Para o CFO e o RH"; três painéis com uma leitura cada.
- `canva-src.html` e `canva.html`: versão achatada para o Canva (conferida: igual ao PNG), pronta para importar.
- `legenda.txt`: ig-caption (`caption.py` com "programa de saúde, adesão, indicadores": 3/3) e ig-human (`detect.py`
  REVIEW só pelo VOICE, como nos outros posts).
- **Sem o nome do cliente** ("uma indústria química atendida", pedido da Nina em 23/11) até os sócios liberarem (decisão de 30/10). Sexta de Black Friday: sem
  linguagem de promoção.

Texto alternativo: "Relatório do Escritório do Cuidado de uma indústria química atendida, de janeiro a novembro de 2026: adesão de
92,7%, retorno de 96,1%, 210 atendimentos, 48 smartwatches, 94,3% presencial, tipos de atendimento e faixas de idade,
cada número com o que significa para o CFO e o RH."

## v1: carrossel de 8 slides

`slides-v1-carrossel.html`, `png-v1-carrossel/`, `previa-v1-carrossel.png`, `legenda-v1-carrossel.txt`, `canva-v1-carrossel.html`
(números do 1º semestre). A capa usava `fotos/capa.jpg` (`gerar.py`).

## Pendências

- Sócios: o case sai? Com ou sem o nome Chemitec?
