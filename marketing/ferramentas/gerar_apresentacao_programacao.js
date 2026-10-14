// Gera a apresentação da programação do Instagram (12 posts, 19/10 a 13/11) em PowerPoint.
// Base: marketing/calendario-12-posts.md, "Distribuição do próximo mês, versão de 3 posts por semana".
//
// Uso (pptxgenjs, react-icons, react, react-dom e sharp instalados numa pasta node_modules):
//   NODE_PATH=<pasta>/node_modules node marketing/ferramentas/gerar_apresentacao_programacao.js saida.pptx
// Fonte: Raleway (da marca). Quem abrir no PowerPoint precisa ter a Raleway instalada (Google Fonts, gratuita).
const path = require("path");
const fs = require("fs");
const pptxgen = require("pptxgenjs");
const sharp = require("sharp");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const { FiFilm, FiLayers, FiImage, FiCheckCircle } = require("react-icons/fi");

const SAIDA = process.argv[2] || "Programacao_Instagram.pptx";
const RAIZ = path.resolve(__dirname, "..", "..");
const SKILL_THEME = process.env.APPLY_THEME; // caminho do apply_theme.js (opcional)

// ---------------------------------------------------------------- marca
const HEX = { tif: "96C5BD", verde: "1F3A36", creme: "F0F0E9", tclaro: "BFE0D9", vlogo: "2F6B64", noite: "0D1816", branco: "FFFFFF" };
const THEME = {
  name: "fairhealth",
  headFontFace: "Raleway",
  bodyFontFace: "Raleway",
  colors: {
    dk1: HEX.verde, lt1: HEX.branco, dk2: HEX.vlogo, lt2: HEX.creme,
    accent1: HEX.tif, accent2: HEX.tclaro, accent3: HEX.noite, accent4: "5FA89A", accent5: HEX.verde, accent6: HEX.vlogo,
    hlink: HEX.vlogo, folHlink: HEX.verde,
  },
};

// ---------------------------------------------------------------- conteúdo
const BLOCOS = {
  1: { nome: "Reconhecimento", pergunta: "Quem somos e por que existimos?",
       intuito: "Apresentar a marca e criar vínculo com a origem. Quem chega ao perfil entende quem é a fairhealth, de onde ela vem e quem está por trás do cuidado.",
       fundo: "verde" },
  2: { nome: "Relevância", pergunta: "Por que as empresas precisam olhar para isso?",
       intuito: "Fazer o RH se reconhecer no problema: o cuidado costuma chegar tarde, quando a doença já apareceu. A prevenção precisa fazer parte da rotina.",
       fundo: "teal" },
  3: { nome: "Compreensão", pergunta: "Como a fairhealth transforma isso em cuidado real?",
       intuito: "Mostrar como o cuidado funciona na prática, pela experiência de quem é atendido, sem repetir a apresentação do Escritório do Cuidado.",
       fundo: "tif" },
  4: { nome: "Confiança", pergunta: "Por que acreditar na metodologia e na empresa?",
       intuito: "Dar provas (a trajetória do método, os resultados e a ciência) e fechar com um caminho claro para o RH.",
       fundo: "tclaro" },
};
const FORMATOS = { reel: "Reel", carrossel: "Carrossel", foto: "Foto única" };

const POSTS = [
  { bloco: 1, sem: 1, data: "19/10", dia: "segunda-feira", fmt: "reel", fmtTxt: "Reel falado · 30 a 45 s", cal: "Novo (antes do 02)",
    curto: "Reel do Dr. Ronald: quem somos e de onde viemos",
    titulo: "O que você viu até aqui, na voz de quem começou essa história",
    mostra: "O Dr. Ronald, fundador do Escritório do Paciente, resume os dois posts já publicados: o que é a fairhealth e o Escritório do Cuidado. Termina puxando a origem: \"e tudo isso começou num hospital, em 2009\".",
    porTras: "Dar rosto e voz médica à marca. Humaniza, gera confiança e costura o que já saiu com o próximo post.",
    prod: "Roteiro a escrever · gravação",
    ponte: "Vem dos posts publicados (01 e 07). Leva para a origem (21/10)." },
  { bloco: 1, sem: 1, data: "21/10", dia: "quarta-feira", fmt: "carrossel", fmtTxt: "Carrossel · 6 slides", cal: "Post 02",
    curto: "Nossa história começou em um hospital",
    titulo: "Antes de chegar às empresas, nossa história começou em um hospital",
    mostra: "A origem em 2009, com o Escritório do Paciente; a escuta como essência; a evolução até o trabalho; a fairhealth hoje. Um fio atravessa os seis slides, de 2009 até o logo.",
    porTras: "A fairhealth não é mais uma startup de bem-estar: o modelo tem história e nasceu no cuidado de verdade. O cuidado começa pela pessoa.",
    prod: "Arte pronta (v2)",
    ponte: "Vem do reel do Dr. Ronald. Leva para o bloco de relevância: por que cuidar antes." },
  { bloco: 2, sem: 1, data: "23/10", dia: "sexta-feira", fmt: "carrossel", fmtTxt: "Carrossel de trás para frente", cal: "Post 04",
    curto: "Cuidar não deveria começar quando algo vai mal",
    titulo: "Cuidar da saúde não deveria começar quando algo vai mal",
    mostra: "Cada slide volta um passo no tempo: antes do afastamento, o atestado; antes do atestado, a semana pesada; antes dela, a noite sem dormir. Fecha em \"a gente cuida antes\".",
    porTras: "A diferença entre cuidado reativo e preventivo. O plano de saúde entra depois; a fairhealth entra antes.",
    prod: "A produzir",
    ponte: "Abre o bloco de relevância. Leva para o que acontece quando o cuidado não está na rotina." },
  { bloco: 2, sem: 2, data: "26/10", dia: "segunda-feira", fmt: "reel", fmtTxt: "Reel tipográfico", cal: "Post 05",
    curto: "Quando o cuidado não faz parte da rotina",
    titulo: "O que acontece quando o cuidado não faz parte da rotina?",
    mostra: "Um número forte, com fonte: as licenças por saúde mental em 2024 (Ministério da Previdência). E três barreiras: falta de tempo, distância do cuidado e falta de continuidade.",
    porTras: "O problema não é a falta de plano de saúde. É o cuidado não estar perto nem ser contínuo. Proximidade gera adesão.",
    prod: "A produzir · confirmar o número",
    ponte: "Vem do \"cuidar antes\". Leva para o argumento de investimento." },
  { bloco: 2, sem: 2, data: "28/10", dia: "quarta-feira", fmt: "foto", fmtTxt: "Foto única", cal: "Extra",
    curto: "Prevenção também é investimento",
    titulo: "Prevenção também é investimento",
    mostra: "Dois resultados de estudos externos, com a fonte visível: −28% de absenteísmo (Harvard Business Review, 2022) e −22% de custos com saúde (SHRM, 2023).",
    porTras: "Falar com o RH e com o financeiro: cuidar antes faz bem às pessoas e também à empresa. O retorno é consequência, não promessa.",
    prod: "Arte pronta no Canva",
    ponte: "Vem do problema. Leva para como a prevenção vira rotina." },
  { bloco: 2, sem: 2, data: "30/10", dia: "sexta-feira", fmt: "carrossel", fmtTxt: "Carrossel passo a passo", cal: "Post 06",
    curto: "Como a prevenção vira rotina na empresa",
    titulo: "Como transformar a prevenção em parte da rotina de uma empresa?",
    mostra: "Cinco movimentos: levar o cuidado para perto (dentro da empresa), começar pela escuta, montar um plano que caiba na rotina, acompanhar de forma contínua e dar ao RH indicadores do grupo.",
    porTras: "A ponte entre o problema e o modelo da fairhealth. Prevenção é estrutura, não campanha pontual.",
    prod: "A produzir",
    ponte: "Fecha o bloco de relevância. Leva para como o cuidado funciona na prática." },
  { bloco: 3, sem: 3, data: "03/11", dia: "terça-feira", fmt: "carrossel", fmtTxt: "Carrossel com história", cal: "Post 08",
    curto: "O cuidado na prática: a jornada da Clara",
    titulo: "Como funciona o cuidado na prática?",
    mostra: "A jornada contada pela Clara, personagem fictícia e sinalizada: a escuta (\"o que é importante para você?\"), anamnese e medições, um plano com três ações pequenas e o acompanhamento.",
    porTras: "Retomar o Escritório do Cuidado pela experiência de quem é atendido, sem repetir a apresentação. O plano é possível e humano.",
    prod: "A produzir · decidir sobre a Clara",
    ponte: "Abre o bloco de compreensão. Leva para as quatro frentes." },
  { bloco: 3, sem: 3, data: "04/11", dia: "quarta-feira", fmt: "reel", fmtTxt: "Reel em motion", cal: "Post 09",
    curto: "Quatro frentes, um cuidado conectado",
    titulo: "Quatro frentes, um cuidado conectado",
    mostra: "Escritório do Cuidado, Programa de Medicina do Estilo de Vida, plataforma digital e wearables aparecem um a um, e o fio contínuo liga os quatro.",
    porTras: "Não são quatro produtos soltos: é um cuidado só, que funciona melhor junto.",
    prod: "A produzir",
    ponte: "Vem da jornada. Leva para a trajetória do método." },
  { bloco: 4, sem: 3, data: "06/11", dia: "sexta-feira", fmt: "carrossel", fmtTxt: "Carrossel linha do tempo", cal: "Post 10",
    curto: "Uma história que começou em 2009",
    titulo: "Uma história de cuidado que começou em 2009",
    mostra: "Os marcos do método: Triple Aim (2007), Escritório do Paciente (2009), Quadruple Aim (2014), Quintuple Aim (2021) e Escritório do Cuidado (2024 e 2025). E o caso do hospital, sem o nome.",
    porTras: "O post de 21/10 contou por que o modelo surgiu. Este mostra que ele tem método, base internacional e trajetória.",
    prod: "A produzir · conferir as datas",
    ponte: "Abre o bloco de confiança. Leva para os resultados." },
  { bloco: 4, sem: 4, data: "09/11", dia: "segunda-feira", fmt: "reel", fmtTxt: "Reel falado · números na tela", cal: "Post 11",
    curto: "Resultados reais, com o Dr. Ronald",
    titulo: "Cuidado na prática: experiências e resultados reais",
    mostra: "O Dr. Ronald conta o que a equipe viu na prática, com os números na tela: numa indústria atendida, 8 em cada 10 pessoas voltaram para mais de um atendimento, e a adesão chegou a 98%.",
    porTras: "A prova de que as pessoas usam e voltam. Ninguém volta a um lugar onde não se sentiu cuidado.",
    prod: "Gravar junto com o reel de 19/10",
    ponte: "Vem do método. Leva para a ciência por trás do cuidado." },
  { bloco: 4, sem: 4, data: "11/11", dia: "quarta-feira", fmt: "carrossel", fmtTxt: "Carrossel · 7 slides", cal: "Extra",
    curto: "Estilo de vida também é tratamento sério",
    titulo: "Estilo de vida também é tratamento sério",
    mostra: "O estudo clássico Diabetes Prevention Program (New England Journal of Medicine, 2002): mudanças de rotina reduziram em 58% os novos casos de diabetes tipo 2 em adultos com risco. Na semana do Dia Mundial do Diabetes (14/11).",
    porTras: "A Medicina do Estilo de Vida tem evidência científica. O cuidado começa pela rotina porque a ciência mostra que ela importa.",
    prod: "Roteiro pronto",
    ponte: "Vem dos resultados. Leva para o convite final." },
  { bloco: 4, sem: 4, data: "13/11", dia: "sexta-feira", fmt: "carrossel", fmtTxt: "Carrossel de fechamento", cal: "Post 12",
    curto: "Como levar a fairhealth para sua empresa",
    titulo: "Como levar a fairhealth para sua empresa?",
    mostra: "Três passos: diagnóstico, proposta personalizada e implementação. E o convite para falar com a gente pelo direct.",
    porTras: "Fechar a apresentação inicial com um caminho claro e simples para o RH. Um convite suave, sem preço e sem promessa.",
    prod: "A produzir",
    ponte: "Fecha a programação. Daqui, o próximo mês." },
];
const SEMANAS = { 1: "19 a 23/10", 2: "26 a 30/10", 3: "03 a 06/11", 4: "09 a 13/11" };

// ---------------------------------------------------------------- imagens (ícones e fio)
async function png(svg) {
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}
async function icone(Comp, cor) {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { size: 256, color: "#" + cor, strokeWidth: 2 }));
  return png(svg);
}
const ICONE = { reel: FiFilm, carrossel: FiLayers, foto: FiImage };

// fio: onda suave; marcas: lista de {t (0..1), r, cor, borda}
function onda(w, h, cor, esp, marcas = [], amp = 0.28, ciclos = 1.15, fase = 0.6, traco = esp * 0.55) {
  const N = 240, pts = [];
  const y = (t) => h * 0.5 + h * amp * Math.sin(2 * Math.PI * (ciclos * t + fase)) * (0.65 + 0.35 * Math.sin(Math.PI * t));
  for (let i = 0; i <= N; i++) { const t = i / N; pts.push([esp + t * (w - 2 * esp), y(t)]); }
  const d = "M" + pts.map((p) => p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" L");
  const bolas = marcas.map((m) => {
    const x = esp + m.t * (w - 2 * esp), yy = y(m.t);
    return `<circle cx="${x.toFixed(1)}" cy="${yy.toFixed(1)}" r="${m.r}" fill="#${m.cor}"${m.borda ? ` stroke="#${m.borda}" stroke-width="${m.bw || 6}"` : ""}/>`;
  }).join("");
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}"><path d="${d}" fill="none" stroke="#${cor}" stroke-width="${traco}" stroke-linecap="round" stroke-linejoin="round"/>${bolas}</svg>`;
}

// ---------------------------------------------------------------- apresentação
async function main() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13,333 × 7,5 pol.
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = "Programação do Instagram · 19/10 a 13/11";
  pres.author = "fairhealth";
  const C = pres.SchemeColor;
  const COR = { verde: C.text1, branco: C.background1, vlogo: C.text2, creme: C.background2, tif: C.accent1, tclaro: C.accent2, noite: C.accent3, teal: C.accent4 };
  const TXT_SOBRE = { verde: COR.creme, vlogo: COR.creme, teal: COR.verde, tif: COR.verde, tclaro: COR.verde };

  const W = 13.333, H = 7.5, M = 0.6;
  const rodape = (cor) => [
    { text: { text: "fairhealth · Programação do Instagram · 19/10 a 13/11", options: { x: M, y: 6.95, w: 7, h: 0.3, fontSize: 10, color: cor, margin: 0 } } },
  ];
  const num = (cor) => ({ x: W - M - 0.6, y: 6.95, w: 0.6, h: 0.3, fontSize: 10, color: cor, align: "right" });

  pres.defineSlideMaster({ title: "CAPA", background: { color: COR.tif },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: M, y: 2.35, w: 9.5, h: 1.6, fontSize: 48, bold: true, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "body", type: "body", x: M, y: 4.0, w: 9.5, h: 0.6, fontSize: 22, color: COR.verde, valign: "top", margin: 0 }, text: "" } },
    ] });
  pres.defineSlideMaster({ title: "BLOCO", background: { color: COR.tif },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: M, y: 1.55, w: 6.6, h: 0.9, fontSize: 44, bold: true, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } },
      ...rodape(COR.verde),
    ], slideNumber: num(COR.verde) });
  pres.defineSlideMaster({ title: "CONTEUDO", background: { color: COR.branco },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: M, y: 0.45, w: W - 2 * M, h: 0.8, fontSize: 36, bold: true, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } },
      ...rodape(COR.vlogo),
    ], slideNumber: num(COR.vlogo) });
  pres.defineSlideMaster({ title: "POST", background: { color: COR.branco },
    objects: [
      { rect: { x: 0, y: 0, w: 4.55, h: H, fill: { color: COR.tif }, line: { type: "none" } } },
      { placeholder: { options: { name: "title", type: "title", x: 5.1, y: 0.55, w: W - 5.1 - M, h: 1.45, fontSize: 30, bold: true, color: COR.verde, align: "left", valign: "top", margin: 0 }, text: "" } },
      { text: { text: "fairhealth · Programação do Instagram · 19/10 a 13/11", options: { x: 5.1, y: 6.95, w: 6, h: 0.3, fontSize: 10, color: C.text2, margin: 0 } } },
    ], slideNumber: num(COR.vlogo) });

  // imagens
  const logo = "image/png;base64," + fs.readFileSync(path.join(RAIZ, "instagram/marca/logo-circulo.png")).toString("base64");
  const icCreme = {}, icVerde = {};
  for (const k of Object.keys(ICONE)) { icCreme[k] = await icone(ICONE[k], HEX.creme); icVerde[k] = await icone(ICONE[k], HEX.verde); }
  const icCheck = await icone(FiCheckCircle, HEX.vlogo);
  const fioCapa = await png(onda(2667, 420, HEX.creme, 22, [{ t: 0, r: 22, cor: HEX.creme }, { t: 1, r: 30, cor: HEX.verde, borda: HEX.creme, bw: 10 }], 0.26, 1.1, 0.55));
  const fioBloco = await png(onda(2667, 360, HEX.creme, 20, [], 0.3, 1.3, 0.2));
  const fioVisao = await png(onda(2400, 300, HEX.tif, 18, [], 0.32, 1.6, 0.1));

  // ---------------------------------------------------------------- 1 · capa
  pres.addSection({ title: "Visão geral" });
  let s = pres.addSlide({ masterName: "CAPA", sectionTitle: "Visão geral" });
  s.addImage({ data: logo, x: M, y: 0.6, w: 1.05, h: 1.05, altText: "Logo da fairhealth" });
  s.addText("Programação do Instagram", { placeholder: "title" });
  s.addText("19/10 a 13/11 · 4 semanas · 12 posts · 3 por semana", { placeholder: "body" });
  s.addImage({ data: fioCapa, x: 0, y: 5.05, w: W, h: 2.1, altText: "Fio contínuo da marca, que nasce num ponto e termina num círculo" });
  s.addText("@fairhealth.br", { x: W - M - 3, y: 0.75, w: 3, h: 0.4, fontSize: 16, color: COR.verde, align: "right", margin: 0, isTextBox: true });
  s.addNotes("Programação de 12 posts em 4 semanas (3 por semana), a partir do calendário inicial de 12 posts. O post do time segue segurado.");

  // ---------------------------------------------------------------- 2 · a história em quatro blocos
  s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Visão geral" });
  s.addText("A história em quatro blocos", { placeholder: "title" });
  s.addText("Cada bloco responde a uma pergunta de quem chega ao perfil. Juntos, contam a marca do começo ao convite.", { x: M, y: 1.2, w: 11, h: 0.45, fontSize: 16, color: COR.vlogo, margin: 0, isTextBox: true });
  s.addImage({ data: fioVisao, x: 0.2, y: 3.2, w: W - 0.4, h: 1.6, altText: "Fio que liga os quatro blocos" });
  const cw = 2.86, cg = (W - 2 * M - 4 * cw) / 3;
  for (let b = 1; b <= 4; b++) {
    const B = BLOCOS[b], x = M + (b - 1) * (cw + cg), cor = COR[B.fundo], tc = TXT_SOBRE[B.fundo];
    const posts = POSTS.filter((p) => p.bloco === b);
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.9, w: cw, h: 4.8, fill: { color: cor }, line: { type: "none" }, rectRadius: 0.18, objectName: `Bloco ${b}` });
    s.addText([
      { text: `0${b}`, options: { fontSize: 14, bold: true, charSpacing: 3, breakLine: true } },
      { text: B.nome, options: { fontSize: 20, bold: true, breakLine: true } },
      { text: B.pergunta, options: { fontSize: 15, italic: true, bold: true, paraSpaceBefore: 6, breakLine: true } },
      { text: B.intuito, options: { fontSize: 14, paraSpaceBefore: 10 } },
    ], { x: x + 0.25, y: 2.1, w: cw - 0.5, h: 3.75, color: tc, valign: "top", margin: 0, isTextBox: true });
    s.addText(`${posts.length} posts · ${posts[0].data} a ${posts[posts.length - 1].data}`,
      { x: x + 0.25, y: 6.1, w: cw - 0.5, h: 0.35, fontSize: 13, bold: true, color: tc, margin: 0, isTextBox: true });
  }
  s.addNotes("Já publicados antes desta programação: 01 \"O que é a fairhealth?\" e 07 \"Conheça o Escritório do Cuidado\". O post 03 (time) segue segurado.");

  // ---------------------------------------------------------------- 3 · o mês em uma página
  s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Visão geral" });
  s.addText("O mês em uma página", { placeholder: "title" });
  const gw = 2.9, gg = (W - 2 * M - 4 * gw) / 3, gh = 1.38, gy0 = 1.85;
  for (let w = 1; w <= 4; w++) {
    const x = M + (w - 1) * (gw + gg);
    s.addText([{ text: `Semana ${w}`, options: { bold: true, fontSize: 16, breakLine: true } }, { text: SEMANAS[w], options: { fontSize: 13 } }],
      { x, y: 1.3, w: gw, h: 0.55, color: COR.verde, margin: 0, isTextBox: true });
    POSTS.filter((p) => p.sem === w).forEach((p, i) => {
      const y = gy0 + 0.1 + i * (gh + 0.13), B = BLOCOS[p.bloco], cor = COR[B.fundo], tc = TXT_SOBRE[B.fundo];
      const escuro = B.fundo === "verde";
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w: gw, h: gh, fill: { color: cor }, line: { type: "none" }, rectRadius: 0.12, objectName: `Post ${p.data}` });
      s.addText(`${p.dia.split("-")[0]} ${p.data}`, { x: x + 0.18, y: y + 0.12, w: 1.8, h: 0.3, fontSize: 12, bold: true, color: tc, margin: 0, isTextBox: true });
      s.addImage({ data: escuro ? icCreme[p.fmt] : icVerde[p.fmt], x: x + gw - 0.45, y: y + 0.13, w: 0.26, h: 0.26, altText: FORMATOS[p.fmt] });
      s.addText(p.curto, { x: x + 0.18, y: y + 0.42, w: gw - 0.36, h: 0.62, fontSize: 13, bold: true, color: tc, valign: "top", margin: 0, isTextBox: true });
      s.addText(FORMATOS[p.fmt], { x: x + 0.18, y: y + gh - 0.34, w: gw - 0.36, h: 0.26, fontSize: 11, color: tc, margin: 0, isTextBox: true });
    });
  }
  // legenda dos blocos
  let lx = M;
  for (let b = 1; b <= 4; b++) {
    const B = BLOCOS[b];
    s.addShape(pres.shapes.OVAL, { x: lx, y: 6.58, w: 0.18, h: 0.18, fill: { color: COR[B.fundo] }, line: { type: "none" } });
    s.addText(`${B.nome}`, { x: lx + 0.25, y: 6.52, w: 1.9, h: 0.3, fontSize: 12, color: COR.verde, margin: 0, isTextBox: true });
    lx += 2.2;
  }
  s.addText("Ícones: reel · carrossel · foto única", { x: W - M - 3.6, y: 6.52, w: 3.6, h: 0.3, fontSize: 12, color: COR.vlogo, align: "right", margin: 0, isTextBox: true });

  // ---------------------------------------------------------------- 4 · ritmo e formatos
  s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Visão geral" });
  s.addText("Ritmo e formatos", { placeholder: "title" });
  const stats = [["12", "posts em 4 semanas"], ["4", "reels, 2 com o Dr. Ronald"], ["7", "carrosséis"], ["1", "foto única"]];
  const sw = 2.86, sg = (W - 2 * M - 4 * sw) / 3;
  stats.forEach(([n, l], i) => {
    const x = M + i * (sw + sg), dest = i === 0;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 1.45, w: sw, h: 2.2, fill: { color: dest ? COR.tif : COR.creme }, line: { type: "none" }, rectRadius: 0.16 });
    s.addText(n, { x: x + 0.3, y: 1.6, w: sw - 0.6, h: 1.2, fontSize: 66, bold: true, color: COR.verde, margin: 0, isTextBox: true });
    s.addText(l, { x: x + 0.3, y: 2.8, w: sw - 0.6, h: 0.65, fontSize: 16, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
  });
  const linhas = [
    ["Ritmo", "3 posts por semana: segunda, quarta e sexta. Na semana de Finados (02/11), terça, quarta e sexta. 20/11 fica fora."],
    ["Mistura", "1 reel e 2 posts estáticos por semana. Nunca dois reels seguidos."],
    ["Já pronto", "Post de 21/10 (arte v2), \"Prevenção também é investimento\" (arte no Canva) e o roteiro de \"Estilo de vida também é tratamento sério\"."],
    ["Gravação", "As duas falas do Dr. Ronald (19/10 e 09/11) podem ser gravadas no mesmo dia."],
  ];
  linhas.forEach(([k, v], i) => {
    const y = 4.0 + i * 0.68;
    s.addText(k, { x: M, y, w: 1.9, h: 0.55, fontSize: 15, bold: true, color: COR.vlogo, valign: "top", margin: 0, isTextBox: true });
    s.addText(v, { x: M + 2.0, y, w: W - 2 * M - 2.0, h: 0.6, fontSize: 15, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
  });

  // ---------------------------------------------------------------- blocos e posts
  let k = 0;
  for (let b = 1; b <= 4; b++) {
    const B = BLOCOS[b], sec = `Bloco 0${b} · ${B.nome}`;
    const posts = POSTS.filter((p) => p.bloco === b);
    pres.addSection({ title: sec });
    s = pres.addSlide({ masterName: "BLOCO", sectionTitle: sec });
    s.addText(`BLOCO 0${b}`, { x: M, y: 0.85, w: 4, h: 0.4, fontSize: 16, bold: true, charSpacing: 4, color: COR.verde, margin: 0, isTextBox: true });
    s.addText(B.nome, { placeholder: "title" });
    s.addText(B.pergunta, { x: M, y: 2.55, w: 6.6, h: 0.9, fontSize: 24, italic: true, bold: true, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
    s.addText([{ text: "Intuito", options: { bold: true, fontSize: 14, charSpacing: 2, breakLine: true } }, { text: B.intuito, options: { fontSize: 17, paraSpaceBefore: 4 } }],
      { x: M, y: 3.7, w: 6.4, h: 1.6, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
    // lista dos posts do bloco
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 7.65, y: 0.85, w: W - 7.65 - M, h: 0.85 + posts.length * 0.92, fill: { color: COR.verde }, line: { type: "none" }, rectRadius: 0.18 });
    s.addText("Posts do bloco", { x: 7.95, y: 1.05, w: 4.5, h: 0.4, fontSize: 14, bold: true, charSpacing: 2, color: COR.tif, margin: 0, isTextBox: true });
    posts.forEach((p, i) => {
      const y = 1.6 + i * 0.92;
      s.addImage({ data: icCreme[p.fmt], x: 7.95, y: y + 0.06, w: 0.3, h: 0.3, altText: FORMATOS[p.fmt] });
      s.addText([{ text: `${p.dia.split("-")[0]} ${p.data} · ${FORMATOS[p.fmt]}`, options: { fontSize: 12, color: COR.tif, bold: true, breakLine: true } },
                 { text: p.curto, options: { fontSize: 15, color: COR.creme } }],
        { x: 8.4, y, w: W - 8.4 - M - 0.25, h: 0.82, valign: "top", margin: 0, isTextBox: true });
    });
    if (b === 1) s.addText("Já publicados antes: \"O que é a fairhealth?\" e \"Conheça o Escritório do Cuidado\". O post do time segue segurado.",
      { x: M, y: 5.05, w: 6.4, h: 0.6, fontSize: 13, italic: true, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
    s.addImage({ data: fioBloco, x: 0, y: 5.55, w: W, h: 1.35, altText: "Fio contínuo da marca" });

    for (const p of posts) {
      k++;
      s = pres.addSlide({ masterName: "POST", sectionTitle: sec });
      // painel tiffany
      s.addText(`BLOCO 0${b} · ${B.nome.toUpperCase()}`, { x: 0.5, y: 0.55, w: 3.7, h: 0.3, fontSize: 12, bold: true, charSpacing: 3, color: COR.verde, margin: 0, isTextBox: true });
      s.addText(`Semana ${p.sem} · ${p.dia}`, { x: 0.5, y: 1.05, w: 3.7, h: 0.35, fontSize: 16, color: COR.verde, margin: 0, isTextBox: true });
      s.addText(p.data, { x: 0.5, y: 1.4, w: 3.7, h: 1.2, fontSize: 72, bold: true, color: COR.verde, margin: 0, isTextBox: true });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.5, y: 2.85, w: 3.55, h: 0.6, fill: { color: COR.verde }, line: { type: "none" }, rectRadius: 0.3, objectName: "Formato" });
      s.addImage({ data: icCreme[p.fmt], x: 0.72, y: 2.98, w: 0.34, h: 0.34, altText: FORMATOS[p.fmt] });
      s.addText(p.fmtTxt, { x: 1.18, y: 2.85, w: 2.8, h: 0.6, fontSize: 14, bold: true, color: COR.creme, valign: "middle", margin: 0, isTextBox: true });
      s.addText([{ text: "No calendário", options: { bold: true, breakLine: true } }, { text: p.cal, options: { breakLine: true } },
                 { text: "Produção", options: { bold: true, paraSpaceBefore: 8, breakLine: true } }, { text: p.prod }],
        { x: 0.5, y: 3.7, w: 3.7, h: 1.5, fontSize: 14, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
      const marcas = POSTS.map((_, j) => j === k - 1 ? { t: j / 11, r: 20, cor: HEX.verde, borda: HEX.creme, bw: 7 } : { t: j / 11, r: 8, cor: HEX.creme });
      s.addImage({ data: await png(onda(910, 260, HEX.creme, 30, marcas, 0.3, 1.1, 0.4, 7.7)), x: 0.0, y: 5.45, w: 4.55, h: 1.3, altText: `Linha do mês: post ${k} de 12` });
      s.addText(`${k} de 12`, { x: 0.5, y: 6.85, w: 3.7, h: 0.35, fontSize: 12, bold: true, color: COR.verde, margin: 0, isTextBox: true });
      // lado branco
      s.addText(p.titulo, { placeholder: "title" });
      s.addText([{ text: "O QUE O POST MOSTRA", options: { bold: true, fontSize: 12, charSpacing: 3, color: COR.vlogo, breakLine: true } },
                 { text: p.mostra, options: { fontSize: 16, color: COR.verde, paraSpaceBefore: 6 } }],
        { x: 5.1, y: 2.15, w: W - 5.1 - M, h: 2.0, valign: "top", margin: 0, isTextBox: true });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 5.1, y: 4.3, w: W - 5.1 - M, h: 2.3, fill: { color: COR.creme }, line: { type: "none" }, rectRadius: 0.16, objectName: "Por trás do título" });
      s.addText([{ text: "O QUE ESTAMOS DIZENDO POR TRÁS DO TÍTULO", options: { bold: true, fontSize: 12, charSpacing: 3, color: COR.vlogo, breakLine: true } },
                 { text: p.porTras, options: { fontSize: 18, bold: true, color: COR.verde, paraSpaceBefore: 6 } }],
        { x: 5.4, y: 4.5, w: W - 5.1 - M - 0.6, h: 1.95, valign: "top", margin: 0, isTextBox: true });
      s.addNotes(`Fio da história: ${p.ponte}`);
    }
  }

  // ---------------------------------------------------------------- validação
  pres.addSection({ title: "Antes de publicar" });
  s = pres.addSlide({ masterName: "CONTEUDO", sectionTitle: "Antes de publicar" });
  s.addText("O que validar antes de publicar", { placeholder: "title" });
  const cab = { bold: true, fontSize: 13, color: COR.verde, fill: { color: COR.tif } };
  const val = [
    ["19/10 e 09/11 · Reels do Dr. Ronald", "Autorização de uso de imagem. Exceção à decisão de não ter o time em cena (o post do time segue segurado).", "Sócios e Dr. Ronald"],
    ["26/10 · Cuidado fora da rotina", "Conferir o número de licenças por saúde mental de 2024 no painel do Ministério da Previdência.", "Comunicação"],
    ["28/10 · Prevenção é investimento", "O que os estudos da HBR e da SHRM mediram (tipo de programa e população).", "Comunicação e responsável médica"],
    ["03/11 · A jornada da Clara", "Manter a personagem fictícia, sinalizada como história ilustrativa, ou contar sem personagem.", "Nina"],
    ["06/11 · História desde 2009", "Datas da linha do tempo. \"Validado no SUS\" fica de fora até ter fonte.", "Time fairhealth"],
    ["09/11 · Resultados reais", "Só números liberados, sem o nome da indústria atendida.", "Sócios"],
    ["11/11 · Estilo de vida", "Leitura do estudo pela responsável médica: vale para adultos com risco aumentado, não é promessa individual.", "Responsável médica"],
    ["13/11 · Como levar a fairhealth", "\"Diagnóstico\" sem \"gratuito\". Quem responde o direct.", "Comunicação"],
  ];
  const rows = [[{ text: "Post", options: cab }, { text: "O que validar", options: cab }, { text: "Quem confirma", options: cab }]]
    .concat(val.map((r, i) => r.map((t, j) => ({ text: t, options: { fontSize: 13, bold: j === 0, color: COR.verde, fill: { color: i % 2 ? COR.branco : COR.creme } } }))));
  s.addTable(rows, { x: M, y: 1.35, w: W - 2 * M, colW: [3.0, 6.7, 2.433], rowH: 0.6, valign: "middle", margin: [0.06, 0.12, 0.06, 0.12], border: { type: "none" } });

  // ---------------------------------------------------------------- próximos passos
  s = pres.addSlide({ masterName: "BLOCO", sectionTitle: "Antes de publicar" });
  s.addText("Próximos passos", { placeholder: "title" });
  const passos = [
    ["Aprovar a programação", "Datas, formatos e a decisão sobre a Clara (post de 03/11)."],
    ["Gravar com o Dr. Ronald", "Roteiro dos dois reels (19/10 e 09/11) e gravação no mesmo dia, com a autorização de imagem."],
    ["Produzir e organizar", "Levar o post de 21/10 para o Canva e passar a programação para a planilha do calendário."],
  ];
  passos.forEach(([t, d], i) => {
    const x = M + i * 4.1;
    s.addShape(pres.shapes.OVAL, { x, y: 2.75, w: 0.75, h: 0.75, fill: { color: COR.verde }, line: { type: "none" } });
    s.addText(String(i + 1), { x, y: 2.75, w: 0.75, h: 0.75, fontSize: 24, bold: true, color: COR.tif, align: "center", valign: "middle", margin: 0, isTextBox: true });
    s.addText([{ text: t, options: { bold: true, fontSize: 20, breakLine: true } }, { text: d, options: { fontSize: 15, paraSpaceBefore: 6 } }],
      { x, y: 3.7, w: 3.7, h: 1.7, color: COR.verde, valign: "top", margin: 0, isTextBox: true });
  });
  s.addImage({ data: fioBloco, x: 0, y: 5.55, w: W, h: 1.35, altText: "Fio contínuo da marca" });

  await pres.writeFile({ fileName: SAIDA });
  if (SKILL_THEME) { const { applyTheme } = require(SKILL_THEME); await applyTheme(SAIDA, THEME); }
  console.log("ok", SAIDA);
}
main().catch((e) => { console.error(e); process.exit(1); });
