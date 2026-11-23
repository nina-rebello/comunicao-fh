// Achata um carrossel para o Canva: abre o slides.html no navegador, mede cada bloco de texto, cada linha (régua ou
// borda de lista) e cada imagem, e escreve um HTML novo em que tudo fica em posição absoluta, com as quebras de linha
// do navegador viradas <br>, as cores já resolvidas (opacidade misturada ao fundo liso do slide) e as fontes da marca.
// É o que o Canva respeita na importação (ver CLAUDE.md, "Levar um post para o Canva").
// Uso: node instagram/ferramentas/achatar.mjs caminho/slides.html caminho/saida.html [vagas.json]
// vagas.json (opcional): {"<id do slide>": [{"sel": "seletor CSS", "src": "fotos-canva/x.jpg", "alt": "..."}]}
//   troca cada vaga de foto (o elemento do seletor) por <img> do mesmo tamanho; use "sel": "section" para a foto de
//   fundo do slide inteiro, "sobre": "fotos-canva/degrade.png" para pôr uma camada por cima dela e "z" para a ordem
//   (0 fica no fundo; 2 é a altura das imagens do slide; o texto fica em 3).
// Depois: node instagram/ferramentas/canva.mjs saida.html canva.html
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); }
catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }

const [src, out, vagasArq] = process.argv.slice(2);
const vagas = vagasArq ? JSON.parse(fs.readFileSync(vagasArq, 'utf8')) : {};
const browser = await pw.chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await page.goto(pathToFileURL(path.resolve(src)).href);
await page.evaluate(() => document.fonts.ready);

const slides = await page.evaluate((vagas) => {
  const r2 = (n) => Math.round(n * 10) / 10;
  const rgba = (s) => { const m = s.match(/[\d.]+/g).map(Number); return { r: m[0], g: m[1], b: m[2], a: m.length > 3 ? m[3] : 1 }; };
  const hex = (c) => '#' + [c.r, c.g, c.b].map((v) => Math.round(v).toString(16).padStart(2, '0')).join('');
  const mistura = (c, a, fundo) => fundo ? { r: c.r * a + fundo.r * (1 - a), g: c.g * a + fundo.g * (1 - a), b: c.b * a + fundo.b * (1 - a) } : c;
  const opac = (el, ate) => { let o = 1; for (let e = el; e && e !== ate.parentElement; e = e.parentElement) o *= +getComputedStyle(e).opacity; return o; };
  const res = [];
  for (const sec of document.querySelectorAll('section.slide')) {
    const S = sec.getBoundingClientRect();
    const cs = getComputedStyle(sec);
    const bgc = rgba(cs.backgroundColor);
    const fotoFundo = cs.backgroundImage !== 'none' || sec.classList.contains('foto');
    const fundo = fotoFundo ? null : bgc;
    const itens = [];
    const pos = (r) => ({ x: r2(r.left - S.left), y: r2(r.top - S.top), w: r2(r.width), h: r2(r.height) });
    // vagas de foto
    const ignorar = new Set();
    for (const v of vagas[sec.id] || []) {
      const el = v.sel === 'section' ? sec : sec.querySelector(v.sel);
      const p = v.sel === 'section' ? { x: 0, y: 0, w: S.width, h: S.height } : pos(el.getBoundingClientRect());
      if (v.sel !== 'section') { ignorar.add(el); el.querySelectorAll('*').forEach((f) => ignorar.add(f)); }
      itens.push({ tipo: 'img', src: v.src, alt: v.alt || '', ...p, z: v.z ?? 0 });
      if (v.sobre) itens.push({ tipo: 'img', src: v.sobre, alt: '', ...p, z: 1 });
    }
    if (fotoFundo) sec.querySelectorAll(':scope > .aviso').forEach((e) => ignorar.add(e));
    for (const el of sec.querySelectorAll('*')) {
      if (ignorar.has(el)) continue;
      const st = getComputedStyle(el);
      if (st.display === 'none' || st.visibility === 'hidden') continue;
      const r = el.getBoundingClientRect();
      if (el.tagName === 'IMG') {
        itens.push({ tipo: 'img', src: el.getAttribute('src'), alt: el.getAttribute('alt') || '', ...pos(r), z: 2,
          raio: st.borderRadius !== '0px' ? st.borderRadius : '' });
        continue;
      }
      // linhas: borda de cima (régua) ou de baixo (itens de lista)
      for (const lado of ['Top', 'Bottom']) {
        const w = parseFloat(st[`border${lado}Width`]);
        if (w > 0 && st[`border${lado}Style`] !== 'none') {
          const c = rgba(st[`border${lado}Color`]);
          const a = c.a * opac(el, sec);
          const y = lado === 'Top' ? r.top : r.bottom - w;
          itens.push({ tipo: 'linha', x: r2(r.left - S.left), y: r2(y - S.top), w: r2(r.width), h: w,
            cor: hex(mistura(c, a, fundo)), op: fundo ? 1 : r2(a), z: 2 });
        }
      }
      // bloco de texto: tem texto direto e não é inline
      const temTexto = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
      if (!temTexto || st.display === 'inline') continue;
      // quebras do navegador viram <br>: marca o espaço antes de cada palavra que abre linha nova
      const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const nos = []; while (walker.nextNode()) nos.push(walker.currentNode);
      let topoAnt = null; let ant = null; const quebras = [];
      for (const n of nos) {
        const t = n.textContent;
        for (let i = 0; i < t.length; i++) {
          if (/\s/.test(t[i])) continue;
          if (i > 0 && !/\s/.test(t[i - 1])) continue;
          const rg = document.createRange(); rg.setStart(n, i); rg.setEnd(n, i + 1);
          const rr = rg.getClientRects()[0]; if (!rr) continue;
          if (topoAnt !== null && rr.top > topoAnt + 4) {
            if (i > 0) quebras.push([n, i - 1]);
            // a linha nova começa num trecho (span) novo: o espaço que quebra é o do fim do trecho anterior
            // (se o anterior não termina em espaço, a quebra já é um <br> do próprio HTML)
            else if (ant && /\s$/.test(ant.textContent)) quebras.push([ant, ant.textContent.length - 1]);
          }
          topoAnt = rr.top;
        }
        ant = n;
      }
      for (const [n, i] of quebras.reverse()) n.textContent = n.textContent.slice(0, i) + '\u2028' + n.textContent.slice(i + 1);
      // cores e pesos dos trechos internos, resolvidos
      const corDe = (e) => { const c = rgba(getComputedStyle(e).color); return hex(mistura(c, c.a * opac(e, sec), fundo)); };
      const clone = el.cloneNode(true);
      const origs = [el, ...el.querySelectorAll('*')]; const cl = [clone, ...clone.querySelectorAll('*')];
      // trechos que são blocos (display:block) saem desta caixa: viram caixas próprias, medidas à parte
      cl.forEach((c, k) => { if (k && c.tagName !== 'BR' && getComputedStyle(origs[k]).display !== 'inline') c.dataset.fora = '1'; });
      cl.forEach((c, k) => {
        if (k === 0 || c.tagName === 'BR') return;
        const so = getComputedStyle(origs[k]);
        c.removeAttribute('class');
        c.setAttribute('style', `color:${corDe(origs[k])};font-weight:${so.fontWeight};font-style:${so.fontStyle}` +
          (so.fontFamily !== st.fontFamily ? `;font-family:${so.fontFamily};font-size:${so.fontSize};letter-spacing:${so.letterSpacing}` : ''));
      });
      clone.querySelectorAll('[data-fora]').forEach((c) => c.remove());
      const html = clone.innerHTML.replace(/\u2028/g, '<br>').replace(/\s*\n\s*/g, ' ').trim().replace(/(\s*<br>)+$/, '');
      itens.push({ tipo: 'texto', html, ...pos(r), z: 3,
        estilo: `font-family:${st.fontFamily.replace(/"/g, "'")};font-size:${st.fontSize};font-weight:${st.fontWeight};font-style:${st.fontStyle};` +
          `letter-spacing:${st.letterSpacing};line-height:${st.lineHeight};color:${corDe(el)};text-transform:${st.textTransform};font-variant-numeric:${st.fontVariantNumeric};` +
          (fundo ? '' : (opac(el, sec) < 1 ? `opacity:${r2(opac(el, sec))};` : '')) });
    }
    res.push({ id: sec.id, fundo: hex(bgc), fotoFundo, itens });
  }
  return res;
}, vagas);

// estilos de fonte e cores de base vêm do próprio slides.html (o <link> e os @font-face são mantidos)
const original = fs.readFileSync(src, 'utf8');
const cabeca = original.match(/<head>([\s\S]*?)<\/head>/)[1]
  .replace(/<style>[\s\S]*?<\/style>/g, (css) => (css.match(/@font-face\{[^}]*\}/g) || []).join('\n').replace(/^/, '<style>\n') + '\n</style>');
const corpo = slides.map((s) => {
  const els = s.itens.sort((a, b) => a.z - b.z).map((i) => {
    const box = `position:absolute;left:${i.x}px;top:${i.y}px;width:${i.w}px;height:${i.h}px`;
    if (i.tipo === 'img') return `  <img src="${i.src}" alt="${i.alt}" style="${box};object-fit:cover${i.raio ? `;border-radius:${i.raio}` : ''}">`;
    if (i.tipo === 'linha') return `  <div style="${box};background:${i.cor}${i.op < 1 ? `;opacity:${i.op}` : ''}"></div>`;
    // texto: largura com folga (o Canva desenha o texto um pouco mais largo), sem quebra automática
    return `  <p style="position:absolute;margin:0;left:${i.x}px;top:${i.y}px;width:${Math.min(Math.ceil(i.w * 1.08), Math.ceil(1080 - i.x))}px;white-space:nowrap;text-align:left;${i.estilo}">${i.html}</p>`;
  }).join('\n');
  return `<section class="slide" id="${s.id}" style="background:${s.fundo};padding:0;display:block">\n${els}\n</section>`;
}).join('\n\n');
fs.writeFileSync(out, `<!doctype html>\n<html lang="pt-BR"><head>${cabeca}<style>body{margin:0}.slide{margin:0 0 40px}</style>\n` +
  `<style media="canva">body{background:none}.slide{margin:0}</style>\n</head><body>\n${corpo}\n</body></html>\n`);
console.log('ok', out, slides.map((s) => `${s.id}:${s.itens.length}`).join(' '));
await browser.close();
