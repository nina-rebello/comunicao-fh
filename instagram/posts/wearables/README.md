# Carrossel: wearables no Escritório do Cuidado · 8 slides

Fase 2 (Produto). Estilo fairedu, mesmo da estreia. O texto de cada slide está
em `slides.html`, as artes em `png/` e a prévia em `previa.png`.

**Status:** a capa ainda está com um espaço reservado para a foto.

## A foto da capa

- **Cena:** braço e pulso de um modelo usando a smartband. Sem rosto.
- **Formato:** vertical 4:5, no mínimo 1080x1350.
- **Espaço para o texto:** o título fica na metade de baixo. Deixar a metade de
  baixo mais limpa ou escura, e o braço na metade de cima.
- **Luz:** natural. Um cenário real ajuda (mesa de atendimento, caneca de café,
  caminhada), para parecer rotina e não anúncio.
- **Evitar:** tatuagens, joias ou crachá que identifiquem a pessoa, e a tela da
  pulseira com dados reais.
- **Autorização de uso de imagem** assinada pelo modelo, mesmo sem rosto.
- **Depois de fotografar:** salvar como `instagram/posts/wearables/foto-capa.jpg`.
  No `slides.html`, trocar a classe `sem-foto` por
  `style="background-image:url(foto-capa.jpg)"`, apagar o aviso e rodar:
  `node instagram/ferramentas/render.mjs instagram/posts/wearables/slides.html instagram/posts/wearables/png`

## Confirmar antes de publicar

- **[PENDENTE]** Quais dados a smartband de vocês registra. O slide 3 cita
  sono, atividade física e frequência cardíaca, que são os mais comuns.
- **[PENDENTE]** Se todos os atendidos usam a pulseira. Na Chemitec, são 46
  smartbands para 48 atendidos. Se não for regra, o slide 3 vira "quem é
  acompanhado pode usar".
- A marca e o modelo da pulseira não aparecem no post, de propósito.

## Legenda

```
E se o cuidado continuasse depois que a consulta acaba?

Uma consulta mostra como a pessoa está naquele momento. Mas sono, estresse e movimento acontecem no resto da semana, longe do consultório.

Por isso, no Escritório do Cuidado, usamos wearables. A smartband acompanha a rotina, e a bioimpedância mostra a composição corporal ao longo do tempo. Na consulta, a conversa deixa de ser "acho que durmo mal" e passa a olhar, junto com a pessoa, como foram as últimas semanas.

Isso não transforma o cuidado em vigilância. Os dados de cada pessoa ficam no atendimento. O RH recebe apenas indicadores do grupo, anonimizados.

Quer entender como isso funcionaria na sua empresa? Comente CUIDADO e enviamos como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #wearables #medicinadoestilodevida #gestaodepessoas
```

**Alt text da capa:** Braço de uma pessoa usando uma smartband, com o texto "O
cuidado não para quando a consulta acaba."
