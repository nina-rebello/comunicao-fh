// Layout da programação mensal do Instagram e do LinkedIn (capa, calendário único e uma página por semana), usado por novembro e dezembro.
// Cada mês tem um config.js e um gerar_pptx.js em marketing/calendario-<mes>/.
// Uso: NODE_PATH=<pasta com pptxgenjs, react, react-dom, react-icons e sharp> node gerar_pptx.js
// Depois: soffice --headless --convert-to pdf Programacao_Instagram_LinkedIn_<Mes>_2026.pptx
// O config.js de cada mês traz POSTS (Instagram) e LINKEDIN: [dia, formato, bloco, eixo, título curto, título, descrição, chamada].
const path = require("path");
const pptxgen = require("pptxgenjs");
const React = require("react");
const { renderToStaticMarkup } = require("react-dom/server");
const sharp = require("sharp");
const { MdOutlineSmartDisplay, MdOutlineFilterNone, MdOutlineImage } = require("react-icons/md");
const { FaLinkedinIn } = require("react-icons/fa");

const REPO = path.resolve(__dirname, "../..");
const LOGO = path.join(REPO, "instagram/marca/logo-circulo.png");

const K = { escuro: "1F3B36", verde: "2F6B64", agua: "96C3BA", menta: "C0E1DA", papel: "F0F0EA", branco: "FFFFFF", linha: "A9CFC6", apagado: "B9C4C1" };
const FONT = "Calibri";

async function icone(Comp, cor = K.escuro) {
  const svg = renderToStaticMarkup(React.createElement(Comp, { size: 256, color: "#" + cor }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

const FORM = { reel: "Reel", carrossel: "Carrossel", foto: "Foto única" };
const FORM_LI = { texto: "Texto", imagem: "Imagem + texto", documento: "Documento PDF" };
const TIPO = { P: "Produto", I: "Institucional", E: "Evento" };
const DIAS = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"];
const f2 = n => String(n).padStart(2, "0");

async function build(cfg) {
  const { POSTS, DATAS, SEMANAS, mes } = cfg; // mes: índice do mês (0 a 11)
  const LI = cfg.LINKEDIN || [];
  const mm = f2(mes + 1);

  const ICON = { reel: await icone(MdOutlineSmartDisplay), carrossel: await icone(MdOutlineFilterNone), foto: await icone(MdOutlineImage) };
  const ICON_LI = await icone(FaLinkedinIn, K.branco);
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };
  pres.title = `Programação do Instagram e do LinkedIn · ${cfg.nomeMes} 2026`;
  pres.author = "fairhealth";
  const T = (s, txt, o) => s.addText(txt, Object.assign({ fontFace: FONT, margin: 0, isTextBox: true }, o));

  // ---------- capa ----------
  {
    const s = pres.addSlide();
    s.background = { color: K.agua };
    T(s, `PROGRAMAÇÃO DO INSTAGRAM E DO LINKEDIN  ·  ${cfg.periodo.toUpperCase()}`, { x: 0.9, y: 0.75, w: 11, h: 0.35, fontSize: 12, bold: true, color: K.branco, charSpacing: 3 });
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
    T(s, [{ text: "Calendário", options: { bold: true } }, { text: " de conteúdo" }], { x: 0.7, y: 0.3, w: 6.6, h: 0.8, fontSize: 40, color: K.escuro, valign: "middle" });
    T(s, `${cfg.periodo}  ·  ${cfg.sub}`, { x: 0.7, y: 1.0, w: 6.8, h: 0.4, fontSize: 16, color: K.verde });
    [["reel", "Reel", K.agua, K.agua], ["carrossel", "Carrossel", K.escuro, K.escuro], ["foto", "Foto única", K.branco, K.escuro], ["li", "LinkedIn", K.menta, K.verde]].forEach(([k, t, f, l], i) => {
      const x = 7.55 + i * 1.3;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 0.55, w: 0.45, h: 0.2, rectRadius: 0.1, fill: { color: f }, line: { color: l, width: 1 } });
      T(s, t, { x: x + 0.52, y: 0.48, w: 0.8, h: 0.34, fontSize: 12, color: K.escuro, valign: "middle" });
    });
    Object.entries(TIPO).forEach(([k, t], i) => {
      const x = 7.55 + i * 1.3;
      s.addShape(pres.shapes.OVAL, { x, y: 1.0, w: 0.24, h: 0.24, fill: { color: K.branco }, line: { color: K.escuro, width: 1 } });
      T(s, k, { x, y: 1.0, w: 0.24, h: 0.24, fontSize: 10, bold: true, color: K.escuro, align: "center", valign: "middle" });
      T(s, t, { x: x + 0.32, y: 0.95, w: 1.0, h: 0.34, fontSize: 12, color: K.escuro, valign: "middle" });
    });
    const gx = 2.0, gy = 1.84, cw = (12.63 - gx) / 7, rh = 1.05;
    ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"].forEach((d, i) => T(s, d, { x: gx + i * cw, y: 1.5, w: cw, h: 0.3, fontSize: 14, color: K.escuro, align: "center" }));
    const porDia = Object.fromEntries(POSTS.map(p => [p[0], p]));
    const liDia = Object.fromEntries(LI.map(p => [p[0], p]));
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
        const p = porDia[dia], l = liDia[dia];
        if (p) {
          const [, fmt, , tipo, , curto] = p;
          const fill = fmt === "reel" ? K.agua : fmt === "carrossel" ? K.escuro : K.branco;
          const tc = fmt === "carrossel" ? K.branco : K.escuro;
          const bh = l ? 0.47 : 0.78;
          s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.07, y: y + 0.22, w: cw - 0.14, h: bh, rectRadius: 0.08, fill: { color: fill }, line: { color: fmt === "foto" ? K.escuro : fill, width: 1 } });
          T(s, curto, { x: x + 0.1, y: y + 0.23, w: cw - 0.42, h: bh - 0.02, fontSize: l ? 9 : 10, bold: true, color: tc, align: "center", valign: "middle", fit: "shrink" });
          s.addShape(pres.shapes.OVAL, { x: x + cw - 0.29, y: y + 0.26, w: 0.18, h: 0.18, fill: { color: K.branco }, line: { color: K.escuro, width: 0.75 } });
          T(s, tipo, { x: x + cw - 0.29, y: y + 0.26, w: 0.18, h: 0.18, fontSize: 8, bold: true, color: K.escuro, align: "center", valign: "middle" });
        } else if (DATAS[dia] && !l) {
          T(s, DATAS[dia], { x: x + 0.07, y: y + 0.28, w: cw - 0.14, h: 0.45, fontSize: 10, italic: true, color: K.verde, valign: "top" });
        }
        if (l) {
          const ly = p ? y + 0.72 : y + 0.22, lh = p ? 0.29 : 0.78;
          s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + 0.07, y: ly, w: cw - 0.14, h: lh, rectRadius: 0.08, fill: { color: K.menta }, line: { color: K.verde, width: 1 } });
          s.addShape(pres.shapes.OVAL, { x: x + 0.1, y: ly + (lh - 0.18) / 2, w: 0.18, h: 0.18, fill: { color: K.verde }, line: { color: K.verde, width: 0.5 } });
          s.addImage({ data: ICON_LI, x: x + 0.135, y: ly + (lh - 0.18) / 2 + 0.035, w: 0.11, h: 0.11, altText: "LinkedIn" });
          T(s, l[4], { x: x + 0.31, y: ly + 0.01, w: cw - 0.42, h: lh - 0.02, fontSize: p ? 8 : 10, bold: true, color: K.escuro, align: "left", valign: "middle", fit: "shrink" });
        }
      }
    }
    const n = k => POSTS.filter(p => p[1] === k).length;
    T(s, `${n("reel")} reels  ·  ${n("carrossel")} carrosséis  ·  ${n("foto")} ${n("foto") === 1 ? "foto única" : "fotos únicas"}  ·  ${LI.length} ${LI.length === 1 ? "post" : "posts"} no LinkedIn  ·  feriados sem post`, { x: gx, y: 7.15, w: 10.6, h: 0.25, fontSize: 12, color: K.verde });
  }

  // ---------- detalhamento por semana ----------
  const painel = (s, x, y, w, h, largo) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, rectRadius: 0.14, fill: { color: K.escuro }, line: { color: K.escuro } });
    T(s, cfg.painel.titulo, { x: x + (largo ? 0.4 : 0.3), y: y + 0.3, w: w - 0.6, h: 0.45, fontSize: largo ? 20 : 18, bold: true, color: K.branco });
    T(s, cfg.painel.itens.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < cfg.painel.itens.length - 1 } })),
      { x: x + (largo ? 0.4 : 0.3), y: y + 0.95, w: w - (largo ? 0.8 : 0.6), h: h - 1.15, fontSize: largo ? 14 : 11, color: K.menta, valign: "top", paraSpaceAfter: largo ? 8 : 5 });
  };
  for (const sem of SEMANAS) {
    const s = pres.addSlide();
    s.background = { color: K.papel };
    T(s, `Semana ${sem.n}`, { x: 0.7, y: 0.75, w: 6.5, h: 1.0, fontSize: 54, color: K.escuro, valign: "middle" });
    T(s, sem.rotulo, { x: 0.7, y: 1.7, w: 6.5, h: 0.5, fontSize: 22, color: K.verde });
    s.addImage({ path: LOGO, x: 12.13, y: 6.68, w: 0.46, h: 0.46 });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.7, y: 6.72, w: 1.76, h: 0.38, rectRadius: 0.19, fill: { color: K.papel }, line: { color: K.escuro, width: 1 } });
    T(s, cfg.periodo.toUpperCase(), { x: 0.7, y: 6.72, w: 1.76, h: 0.38, fontSize: 11, bold: true, color: K.escuro, align: "center", valign: "middle", charSpacing: 3 });
    T(s, sem.desc, { x: 8.45, y: 0.8, w: 4.18, h: 1.2, fontSize: 14, color: K.verde, valign: "top" });
    const cards = [];
    POSTS.filter(p => p[0] >= sem.ini && p[0] <= sem.fim).forEach(p => cards.push({ canal: "ig", dia: p[0], p }));
    LI.filter(p => p[0] >= sem.ini && p[0] <= sem.fim).forEach(p => cards.push({ canal: "li", dia: p[0], p }));
    cards.sort((a, b) => a.dia - b.dia || (a.canal === "ig" ? -1 : 1));
    const ultima = sem.n === SEMANAS.length;
    const estreito = cards.length >= 4;
    const cw = estreito ? 2.8 : 3.78, gap = estreito ? 0.2 : 0.3, cy = 2.45, ch = 4.0;
    const pad = estreito ? 0.22 : 0.3, ib = estreito ? 0.48 : 0.55;
    cards.forEach((c, i) => {
      const x = 0.7 + i * (cw + gap), li = c.canal === "li";
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: cy, w: cw, h: ch, rectRadius: 0.14, fill: { color: li ? "E9F3F0" : K.branco }, line: { color: li ? K.agua : K.branco, width: li ? 1.5 : 0.5 } });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: x + pad, y: cy + pad, w: ib, h: ib, rectRadius: 0.1, fill: { color: li ? K.verde : K.agua }, line: { color: li ? K.verde : K.agua } });
      let rotulo, titulo, desc, cta, eixoTxt;
      if (li) {
        const [d, fmt, bloco, eixo, , tit, ds, ct] = c.p;
        s.addImage({ data: ICON_LI, x: x + pad + ib * 0.25, y: cy + pad + ib * 0.25, w: ib * 0.5, h: ib * 0.5, altText: "LinkedIn" });
        rotulo = `LinkedIn  ·  ${FORM_LI[fmt]}`; titulo = tit; desc = ds; cta = ct; eixoTxt = `${bloco}  ·  ${eixo}`;
      } else {
        const [d, fmt, bloco, tipo, eixo, , tit, ds, ct] = c.p;
        s.addImage({ data: ICON[fmt], x: x + pad + ib * 0.18, y: cy + pad + ib * 0.18, w: ib * 0.64, h: ib * 0.64, altText: FORM[fmt] });
        rotulo = `Instagram  ·  ${FORM[fmt]}  ·  bloco ${bloco}`; titulo = tit; desc = ds; cta = `Chamada: ${ct}`; eixoTxt = TIPO[tipo] === eixo ? TIPO[tipo] : `${TIPO[tipo]}  ·  ${eixo}`;
      }
      T(s, rotulo, { x: x + pad + ib + 0.15, y: cy + pad, w: cw - pad * 2 - ib - 0.15, h: ib, fontSize: estreito ? 10.5 : 12, color: K.verde, valign: "middle", fit: "shrink" });
      const data = new Date(2026, mes, c.dia);
      T(s, `${DIAS[data.getDay()]}, ${f2(c.dia)}/${mm}`, { x: x + pad, y: cy + 1.05, w: cw - pad * 2, h: 0.3, fontSize: estreito ? 13 : 14, bold: true, color: K.escuro });
      T(s, titulo, { x: x + pad, y: cy + 1.38, w: cw - pad * 2, h: 1.0, fontSize: estreito ? 14 : 17, bold: true, color: K.escuro, valign: "top", fit: "shrink" });
      T(s, desc, { x: x + pad, y: cy + 2.42, w: cw - pad * 2, h: 0.9, fontSize: estreito ? 10.5 : 12, color: K.escuro, valign: "top", fit: "shrink" });
      T(s, [{ text: eixoTxt, options: { bold: true, breakLine: true } }, { text: cta }],
        { x: x + pad, y: cy + 3.35, w: cw - pad * 2, h: 0.55, fontSize: estreito ? 10 : 11, color: K.verde, valign: "top", fit: "shrink" });
    });
    if (ultima && cards.length <= 2) painel(s, 0.7 + cards.length * (cw + gap), cy, 12.63 - (0.7 + cards.length * (cw + gap)), ch, true);
    if (ultima && cards.length > 2) {
      const s2 = pres.addSlide();
      s2.background = { color: K.papel };
      T(s2, cfg.painel.titulo, { x: 0.7, y: 0.75, w: 9, h: 1.0, fontSize: 44, color: K.escuro, valign: "middle" });
      T(s2, cfg.periodo, { x: 0.7, y: 1.7, w: 6.5, h: 0.5, fontSize: 22, color: K.verde });
      s2.addImage({ path: LOGO, x: 12.13, y: 6.68, w: 0.46, h: 0.46 });
      const itens = cfg.painel.itens, meio = Math.ceil(itens.length / 2);
      [itens.slice(0, meio), itens.slice(meio)].forEach((col, k) => {
        const x = 0.7 + k * 6.05, w = 5.88;
        s2.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.45, w, h: 3.95, rectRadius: 0.14, fill: { color: K.escuro }, line: { color: K.escuro } });
        T(s2, col.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < col.length - 1 } })),
          { x: x + 0.35, y: 2.75, w: w - 0.7, h: 3.4, fontSize: 13, color: K.menta, valign: "top", paraSpaceAfter: 8 });
      });
    }
  }
  await pres.writeFile({ fileName: cfg.out });
  console.log(cfg.out);
}
module.exports = { build };
