// Gera um PDF (1 página por slide, 1080x1350) com texto real, para importar no Canva.
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
const page = await browser.newPage();
await page.goto('file://' + path.resolve(html));
await page.addStyleTag({ content: '@page{size:1080px 1350px;margin:0} body{background:none!important;margin:0} .slide{margin:0!important;break-after:page}' });
await page.evaluate(() => document.fonts.ready);
await page.pdf({ path: out, width: '1080px', height: '1350px', printBackground: true, preferCSSPageSize: true });
await browser.close();
console.log('ok', out);
