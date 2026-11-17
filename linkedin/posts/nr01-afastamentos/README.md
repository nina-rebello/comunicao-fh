# LinkedIn 18/11: Recorde de afastamentos por saúde mental e a NR-01 · documento em PDF, 6 slides

Versão LinkedIn do carrossel do Instagram de 18/11 (`instagram/posts/nr01-afastamentos/`). Mesmos 6 slides e mesmo
texto, em **1080 x 1080** (quadrado, como o post #1 da página).

- **Artes:** `png/n-01.png` … `n-06.png`. Prévia em `previa.png`.
- **PDF para subir como documento:** `nr01-afastamentos-linkedin.pdf` (6 páginas quadradas). Título do documento
  sugerido: "546,2 mil afastamentos por saúde mental e a NR-01".
- **Legenda:** `legenda.txt`. **Primeiro comentário** (com o link): `comentario.txt`.
- **Canva:** `canva.html` (leve, cerca de 2,3 MB, de `canva-leve.py`). Importar pelo endereço raw com o hash do commit.
- **Para regerar:** `python3 linkedin/posts/nr01-afastamentos/gerar.py`, depois
  `node instagram/ferramentas/render.mjs linkedin/posts/nr01-afastamentos/slides.html linkedin/posts/nr01-afastamentos/png`,
  `ALTURA=1080 node instagram/ferramentas/pdf.mjs linkedin/posts/nr01-afastamentos/slides.html linkedin/posts/nr01-afastamentos/nr01-afastamentos-linkedin.pdf`
  e `python3 linkedin/posts/nr01-afastamentos/canva-leve.py`.

## O que muda em relação ao Instagram

- **Quadro:** 1080 x 1080 (a arte 4:5 foi refeita, não cortada). A foto do slide 5 é uma faixa de 1080 x 300 (do
  caderno ao smartwatch); a lista do MTE ficou mais compacta; o gráfico, mais baixo.
- **Marca:** "fairhealth" no topo e no selo, no lugar do @ do Instagram. "Deslize para o lado" no lugar de "Arraste".
- **Convite (slide 6):** "pelo link abaixo", porque no LinkedIn não existe link da bio e o link vai no primeiro
  comentário (regra do `linkedin/README.md`). O restante do texto é o mesmo.
- **Legenda:** a primeira linha se sustenta sozinha, sem link no texto, uma chamada só, 3 hashtags
  (`linkedin/README.md`) e a mesma base de dados e fontes do post do Instagram.
- **Slide 5:** a foto de escuta tem **origem e licença a confirmar** (não é do banco da marca), como no Instagram.

- **Sem CVV 188 e com o último slide preenchido** ("O que a empresa recebe"), como no Instagram (17/11).

## Pendências

- [ ] Aprovação da Nina.
- [ ] Link do primeiro comentário (www.fairhealth.com.br a confirmar, com UTM do LinkedIn).
- [ ] Dr. Ronald: revisar o texto de saúde mental (CFM) e a leitura da NR-01, como no Instagram.
- [ ] Data e perfil: o calendário do LinkedIn (`linkedin/README.md`) não tem este post; a quinta 19/11 é "Prevenção
      também é investimento". Decidir se este sai na quinta 19/11, no lugar ou junto. Publicação pelo perfil da FairJob
      (`voice.md`).

## v7 (17/11): mesmas mudanças do Instagram

Slide 5 com a frase "A fairdata mede o risco. A fairhealth complementa com o cuidado." em uma linha, sob os cartões, slide 6 com
"Medir e cuidar andam juntos." e "pelo link abaixo", legenda e primeiro comentário atualizados.
