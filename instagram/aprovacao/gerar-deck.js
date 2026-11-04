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
pres.title = 'Posts para aprovação · 06 a 13/11';
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

// ---------- 1. capa ----------
let s = pres.addSlide({ masterName: 'CAPA' });
s.addText('Posts para aprovação', { placeholder: 'title' });
s.addText('Instagram · de 06 a 13 de novembro · prévia das artes e legendas', { placeholder: 'body' });

// ---------- 2. visão geral ----------
pres.addSection({ title: 'Visão geral' });
s = pres.addSlide({ masterName: 'CONTEUDO', sectionTitle: 'Visão geral' });
s.addText('VISÃO GERAL', { placeholder: 'kicker' });
s.addText('Quatro posts até 13/11, três prontos para revisar', { placeholder: 'title' });
const linhas = [
  ['Sex 06/11', 'Foto única', 'Uma história de cuidado que começou em 2009', 'Arte e legenda prontas', true],
  ['Seg 09/11', 'Reel', 'Cuidado na prática: resultados reais, com o Dr. Ronald', 'Ainda em elaboração (não está neste deck)', false],
  ['Qua 11/11', 'Carrossel · 6 slides', 'Estilo de vida também é tratamento sério', 'Arte e legenda prontas · falta revisão da equipe médica', true],
  ['Sex 13/11', 'Carrossel · 6 slides', 'Como levar a fairhealth para a sua empresa?', 'Texto e legenda para aprovar · design depois', true],
];
linhas.forEach((l, i) => {
  const y = 1.8 + i * 1.18;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y, w: 12.1, h: 1.0, rectRadius: 0.12, fill: { color: l[4] ? 'E4EEEB' : 'F2F2F2' }, line: { color: l[4] ? 'E4EEEB' : 'F2F2F2' }, objectName: `linha-${i + 1}` });
  s.addText(l[0], { x: 0.9, y, w: 1.6, h: 1.0, fontSize: 18, bold: true, color: C.accent2, valign: 'middle', margin: 0, isTextBox: true });
  s.addText(l[1], { x: 2.6, y, w: 2.3, h: 1.0, fontSize: 14, color: C.accent4, valign: 'middle', margin: 0, isTextBox: true });
  s.addText(l[2], { x: 5.0, y, w: 4.4, h: 1.0, fontSize: 16, bold: true, color: C.text1, valign: 'middle', margin: 0, isTextBox: true });
  s.addText(l[3], { x: 9.5, y, w: 3.0, h: 1.0, fontSize: 13, color: l[4] ? C.accent2 : C.accent4, italic: !l[4], valign: 'middle', margin: 0, isTextBox: true });
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

// ---------- 3. 06/11 ----------
pres.addSection({ title: '06/11 · Foto única' });
slidePost({
  secao: '06/11 · Foto única', kicker: 'SEXTA, 06/11 · FOTO ÚNICA',
  titulo: 'Uma história de cuidado que começou em 2009',
  img: 'posts/historia-2009/foto-unica.png', iw: 1080, ih: 1350,
  legenda: ler('posts/historia-2009/legenda-foto.txt'), rodape: 11,
  notas: 'Foto: poltronas do Escritório do Cuidado (enviada pela Nina). Escritório do Paciente aparece só como parte da história. O que está no Escritório do Cuidado é sempre "atendimento".',
});

// ---------- 4-6. 11/11 ----------
pres.addSection({ title: '11/11 · Carrossel' });
slidePost({
  secao: '11/11 · Carrossel', kicker: 'QUARTA, 11/11 · CARROSSEL · SEMANA DO DIA MUNDIAL DO DIABETES',
  titulo: 'Estilo de vida também é tratamento sério',
  img: 'posts/estilo-de-vida/previa.png', iw: 1320, ih: 1092,
  legenda: ler('posts/estilo-de-vida/legenda.txt'), rodape: 10,
  notas: 'Fontes conferidas nos originais: IDF Diabetes Atlas 11ª ed. (2025); Diabetes Prevention Program, NEJM 2002; DPP Outcomes Study, Lancet Diabetes & Endocrinology 2015. Precisa da revisão da equipe médica (CFM) antes de publicar.',
});
for (const [a, b] of [[1, 3], [4, 6]]) {
  const sl = pres.addSlide({ masterName: 'CONTEUDO', sectionTitle: '11/11 · Carrossel' });
  sl.addText(`QUARTA, 11/11 · SLIDES ${a} A ${b} EM TAMANHO MAIOR`, { placeholder: 'kicker' });
  sl.addText('Estilo de vida também é tratamento sério', { placeholder: 'title' });
  for (let k = a; k <= b; k++) {
    const i = k - a, h = 5.0, w = h * 1080 / 1350, gap = 0.35, x0 = (13.33 - (3 * w + 2 * gap)) / 2, x = x0 + i * (w + gap);
    sl.addImage({ path: R(`posts/estilo-de-vida/png/e-0${k}.png`), x, y: 1.65, w, h, altText: `Slide ${k} do carrossel de 11/11`, objectName: `slide-${k}` });
  }
}

// ---------- 7-8. 13/11 ----------
pres.addSection({ title: '13/11 · Carrossel' });
s = pres.addSlide({ masterName: 'CONTEUDO', sectionTitle: '13/11 · Carrossel' });
s.addText('SEXTA, 13/11 · CARROSSEL · TEXTO PARA APROVAR (DESIGN DEPOIS)', { placeholder: 'kicker' });
s.addText('Como levar a fairhealth para a sua empresa?', { placeholder: 'title' });
const cards = [
  ['1 · Capa', 'Como levar a fairhealth para a sua empresa?', 'Pílula: 3 passos, e o primeiro é uma conversa →'],
  ['2 · Antes de começar', 'O que o Escritório do Cuidado é, e o que não é', 'É: atendimento médico, psicológico e social dentro da empresa, presencial ou remoto; cuidado contínuo com MEV; relatórios anonimizados. Não é: substituto do plano de saúde ou do SST; campanha de um mês; solução só digital.'],
  ['3 · Passo 01', 'Diagnóstico gratuito', 'Uma reunião para entender as pessoas, a rotina de trabalho e onde o cuidado ainda não chega. Sem custo e sem compromisso. CTA: mande este post para quem decide.'],
  ['4 · Passo 02', 'Uma proposta do tamanho da sua empresa', 'Montada a partir do diagnóstico: quais frentes fazem sentido (Escritório do Cuidado, Programa de MEV, plataforma e wearables).'],
  ['5 · Passo 03', 'A implementação, com o RH junto', 'Onboarding e primeiros atendimentos. Depois, 12 meses de plantões de médicos e psicólogos, workshops e relatórios anonimizados.'],
  ['6 · Convite', 'O primeiro passo é uma conversa', 'Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito. Na segunda: Novembro Azul.'],
];
cards.forEach((c, i) => {
  const col = i % 3, row = Math.floor(i / 3), w = 3.9, h = 2.45, x = 0.6 + col * (w + 0.2), y = 1.7 + row * (h + 0.2);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.1, fill: { color: i % 2 ? 'F6F8F7' : 'E4EEEB' }, line: { color: 'E4EEEB' }, objectName: `card-${i + 1}` });
  s.addText(c[0].toUpperCase(), { x: x + 0.25, y: y + 0.18, w: w - 0.5, h: 0.3, fontSize: 11, bold: true, charSpacing: 2, color: C.accent2, margin: 0, isTextBox: true });
  s.addText(c[1], { x: x + 0.25, y: y + 0.5, w: w - 0.5, h: 0.65, fontSize: 16, bold: true, fontFace: 'Cambria', color: C.text1, valign: 'top', margin: 0, isTextBox: true });
  s.addText(c[2], { x: x + 0.25, y: y + 1.15, w: w - 0.5, h: h - 1.3, fontSize: 11.5, color: C.text1, valign: 'top', margin: 0, fit: 'shrink', isTextBox: true });
});
s = pres.addSlide({ masterName: 'CONTEUDO', sectionTitle: '13/11 · Carrossel' });
s.addText('SEXTA, 13/11 · LEGENDA E PONTOS PARA VALIDAR', { placeholder: 'kicker' });
s.addText('Como levar a fairhealth para a sua empresa?', { placeholder: 'title' });
s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.6, y: 1.65, w: 6.9, h: 5.15, rectRadius: 0.1, fill: { color: 'F6F8F7' }, line: { color: 'E4EEEB' }, objectName: 'caixa-legenda' });
s.addText('LEGENDA (RASCUNHO)', { x: 0.85, y: 1.8, w: 6.4, h: 0.3, fontSize: 11, bold: true, charSpacing: 2, color: C.accent2, margin: 0, isTextBox: true });
s.addText(ler('posts/levar-para-empresa/legenda.txt'), { x: 0.85, y: 2.15, w: 6.4, h: 4.5, fontSize: 12, color: C.text1, valign: 'top', margin: 0, paraSpaceAfter: 5, fit: 'shrink', isTextBox: true });
s.addText('Para validar com o comercial', { x: 7.9, y: 1.7, w: 4.8, h: 0.5, fontSize: 18, bold: true, fontFace: 'Cambria', color: C.text1, margin: 0, isTextBox: true });
const val = [
  'O diagnóstico é gratuito e sem compromisso de contratação?',
  'Como ele funciona: duração, quem participa, presencial ou on-line',
  'Prazos médios: diagnóstico → proposta → primeiro atendimento',
  'A empresa precisa ceder uma sala?',
  'Página do diagnóstico no ar e resposta automática da palavra CUIDADO até 13/11',
];
s.addText(val.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < val.length - 1 } })), { x: 7.9, y: 2.3, w: 4.8, h: 4.3, fontSize: 14, color: C.text1, valign: 'top', margin: 0, paraSpaceAfter: 10, isTextBox: true });

// ---------- 9. próximos passos ----------
pres.addSection({ title: 'Próximos passos' });
s = pres.addSlide({ masterName: 'CAPA', sectionTitle: 'Próximos passos' });
s.addText('O que precisamos do time', { placeholder: 'title' });
s.addText([
  { text: 'Aprovar 06/11 (arte e legenda) até quinta, 05/11', options: { bullet: true, breakLine: true } },
  { text: 'Revisão médica do carrossel de 11/11 (CFM) até segunda, 09/11', options: { bullet: true, breakLine: true } },
  { text: 'Validar o processo comercial do post de 13/11 até segunda, 09/11', options: { bullet: true } },
], { placeholder: 'body' });

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log('ok', OUT);
})();
