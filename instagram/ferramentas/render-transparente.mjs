// Como render.mjs, mas com fundo transparente e no tamanho de cada <section class="slide">.
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs';
const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); } catch { pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright')); }
const [html, outDir] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });
const browser = await pw.chromium.launch();
const page = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await page.goto(pathToFileURL(path.resolve(html)).href);
await page.evaluate(() => document.fonts.ready);
for (const el of await page.$$('section.slide')) {
  const id = await el.getAttribute('id');
  await el.screenshot({ path: path.join(outDir, `${id}.png`), omitBackground: true });
  console.log('ok', id);
}
await browser.close();
