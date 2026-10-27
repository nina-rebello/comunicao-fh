# Carrossel 28/10: Prevenção também é investimento · 8 slides

Semana 2, bloco 2 (Relevância). Quem monta: Charles. O texto de cada slide está
em `slides.html`, as artes em `png/` e a prévia em `previa.png`.

**Status:** rascunho para aprovação. As fotos ainda são molduras com a
descrição da cena.

## O estilo novo

Referência: carrosséis do @brandsdecoded_. A ideia é manter as cores e as
fontes da marca e mudar a forma.

- **A capa quebra o padrão do feed.** Hoje todas as capas são verde-petróleo,
  com texto centralizado e ambiente interno escurecido. Esta tem foto real de
  uma pessoa, em tons quentes, com o título grande embaixo e alinhado à
  esquerda.
- **O título faz o RH se reconhecer.** Uma pergunta que ele já se fez ("por que
  o plano sobe todo ano?"), e a resposta só vem no slide 2.
- **Quase toda tela tem foto.** Quatro layouts se alternam: foto inteira com
  texto embaixo (1 e 3) ou em cima (6), número grande com foto recortada (2),
  foto sangrando na lateral em fundo claro (4) e faixa de foto embaixo (5).
- **Tipografia de revista:** título em Raleway 800, texto corrido em
  Instrument Serif. O destaque vai em menta no fundo escuro e em verde-escuro
  no fundo claro. Só um trecho por slide.
- **Barra fixa no topo** (fairhealth · @fairhealth.br · 01/08). É ela que faz
  layouts diferentes parecerem uma série.
- **Fonte em todo slide com número.** Dá credibilidade e é exigência para
  publicidade médica.

## Os slides

| # | Layout | Texto |
|---|---|---|
| 1 | Foto inteira, título embaixo | Por que o plano de saúde da sua empresa **sobe todo ano?** |
| 2 | Número + foto recortada, fundo escuro | A maior parte dessa conta vem de doenças que dava para evitar. **70%** dos custos do plano de saúde corporativo vêm de doenças crônicas evitáveis. |
| 3 | Foto inteira, texto embaixo | Cuidar antes deixa menos cadeira vazia. Absenteísmo **27%** menor, em média. |
| 4 | Foto na lateral, fundo claro | Consulta trata o sintoma. Acolhimento descobre o motivo. **+40%** de participação com atendimento presencial. |
| 5 | Número + faixa de foto, fundo verde | Prevenção não é gasto. É conta que fecha. **2,7** de retorno para cada 1 investido. Custos médicos 26% menores. |
| 6 | Foto inteira, texto em cima | Não é campanha de outubro. O resultado no plano aparece em **12 meses**. |
| 7 | Resumo, fundo claro | Os cinco números em lista. É o slide que as pessoas salvam. |
| 8 | CTA, fundo verde | Precisa convencer o financeiro? Mande este post. Na sexta, como a prevenção vira rotina. |

Os slides 1 a 3 seguem o roteiro do cronograma: sinistralidade, absenteísmo e
engajamento (acolhimento).

### Outros títulos possíveis para a capa

- "Plano de saúde mais caro. Gente faltando. De novo." (é a frase do site)
- "Quanto custa não cuidar da saúde do seu time?"

## As fotos

| Slide | Cena | Busca no Unsplash ou Pexels |
|---|---|---|
| 1 | Colaborador exausto na mesa de trabalho, de perto ou visto de cima, luz quente de fim de tarde | `exhausted office worker desk` |
| 2 | Braço com medidor de pressão | `blood pressure cuff arm` |
| 3 | Cadeira vazia na estação de trabalho, casaco pendurado, tela apagada | `empty office chair desk` |
| 4 | Duas pessoas conversando à mesa, só mãos e canecas (cena A4 da sessão de fotos) | `two people talking coffee hands table` |
| 5 | Mãos sobre um relatório com gráfico genérico (cena A5) | `hands report chart desk` |
| 6 | Mão marcando um dia no calendário de mesa (cena D7) | `hand marking calendar` |

- **A capa é o que mais importa.** Precisa ter uma pessoa, emoção real e cor
  quente. Nada de banco de imagem sorrindo para a câmera.
- Nas fotos com texto por cima (1, 3 e 6), o lado do texto precisa ser mais
  escuro ou mais limpo.
- Use só fotos com licença livre para uso comercial, como as do Unsplash e do
  Pexels.
- Nenhum colaborador atendido aparece, nem logo de empresa.
- Para trocar a moldura no `slides.html`, coloque
  `style="background-image:url(fotos/nome.jpg)"` na `div` com classe `img` e
  apague o `aviso`. Depois rode:
  `node instagram/ferramentas/render.mjs instagram/posts/prevencao/slides.html instagram/posts/prevencao/png`
- Para importar no Canva com o texto editável, gere o PDF:
  `node instagram/ferramentas/pdf.mjs instagram/posts/prevencao/slides.html instagram/posts/prevencao/prevencao.pdf`

## Números e fontes

Todos tirados do site (fairjob.com.br/fairhealth):

| Número | Fonte |
|---|---|
| 70% dos custos do plano vêm de doenças crônicas evitáveis | Revista de Saúde Pública da USP |
| −27% de absenteísmo | Chapman, L.S., American Journal of Health Promotion |
| +40% de participação com componente presencial | Journal of Occupational and Environmental Medicine |
| 2,7 de retorno para cada 1 investido | Berry, Mirabito e Baun, Harvard Business Review |
| 12 meses para resultado no plano de saúde | SHRM |
| −26% nos custos médicos | Baicker, Cutler e Song, Health Affairs |

## Confirmar antes de publicar

- **[PENDENTE] Os números do site não batem com os do `referencias.md`.** Lá,
  os oficiais (decisão de 25/09) são −28% de absenteísmo (HBR, 2022) e −22%
  de custos com saúde (SHRM, 2023). Este post usa os do site. Vale decidir qual
  conjunto fica e alinhar o outro.
- **[PENDENTE] A fonte do −26%.** Pelo que conheço, o estudo de Baicker, Cutler
  e Song fala em US$ 3,27 de economia em custos médicos para cada dólar
  investido. O −26% parece vir da meta-análise do Chapman. Confirmar antes de
  publicar, e corrigir no site se for o caso.
- **O 2,7 é em dólar** no estudo original (US$ 2,71 para cada US$ 1). Por isso
  o post diz "2,7 para cada 1", sem moeda. O site usa "R$".
- **O Dr. Ronald aprova o texto** (menção médica, CFM).

## Legenda

```
A resposta quase nunca está no plano. Está no que acontece antes dele.

70% dos custos do plano de saúde corporativo vêm de doenças crônicas evitáveis: hipertensão, diabetes tipo 2, obesidade, burnout. Elas levam anos para se instalar. E aparecem primeiro na sinistralidade, bem antes de você ver o afastamento.

A gente separou o que os estudos de saúde corporativa mostram quando a empresa cuida antes 📊 O absenteísmo cai 27%, em média. A participação sobe 40% quando o atendimento é presencial, perto de quem trabalha. E cada 1 investido volta como 2,7.

Não é campanha de um mês. O resultado no plano costuma aparecer em cerca de 12 meses, quando a prevenção vira rotina. Na sexta, mostramos como isso funciona dentro de uma empresa.

Salve e mande para quem aprova o orçamento de saúde da sua empresa.

Fontes: Revista de Saúde Pública da USP; Chapman, American Journal of Health Promotion; Journal of Occupational and Environmental Medicine; Berry, Mirabito e Baun, Harvard Business Review; SHRM.

#fairhealth #saudecorporativa #medicinapreventiva
```

**Alt text da capa:** Pessoa cansada apoiada na mesa de trabalho, com o texto
"Por que o plano de saúde da sua empresa sobe todo ano?"
