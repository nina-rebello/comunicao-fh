# 04/12 · Carrossel "98% do time aceitou ser cuidado" (case de adesão)

Cronograma: `C01` em `marketing/ferramentas/conteudo_posts_dezembro.py`. Dados: Chemitec, 1º semestre de 2026 (`voice.md`,
"Provas que podemos usar"), sempre agregados.

- `slides.html` → `png/ca-01` a `ca-08`, `previa.png`. 8 slides, um número por slide, sempre com "1º semestre de 2026".
- **Sem o nome do cliente.** A decisão de 30/10 tirou dados de clientes dos posts e os sócios ainda não confirmaram o case.
  Esta versão diz "uma indústria que atendemos". Se os sócios liberarem o nome (com autorização escrita do cliente), troca no
  slide 2 e na legenda.
- Capa: foto de banco `instagram/marca/fotos-banco/industria2.jpg` (Licença Unsplash), recortada nas mãos com luvas, sem rosto,
  com "Foto ilustrativa". `gerar.py` faz o recorte (`fotos/capa.jpg`) e o degradê no verde da marca (`fotos/degrade.png`), o
  mesmo do carrossel de 25/11. Outras opções testadas: `oculos.jpg` (rosto), `solda.jpg` (azul e escuro), `industria1.jpg`.
- Visual: o sistema aprovado em 23/11 (verde da marca, papel, Tiffany no 4 e no fecho).
- `canva-src.html` e `canva.html`: versão achatada para o Canva. Ainda não importada (só depois da aprovação).
- `legenda.txt`: ig-caption (`caption.py` com "programa de saúde, adesão, saúde corporativa": 3/3) e ig-human (`detect.py`
  56,6, REVIEW pelo VOICE, como nos outros posts).

## Slides

1. 98% / do time aceitou ser cuidado. / O que essa indústria fez diferente?
2. O case / Uma indústria, no primeiro semestre de 2026. / O Escritório do Cuidado dentro da empresa, perto de quem trabalha. /
   Os números a seguir são do grupo, sem identificar ninguém.
3. Adesão / 98% / de adesão ao Escritório do Cuidado. / 48 colaboradores atendidos · 1º semestre de 2026
4. Volume / 161 / atendimentos no semestre.
5. Continuidade / 81,3% / voltaram para dois ou mais atendimentos.
6. Entre as consultas / 46 / smartwatches em uso, acompanhando a rotina. / Nas consultas, as medições usam bioimpedância. O RH
   recebe só indicadores do grupo, anonimizados.
7. O que estava por trás / Três escolhas do Escritório do Cuidado: o cuidado perto de quem trabalha, dentro da empresa; a
   primeira consulta começa pela pergunta "o que importa para você?"; um plano pela Medicina do Estilo de Vida que cabe no turno.
8. Planejando 2027? / Comente CUIDADO e enviamos na DM como funciona o Escritório do Cuidado. / Nota dos dados e da foto.

Texto alternativo da capa: "Mãos com luvas de proteção trabalhando num painel elétrico, com '98% do time aceitou ser cuidado'
em destaque (foto ilustrativa)."

## Pendências

- Sócios: o case sai? Com ou sem o nome? (decisão de 30/10).
- Conferir como foi a implantação (slide 2 e slide 7 só descrevem o método do site; nada específico da implantação).
- O `voice.md` fala em "46 smartbands"; nos posts o nome é "smartwatch" (regra de 12/11).
