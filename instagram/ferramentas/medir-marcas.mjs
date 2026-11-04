// Mede as caixas dos marca-textos (p.mk span) de cada slide, relativas ao slide.
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
const r = await page.evaluate(() => [...document.querySelectorAll('[data-mk]')].map(p => {
  const s = p.querySelector('span').getBoundingClientRect(), sec = p.closest('section').getBoundingClientRect();
  return { id: p.dataset.mk, x: s.left - sec.left, y: s.top - sec.top, w: s.width, h: s.height };
}));
console.log(JSON.stringify(r));
await browser.close();
