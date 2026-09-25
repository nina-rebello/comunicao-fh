// Renderiza cada <section class="slide" id="..."> de um HTML em PNG 1080x1350.
// Uso: node instagram/ferramentas/render.mjs caminho/slides.html pasta/saida
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';

// Usa o playwright local, ou o instalado globalmente.
const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); }
catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }
const { chromium } = pw;

const [html, outDir] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await page.goto(pathToFileURL(path.resolve(html)).href);
await page.evaluate(() => document.fonts.ready);
for (const el of await page.$$('section.slide')) {
  const id = await el.getAttribute('id');
  await el.screenshot({ path: path.join(outDir, `${id}.png`) });
  console.log('ok', id);
}
await browser.close();
