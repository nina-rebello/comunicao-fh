// Mede a largura do texto de cada pílula ([data-pl]) do slides.html, relativa ao slide. Usado por gerar.py.
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
const require = createRequire(import.meta.url);
let pw; try { pw = require('playwright'); } catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }
const browser = await pw.chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await page.goto(pathToFileURL(path.resolve(process.argv[2])).href);
await page.evaluate(() => document.fonts.ready);
const r = await page.evaluate(() => [...document.querySelectorAll('[data-pl]')].map(p => {
  const s = p.getBoundingClientRect(), sec = p.closest('section').getBoundingClientRect();
  return { id: p.dataset.pl, x: s.left - sec.left, w: s.width };
}));
console.log(JSON.stringify(r));
await browser.close();
