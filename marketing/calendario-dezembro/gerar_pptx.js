// Programação do Instagram de dezembro de 2026: capa, calendário e uma página por semana (mesmo layout de novembro).
// Uso: NODE_PATH=<pasta com pptxgenjs, react, react-dom, react-icons e sharp> node gerar_pptx.js
// Depois: soffice --headless --convert-to pdf Programacao_Instagram_Dezembro_2026.pptx
// Conteúdo dos posts: marketing/ferramentas/conteudo_posts_dezembro.py (mesma ordem e datas).
const path = require("path");
const pptxgen = require("pptxgenjs");
const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const sharp = require("sharp");
const { MdOutlineSmartDisplay, MdOutlineFilterNone, MdOutlineImage } = require("react-icons/md");

const REPO = path.resolve(__dirname, "../..");
const OUT = path.join(__dirname, "Programacao_Instagram_Dezembro_2026.pptx");
const LOGO = path.join(REPO, "instagram/marca/logo-circulo.png");

const K = { escuro: "1F3B36", verde: "2F6B64", agua: "96C3BA", menta: "C0E1DA", papel: "F0F0EA", branco: "FFFFFF", linha: "A9CFC6", apagado: "B9C4C1" };
const FONT = "Calibri";

async function icone(Comp) {
  const svg = renderToStaticMarkup(React.createElement(Comp, { size: 256, color: "#" + K.escuro }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

const FORM = { reel: "Reel", carrossel: "Carrossel", foto: "Foto única" };
const TIPO = { P: "Produto", I: "Institucional", E: "Evento" };
// d, formato, bloco, tipo, eixo, título curto (calendário), título, descrição, chamada
const POSTS = [
  [2, "carrossel", 7, "P", "Cultura", "Por que as pessoas pedem demissão?", "Por que as pessoas pedem demissão?",
    "O motivo que o RH só descobre na entrevista de desligamento e o que existe por trás dele", "Comente CUIDADO"],
  [4, "foto", 7, "P", "Produto", "Todo mundo precisa de alguém por perto", "Todo mundo precisa de alguém por perto",
    "Escuta, clareza e um plano possível, dentro da empresa", "Mande para quem cuida das pessoas"],
  [7, "carrossel", 8, "P", "Cultura", "Seu sono virou nota no relógio", "Seu sono virou nota no relógio. Por que o cansaço continua?",
    "O que o smartwatch mostra, o que ele não mostra e onde o cuidado começa", "Comente CUIDADO"],
  [9, "reel", 8, "P", "Cultura", "Acordar toda hora: você dorme, mas não descansa", "Acordar toda hora: você dorme, mas não descansa",
    "Por que oito horas na cama nem sempre são oito horas de descanso", "Mande para quem cuida do time"],
  [11, "reel", 8, "P", "Produto", "O número do dia não conta a história toda", "O número do dia não conta a história toda",
    "Bioimpedância e smartwatch: a tendência de semanas entra na consulta", "Mande para quem cuida do time"],
  [14, "carrossel", 9, "P", "Notícias", "3 sinais de esgotamento que a OMS descreve", "3 sinais de esgotamento no trabalho que a OMS descreve",
    "O cansaço constante não é fraqueza. O que o líder pode fazer e onde pedir ajuda", "Comente CUIDADO"],
  [16, "carrossel", 9, "P", "Cultura", "O que influencia a felicidade dos colaboradores?", "O que influencia a felicidade dos seus colaboradores?",
    "Sono, relações, contas e propósito: o que pesa e quem cuida de cada parte", "Comente CUIDADO"],
  [18, "reel", 9, "P", "Notícias", "A empresa acha que cuida. O time percebe?", "A empresa acha que cuida. O time percebe?",
    "A distância entre querer um empregador que cuide e sentir que a empresa cuida", "Mande para quem cuida de gente"],
  [21, "carrossel", 10, "P", "Produto", "O que o RH recebe do Escritório do Cuidado?", "O que o RH recebe do Escritório do Cuidado?",
    "Um relatório de indicadores do grupo, anonimizados, sem o nome de ninguém", "Comente CUIDADO"],
  [23, "reel", 10, "P", "Produto", "Janeiro está aí: por onde o cuidado começa", "Janeiro está aí: por onde o cuidado começa na empresa",
    "Conversa, proposta personalizada e implementação, num programa de 4 meses", "Comente CUIDADO"],
  [24, "foto", 10, "I", "Institucional", "Boas festas do time fairhealth", "Boas festas do time fairhealth",
    "Uma pausa de fim de ano para quem cuida de gente. Sem promoção", "nenhuma (post de agradecimento)"],
  [28, "reel", 11, "I", "Institucional", "O que é importante para você? O time responde", "O que é importante para você? O time responde",
    "A pergunta que abre cada atendimento, respondida por quem cuida", "Responda nos comentários"],
  [30, "carrossel", 11, "P", "Mercado", "5 perguntas para o RH levar ao planejamento de 2027", "5 perguntas para o RH levar ao planejamento de 2027",
    "Adesão, dados, prevenção, NR-01 e medição: o que perguntar antes de fechar o programa de saúde", "Comente CUIDADO"],
];
const DATAS = { 1: "Dezembro começa", 24: "Véspera de Natal", 25: "Natal (feriado)", 31: "Réveillon" };
const DIAS = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"];

const SEMANAS = [
  { n: 1, ini: 1, fim: 6, rotulo: "02 a 04/12", desc: "Causas. Por que as pessoas saem e por que todo mundo precisa de alguém por perto: o cuidado que começa pela escuta." },
  { n: 2, ini: 7, fim: 11, rotulo: "07 a 11/12", desc: "Sono e dados. O sono que não descansa, a nota do relógio e a tendência que a bioimpedância e o smartwatch mostram na consulta." },
  { n: 3, ini: 14, fim: 18, rotulo: "14 a 18/12", desc: "Esgotamento e felicidade. O que a OMS descreve, o que pesa na vida de quem trabalha e a distância entre querer e sentir cuidado." },
  { n: 4, ini: 21, fim: 25, rotulo: "21 a 24/12", desc: "Começar. O que o RH recebe, como o programa de 4 meses começa e uma pausa de fim de ano. Sexta, 25/12, é feriado." },
  { n: 5, ini: 28, fim: 31, rotulo: "28 a 30/12", desc: "Virada do ano. O time responde à pergunta que abre cada atendimento e o RH leva 5 perguntas para o planejamento de 2027." },
];

(async () => {
  const ICON = { reel: await icone(MdOutlineSmartDisplay), carrossel: await icone(MdOutlineFilterNone), foto: await icone(MdOutlineImage) };
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  pres.title = "Programação do Instagram · dezembro 2026";
  pres.author = "fairhealth";
  const T = (s, txt, o) => s.addText(txt, Object.assign({ fontFace: FONT, margin: 0, isTextBox: true }, o));

  // ---------- capa ----------
  {
    const s = pres.addSlide();
    s.background = { color: K.agua };
    T(s, "PROGRAMAÇÃO DO INSTAGRAM  ·  02/12 A 30/12", { x: 0.9, y: 0.75, w: 9, h: 0.35, fontSize: 12, bold: true, color: K.branco, charSpacing: 3 });
    T(s, [{ text: "Programação de posts", options: { breakLine: true, color: K.branco } }, { text: "DEZEMBRO", options: { color: K.escuro } }],
      { x: 0.9, y: 2.0, w: 11, h: 2.3, fontSize: 66, valign: "top" });
    T(s, [
      { text: "Nosso objetivo este mês", options: { bold: true, breakLine: true } },
      { text: "Fechar o ano mostrando o cuidado por trás dos temas que o RH já tem na cabeça: a saída de pessoas, o sono, os dados, o esgotamento e a felicidade. Cada tema leva ao Escritório do Cuidado e ao que o RH recebe, indicadores do grupo e anonimizados. Terminamos com como o programa de 4 meses começa, enquanto o RH planeja 2027." },
    ], { x: 0.9, y: 4.55, w: 8.6, h: 2.0, fontSize: 16, color: K.escuro, valign: "top", paraSpaceAfter: 6 });
    s.addImage({ path: LOGO, x: 11.83, y: 6.38, w: 0.66, h: 0.66 });
  }

  // ---------- calendário ----------
  {
    const s = pres.addSlide();
    s.background = { color: K.papel };
    T(s, [{ text: "Calendário", options: { bold: true } }, { text: " de conteúdo" }], { x: 0.7, y: 0.4, w: 7.2, h: 0.9, fontSize: 40, color: K.escuro, valign: "middle" });
    T(s, "02/12 a 30/12  ·  2 a 3 posts por semana", { x: 0.7, y: 1.25, w: 7.2, h: 0.4, fontSize: 18, color: K.verde });
    [["reel", "Reel", K.agua, K.agua], ["carrossel", "Carrossel", K.escuro, K.escuro], ["foto", "Foto única", K.branco, K.escuro]].forEach(([k, t, f, l], i) => {
      const x = 8.25 + i * 1.62;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 0.55, w: 0.5, h: 0.2, rectRadius: 0.1, fill: { color: f }, line: { color: l, width: 1 } });
      T(s, t, { x: x + 0.58, y: 0.48, w: 1.0, h: 0.34, fontSize: 12, color: K.escuro, valign: "middle" });
    });
    Object.entries(TIPO).forEach(([k, t], i) => {
      const x = 8.25 + i * 1.62;
      s.addShape(pres.shapes.OVAL, { x, y: 1.0, w: 0.24, h: 0.24, fill: { color: K.branco }, line: { color: K.escuro, width: 1 } });
      T(s, k, { x, y: 1.0, w: 0.24, h: 0.24, fontSize: 10, bold: true, color: K.escuro, align: "center", valign: "middle" });
      T(s, t, { x: x + 0.32, y: 0.95, w: 1.25, h: 0.34, fontSize: 12, color: K.escuro, valign: "middle" });
    });
    const gx = 2.0, gy = 2.12, cw = (12.63 - gx) / 7, rh = 0.98;
    ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"].forEach((d, i) => T(s, d, { x: gx + i * cw, y: 1.72, w: cw, h: 0.34, fontSize: 14, color: K.escuro, align: "center" }));
    const porDia = Object.fromEntries(POSTS.map(p => [p[0], p]));
    const inicio = new Date(2026, 10, 30);
    const f = d => `${String(d.getDate()).padStart(2, "0")}/${String(d.getMonth() + 1).padStart(2, "0")}`;
    for (let r = 0; r < 5; r++) {
      const seg = new Date(inicio); seg.setDate(seg.getDate() + r * 7);
      const sex = new Date(seg); sex.setDate(sex.getDate() + 4);
      T(s, [{ text: `Semana ${r + 1}`, options: { bold: true, breakLine: true } }, { text: `${f(seg)} a ${f(sex)}`, options: { fontSize: 11 } }],
        { x: 0.7, y: gy + r * rh, w: 1.25, h: rh, fontSize: 14, color: K.escuro, valign: "middle" });
      for (let c = 0; c < 7; c++) {
        const d = new Date(seg); d.setDate(d.getDate() + c);
        const fora = d.getMonth() !== 11;
        const x = gx + c * cw, y = gy + r * rh, dia = d.getDate();
        s.addShape(pres.shapes.RECTANGLE, { x, y, w: cw, h: rh, fill: { color: K.papel }, line: { color: K.linha, width: 0.75 } });
        T(s, String(dia).padStart(2, "0"), { x: x + 0.07, y: y + 0.04, w: 0.4, h: 0.2, fontSize: 10, color: fora ? K.apagado : K.verde });
        if (fora) continue;
        const p = porDia[dia];
        if (p) {
          const [, fmt, , tipo, , curto] = p;
          const fill = fmt === "reel" ? K.agua : fmt === "carrossel" ? K.escuro : K.branco;
          const tc = fmt === "carrossel" ? K.branco : K.escuro;
          s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.07, y: y + 0.24, w: cw - 0.14, h: rh - 0.3, rectRadius: 0.08, fill: { color: fill }, line: { color: fmt === "foto" ? K.escuro : fill, width: 1 } });
          T(s, curto, { x: x + 0.1, y: y + 0.26, w: cw - 0.42, h: rh - 0.34, fontSize: 10, bold: true, color: tc, align: "center", valign: "middle", fit: "shrink" });
          s.addShape(pres.shapes.OVAL, { x: x + cw - 0.29, y: y + 0.28, w: 0.18, h: 0.18, fill: { color: K.branco }, line: { color: K.escuro, width: 0.75 } });
          T(s, tipo, { x: x + cw - 0.29, y: y + 0.28, w: 0.18, h: 0.18, fontSize: 8, bold: true, color: K.escuro, align: "center", valign: "middle" });
        } else if (DATAS[dia]) {
          T(s, DATAS[dia], { x: x + 0.07, y: y + 0.28, w: cw - 0.14, h: 0.45, fontSize: 10, italic: true, color: K.verde, valign: "top" });
        }
      }
    }
    const n = k => POSTS.filter(p => p[1] === k).length;
    T(s, `${n("reel")} reels  ·  ${n("carrossel")} carrosséis  ·  ${n("foto")} fotos únicas  ·  feriados sem post`, { x: gx, y: 7.17, w: 9, h: 0.25, fontSize: 12, color: K.verde });
  }

  // ---------- detalhamento por semana ----------
  for (const sem of SEMANAS) {
    const s = pres.addSlide();
    s.background = { color: K.papel };
    T(s, `Semana ${sem.n}`, { x: 0.7, y: 0.75, w: 6.5, h: 1.0, fontSize: 54, color: K.escuro, valign: "middle" });
    T(s, sem.rotulo, { x: 0.7, y: 1.7, w: 6.5, h: 0.5, fontSize: 22, color: K.verde });
    s.addImage({ path: LOGO, x: 12.13, y: 6.68, w: 0.46, h: 0.46 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.7, y: 6.72, w: 1.76, h: 0.38, rectRadius: 0.19, fill: { color: K.papel }, line: { color: K.escuro, width: 1 } });
    T(s, "02/12 A 30/12", { x: 0.7, y: 6.72, w: 1.76, h: 0.38, fontSize: 11, bold: true, color: K.escuro, align: "center", valign: "middle", charSpacing: 3 });
    T(s, sem.desc, { x: 8.45, y: 0.8, w: 4.18, h: 1.2, fontSize: 14, color: K.verde, valign: "top" });
    const posts = POSTS.filter(p => p[0] >= sem.ini && p[0] <= sem.fim);
    const cw = 3.78, gap = 0.3, cy = 2.45, ch = 4.0;
    posts.forEach((p, i) => {
      const [d, fmt, bloco, tipo, eixo, , titulo, desc, cta] = p;
      const x = 0.7 + i * (cw + gap);
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: cy, w: cw, h: ch, rectRadius: 0.14, fill: { color: K.branco }, line: { color: K.branco } });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.3, y: cy + 0.3, w: 0.55, h: 0.55, rectRadius: 0.1, fill: { color: K.agua }, line: { color: K.agua } });
      s.addImage({ data: ICON[fmt], x: x + 0.4, y: cy + 0.4, w: 0.35, h: 0.35, altText: FORM[fmt] });
      T(s, `${FORM[fmt]}  ·  bloco ${bloco}`, { x: x + 1.05, y: cy + 0.3, w: cw - 1.3, h: 0.55, fontSize: 12, color: K.verde, valign: "middle" });
      const data = new Date(2026, 11, d);
      T(s, `${DIAS[data.getDay()]}, ${String(d).padStart(2, "0")}/12`, { x: x + 0.3, y: cy + 1.05, w: cw - 0.6, h: 0.3, fontSize: 14, bold: true, color: K.escuro });
      T(s, titulo, { x: x + 0.3, y: cy + 1.38, w: cw - 0.6, h: 0.95, fontSize: 17, bold: true, color: K.escuro, valign: "top", fit: "shrink" });
      T(s, desc, { x: x + 0.3, y: cy + 2.4, w: cw - 0.6, h: 0.9, fontSize: 12, color: K.escuro, valign: "top", fit: "shrink" });
      T(s, [
        { text: TIPO[tipo] === eixo ? TIPO[tipo] : `${TIPO[tipo]}  ·  ${eixo}`, options: { bold: true, breakLine: true } },
        { text: `Chamada: ${cta}` },
      ], { x: x + 0.3, y: cy + 3.38, w: cw - 0.6, h: 0.5, fontSize: 11, color: K.verde, valign: "top" });
    });
    if (sem.n === 5) {
      const x = 0.7 + 2 * (cw + gap), w = 12.63 - x;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: cy, w, h: ch, rectRadius: 0.14, fill: { color: K.escuro }, line: { color: K.escuro } });
      T(s, "Para dezembro funcionar", { x: x + 0.3, y: cy + 0.3, w: w - 0.6, h: 0.45, fontSize: 18, bold: true, color: K.branco });
      const itens = [
        "Até 02/12: pesquisa dos motivos de demissão achada e conferida",
        "Até 09/12: Dr. Ronald revisa o reel do sono e os dados do smartwatch e da bioimpedância",
        "Até 14/12: texto da OMS e da NR-01 conferidos nos originais",
        "Até 16/12: percentuais da felicidade e da lacuna com fonte",
        "Sócios liberam os dados de cliente (18/12)",
        "Até 23/12: resposta automática da palavra CUIDADO no ar",
        "Quem do time grava o reel de 28/12",
      ];
      T(s, itens.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < itens.length - 1 } })),
        { x: x + 0.3, y: cy + 0.85, w: w - 0.6, h: ch - 1.05, fontSize: 11, color: K.menta, valign: "top", paraSpaceAfter: 5 });
    }
  }
  await pres.writeFile({ fileName: OUT });
  console.log(OUT);
})();
