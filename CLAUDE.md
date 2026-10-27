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
