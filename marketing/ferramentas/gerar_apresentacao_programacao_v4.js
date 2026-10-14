// v4 (14/10): a v3 totalmente editável (pedido da Nina). Os ícones de formato são formas nativas do PowerPoint, e não
// imagens. Nada fica preso no layout: rodapé, pílula de datas e logo estão em cada slide. O texto de cada post do
// calendário fica dentro da própria forma. Só o logo continua imagem (não há versão vetorial no repositório).
//
// v3 (14/10): a partir de três referências enviadas pela Nina.
//   slide 1: os 4 blocos em colunas coloridas, com números grandes e setas entre elas;
//   slide 2: o mês numa página, em formato de calendário, com uma cor por formato;
//   slides 3 a 6: uma semana por slide, com 3 cartões (data, título e subtítulo).
// v1 (22 slides) e v2 (5 slides) ficam guardadas nos geradores e arquivos anteriores.
//
// Uso: NODE_PATH=<pasta>/node_modules APPLY_THEME=<apply_theme.js> node gerar_apresentacao_programacao_v3.js saida.pptx
// Fonte: Raleway (da marca), que precisa estar instalada para abrir como planejado.
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");

const SAIDA = process.argv[2] || "Programacao_Instagram_v4.pptx";
const RAIZ = path.resolve(__dirname, "..", "..");
const HEX = { tif: "96C5BD", verde: "1F3A36", creme: "F0F0E9", tclaro: "BFE0D9", vlogo: "2F6B64", branco: "FFFFFF" };
const THEME = {
  name: "fairhealth", headFontFace: "Raleway", bodyFontFace: "Raleway",
  colors: { dk1: HEX.verde, lt1: HEX.branco, dk2: HEX.vlogo, lt2: HEX.creme, accent1: HEX.tif, accent2: HEX.tclaro,
            accent3: "0D1816", accent4: "5FA89A", accent5: HEX.verde, accent6: HEX.vlogo, hlink: HEX.vlogo, folHlink: HEX.verde },
};

const BLOCOS = [
  { n: "1", nome: "Reconhecimento", pergunta: "Quem somos e por que existimos?", intuito: "Apresentar a marca e criar vínculo com a origem.", posts: "2 posts · 19 e 21/10" },
  { n: "2", nome: "Relevância", pergunta: "Por que as empresas precisam olhar para isso?", intuito: "Fazer o RH se reconhecer no problema: o cuidado costuma chegar tarde.", posts: "4 posts · 23 a 30/10" },
  { n: "3", nome: "Compreensão", pergunta: "Como a FairHealth transforma isso em cuidado real?", intuito: "Mostrar o cuidado na prática, pela experiência de quem é atendido.", posts: "2 posts · 03 e 04/11" },
  { n: "4", nome: "Confiança", pergunta: "Por que acreditar na metodologia e na empresa?", intuito: "Dar provas e abrir um caminho claro para o RH.", posts: "4 posts · 06 a 13/11" },
];
const FMT = { reel: "Reel", carrossel: "Carrossel", foto: "Foto única" };
// col: 0 = segunda ... 6 = domingo
const POSTS = [
  { sem: 1, col: 0, dia: "segunda", data: "19/10", fmt: "reel", b: 0, curto: "Reel do Dr. Ronald: quem somos",
    titulo: "Quem somos, na voz do Dr. Ronald", sub: "Resumo dos posts já publicados, contado pelo fundador do Escritório do Paciente, puxando a origem em 2009" },
  { sem: 1, col: 2, dia: "quarta", data: "21/10", fmt: "carrossel", b: 0, curto: "Por que a FairHealth existe?",
    titulo: "Por que a FairHealth existe?", sub: "A origem do modelo de cuidado em 2009 e sua evolução até as empresas" },
  { sem: 1, col: 4, dia: "sexta", data: "23/10", fmt: "carrossel", b: 1, curto: "Cuidar antes, não depois",
    titulo: "Cuidar da saúde não deveria começar quando algo vai mal", sub: "A importância de uma abordagem preventiva, e não apenas reativa" },
  { sem: 2, col: 0, dia: "segunda", data: "26/10", fmt: "reel", b: 1, curto: "Cuidado fora da rotina",
    titulo: "O que acontece quando o cuidado não faz parte da rotina?", sub: "Desafios da saúde dos colaboradores: acesso e continuidade do cuidado" },
  { sem: 2, col: 2, dia: "quarta", data: "28/10", fmt: "foto", b: 1, curto: "Prevenção é investimento",
    titulo: "Prevenção também é investimento", sub: "O que os estudos mostram sobre absenteísmo e custos com saúde quando a empresa cuida antes" },
  { sem: 2, col: 4, dia: "sexta", data: "30/10", fmt: "carrossel", b: 1, curto: "Prevenção na rotina da empresa",
    titulo: "Como transformar a prevenção em parte da rotina de uma empresa?", sub: "Conectar o problema ao modelo de cuidado oferecido pela FairHealth" },
  { sem: 3, col: 1, dia: "terça", data: "03/11", fmt: "carrossel", b: 2, curto: "O cuidado na prática",
    titulo: "Como funciona o cuidado na prática?", sub: "A jornada entre escuta, atendimento, plano individualizado e acompanhamento" },
  { sem: 3, col: 2, dia: "quarta", data: "04/11", fmt: "reel", b: 2, curto: "Quatro frentes, um cuidado",
    titulo: "Quatro frentes, um cuidado conectado", sub: "Medicina do Estilo de Vida, Escritório do Cuidado, plataforma e wearables" },
  { sem: 3, col: 4, dia: "sexta", data: "06/11", fmt: "carrossel", b: 3, curto: "Uma história desde 2009",
    titulo: "Uma história de cuidado que começou em 2009", sub: "Linha do tempo da metodologia e evolução até a FairHealth" },
  { sem: 4, col: 0, dia: "segunda", data: "09/11", fmt: "reel", b: 3, curto: "Resultados reais, com o Dr. Ronald",
    titulo: "Cuidado na prática: experiências e resultados reais", sub: "Evidências e resultados documentados, contados pelo Dr. Ronald" },
  { sem: 4, col: 2, dia: "quarta", data: "11/11", fmt: "carrossel", b: 3, curto: "Estilo de vida é tratamento sério",
    titulo: "Estilo de vida também é tratamento sério", sub: "O que a ciência mostra sobre mudar a rotina, na semana do Dia Mundial do Diabetes" },
  { sem: 4, col: 4, dia: "sexta", data: "13/11", fmt: "carrossel", b: 3, curto: "Como levar a FairHealth à empresa",
    titulo: "Como levar a FairHealth para sua empresa?", sub: "Encerramento da apresentação inicial com orientação para o RH" },
];
const SEMANAS = [
  { datas: "19 a 23/10", inicio: 19, mesIni: 10, texto: "Reconhecimento e começo da relevância. O Dr. Ronald retoma o que já foi publicado, a origem explica por que existimos e o primeiro post mostra por que cuidar antes.",
    validar: "Reel do Dr. Ronald: autorização de uso de imagem (exceção à decisão de não ter o time em cena; o post do time segue segurado)." },
  { datas: "26 a 30/10", inicio: 26, mesIni: 10, texto: "Relevância. O problema, o argumento de investimento e como a prevenção vira parte da rotina da empresa.",
    validar: "26/10: conferir o número de licenças por saúde mental de 2024 no painel do Ministério da Previdência. 28/10: o que os estudos da HBR e da SHRM mediram." },
  { datas: "03 a 06/11", inicio: 2, mesIni: 11, texto: "Compreensão e começo da confiança. O cuidado na prática, as quatro frentes conectadas e a trajetória do método.",
    validar: "03/11: decidir se a jornada é contada pela Clara (personagem fictícia, sinalizada) ou sem personagem. 06/11: conferir as datas da linha do tempo; \"validado no SUS\" fica de fora." },
  { datas: "09 a 13/11", inicio: 9, mesIni: 11, texto: "Confiança. Resultados reais, a ciência por trás do cuidado e o convite para o RH.",
    validar: "09/11: só números liberados, sem o nome da indústria. 11/11: leitura do estudo pela responsável médica. 13/11: \"Diagnóstico\" sem \"gratuito\"." },
];
const NOTAS_DIA = { "3-0": "Finados", "4-5": "Dia Mundial do Diabetes", "4-6": "Proclamação da República" };

// ícones de formato desenhados com formas nativas (editáveis), dentro de um quadrado de lado t
function icone(pres, s, fmt, x, y, t, cor, fundo) {
  const L = { color: cor, width: 1.25 }, nada = { type: "none" };
  const RR = pres.shapes.ROUNDED_RECTANGLE;
  if (fmt === "reel") {
    s.addShape(RR, { x, y: y + t * 0.14, w: t, h: t * 0.72, fill: { type: "none" }, line: L, rectRadius: t * 0.12, objectName: "Ícone reel" });
    s.addShape(pres.shapes.ISOSCELES_TRIANGLE, { x: x + t * 0.36, y: y + t * 0.36, w: t * 0.32, h: t * 0.28, rotate: 90, fill: { color: cor }, line: nada, objectName: "Ícone reel (play)" });
  } else if (fmt === "carrossel") {
    s.addShape(RR, { x: x + t * 0.28, y, w: t * 0.72, h: t * 0.72, fill: { color: fundo }, line: L, rectRadius: t * 0.1, objectName: "Ícone carrossel (fundo)" });
    s.addShape(RR, { x: x + t * 0.14, y: y + t * 0.14, w: t * 0.72, h: t * 0.72, fill: { color: fundo }, line: L, rectRadius: t * 0.1, objectName: "Ícone carrossel (meio)" });
    s.addShape(RR, { x, y: y + t * 0.28, w: t * 0.72, h: t * 0.72, fill: { color: fundo }, line: L, rectRadius: t * 0.1, objectName: "Ícone carrossel (frente)" });
  } else {
    s.addShape(RR, { x, y: y + t * 0.1, w: t, h: t * 0.8, fill: { type: "none" }, line: L, rectRadius: t * 0.1, objectName: "Ícone foto" });
    s.addShape(pres.shapes.OVAL, { x: x + t * 0.62, y: y + t * 0.24, w: t * 0.16, h: t * 0.16, fill: { color: cor }, line: nada, objectName: "Ícone foto (sol)" });
    s.addShape(pres.shapes.ISOSCELES_TRIANGLE, { x: x + t * 0.12, y: y + t * 0.42, w: t * 0.56, h: t * 0.36, fill: { color: cor }, line: nada, objectName: "Ícone foto (montanha)" });
  }
}

async function main() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = "Programação do Instagram · 19/10 a 13/11";
  pres.author = "fairhealth";
  const C = pres.SchemeColor;
  const COR = { verde: C.text1, branco: C.background1, vlogo: C.text2, creme: C.background2, tif: C.accent1, tclaro: C.accent2 };
  // cor de cada formato no calendário (fundo, texto)
  const COR_FMT = { reel: [COR.tif, COR.verde], carrossel: [COR.verde, COR.creme], foto: [COR.branco, COR.verde] };
  const W = 13.333, H = 7.5, M = 0.7;
  const logo = "image/png;base64," + fs.readFileSync(path.join(RAIZ, "instagram/marca/logo-circulo.png")).toString("base64");

  pres.defineSlideMaster({ title: "BLOCOS", background: { color: COR.creme }, objects: [] });
  pres.defineSlideMaster({ title: "CALENDARIO", background: { color: COR.creme },
    objects: [{ placeholder: { options: { name: "title", type: "title", x: M, y: 0.4, w: 7.5, h: 0.75, fontSize: 36, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } }] });
  pres.defineSlideMaster({ title: "SEMANA", background: { color: COR.creme },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: M, y: 0.8, w: 7, h: 0.85, fontSize: 48, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } },
    ] });

  // ---------------------------------------------------------------- 1 · os quatro blocos
  pres.addSection({ title: "Os blocos" });
  let s = pres.addSlide({ masterName: "BLOCOS", sectionTitle: "Os blocos" });
  const pw = W / 4;
  const PAINEL = [
    { cor: COR.verde, txt: COR.creme, num: COR.creme, topo: 3.55 },
    { cor: COR.tclaro, txt: COR.verde, num: COR.verde, topo: 0.55 },
    { cor: COR.creme, txt: COR.verde, num: COR.vlogo, topo: 2.55 },
    { cor: COR.tif, txt: COR.verde, num: COR.verde, topo: 1.45 },
  ];
  PAINEL.forEach((P, i) => s.addShape(pres.shapes.RECTANGLE, { x: i * pw, y: 0, w: pw + (i < 3 ? 0.01 : 0), h: H, fill: { color: P.cor }, line: { type: "none" }, objectName: `Bloco ${i + 1}` }));
  // setas: a ponta de cada coluna entra na seguinte, na altura do número dela
  for (let i = 0; i < 3; i++) {
    s.addShape(pres.shapes.ISOSCELES_TRIANGLE, { x: (i + 1) * pw - 0.21, y: PAINEL[i + 1].topo + 0.52, w: 0.42, h: 0.26, rotate: 90,
      fill: { color: PAINEL[i].cor }, line: { type: "none" }, objectName: `Seta ${i + 1}` });
  }
  BLOCOS.forEach((B, i) => {
    const P = PAINEL[i], x = i * pw + 0.45, w = pw - 0.8;
    s.addText(B.n, { x, y: P.topo, w, h: 1.45, fontSize: 96, color: P.num, valign: "top", margin: 0, isTextBox: true });
    s.addText([{ text: B.nome, options: { fontSize: 22, breakLine: true } },
               { text: B.pergunta, options: { fontSize: 15, bold: true, paraSpaceBefore: 8, breakLine: true } },
               { text: B.intuito, options: { fontSize: 14, paraSpaceBefore: 8, breakLine: true } },
               { text: B.posts, options: { fontSize: 11, bold: true, charSpacing: 1, paraSpaceBefore: 12 } }],
      { x, y: P.topo + 1.5, w, h: 2.4, color: P.txt, valign: "top", margin: 0, isTextBox: true });
  });
  s.addText("PROGRAMAÇÃO DO INSTAGRAM\n19/10 A 13/11", { x: 0.45, y: 0.5, w: 3.0, h: 0.5, fontSize: 10, bold: true, charSpacing: 2, color: COR.creme, valign: "top", margin: 0, isTextBox: true });
  s.addNotes("Os quatro blocos contam a marca em sequência: quem somos, por que importa, como funciona e por que acreditar. Já publicados antes desta programação: \"O que é a FairHealth?\" e \"Conheça o Escritório do Cuidado\". O post do time segue segurado.");

  // ---------------------------------------------------------------- 2 · calendário
  pres.addSection({ title: "Calendário" });
  s = pres.addSlide({ masterName: "CALENDARIO", sectionTitle: "Calendário" });
  s.addText([{ text: "Calendário ", options: { bold: true } }, { text: "de conteúdo" }], { placeholder: "title" });
  s.addText("19/10 a 13/11  ·  3 posts por semana", { x: M, y: 1.12, w: 6, h: 0.35, fontSize: 16, italic: true, color: COR.vlogo, margin: 0, isTextBox: true });
  // legenda
  let lx = 7.75;
  for (const k of ["reel", "carrossel", "foto"]) {
    const [bg] = COR_FMT[k];
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: lx, y: 0.62, w: 0.6, h: 0.2, fill: { color: bg }, line: k === "foto" ? { color: COR.verde, width: 0.75 } : { type: "none" }, rectRadius: 0.1 });
    s.addText(FMT[k], { x: lx + 0.7, y: 0.54, w: 1.1, h: 0.36, fontSize: 13, color: COR.verde, valign: "middle", margin: 0, isTextBox: true });
    lx += 1.75;
  }
  const gx = 1.8, gw = (W - M - gx) / 7, gy = 1.95, rh = 1.18;
  ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"].forEach((d, c) =>
    s.addText(d, { x: gx + c * gw, y: gy - 0.38, w: gw, h: 0.3, fontSize: 13, color: COR.verde, align: "center", margin: 0, isTextBox: true }));
  // grade fina
  for (let r = 0; r <= 4; r++) s.addShape(pres.shapes.LINE, { x: gx, y: gy + r * rh, w: W - M - gx, h: 0, line: { color: COR.tif, width: 0.75 } });
  for (let c = 0; c <= 7; c++) s.addShape(pres.shapes.LINE, { x: gx + c * gw, y: gy, w: 0, h: 4 * rh, line: { color: COR.tif, width: 0.75 } });
  SEMANAS.forEach((S, r) => {
    const y = gy + r * rh;
    s.addText([{ text: `Semana ${r + 1}`, options: { bold: true, fontSize: 12, breakLine: true } }, { text: S.datas, options: { fontSize: 10 } }],
      { x: M, y: y + 0.38, w: gx - M - 0.05, h: 0.5, color: COR.verde, margin: 0, isTextBox: true });
    for (let c = 0; c < 7; c++) {
      // número do dia
      let dia = S.inicio + c, mes = S.mesIni;
      if (mes === 10 && dia > 31) { dia -= 31; mes = 11; }
      s.addText(String(dia).padStart(2, "0"), { x: gx + c * gw + 0.07, y: y + 0.05, w: 0.4, h: 0.2, fontSize: 10, color: COR.vlogo, margin: 0, isTextBox: true });
      const nota = NOTAS_DIA[`${r + 1}-${c}`];
      if (nota) s.addText(nota, { x: gx + c * gw + 0.07, y: y + 0.32, w: gw - 0.14, h: 0.7, fontSize: 10, italic: true, color: COR.vlogo, valign: "top", margin: 0, isTextBox: true });
    }
  });
  POSTS.forEach((p) => {
    const [bg, tx] = COR_FMT[p.fmt], x = gx + p.col * gw + 0.06, y = gy + (p.sem - 1) * rh + 0.28;
    s.addText(p.curto, { shape: pres.shapes.ROUNDED_RECTANGLE, x, y, w: gw - 0.12, h: rh - 0.36, fill: { color: bg },
      line: p.fmt === "foto" ? { color: COR.verde, width: 0.75 } : { type: "none" }, rectRadius: 0.1,
      fontSize: 11, bold: true, color: tx, align: "center", valign: "middle", margin: 4, objectName: `Post ${p.data}` });
  });
  s.addText("4 reels  ·  7 carrosséis  ·  1 foto única  ·  1 reel e 2 posts estáticos por semana",
    { x: gx, y: gy + 4 * rh + 0.15, w: W - M - gx, h: 0.3, fontSize: 12, color: COR.vlogo, margin: 0, isTextBox: true });
  s.addNotes("Segunda, quarta e sexta; na semana de Finados (02/11), terça, quarta e sexta. As duas falas do Dr. Ronald podem ser gravadas no mesmo dia. Já prontos: o post de 21/10, \"Prevenção também é investimento\" e o roteiro de 11/11.");

  // ---------------------------------------------------------------- 3 a 6 · uma semana por slide
  pres.addSection({ title: "As semanas" });
  const cw = (W - 2 * M - 2 * 0.3) / 3;
  SEMANAS.forEach((S, i) => {
    s = pres.addSlide({ masterName: "SEMANA", sectionTitle: "As semanas" });
    s.addText(`0${i + 1}`, { x: M, y: 0.5, w: 1, h: 0.3, fontSize: 12, color: COR.vlogo, margin: 0, isTextBox: true });
    s.addText(`Semana ${i + 1}`, { placeholder: "title" });
    s.addText(S.datas, { x: M, y: 1.65, w: 6, h: 0.6, fontSize: 30, color: COR.vlogo, margin: 0, isTextBox: true });
    s.addText(S.texto, { x: 8.45, y: 0.85, w: W - M - 8.45, h: 1.4, fontSize: 13, color: COR.vlogo, valign: "top", margin: 0, isTextBox: true });
    POSTS.filter((p) => p.sem === i + 1).forEach((p, k) => {
      const x = M + k * (cw + 0.3), y = 2.75, h = 3.6;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: cw, h, fill: { color: COR.branco }, line: { type: "none" }, rectRadius: 0.14, objectName: `Post ${p.data}` });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.3, y: y + 0.3, w: 0.55, h: 0.55, fill: { color: COR.tif }, line: { type: "none" }, rectRadius: 0.1 });
      icone(pres, s, p.fmt, x + 0.425, y + 0.425, 0.3, COR.verde, COR.tif);
      s.addText(`${FMT[p.fmt]}  ·  bloco ${p.b + 1}`, { x: x + 1.0, y: y + 0.42, w: cw - 1.3, h: 0.3, fontSize: 11, color: COR.vlogo, margin: 0, isTextBox: true });
      s.addText(`${p.dia}, ${p.data}`, { x: x + 0.3, y: y + 1.1, w: cw - 0.6, h: 0.3, fontSize: 13, bold: true, color: COR.verde, margin: 0, isTextBox: true });
      s.addText(p.titulo, { x: x + 0.3, y: y + 1.45, w: cw - 0.6, h: 0.95, fontSize: 17, bold: true, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
      s.addText(p.sub, { x: x + 0.3, y: y + 2.4, w: cw - 0.6, h: 1.05, fontSize: 14, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
    });
    s.addText("19/10 A 13/11", { shape: pres.shapes.ROUNDED_RECTANGLE, rectRadius: 0.19, fill: { type: "none" }, line: { color: COR.verde, width: 0.75 },
      x: M, y: 6.72, w: 1.75, h: 0.38, fontSize: 11, bold: true, charSpacing: 2, color: COR.verde, align: "center", valign: "middle", margin: 0, objectName: "Período" });
    s.addImage({ data: logo, x: W - M - 1.75, y: 6.68, w: 0.45, h: 0.45, altText: "Logo da fairhealth" });
    s.addText("fairhealth", { x: W - M - 1.2, y: 6.72, w: 1.2, h: 0.38, fontSize: 14, color: COR.verde, valign: "middle", margin: 0, isTextBox: true });
    s.addNotes(`Para validar: ${S.validar}`);
  });

  await pres.writeFile({ fileName: SAIDA });
  if (process.env.APPLY_THEME) { const { applyTheme } = require(process.env.APPLY_THEME); await applyTheme(SAIDA, THEME); }
  console.log("ok", SAIDA);
}
main().catch((e) => { console.error(e); process.exit(1); });
