const path = require("path");
const pptxgen = require("pptxgenjs");
const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const sharp = require("sharp");
const { MdOutlineSmartDisplay, MdOutlineFilterNone, MdOutlineImage } = require("react-icons/md");
const { applyTheme } = require(process.env.SKILL + "/scripts/apply_theme.js");

const REPO = "/home/user/Comunica-o-FH";
const OUT = path.join(REPO, "marketing/calendario-novembro/Programacao_Instagram_Novembro_2026.pptx");
const LOGO = path.join(REPO, "instagram/marca/logo-circulo.png");

const THEME = {
  name: "fairhealth",
  headFontFace: "Calibri",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "1F3B36", lt1: "FFFFFF", dk2: "2F6B64", lt2: "F0F0EA",
    accent1: "96C3BA", accent2: "C0E1DA", accent3: "1F3B36", accent4: "2F6B64",
    accent5: "F0F0EA", accent6: "BFE0D9", hlink: "2F6B64", folHlink: "2F6B64",
  },
};
// hex usado só onde a biblioteca exige hex
const HEX = { escuro: "1F3B36", verde: "2F6B64", agua: "96C3BA", menta: "C0E1DA", papel: "F0F0EA", linha: "A9CFC6", apagado: "B9C4C1" };

async function icone(Comp) {
  const svg = renderToStaticMarkup(React.createElement(Comp, { size: 256, color: "#" + HEX.escuro }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

// ---------- conteúdo ----------
const FORM = { reel: "Reel", carrossel: "Carrossel", foto: "Foto única" };
const TIPO = { P: "Produto", I: "Institucional", E: "Evento" };
// d, formato, bloco, tipo, eixo, título curto (calendário), título, descrição, chamada
const POSTS = [
  [3, "carrossel", 3, "P", "Produto", "Como funciona o cuidado na prática?", "Como funciona o cuidado na prática?",
    "A jornada entre escuta, atendimento, plano individualizado e acompanhamento", "a definir"],
  [4, "reel", 3, "P", "Produto", "Quatro frentes, um cuidado conectado", "Quatro frentes, um cuidado conectado",
    "Medicina do Estilo de Vida, Escritório do Cuidado, plataforma e wearables", "a definir"],
  [6, "carrossel", 4, "I", "Cases", "Uma história de cuidado desde 2009", "Uma história de cuidado que começou em 2009",
    "Linha do tempo da metodologia e evolução até a FairHealth (validar com o Dr. Ronald)", "a definir"],
  [9, "reel", 4, "P", "Cases", "Cuidado na prática: resultados reais", "Cuidado na prática: experiências e resultados reais",
    "Evidências e resultados documentados, contados pelo Dr. Ronald", "a definir"],
  [11, "carrossel", 4, "P", "Cultura", "Estilo de vida também é tratamento sério", "Estilo de vida também é tratamento sério",
    "O que a ciência mostra sobre mudar a rotina, na semana do Dia Mundial do Diabetes", "a definir"],
  [13, "carrossel", 4, "P", "Produto", "Como levar a FairHealth para sua empresa?", "Como levar a FairHealth para sua empresa?",
    "Encerramento da apresentação inicial com orientação para o RH", "Comente CUIDADO (comercial)"],
  [16, "reel", 5, "E", "Cultura", "Novembro Azul: ele só vai ao médico quando dói", "Ele só vai ao médico quando dói",
    "Novembro Azul: o homem não deixa de se cuidar por descuido, e sim porque cuidar dá trabalho. Com o cuidado dentro da empresa, a barreira cai o ano todo",
    "Comente CUIDADO"],
  [18, "carrossel", 5, "P", "Notícias", "Afastamentos por saúde mental e a NR-01", "Recorde de afastamentos por saúde mental: o que a NR-01 cobra do RH",
    "546,2 mil licenças em 2025 e a gestão de riscos psicossociais além da planilha", "Comente CUIDADO e receba o guia de NR-01"],
  [19, "foto", 5, "P", "Cases", "Depoimento: “Os meus hábitos mudaram”", "“Os meus hábitos mudaram, e não foi um sacrifício.”",
    "A voz de quem é cuidado: mudança real, sem promessa de resultado clínico. Entra na quinta porque sexta é feriado", "nenhuma (post de prova)"],
  [23, "reel", 5, "P", "Notícias", "O RH cuida de todo mundo. Quem cuida do RH?", "O RH cuida de todo mundo. Quem cuida do RH?",
    "Dados do Panorama da Saúde Emocional do RH 2026 e o cuidado que chega também a quem cuida", "Mande para alguém do RH"],
  [25, "carrossel", 5, "P", "Cultura", "Por que a Geração Z está tão desconectada do trabalho?", "Por que a Geração Z está tão desconectada do trabalho?",
    "Não é preguiça nem falta de compromisso. A resposta começa com a pergunta que quase ninguém faz: o que importa para você?",
    "Comente CUIDADO"],
  [27, "carrossel", 6, "P", "Cases", "Case Chemitec: 98% de adesão", "Como 98% do time aceitou ser cuidado",
    "Case Chemitec: 161 atendimentos e 81,3% de retorno. Convite ao diagnóstico antes do orçamento de 2027", "Comente CUIDADO (diagnóstico gratuito)"],
  [30, "reel", 6, "E", "Cultura", "Dezembro chegou: a corrida das metas também adoece", "Dezembro chegou: a corrida das metas também adoece",
    "Uma prática de 1 minuto para o fim de ano e o convite para cuidar antes de 2027", "Comente CUIDADO"],
];
const DATAS = { 1: "Início do Novembro Azul", 2: "Finados", 14: "Dia Mundial do Diabetes", 15: "Proclamação da República", 20: "Consciência Negra (feriado)" };
const DIAS = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"];

const SEMANAS = [
  { n: 3, ini: 2, fim: 6, rotulo: "03 a 06/11", desc: "Compreensão e começo da confiança. O cuidado na prática, as quatro frentes conectadas e a trajetória do método." },
  { n: 4, ini: 9, fim: 13, rotulo: "09 a 13/11", desc: "Confiança. Resultados reais, a ciência por trás do cuidado e o convite para o RH." },
  { n: 5, ini: 16, fim: 20, rotulo: "16 a 19/11", desc: "Atualidade. Novembro Azul, NR-01 e a voz de quem é cuidado: temas do momento que levam ao Escritório do Cuidado. Sexta, 20/11, é feriado." },
  { n: 6, ini: 23, fim: 27, rotulo: "23 a 27/11", desc: "Atualidade e decisão. Quem cuida do RH, a desconexão dos jovens e a prova da Chemitec, com o convite ao diagnóstico." },
  { n: 7, ini: 30, fim: 30, rotulo: "30/11", desc: "Decisão e passagem para dezembro, com o RH fechando o orçamento de 2027." },
];

(async () => {
  const ICON = { reel: await icone(MdOutlineSmartDisplay), carrossel: await icone(MdOutlineFilterNone), foto: await icone(MdOutlineImage) };

  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = "Programação do Instagram · novembro 2026";
  pres.author = "FairHealth";
  const C = pres.SchemeColor;

  pres.defineSlideMaster({
    title: "OBJETIVO",
    background: { color: C.background2 },
  });
  pres.defineSlideMaster({
    title: "CALENDARIO",
    background: { color: C.background2 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.7, y: 0.4, w: 7.2, h: 0.9, fontSize: 40, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "body", type: "body", x: 0.7, y: 1.25, w: 7.2, h: 0.4, fontSize: 18, color: C.text2, align: "left", margin: 0 }, text: "" } },
    ],
  });
  pres.defineSlideMaster({
    title: "SEMANA",
    background: { color: C.background2 },
    objects: [
      { placeholder: { options: { name: "title", type: "title", x: 0.7, y: 0.75, w: 6.5, h: 1.0, fontSize: 54, color: C.text1, valign: "middle", align: "left", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "body", type: "body", x: 0.7, y: 1.7, w: 6.5, h: 0.5, fontSize: 22, color: C.text2, align: "left", margin: 0 }, text: "" } },
      { image: { path: LOGO, x: 12.13, y: 6.68, w: 0.46, h: 0.46 } },
    ],
  });

  // ---------- 1 · objetivo do mês ----------
  pres.addSection({ title: "Objetivo do mês" });
  {
    const s = pres.addSlide({ masterName: "OBJETIVO", sectionTitle: "Objetivo do mês" });
    s.background = { color: C.text1 };
    s.addText("PROGRAMAÇÃO DO INSTAGRAM  ·  01/11 A 30/11", { x: 0.9, y: 0.75, w: 8, h: 0.35, fontSize: 12, bold: true, color: C.accent2, charSpacing: 3, margin: 0, isTextBox: true });
    s.addText([
      { text: "Programação de posts", options: { breakLine: true } },
      { text: "novembro", options: { color: C.accent1 } },
    ], { x: 0.9, y: 2.0, w: 11, h: 2.3, fontSize: 66, color: C.background1, margin: 0, valign: "top", isTextBox: true, objectName: "titulo-mes" });
    s.addText([
      { text: "Nosso objetivo este mês", options: { bold: true, color: C.background1, breakLine: true } },
      { text: "Fechar a apresentação da FairHealth e abrir a conversa com o RH. Primeiro, mostramos o cuidado na prática e as provas de que ele funciona. Depois, usamos temas do momento (Novembro Azul, NR-01, saúde do RH, Geração Z) para mostrar que entendemos o que as empresas estão vivendo e terminamos com o convite ao diagnóstico, enquanto o RH fecha o orçamento de 2027." },
    ], { x: 0.9, y: 4.55, w: 8.6, h: 2.0, fontSize: 16, color: C.accent2, margin: 0, valign: "top", paraSpaceAfter: 6, isTextBox: true, objectName: "objetivo" });
    s.addImage({ path: LOGO, x: 11.83, y: 6.38, w: 0.66, h: 0.66 });
  }

  // ---------- 2 · calendário ----------
  pres.addSection({ title: "Calendário" });
  {
    const s = pres.addSlide({ masterName: "CALENDARIO", sectionTitle: "Calendário" });
    s.addText([{ text: "Calendário", options: { bold: true } }, { text: " de conteúdo" }], { placeholder: "title" });
    s.addText("01/11 a 30/11  ·  3 posts por semana", { placeholder: "body" });
    // legendas
    const leg = [["reel", "Reel", C.accent1, C.accent1], ["carrossel", "Carrossel", C.text1, C.text1], ["foto", "Foto única", C.background1, C.text1]];
    leg.forEach(([k, t, f, l], i) => {
      const x = 8.25 + i * 1.62;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 0.55, w: 0.5, h: 0.2, rectRadius: 0.1, fill: { color: f }, line: { color: l, width: 1 }, objectName: `legenda-${k}` });
      s.addText(t, { x: x + 0.58, y: 0.48, w: 1.0, h: 0.34, fontSize: 12, color: C.text1, margin: 0, valign: "middle", isTextBox: true });
    });
    Object.entries(TIPO).forEach(([k, t], i) => {
      const x = 8.25 + i * 1.62;
      s.addShape(pres.shapes.OVAL, { x, y: 1.0, w: 0.24, h: 0.24, fill: { color: C.background1 }, line: { color: C.text1, width: 1 }, objectName: `legenda-tipo-${k}` });
      s.addText(k, { x, y: 1.0, w: 0.24, h: 0.24, fontSize: 10, bold: true, color: C.text1, align: "center", valign: "middle", margin: 0, isTextBox: true });
      s.addText(t, { x: x + 0.32, y: 0.95, w: 1.25, h: 0.34, fontSize: 12, color: C.text1, margin: 0, valign: "middle", isTextBox: true });
    });

    const gx = 2.0, gy = 2.12, cw = (12.63 - gx) / 7, rh = 0.98;
    ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"].forEach((d, i) =>
      s.addText(d, { x: gx + i * cw, y: 1.72, w: cw, h: 0.34, fontSize: 14, color: C.text1, align: "center", margin: 0, isTextBox: true }));
    const porDia = Object.fromEntries(POSTS.map(p => [p[0], p]));
    const inicio = new Date(2026, 10, 2);
    for (let r = 0; r < 5; r++) {
      const seg = new Date(inicio); seg.setDate(seg.getDate() + r * 7);
      const sex = new Date(seg); sex.setDate(sex.getDate() + 4);
      const f = d => `${String(d.getDate()).padStart(2, "0")}/${String(d.getMonth() + 1).padStart(2, "0")}`;
      s.addText([{ text: `Semana ${r + 3}`, options: { bold: true, breakLine: true } }, { text: `${f(seg)} a ${f(sex)}`, options: { fontSize: 11 } }],
        { x: 0.7, y: gy + r * rh, w: 1.25, h: rh, fontSize: 14, color: C.text1, valign: "middle", margin: 0, isTextBox: true });
      for (let c = 0; c < 7; c++) {
        const d = new Date(seg); d.setDate(d.getDate() + c);
        const fora = d.getMonth() !== 10;
        const x = gx + c * cw, y = gy + r * rh, dia = d.getDate();
        s.addShape(pres.shapes.RECTANGLE, { x, y, w: cw, h: rh, fill: { color: C.background2 }, line: { color: HEX.linha, width: 0.75 }, objectName: `celula-${f(d)}` });
        s.addText(String(dia).padStart(2, "0"), { x: x + 0.07, y: y + 0.04, w: 0.4, h: 0.2, fontSize: 10, color: fora ? HEX.apagado : C.text2, margin: 0, isTextBox: true });
        if (fora) continue;
        const p = porDia[dia];
        if (p) {
          const [, fmt, , tipo, , curto] = p;
          const fill = fmt === "reel" ? C.accent1 : fmt === "carrossel" ? C.text1 : C.background1;
          const tc = fmt === "carrossel" ? C.background1 : C.text1;
          s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.07, y: y + 0.24, w: cw - 0.14, h: rh - 0.3, rectRadius: 0.08, fill: { color: fill }, line: { color: fmt === "foto" ? C.text1 : fill, width: 1 }, objectName: `post-${dia}` });
          s.addText(curto, { x: x + 0.1, y: y + 0.26, w: cw - 0.42, h: rh - 0.34, fontSize: 11, bold: true, color: tc, align: "center", valign: "middle", margin: 0, fit: "shrink", isTextBox: true });
          s.addShape(pres.shapes.OVAL, { x: x + cw - 0.29, y: y + 0.28, w: 0.18, h: 0.18, fill: { color: C.background1 }, line: { color: C.text1, width: 0.75 }, objectName: `tipo-${dia}` });
          s.addText(tipo, { x: x + cw - 0.29, y: y + 0.28, w: 0.18, h: 0.18, fontSize: 8, bold: true, color: C.text1, align: "center", valign: "middle", margin: 0, isTextBox: true });
        } else if (DATAS[dia]) {
          s.addText(DATAS[dia], { x: x + 0.07, y: y + 0.28, w: cw - 0.14, h: 0.45, fontSize: 10, italic: true, color: C.text2, margin: 0, valign: "top", isTextBox: true });
        }
      }
    }
    const n = k => POSTS.filter(p => p[1] === k).length;
    s.addText(`${n("reel")} reels  ·  ${n("carrossel")} carrosséis  ·  ${n("foto")} foto única  ·  1 reel e 2 posts estáticos por semana  ·  feriados sem post`,
      { x: gx, y: 7.17, w: 9, h: 0.25, fontSize: 12, color: C.text2, margin: 0, isTextBox: true });
  }

  // ---------- 3+ · detalhamento por semana ----------
  pres.addSection({ title: "Detalhamento" });
  for (const sem of SEMANAS) {
    const s = pres.addSlide({ masterName: "SEMANA", sectionTitle: "Detalhamento" });
    s.addText(`Semana ${sem.n}`, { placeholder: "title" });
    s.addText(sem.rotulo, { placeholder: "body" });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.7, y: 6.72, w: 1.76, h: 0.38, rectRadius: 0.19, fill: { color: C.background2 }, line: { color: C.text1, width: 1 }, objectName: "periodo" });
    s.addText("01/11 A 30/11", { x: 0.7, y: 6.72, w: 1.76, h: 0.38, fontSize: 11, bold: true, color: C.text1, align: "center", valign: "middle", charSpacing: 3, margin: 0, isTextBox: true });
    s.addText(sem.desc, { x: 8.45, y: 0.8, w: 4.18, h: 1.0, fontSize: 14, color: C.text2, margin: 0, valign: "top", isTextBox: true });
    const posts = POSTS.filter(p => p[0] >= sem.ini && p[0] <= sem.fim);
    const cw = 3.78, gap = 0.3, cy = 2.45, ch = 4.0;
    posts.forEach((p, i) => {
      const [d, fmt, bloco, tipo, eixo, , titulo, desc, cta] = p;
      const x = 0.7 + i * (cw + gap);
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: cy, w: cw, h: ch, rectRadius: 0.14, fill: { color: C.background1 }, line: { color: C.background1 }, objectName: `cartao-${d}` });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.3, y: cy + 0.3, w: 0.55, h: 0.55, rectRadius: 0.1, fill: { color: C.accent1 }, line: { color: C.accent1 }, objectName: `icone-fundo-${d}` });
      s.addImage({ data: ICON[fmt], x: x + 0.4, y: cy + 0.4, w: 0.35, h: 0.35, altText: FORM[fmt] });
      s.addText(`${FORM[fmt]}  ·  bloco ${bloco}`, { x: x + 1.05, y: cy + 0.3, w: cw - 1.3, h: 0.55, fontSize: 12, color: C.text2, valign: "middle", margin: 0, isTextBox: true });
      const data = new Date(2026, 10, d);
      s.addText(`${DIAS[data.getDay()]}, ${String(d).padStart(2, "0")}/11`, { x: x + 0.3, y: cy + 1.05, w: cw - 0.6, h: 0.3, fontSize: 14, bold: true, color: C.text1, margin: 0, isTextBox: true });
      s.addText(titulo, { x: x + 0.3, y: cy + 1.38, w: cw - 0.6, h: 0.95, fontSize: 17, bold: true, color: C.text1, margin: 0, valign: "top", fit: "shrink", isTextBox: true });
      s.addText(desc, { x: x + 0.3, y: cy + 2.4, w: cw - 0.6, h: 0.9, fontSize: 12, color: C.text1, margin: 0, valign: "top", fit: "shrink", isTextBox: true });
      s.addText([
        { text: TIPO[tipo] === eixo ? TIPO[tipo] : `${TIPO[tipo]}  ·  ${eixo}`, options: { bold: true, breakLine: true } },
        { text: `Chamada: ${cta}` },
      ], { x: x + 0.3, y: cy + 3.38, w: cw - 0.6, h: 0.5, fontSize: 11, color: C.text2, margin: 0, valign: "top", isTextBox: true });
    });
    if (sem.n === 7) {
      const x = 0.7 + cw + gap, w = 12.63 - x;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: cy, w, h: ch, rectRadius: 0.14, fill: { color: C.text1 }, line: { color: C.text1 }, objectName: "pendencias" });
      s.addText("Para novembro funcionar", { x: x + 0.4, y: cy + 0.35, w: w - 0.8, h: 0.45, fontSize: 20, bold: true, color: C.background1, margin: 0, isTextBox: true });
      const itens = [
        "Até 13/11: guia de NR-01 pronto e validado pelo Dr. Ronald",
        "Até 13/11: resposta automática da palavra CUIDADO e página do diagnóstico no ar",
        "Até 06/11: Chemitec autoriza o uso do nome (e, se topar, post em coautoria)",
        "Revisão técnica dos posts de Novembro Azul, NR-01 e saúde mental",
        "Conferir na fonte original os dados do INSS, da Flash e da pesquisa sobre homens e saúde",
        "Definir quem do comercial responde os contatos em até 24 h",
      ];
      s.addText(itens.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < itens.length - 1 } })),
        { x: x + 0.4, y: cy + 0.95, w: w - 0.8, h: ch - 1.25, fontSize: 14, color: C.accent2, margin: 0, valign: "top", paraSpaceAfter: 8, isTextBox: true });
    }
  }

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log(OUT);
})();
