// Lê slides-v7.html e devolve, por slide, as caixas de texto e as formas (sem SVG e sem a luz), em JSON.
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';
const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); } catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }
const [html, out] = process.argv.slice(2);
const browser = await pw.chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await page.goto(pathToFileURL(path.resolve(html)).href);
await page.evaluate(() => document.fonts.ready);
const data = await page.evaluate(() => {
  const DECOR = ['feixe', 'brilho', 'vinheta', 'grao'];
  const alpha = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return 1; const p = m[1].split(',').map(s => s.trim()); return p.length > 3 ? parseFloat(p[3]) : 1; };
  const effOp = el => { let o = 1; for (let e = el; e && !e.classList?.contains('slide'); e = e.parentElement) o *= parseFloat(getComputedStyle(e).opacity); return o; };
  const isBlock = el => !['inline'].includes(getComputedStyle(el).display);
  function inner(el) {
    let s = '';
    for (const n of el.childNodes) {
      if (n.nodeType === 3) s += n.textContent.replace(/&/g, '&amp;').replace(/</g, '&lt;');
      else if (n.nodeType === 1) {
        if (n.tagName === 'BR') { s += '<br>'; continue; }
        if (isBlock(n)) continue;
        const c = getComputedStyle(n);
        let col = c.color;
        s += `<span style="font-weight:${c.fontWeight};font-style:${c.fontStyle};color:${col}">` + inner(n) + '</span>';
      }
    }
    return s;
  }
  const res = [];
  for (const sec of document.querySelectorAll('section.slide')) {
    const sr = sec.getBoundingClientRect();
    const items = [];
    const walk = el => {
      for (const ch of el.children) {
        if (ch.tagName === 'svg' || ch.tagName === 'SVG') continue;
        if ([...ch.classList].some(c => DECOR.includes(c))) continue;
        const c = getComputedStyle(ch);
        const r = ch.getBoundingClientRect();
        const box = { x: r.left - sr.left, y: r.top - sr.top, w: r.width, h: r.height };
        if (ch.tagName === 'IMG') { items.push({ t: 'img', src: ch.getAttribute('src'), ...box }); continue; }
        // forma: fundo ou borda
        const bg = alpha(c.backgroundColor) > 0 ? c.backgroundColor : null;
        const bw = ['Top', 'Right', 'Bottom', 'Left'].map(s => parseFloat(c['border' + s + 'Width']) && alpha(c['border' + s + 'Color']) > 0 ? parseFloat(c['border' + s + 'Width']) : 0);
        const bc = c.borderTopColor !== 'rgba(0, 0, 0, 0)' ? c.borderTopColor : c.borderBottomColor;
        if (bg || bw.some(v => v)) {
          const full = bw.every(v => v === bw[0] && v > 0);
          if (bg || full) items.push({ t: 'box', bg, radius: c.borderTopLeftRadius, border: full ? `${bw[0]}px solid ${c.borderTopColor}` : null, op: effOp(ch), ...box });
          if (!full) {
            if (bw[0]) items.push({ t: 'box', bg: c.borderTopColor, radius: '0px', op: effOp(ch), x: box.x, y: box.y, w: box.w, h: bw[0] });
            if (bw[2]) items.push({ t: 'box', bg: c.borderBottomColor, radius: '0px', op: effOp(ch), x: box.x, y: box.y + box.h - bw[2], w: box.w, h: bw[2] });
          }
        }
        // texto: nós de texto diretos
        const own = [...ch.childNodes].filter(n => (n.nodeType === 3 && n.textContent.trim()) || (n.nodeType === 1 && !isBlock(n) && n.tagName !== 'BR'));
        if (own.length && c.display !== 'inline') {
          const pl = parseFloat(c.paddingLeft) + parseFloat(c.borderLeftWidth), pr = parseFloat(c.paddingRight) + parseFloat(c.borderRightWidth);
          const pt = parseFloat(c.paddingTop) + parseFloat(c.borderTopWidth);
          const rg = document.createRange();
          let tr = null;
          for (const n of own) { rg.selectNode(n); const rr = rg.getBoundingClientRect(); tr = tr ? { l: Math.min(tr.l, rr.left), t: Math.min(tr.t, rr.top), r: Math.max(tr.r, rr.right), b: Math.max(tr.b, rr.bottom) } : { l: rr.left, t: rr.top, r: rr.right, b: rr.bottom }; }
          const lh = parseFloat(c.lineHeight);
          const lines = Math.round((tr.b - tr.t) / lh);
          let color = c.color;
          if (alpha(color) === 0 || c.webkitTextFillColor === 'rgba(0, 0, 0, 0)') color = '#F0F0E9';
          items.push({ t: 'text', html: inner(ch), x: r.left - sr.left + pl, y: tr.t - sr.top, w: r.width - pl - pr, tw: tr.r - tr.l, tx: tr.l - sr.left, lines,
            fs: c.fontSize, lh: c.lineHeight, fw: c.fontWeight, fst: c.fontStyle, color, ls: c.letterSpacing, tt: c.textTransform, ta: c.textAlign, op: effOp(ch) });
        }
        walk(ch);
      }
    };
    walk(sec);
    res.push({ id: sec.id, bg: getComputedStyle(sec).backgroundColor, cls: sec.className, items });
  }
  return res;
});
fs.writeFileSync(out, JSON.stringify(data, null, 1));
await browser.close();
console.log('ok', data.length);
