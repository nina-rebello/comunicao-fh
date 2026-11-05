// Deck de aprovação dos posts de 06 a 13/11 (pptxgenjs). Uso: node instagram/aprovacao/gerar-deck.js
const pptxgen = require('pptxgenjs');
const fs = require('fs');
const path = require('path');
const { applyTheme } = require(process.env.PPTX_SKILL + '/scripts/apply_theme.js');

const R = (p) => path.resolve(__dirname, '..', p);
const ler = (p) => fs.readFileSync(R(p), 'utf8').trim();
const OUT = path.resolve(__dirname, 'posts-06-a-13-11.pptx');

const THEME = {
  name: 'fairhealth',
  headFontFace: 'Cambria',
  bodyFontFace: 'Calibri',
  colors: {
    dk1: '141B1B', lt1: 'FFFFFF', dk2: '2F6B64', lt2: 'F6F8F7',
    accent1: '9FC5BD', accent2: '2F6B64', accent3: 'BFE0D9', accent4: '5E6B69',
    accent5: 'E4EEEB', accent6: '141B1B', hlink: '2F6B64', folHlink: '2F6B64',
  },
};

const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = 'Posts para aprovação · 06, 11 e 13/11';
pres.author = 'Comunicação fairhealth';
const C = pres.SchemeColor;

pres.defineSlideMaster({
  title: 'CAPA',
  background: { color: '2F6B64' },
  objects: [
    { image: { path: R('marca/logo-circulo.png'), x: 0.7, y: 6.2, w: 0.7, h: 0.69 } },
    { text: { text: '@fairhealth.br', options: { x: 1.55, y: 6.3, w: 4, h: 0.5, fontSize: 16, bold: true, color: C.background1, margin: 0 } } },

    { placeholder: { options: { name: 'title', type: 'title', x: 0.7, y: 2.1, w: 11.5, h: 1.6, fontSize: 48, bold: true, color: C.background1, fontFace: 'Cambria', valign: 'bottom', align: 'left', margin: 0 }, text: 'Texto' } },
    { placeholder: { options: { name: 'body', type: 'body', x: 0.7, y: 3.9, w: 11.5, h: 1.2, fontSize: 20, color: C.accent3, valign: 'top', align: 'left', margin: 0 }, text: 'Texto' } },
  ],
});
pres.defineSlideMaster({
  title: 'CONTEUDO',
  background: { color: 'FFFFFF' },
  slideNumber: { x: 12.4, y: 7.0, w: 0.5, h: 0.3, fontSize: 10, color: '5E6B69', align: 'right' },
  objects: [
    { text: { text: 'fairhealth · posts para aprovação · 06 a 13/11', options: { x: 0.6, y: 7.0, w: 8, h: 0.3, fontSize: 10, color: C.accent4, margin: 0 } } },

    { placeholder: { options: { name: 'kicker', type: 'body', x: 0.6, y: 0.35, w: 12, h: 0.35, fontSize: 12, bold: true, charSpacing: 2, color: C.accent2, align: 'left', margin: 0 }, text: 'Texto' } },
    { placeholder: { options: { name: 'title', type: 'title', x: 0.6, y: 0.7, w: 12, h: 0.8, fontSize: 30, bold: true, color: C.text1, fontFace: 'Cambria', valign: 'top', align: 'left', margin: 0 }, text: 'Texto' } },
  ],
});

// helper: slide de post com imagem e legenda ao lado
function slidePost({ secao, kicker, titulo, img, iw, ih, legenda, notas, rodape }) {
  const sl = pres.addSlide({ masterName: 'CONTEUDO', sectionTitle: secao });
  sl.addText(kicker, { placeholder: 'kicker' });
  sl.addText(titulo, { placeholder: 'title' });
  const maxH = 5.2, y0 = 1.65;
  let h = maxH, w = h * iw / ih;
  if (w > 7.1) { w = 7.1; h = w * ih / iw; }
  sl.addImage({ path: R(img), x: 0.6, y: y0, w, h, altText: titulo, objectName: 'previa' });
  const x = 0.6 + w + 0.4, cw = 12.73 - x;
  sl.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: y0, w: cw, h: maxH, rectRadius: 0.1, fill: { color: 'F6F8F7' }, line: { color: 'E4EEEB' }, objectName: 'caixa-legenda' });
  sl.addText('LEGENDA', { x: x + 0.25, y: y0 + 0.15, w: cw - 0.5, h: 0.3, fontSize: 11, bold: true, charSpacing: 2, color: C.accent2, margin: 0, isTextBox: true });
  sl.addText(legenda, { x: x + 0.25, y: y0 + 0.5, w: cw - 0.5, h: maxH - 0.65, fontSize: rodape || 10.5, color: C.text1, valign: 'top', margin: 0, paraSpaceAfter: 4, fit: 'shrink', isTextBox: true, objectName: 'legenda' });
  if (notas) sl.addNotes(notas);
  return sl;
}

// Um slide por post (pedido da Nina, 04/11): prévia à esquerda, legenda à direita.
pres.addSection({ title: '06/11' });
slidePost({
  secao: '06/11', kicker: 'SEXTA, 06/11 · FOTO ÚNICA · ARTE E LEGENDA PRONTAS',
  titulo: 'Uma história de cuidado que começou em 2009',
  img: 'posts/historia-2009/foto-unica.png', iw: 1080, ih: 1350,
  legenda: ler('posts/historia-2009/legenda-foto.txt'), rodape: 11,
});
pres.addSection({ title: '11/11' });
slidePost({
  secao: '11/11', kicker: 'QUARTA, 11/11 · CARROSSEL · ARTE E LEGENDA PRONTAS · FALTA REVISÃO MÉDICA',
  titulo: 'Estilo de vida também é tratamento sério',
  img: 'posts/estilo-de-vida/previa.png', iw: 1320, ih: 1092,
  legenda: ler('posts/estilo-de-vida/legenda.txt'), rodape: 10,
  notas: 'Fontes conferidas nos originais: IDF Diabetes Atlas 11ª ed. (2025); Diabetes Prevention Program, NEJM 2002; DPP Outcomes Study, Lancet Diabetes & Endocrinology 2015.',
});
pres.addSection({ title: '13/11' });
let s13 = pres.addSlide({ masterName: 'CONTEUDO', sectionTitle: '13/11' });
s13.addText('SEXTA, 13/11 · CARROSSEL · TEXTO PARA APROVAR · DESIGN DEPOIS', { placeholder: 'kicker' });
s13.addText('Como levar a fairhealth para a sua empresa?', { placeholder: 'title' });
const slides13 = [
  ['Capa', 'Como levar a fairhealth para a sua empresa? · 3 passos, e o primeiro é uma conversa'],
  ['Antes de começar', 'O que o Escritório do Cuidado é (atendimento dentro da empresa, cuidado contínuo, relatórios anonimizados) e o que não é (substituto do plano ou do SST, campanha, solução só digital)'],
  ['Passo 01', 'Diagnóstico gratuito: uma reunião para entender as pessoas e a rotina. Sem custo e sem compromisso'],
  ['Passo 02', 'Uma proposta do tamanho da sua empresa, com as frentes que fazem sentido'],
  ['Passo 03', 'Implementação com o RH junto: onboarding, primeiros atendimentos e 12 meses de acompanhamento'],
  ['Convite', 'O primeiro passo é uma conversa. Comente CUIDADO'],
];
s13.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 1.65, w: 6.0, h: 5.2, rectRadius: 0.1, fill: { color: 'E4EEEB' }, line: { color: 'E4EEEB' }, objectName: 'caixa-slides' });
s13.addText('OS 6 SLIDES', { x: 0.85, y: 1.8, w: 5.5, h: 0.3, fontSize: 11, bold: true, charSpacing: 2, color: C.accent2, margin: 0, isTextBox: true });
s13.addText(slides13.map(([t, d], i) => [
  { text: `${i + 1}. ${t}  `, options: { bold: true, color: C.accent2 } },
  { text: d, options: { breakLine: i < slides13.length - 1 } },
]).flat(), { x: 0.85, y: 2.2, w: 5.5, h: 4.5, fontSize: 13, color: C.text1, valign: 'top', margin: 0, paraSpaceAfter: 9, fit: 'shrink', isTextBox: true, objectName: 'texto-slides' });
s13.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 6.9, y: 1.65, w: 5.83, h: 5.2, rectRadius: 0.1, fill: { color: 'F6F8F7' }, line: { color: 'E4EEEB' }, objectName: 'caixa-legenda' });
s13.addText('LEGENDA', { x: 7.15, y: 1.8, w: 5.3, h: 0.3, fontSize: 11, bold: true, charSpacing: 2, color: C.accent2, margin: 0, isTextBox: true });
s13.addText(ler('posts/levar-para-empresa/legenda.txt'), { x: 7.15, y: 2.2, w: 5.3, h: 4.5, fontSize: 11, color: C.text1, valign: 'top', margin: 0, paraSpaceAfter: 4, fit: 'shrink', isTextBox: true, objectName: 'legenda' });
s13.addNotes('Validar com o comercial: diagnóstico gratuito e sem compromisso; como funciona; prazos médios; se a empresa precisa ceder uma sala; página do diagnóstico e resposta automática da palavra CUIDADO até 13/11.');

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log('ok', OUT);
})();
