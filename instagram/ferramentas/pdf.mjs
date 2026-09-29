// Gera um PDF (1 página por slide, 1080x1350) com texto real, para importar no Canva.
// Cada linha de texto vira uma caixa posicionada e sem quebra automática, para o
// Canva não refazer as quebras nem o entrelinhamento com as métricas dele.
// Uso: node instagram/ferramentas/pdf.mjs caminho/slides.html saida.pdf
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import path from 'node:path';
const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); }
catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }
const [html, out] = process.argv.slice(2);
const browser = await pw.chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await page.goto('file://' + path.resolve(html));
await page.evaluate(() => document.fonts.ready);

await page.evaluate(() => {
  const ASC = 0.94; // ascendente da Raleway (em), para achar a linha de base do sublinhado
  const posAncestral = el => {
    for (let a = el; a; a = a.parentElement) if (getComputedStyle(a).position !== 'static') return a;
    return document.body;
  };
  const tarefas = [];
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  for (let n; (n = walker.nextNode());) {
    if (!n.data.trim() || !n.parentElement.closest('section.slide')) continue;
    const el = n.parentElement, cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') continue;
    // agrupa palavras por linha
    const linhas = [];
    for (const m of n.data.matchAll(/\S+/g)) {
      const r = document.createRange();
      r.setStart(n, m.index); r.setEnd(n, m.index + m[0].length);
      const top = Math.round(r.getBoundingClientRect().top);
      const ult = linhas[linhas.length - 1];
      if (ult && Math.abs(ult.top - top) < 2) ult.fim = m.index + m[0].length;
      else linhas.push({ top, ini: m.index, fim: m.index + m[0].length });
    }
    const box = posAncestral(el), br = box.getBoundingClientRect();
    let u = null;
    for (let a = el; a && !a.matches('section'); a = a.parentElement) {
      const s = getComputedStyle(a);
      if (s.textDecorationLine.includes('underline')) { u = s; break; }
    }
    for (const l of linhas) {
      const r = document.createRange();
      r.setStart(n, l.ini); r.setEnd(n, l.fim);
      const rc = r.getBoundingClientRect();
      tarefas.push({ box, texto: n.data.slice(l.ini, l.fim), cs,
        x: rc.left - br.left - box.clientLeft, y: rc.top - br.top - box.clientTop, w: rc.width, h: rc.height, u });
    }
    tarefas.push({ esconder: n });
  }
  for (const t of tarefas) {
    if (t.esconder) {
      const s = document.createElement('span');
      s.style.visibility = 'hidden';
      t.esconder.replaceWith(s); s.append(t.esconder);
      continue;
    }
    const { cs } = t, d = document.createElement('div');
    Object.assign(d.style, {
      position: 'absolute', left: t.x + 'px', top: t.y + 'px', margin: 0, padding: 0, border: 0,
      whiteSpace: 'pre', lineHeight: t.h + 'px', height: t.h + 'px', transform: 'none', background: 'none',
      fontFamily: cs.fontFamily, fontSize: cs.fontSize, fontWeight: cs.fontWeight, fontStyle: cs.fontStyle,
      letterSpacing: cs.letterSpacing, textTransform: cs.textTransform, color: cs.color,
      textDecoration: 'none', textAlign: 'left', zIndex: 'auto', inset: 'auto', width: 'auto'
    });
    d.style.left = t.x + 'px'; d.style.top = t.y + 'px';
    d.textContent = t.texto;
    t.box.append(d);
    if (t.u) {
      const fs = parseFloat(cs.fontSize), esp = parseFloat(t.u.textDecorationThickness) || 3;
      const off = parseFloat(t.u.textUnderlineOffset) || 0;
      const ln = document.createElement('div');
      Object.assign(ln.style, { position: 'absolute', left: t.x + 'px', top: (t.y + ASC * fs + off) + 'px',
        width: t.w + 'px', height: esp + 'px', background: t.u.textDecorationColor, margin: 0, padding: 0, border: 0,
        transform: 'none', inset: 'auto' });
      ln.style.left = t.x + 'px'; ln.style.top = (t.y + ASC * fs + off) + 'px';
      t.box.append(ln);
    }
  }
});

await page.addStyleTag({ content: '@page{size:1080px 1350px;margin:0} body{background:none!important;margin:0} .slide{margin:0!important;break-after:page}' });
if (process.env.PREVIA) await page.screenshot({ path: process.env.PREVIA, fullPage: true });
await page.pdf({ path: out, width: '1080px', height: '1350px', printBackground: true, preferCSSPageSize: true });
await browser.close();
console.log('ok', out);
