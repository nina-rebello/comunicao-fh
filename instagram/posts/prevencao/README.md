# Carrossel 28/10: Prevenção também é investimento · 6 slides

Semana 2, bloco 2 (Relevância). Quem monta: Charles. Segue o guia
`instagram/carrossel.md`, na versão curta. O texto de cada slide está em
`slides.html`, as artes em `png/`, a prévia em `previa.png` e o PDF para o
Canva em `prevencao.pdf`.

**Status:** rascunho para aprovação. As fotos ainda são molduras com a
descrição da cena.

## Os três Cs deste post

- **Capa:** "Por que o plano de saúde da sua empresa sobe todo ano?" (10
  palavras). É a dúvida do RH, e o miolo responde.
- **CTA, no slide 3:** "Vai levar isso ao financeiro? Salve este post. Os
  números e as fontes estão todos aqui." Vem depois da primeira prova e diz por
  que salvar.
- **Convite, no slide 6:** "Comente CUIDADO e enviamos na DM como funciona o
  diagnóstico gratuito."

## Os slides

Um argumento por slide: os três do roteiro (sinistralidade, absenteísmo e
engajamento) e o retorno, que é o "investimento" do título.

| # | Função | Layout | Texto |
|---|---|---|---|
| 1 | Capa | Foto colorida inteira, título embaixo | Por que o plano de saúde da sua empresa **sobe todo ano?** |
| 2 | Sinistralidade | Número grande + foto recortada, fundo escuro | 70% dos custos do plano vêm de doenças crônicas evitáveis. *O plano sobe pelo que acontece antes dele.* |
| 3 | Absenteísmo + CTA | Foto inteira, texto embaixo | Cuidar antes deixa menos cadeira vazia: absenteísmo 27% menor. Faixa com o CTA de salvar. |
| 4 | Engajamento | Foto na lateral, fundo claro | Consulta trata o sintoma, acolhimento descobre o motivo. +40% de participação. *Perto, as pessoas vão. E voltam.* |
| 5 | Retorno | Número + faixa de foto, fundo água | Prevenção não é gasto, é conta que fecha: 2,7 para cada 1, resultado em 12 meses. *Não cuidar também custa.* |
| 6 | Convite | Fundo verde | Quanto a sua empresa gasta com o que dava para evitar? Comente CUIDADO. |

Em itálico, a frase de fecho de cada slide (Instrument Serif, na cor de
destaque).

### Outros títulos possíveis para a capa

- "Plano de saúde mais caro. Gente faltando. De novo." (é a frase do site)
- "Quanto custa não cuidar da saúde do seu time?"

## As fotos

A capa é colorida. No miolo, as fotos ficam em preto e branco com retícula: o
`slides.html` já aplica esse efeito sozinho em qualquer foto que entrar.

| Slide | Cena | Busca no Unsplash ou Pexels |
|---|---|---|
| 1 | Colaborador exausto na mesa de trabalho, de perto ou visto de cima, luz quente de fim de tarde | `exhausted office worker desk` |
| 2 | Braço com medidor de pressão | `blood pressure cuff arm` |
| 3 | Cadeira vazia na estação de trabalho, casaco pendurado, tela apagada | `empty office chair desk` |
| 4 | Duas pessoas conversando à mesa, só mãos e canecas (cena A4 da sessão de fotos) | `two people talking coffee hands table` |
| 5 | Mãos sobre um relatório com gráfico genérico (cena A5) | `hands report chart desk` |

- **A capa é o que mais importa.** Precisa ter uma pessoa, emoção real e cor
  quente. Nada de banco de imagem sorrindo para a câmera.
- Nas fotos com texto por cima (1 e 3), o lado do texto precisa ser mais escuro
  ou mais limpo.
- Use só fotos com licença livre para uso comercial, como as do Unsplash e do
  Pexels.
- Nenhum colaborador atendido aparece, nem logo de empresa.
- Para trocar a moldura no `slides.html`, coloque
  `style="background-image:url(fotos/nome.jpg)"` na `div` com classe `img` e
  apague o `aviso`. Depois rode:
  `node instagram/ferramentas/render.mjs instagram/posts/prevencao/slides.html instagram/posts/prevencao/png`
- Para importar no Canva com o texto editável:
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

## Confirmar antes de publicar

- **[PENDENTE] Os números do site não batem com os do `referencias.md`.** Lá,
  os oficiais (decisão de 25/09) são −28% de absenteísmo (HBR, 2022) e −22%
  de custos com saúde (SHRM, 2023). Este post usa os do site. Vale decidir qual
  conjunto fica e alinhar o outro.
- **O −26% de custos médicos saiu do post.** O site atribui o número a Baicker,
  Cutler e Song, mas esse estudo fala em US$ 3,27 de economia por dólar
  investido. O −26% parece vir da meta-análise do Chapman. Vale corrigir no
  site.
- **O 2,7 é em dólar** no estudo original (US$ 2,71 para cada US$ 1). Por isso
  o post diz "2,7 para cada 1", sem moeda. O site usa "R$".
- **[PENDENTE] Quem responde as DMs do "CUIDADO".** O guia pede um convite que
  o perfil consiga cumprir. Alguém precisa mandar como funciona o diagnóstico
  gratuito no mesmo dia.
- **O Dr. Ronald aprova o texto** (menção médica, CFM).

## Legenda

```
A resposta quase nunca está no plano. Está no que acontece antes dele.

70% dos custos do plano de saúde corporativo vêm de doenças crônicas evitáveis: hipertensão, diabetes tipo 2, obesidade, burnout. Elas levam anos para se instalar. E aparecem primeiro na sinistralidade, bem antes de você ver o afastamento.

A gente separou o que os estudos de saúde corporativa mostram quando a empresa cuida antes 📊 O absenteísmo cai 27%, em média. A participação sobe 40% quando o atendimento é presencial, perto de quem trabalha. E cada 1 investido volta como 2,7.

Não é campanha de um mês. O resultado no plano costuma aparecer em cerca de 12 meses, quando a prevenção vira rotina. Na sexta, mostramos como isso funciona dentro de uma empresa.

Quer saber por onde começar na sua empresa? Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

Fontes: Revista de Saúde Pública da USP; Chapman, American Journal of Health Promotion; Journal of Occupational and Environmental Medicine; Berry, Mirabito e Baun, Harvard Business Review; SHRM.

#fairhealth #saudecorporativa #medicinapreventiva
```

**Alt text da capa:** Pessoa cansada apoiada na mesa de trabalho, com o texto
"Por que o plano de saúde da sua empresa sobe todo ano?"
