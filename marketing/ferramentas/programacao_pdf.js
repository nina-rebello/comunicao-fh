// Layout da programação mensal do Instagram (capa, calendário e uma página por semana), usado por novembro e dezembro.
// Cada mês tem um config.js e um gerar_pptx.js em marketing/calendario-<mes>/.
// Uso: NODE_PATH=<pasta com pptxgenjs, react, react-dom, react-icons e sharp> node gerar_pptx.js
// Depois: soffice --headless --convert-to pdf Programacao_Instagram_<Mes>_2026.pptx
const path = require("path");
const pptxgen = require("pptxgenjs");
const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const sharp = require("sharp");
const { MdOutlineSmartDisplay, MdOutlineFilterNone, MdOutlineImage } = require("react-icons/md");

const REPO = path.resolve(__dirname, "../..");
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
const DIAS = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"];
const f2 = n => String(n).padStart(2, "0");

async function build(cfg) {
  const { POSTS, DATAS, SEMANAS, mes } = cfg; // mes: índice do mês (0 a 11)
  const mm = f2(mes + 1);

  const ICON = { reel: await icone(MdOutlineSmartDisplay), carrossel: await icone(MdOutlineFilterNone), foto: await icone(MdOutlineImage) };
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  pres.title = `Programação do Instagram · ${cfg.nomeMes} 2026`;
  pres.author = "fairhealth";
  const T = (s, txt, o) => s.addText(txt, Object.assign({ fontFace: FONT, margin: 0, isTextBox: true }, o));

  // ---------- capa ----------
  {
    const s = pres.addSlide();
    s.background = { color: K.agua };
    T(s, `PROGRAMAÇÃO DO INSTAGRAM  ·  ${cfg.periodo.toUpperCase().replace(" A ", " A ")}`, { x: 0.9, y: 0.75, w: 9, h: 0.35, fontSize: 12, bold: true, color: K.branco, charSpacing: 3 });
    T(s, [{ text: "Programação de posts", options: { breakLine: true, color: K.branco } }, { text: cfg.nomeMes.toUpperCase(), options: { color: K.escuro } }],
      { x: 0.9, y: 2.0, w: 11, h: 2.3, fontSize: 66, valign: "top" });
    T(s, [
      { text: "Nosso objetivo este mês", options: { bold: true, breakLine: true } },
      { text: cfg.objetivo },
    ], { x: 0.9, y: 4.55, w: 8.6, h: 2.0, fontSize: 16, color: K.escuro, valign: "top", paraSpaceAfter: 6 });
    s.addImage({ path: LOGO, x: 11.83, y: 6.38, w: 0.66, h: 0.66 });
  }

  // ---------- calendário ----------
  {
    const s = pres.addSlide();
    s.background = { color: K.papel };
    T(s, [{ text: "Calendário", options: { bold: true } }, { text: " de conteúdo" }], { x: 0.7, y: 0.4, w: 7.2, h: 0.9, fontSize: 40, color: K.escuro, valign: "middle" });
    T(s, `${cfg.periodo}  ·  ${cfg.sub}`, { x: 0.7, y: 1.25, w: 7.2, h: 0.4, fontSize: 18, color: K.verde });
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
    const inicio = cfg.gradeInicio;
    const f = d => `${String(d.getDate()).padStart(2, "0")}/${String(d.getMonth() + 1).padStart(2, "0")}`;
    for (let r = 0; r < cfg.semanasNaGrade; r++) {
      const seg = new Date(inicio); seg.setDate(seg.getDate() + r * 7);
      const sex = new Date(seg); sex.setDate(sex.getDate() + 4);
      T(s, [{ text: `Semana ${r + 1}`, options: { bold: true, breakLine: true } }, { text: `${f(seg)} a ${f(sex)}`, options: { fontSize: 11 } }],
        { x: 0.7, y: gy + r * rh, w: 1.25, h: rh, fontSize: 14, color: K.escuro, valign: "middle" });
      for (let c = 0; c < 7; c++) {
        const d = new Date(seg); d.setDate(d.getDate() + c);
        const fora = d.getMonth() !== mes;
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
    T(s, `${n("reel")} reels  ·  ${n("carrossel")} carrosséis  ·  ${n("foto")} ${n("foto") === 1 ? "foto única" : "fotos únicas"}  ·  feriados sem post`, { x: gx, y: 7.17, w: 9, h: 0.25, fontSize: 12, color: K.verde });
  }

  // ---------- detalhamento por semana ----------
  for (const sem of SEMANAS) {
    const s = pres.addSlide();
    s.background = { color: K.papel };
    T(s, `Semana ${sem.n}`, { x: 0.7, y: 0.75, w: 6.5, h: 1.0, fontSize: 54, color: K.escuro, valign: "middle" });
    T(s, sem.rotulo, { x: 0.7, y: 1.7, w: 6.5, h: 0.5, fontSize: 22, color: K.verde });
    s.addImage({ path: LOGO, x: 12.13, y: 6.68, w: 0.46, h: 0.46 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.7, y: 6.72, w: 1.76, h: 0.38, rectRadius: 0.19, fill: { color: K.papel }, line: { color: K.escuro, width: 1 } });
    T(s, cfg.periodo.toUpperCase(), { x: 0.7, y: 6.72, w: 1.76, h: 0.38, fontSize: 11, bold: true, color: K.escuro, align: "center", valign: "middle", charSpacing: 3 });
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
      const data = new Date(2026, mes, d);
      T(s, `${DIAS[data.getDay()]}, ${f2(d)}/${mm}`, { x: x + 0.3, y: cy + 1.05, w: cw - 0.6, h: 0.3, fontSize: 14, bold: true, color: K.escuro });
      T(s, titulo, { x: x + 0.3, y: cy + 1.38, w: cw - 0.6, h: 0.95, fontSize: 17, bold: true, color: K.escuro, valign: "top", fit: "shrink" });
      T(s, desc, { x: x + 0.3, y: cy + 2.4, w: cw - 0.6, h: 0.9, fontSize: 12, color: K.escuro, valign: "top", fit: "shrink" });
      T(s, [
        { text: TIPO[tipo] === eixo ? TIPO[tipo] : `${TIPO[tipo]}  ·  ${eixo}`, options: { bold: true, breakLine: true } },
        { text: `Chamada: ${cta}` },
      ], { x: x + 0.3, y: cy + 3.38, w: cw - 0.6, h: 0.5, fontSize: 11, color: K.verde, valign: "top" });
    });
    if (sem.n === SEMANAS.length) {
      const x = 0.7 + posts.length * (cw + gap), w = 12.63 - x;
      const largo = w > 5;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: cy, w, h: ch, rectRadius: 0.14, fill: { color: K.escuro }, line: { color: K.escuro } });
      T(s, cfg.painel.titulo, { x: x + (largo ? 0.4 : 0.3), y: cy + 0.3, w: w - 0.6, h: 0.45, fontSize: largo ? 20 : 18, bold: true, color: K.branco });
      T(s, cfg.painel.itens.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < cfg.painel.itens.length - 1 } })),
        { x: x + (largo ? 0.4 : 0.3), y: cy + 0.95, w: w - (largo ? 0.8 : 0.6), h: ch - 1.15, fontSize: largo ? 14 : 11, color: K.menta, valign: "top", paraSpaceAfter: largo ? 8 : 5 });
    }
  }
  await pres.writeFile({ fileName: cfg.out });
  console.log(cfg.out);
}
module.exports = { build };
