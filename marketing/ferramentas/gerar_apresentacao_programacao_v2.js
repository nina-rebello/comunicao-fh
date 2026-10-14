// v2 (14/10): versão fina e minimalista, em 5 slides (pedido da Nina). A v1 (22 slides) fica em
// gerar_apresentacao_programacao.js e Programacao_Instagram_19-10_a_13-11.pptx.
// Slide 1: capa com o mês inteiro (4 semanas × 3 posts). Slides 2 a 5: um bloco por slide, com os posts resumidos.
// As validações e as ligações entre os posts vão nas notas do apresentador.
//
// Uso: NODE_PATH=<pasta>/node_modules APPLY_THEME=<apply_theme.js> node gerar_apresentacao_programacao_v2.js saida.pptx
// Fonte: Raleway (da marca), que precisa estar instalada para abrir como planejado.
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const sharp = require("sharp");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const { FiFilm, FiLayers, FiImage } = require("react-icons/fi");

const SAIDA = process.argv[2] || "Programacao_Instagram_v2.pptx";
const RAIZ = path.resolve(__dirname, "..", "..");
const HEX = { tif: "96C5BD", verde: "1F3A36", creme: "F0F0E9", tclaro: "BFE0D9", vlogo: "2F6B64", branco: "FFFFFF" };
const THEME = {
  name: "fairhealth", headFontFace: "Raleway", bodyFontFace: "Raleway",
  colors: { dk1: HEX.verde, lt1: HEX.branco, dk2: HEX.vlogo, lt2: HEX.creme, accent1: HEX.tif, accent2: HEX.tclaro,
            accent3: "0D1816", accent4: "5FA89A", accent5: HEX.verde, accent6: HEX.vlogo, hlink: HEX.vlogo, folHlink: HEX.verde },
};

const FMT = { reel: "Reel", carrossel: "Carrossel", foto: "Foto única" };
const BLOCOS = [
  { n: "01", nome: "Reconhecimento", pergunta: "Quem somos e por que existimos?",
    intuito: "Apresentar a marca e criar vínculo com a origem.",
    extra: "Já publicados: \"O que é a fairhealth?\" e \"Conheça o Escritório do Cuidado\". O post do time segue segurado.",
    validar: "Reels do Dr. Ronald: autorização de uso de imagem (exceção à decisão de não ter o time em cena)." },
  { n: "02", nome: "Relevância", pergunta: "Por que as empresas precisam olhar para isso?",
    intuito: "Fazer o RH se reconhecer no problema: o cuidado costuma chegar tarde.",
    validar: "26/10: conferir o número de licenças por saúde mental de 2024 no painel do Ministério da Previdência. 28/10: o que os estudos da HBR e da SHRM mediram." },
  { n: "03", nome: "Compreensão", pergunta: "Como a fairhealth transforma isso em cuidado real?",
    intuito: "Mostrar o cuidado na prática, pela experiência de quem é atendido.",
    validar: "03/11: manter a Clara (personagem fictícia, sinalizada como história ilustrativa) ou contar sem personagem." },
  { n: "04", nome: "Confiança", pergunta: "Por que acreditar na metodologia e na empresa?",
    intuito: "Dar provas (método, resultados e ciência) e abrir um caminho claro para o RH.",
    validar: "06/11: datas da linha do tempo; \"validado no SUS\" fica de fora. 09/11: só números liberados, sem o nome da indústria. 11/11: leitura do estudo pela responsável médica. 13/11: \"Diagnóstico\" sem \"gratuito\"." },
];
const POSTS = [
  { b: 0, sem: 1, dia: "seg", data: "19/10", fmt: "reel", prod: "a gravar", titulo: "Reel do Dr. Ronald",
    resumo: "O fundador do Escritório do Paciente resume os dois posts publicados e puxa a origem: tudo começou num hospital, em 2009.",
    porTras: "Rosto e voz médica para a marca, com confiança desde o começo." },
  { b: 0, sem: 1, dia: "qua", data: "21/10", fmt: "carrossel", prod: "arte pronta", titulo: "Nossa história começou em um hospital",
    resumo: "Do Escritório do Paciente, em 2009, à fairhealth hoje: a escuta como essência e o fio que liga a origem ao presente.",
    porTras: "O modelo tem história: não somos mais uma startup de bem-estar." },
  { b: 1, sem: 1, dia: "sex", data: "23/10", fmt: "carrossel", prod: "a produzir", titulo: "Cuidar não deveria começar quando algo vai mal",
    resumo: "Cada slide volta um passo: afastamento, atestado, semana pesada, noite sem dormir. Fecha em \"a gente cuida antes\".",
    porTras: "O plano de saúde entra depois. A fairhealth entra antes." },
  { b: 1, sem: 2, dia: "seg", data: "26/10", fmt: "reel", prod: "a produzir", titulo: "Quando o cuidado não faz parte da rotina",
    resumo: "Um número com fonte (licenças por saúde mental em 2024) e três barreiras: tempo, acesso e continuidade.",
    porTras: "O problema não é a falta de plano: é o cuidado estar longe." },
  { b: 1, sem: 2, dia: "qua", data: "28/10", fmt: "foto", prod: "arte pronta", titulo: "Prevenção também é investimento",
    resumo: "−28% de absenteísmo (HBR, 2022) e −22% de custos com saúde (SHRM, 2023), com a fonte visível.",
    porTras: "Cuidar antes também faz sentido para o financeiro." },
  { b: 1, sem: 2, dia: "sex", data: "30/10", fmt: "carrossel", prod: "a produzir", titulo: "Como a prevenção vira rotina na empresa",
    resumo: "Cuidado perto, escuta, plano que cabe na rotina, acompanhamento e indicadores para o RH.",
    porTras: "Prevenção é estrutura, não campanha pontual." },
  { b: 2, sem: 3, dia: "ter", data: "03/11", fmt: "carrossel", prod: "a produzir", titulo: "O cuidado na prática",
    resumo: "A jornada de uma pessoa (a Clara, personagem fictícia): escuta, medições, plano e acompanhamento.",
    porTras: "O Escritório do Cuidado pela experiência, sem repetir a apresentação." },
  { b: 2, sem: 3, dia: "qua", data: "04/11", fmt: "reel", prod: "a produzir", titulo: "Quatro frentes, um cuidado conectado",
    resumo: "Escritório do Cuidado, Programa de Medicina do Estilo de Vida, plataforma digital e wearables, ligados pelo fio.",
    porTras: "Não são quatro produtos: é um cuidado só." },
  { b: 3, sem: 3, dia: "sex", data: "06/11", fmt: "carrossel", prod: "a produzir", titulo: "Uma história que começou em 2009",
    resumo: "A linha do tempo do método, de 2007 a 2025, e o caso do hospital onde tudo começou, sem o nome.",
    porTras: "O método tem base, trajetória e evidência." },
  { b: 3, sem: 4, dia: "seg", data: "09/11", fmt: "reel", prod: "a gravar", titulo: "Resultados reais, com o Dr. Ronald",
    resumo: "Numa indústria atendida, 8 em cada 10 pessoas voltaram para mais de um atendimento, com 98% de adesão.",
    porTras: "Ninguém volta a um lugar onde não se sentiu cuidado." },
  { b: 3, sem: 4, dia: "qua", data: "11/11", fmt: "carrossel", prod: "roteiro pronto", titulo: "Estilo de vida também é tratamento sério",
    resumo: "O Diabetes Prevention Program: mudar a rotina reduziu em 58% os novos casos de diabetes tipo 2. Semana do Dia Mundial do Diabetes.",
    porTras: "A Medicina do Estilo de Vida tem ciência por trás." },
  { b: 3, sem: 4, dia: "sex", data: "13/11", fmt: "carrossel", prod: "a produzir", titulo: "Como levar a fairhealth para sua empresa",
    resumo: "Diagnóstico, proposta personalizada e implementação, com o convite para falar pelo direct.",
    porTras: "Um caminho claro para o RH, sem preço e sem promessa." },
];
const SEMANAS = ["19 a 23/10", "26 a 30/10", "03 a 06/11", "09 a 13/11"];
const DIAS = { seg: "segunda", ter: "terça", qua: "quarta", sex: "sexta" };

async function icone(Comp, cor) {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { size: 256, color: "#" + cor, strokeWidth: 1.4 }));
  return "image/png;base64," + (await sharp(Buffer.from(svg)).png().toBuffer()).toString("base64");
}

async function main() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = "Programação do Instagram · 19/10 a 13/11";
  pres.author = "fairhealth";
  const C = pres.SchemeColor;
  const COR = { verde: C.text1, branco: C.background1, vlogo: C.text2, tif: C.accent1, tclaro: C.accent2 };
  const W = 13.333, M = 0.75;
  const RODAPE = "fairhealth · Programação do Instagram · 19/10 a 13/11";

  pres.defineSlideMaster({ title: "CAPA", background: { color: COR.tif },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: M, y: 1.15, w: 9, h: 0.8, fontSize: 36, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "body", type: "body", x: M, y: 1.9, w: 9, h: 0.4, fontSize: 14, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } },
    ] });
  pres.defineSlideMaster({ title: "BLOCO", background: { color: COR.branco },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: M, y: 0.82, w: 9.6, h: 0.65, fontSize: 28, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } },
      { text: { text: RODAPE, options: { x: M, y: 7.0, w: 6, h: 0.25, fontSize: 10, color: COR.vlogo, margin: 0 } } },
    ], slideNumber: { x: W - M - 0.5, y: 7.0, w: 0.5, h: 0.25, fontSize: 10, color: COR.vlogo, align: "right" } });

  const logo = "image/png;base64," + fs.readFileSync(path.join(RAIZ, "instagram/marca/logo-circulo.png")).toString("base64");
  const ICO = { reel: FiFilm, carrossel: FiLayers, foto: FiImage };
  const ic = {};
  for (const k of Object.keys(ICO)) ic[k] = await icone(ICO[k], HEX.verde);
  const fina = (cor, w = 0.5) => ({ color: cor, width: w });

  // ---------------------------------------------------------------- 1 · capa com o mês
  pres.addSection({ title: "O mês" });
  let s = pres.addSlide({ masterName: "CAPA", sectionTitle: "O mês" });
  s.addImage({ data: logo, x: M, y: 0.4, w: 0.55, h: 0.55, altText: "Logo da fairhealth" });
  s.addText("@fairhealth.br", { x: W - M - 3, y: 0.52, w: 3, h: 0.3, fontSize: 12, color: COR.verde, align: "right", margin: 0, isTextBox: true });
  s.addText("Programação do Instagram", { placeholder: "title" });
  s.addText("19/10 a 13/11  ·  4 semanas  ·  12 posts  ·  3 por semana", { placeholder: "body" });
  // a linha do mês: uma linha fina com um ponto em cada semana
  const cw = (W - 2 * M) / 4;
  s.addShape(pres.shapes.LINE, { x: M, y: 3.05, w: W - 2 * M, h: 0, line: fina(COR.branco, 0.75) });
  for (let w = 0; w < 4; w++) {
    const x = M + w * cw;
    s.addShape(pres.shapes.OVAL, { x: x - 0.05, y: 3.0, w: 0.1, h: 0.1, fill: { color: COR.verde }, line: { type: "none" } });
    s.addText([{ text: `SEMANA ${w + 1}`, options: { fontSize: 10, bold: true, charSpacing: 3, breakLine: true } }, { text: SEMANAS[w], options: { fontSize: 12 } }],
      { x, y: 2.45, w: cw - 0.2, h: 0.5, color: COR.verde, margin: 0, isTextBox: true });
    POSTS.filter((p) => p.sem === w + 1).forEach((p, i) => {
      const y = 3.35 + i * 1.12;
      s.addText([{ text: `${p.dia} ${p.data}`, options: { fontSize: 11, bold: true, breakLine: true } },
                 { text: p.titulo, options: { fontSize: 14, breakLine: true } },
                 { text: `${FMT[p.fmt]}  ·  bloco ${BLOCOS[p.b].n}`, options: { fontSize: 10 } }],
        { x, y, w: cw - 0.3, h: 1.0, color: COR.verde, valign: "top", margin: 0, paraSpaceAfter: 2, isTextBox: true });
    });
  }
  s.addText("Blocos  ·  01 Reconhecimento  ·  02 Relevância  ·  03 Compreensão  ·  04 Confiança",
    { x: M, y: 6.85, w: W - 2 * M, h: 0.3, fontSize: 11, color: COR.verde, margin: 0, isTextBox: true });
  s.addNotes("12 posts em 4 semanas: 1 reel e 2 posts estáticos por semana (4 reels, 7 carrosséis e 1 foto única). Segunda, quarta e sexta; na semana de Finados, terça, quarta e sexta. As duas falas do Dr. Ronald podem ser gravadas no mesmo dia. Já prontos: o post de 21/10, \"Prevenção também é investimento\" e o roteiro de 11/11.");

  // ---------------------------------------------------------------- 2 a 5 · um bloco por slide
  pres.addSection({ title: "Os blocos" });
  for (let b = 0; b < 4; b++) {
    const B = BLOCOS[b], posts = POSTS.filter((p) => p.b === b);
    s = pres.addSlide({ masterName: "BLOCO", sectionTitle: "Os blocos" });
    s.addText(`BLOCO ${B.n}  ·  ${B.nome.toUpperCase()}`, { x: M, y: 0.5, w: 6, h: 0.3, fontSize: 11, bold: true, charSpacing: 4, color: COR.vlogo, margin: 0, isTextBox: true });
    s.addText(B.n, { x: W - M - 2.2, y: 0.3, w: 2.2, h: 1.2, fontSize: 72, color: COR.tif, align: "right", margin: 0, isTextBox: true });
    s.addText(B.pergunta, { placeholder: "title" });
    s.addText(B.intuito, { x: M, y: 1.47, w: 9.6, h: 0.35, fontSize: 14, color: COR.vlogo, margin: 0, isTextBox: true });
    s.addText(`${posts.length} posts  ·  ${posts[0].data} a ${posts[posts.length - 1].data}`,
      { x: W - M - 3.5, y: 1.47, w: 3.5, h: 0.35, fontSize: 12, color: COR.vlogo, align: "right", margin: 0, isTextBox: true });

    const y0 = 2.05, rh = 1.2, xl = M + 0.1;
    s.addShape(pres.shapes.LINE, { x: M, y: y0, w: W - 2 * M, h: 0, line: fina(COR.tclaro) });
    // fio do bloco: uma linha vertical fina que liga os pontos
    if (posts.length > 1) s.addShape(pres.shapes.LINE, { x: xl, y: y0 + 0.36, w: 0, h: (posts.length - 1) * rh, line: fina(COR.tif, 1) });
    posts.forEach((p, i) => {
      const y = y0 + i * rh;
      s.addShape(pres.shapes.OVAL, { x: xl - 0.06, y: y + 0.3, w: 0.12, h: 0.12, fill: { color: COR.tif }, line: { type: "none" } });
      s.addText([{ text: p.data, options: { fontSize: 20, breakLine: true } }, { text: `${DIAS[p.dia]}  ·  semana ${p.sem}`, options: { fontSize: 10, color: COR.vlogo } }],
        { x: xl + 0.3, y: y + 0.18, w: 1.9, h: 0.75, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
      s.addImage({ data: ic[p.fmt], x: 3.05, y: y + 0.25, w: 0.2, h: 0.2, altText: FMT[p.fmt] });
      s.addText([{ text: FMT[p.fmt], options: { fontSize: 12, breakLine: true } }, { text: p.prod, options: { fontSize: 10, color: COR.vlogo } }],
        { x: 3.35, y: y + 0.2, w: 1.6, h: 0.6, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
      s.addText([{ text: p.titulo, options: { fontSize: 15, bold: true, breakLine: true } },
                 { text: p.resumo, options: { fontSize: 14, breakLine: true } },
                 { text: p.porTras, options: { fontSize: 14, italic: true, color: COR.vlogo } }],
        { x: 5.15, y: y + 0.13, w: W - M - 5.15, h: rh - 0.18, color: COR.verde, valign: "top", margin: 0, paraSpaceAfter: 2, isTextBox: true });
      s.addShape(pres.shapes.LINE, { x: M, y: y + rh, w: W - 2 * M, h: 0, line: fina(COR.tclaro) });
    });
    if (B.extra) s.addText(B.extra, { x: M, y: y0 + posts.length * rh + 0.25, w: W - 2 * M, h: 0.3, fontSize: 11, italic: true, color: COR.vlogo, margin: 0, isTextBox: true });
    s.addNotes(`Intuito: ${B.intuito}\nPara validar: ${B.validar}`);
  }

  await pres.writeFile({ fileName: SAIDA });
  if (process.env.APPLY_THEME) { const { applyTheme } = require(process.env.APPLY_THEME); await applyTheme(SAIDA, THEME); }
  console.log("ok", SAIDA);
}
main().catch((e) => { console.error(e); process.exit(1); });
