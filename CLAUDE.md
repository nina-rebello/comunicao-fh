# Comunicação fairhealth

Conteúdo do Instagram da fairhealth (@fairhealth.br). Antes de criar ou revisar
um post, leia:

- `instagram/plan.md`: o cronograma atual (19/10 a 13/11). A fonte é
  `marketing/Programacao_Instagram_19-10_a_13-11.pdf`.
- `instagram/carrossel.md`: o método (três Cs) e o visual dos carrosséis. Onde
  discordar da skill `/ig-carousel`, vale o guia.
- `instagram/voice.md`: a voz, as palavras proibidas, o time e as regras do CFM.
- `instagram/referencias.md`: os números oficiais e os materiais de apoio.
- `instagram/estrategia.md`: a estratégia de fundo. As fases ainda não foram
  alinhadas ao cronograma atual.

A planilha `marketing/Cronograma_Conteudo_FairHealth_90dias.xlsx` está
desatualizada. Não use as datas dela.

Cada post fica em `instagram/posts/<nome>/`, com `slides.html`, `png/`,
`previa.png` e um `README.md` com a legenda e as pendências. Para gerar as
artes e o PDF para o Canva:

```
node instagram/ferramentas/render.mjs instagram/posts/<nome>/slides.html instagram/posts/<nome>/png
node instagram/ferramentas/pdf.mjs instagram/posts/<nome>/slides.html instagram/posts/<nome>/<nome>.pdf
```

## Levar um post para o Canva

O Canva importa HTML por URL pública. O repositório é público, então:

1. Gere um `canva.html` autocontido a partir do `slides.html` com
   `node instagram/ferramentas/canva.mjs <slides.html> <canva.html>`. Ele embute
   CSS, fontes e logo e liga o bloco `<style media="canva">` do post, se houver.
   Por trás, o que o Canva precisa: CSS, fontes e
   logo embutidos em base64 (o GitHub serve CSS e fontes como texto puro, e o
   Canva ignora). Também é preciso marcar cada `<section class="slide">` com
   `data-document-role="page"` e trocar as molduras de foto por formas lisas,
   sem filtro nem retícula.
2. Faça commit e push, e importe pelo endereço raw com o hash do commit (não
   com o nome do branch, que fica em cache):
   `https://raw.githubusercontent.com/nina-rebello/comunicao-fh/<commit>/instagram/posts/<nome>/canva.html`
3. Confira as miniaturas no Canva. O que o Canva não respeita na conversão:
   `display:flex` com `gap` (use posição absoluta), `padding` dentro de texto
   com fundo (use `&nbsp;`), `box-decoration-break` (uma pílula por linha) e
   `border-left` em texto (use uma `div` separada como barra).
   Também (post de 30/10): duas fontes na mesma caixa de texto (o trecho em
   serif vira outra caixa), `inline-block` lado a lado (use posição absoluta),
   SVG com posição absoluta (ponha o SVG dentro de um `div` posicionado),
   `line-height` para centrar texto numa forma (calcule o `top`), texto em
   degradê e elementos girados. Quebre as linhas dos títulos com `<br>` e deixe
   folga na largura: no Canva o texto sai um pouco mais largo.
