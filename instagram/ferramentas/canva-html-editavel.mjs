// Gera um HTML para importar no Canva com todos os elementos editáveis: cada forma dos SVGs vira um SVG próprio,
// recortado no tamanho dela, para o Canva tratar cada uma como um gráfico separado (e não o desenho inteiro como um
// bloco só). Imagens e fontes passam a apontar para o GitHub (raw), e cada <section> vira uma página.
// Uso: node instagram/ferramentas/canva-html-editavel.mjs caminho/slides.html saida.html branch
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); }
catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }

const [src, out, branch] = process.argv.slice(2);
const repo = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const raw = `https://raw.githubusercontent.com/nina-rebello/Comunica-o-FH/${branch}/` +
  path.relative(repo, path.dirname(path.resolve(src))) + '/';

const browser = await pw.chromium.launch();
const page = await browser.newPage();
await page.goto(pathToFileURL(path.resolve(src)).href);
await page.evaluate(() => document.fonts.ready);
const html = await page.evaluate((raw) => {
  const NS = 'http://www.w3.org/2000/svg';
  for (const svg of [...document.querySelectorAll('section.slide svg')]) {
    const pecas = [...svg.children].filter(el => el.tagName !== 'defs');
    if (pecas.length < 2) continue;  // ícones e formas soltas já são um gráfico só
    const sec = svg.closest('section');
    const caixaSec = sec.getBoundingClientRect();
    const caixaSvg = svg.getBoundingClientRect();
    const vb = svg.viewBox.baseVal;
    const esc = vb && vb.width ? caixaSvg.width / vb.width : 1;
    const defs = svg.querySelector('defs');
    for (const el of pecas) {
      const b = el.getBBox();
      const sw = parseFloat(el.getAttribute('stroke-width') || 0);
      const pad = sw ? sw / 2 + 1 : 1;
      const x = b.x - pad, y = b.y - pad, w = b.width + 2 * pad, h = b.height + 2 * pad;
      const novo = document.createElementNS(NS, 'svg');
      novo.setAttribute('viewBox', `${x} ${y} ${w} ${h}`);
      novo.setAttribute('aria-hidden', 'true');
      novo.setAttribute('style', `position:absolute;left:${(caixaSvg.left - caixaSec.left) + (x - (vb?.x || 0)) * esc}px;` +
        `top:${(caixaSvg.top - caixaSec.top) + (y - (vb?.y || 0)) * esc}px;width:${w * esc}px;height:${h * esc}px;overflow:visible`);
      if (defs && /url\(#/.test(el.outerHTML)) novo.appendChild(defs.cloneNode(true));
      novo.appendChild(el.cloneNode(true));
      svg.parentNode.insertBefore(novo, svg);
    }
    svg.remove();
  }
  // imagens com endereço público
  for (const img of document.querySelectorAll('img')) img.setAttribute('src', raw + img.getAttribute('src'));
  for (const sec of document.querySelectorAll('section.slide')) {
    sec.setAttribute('data-document-role', 'page');
    sec.setAttribute('data-label', sec.id);
  }
  return '<!doctype html>\n' + document.documentElement.outerHTML;
}, raw);
await browser.close();

// fontes do Google no lugar das locais; caminhos relativos de imagens já resolvidos acima
const fontes = '<link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,400;0,800;1,400;1,800' +
  '&family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">';
let h = html.replace(/@font-face\{[^}]*\}\n?/g, '')
  .replace('<style>', fontes + '<style>')
  .replace(/src="https:\/\/raw[^"]*?\/\.\.\/\.\.\/marca\//g, `src="https://raw.githubusercontent.com/nina-rebello/Comunica-o-FH/${branch}/instagram/marca/`)
  .replace(/body\{[^}]*\}/, 'body{margin:0;font-family:Raleway,sans-serif}')
  .replace(/font-family:Instrument;/g, "font-family:'Instrument Serif',serif;");
fs.writeFileSync(out, h);
console.log('ok', out);
