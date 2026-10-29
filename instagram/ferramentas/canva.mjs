// Gera o canva.html autocontido de um carrossel, para importar no Canva por URL.
// Embute CSS, fontes e imagens locais em base64, marca cada slide como página e
// aplica os ajustes de conversão do post (o <style id="canva"> do slides.html, se houver).
// Uso: node instagram/ferramentas/canva.mjs caminho/slides.html caminho/canva.html
import fs from 'node:fs';
import path from 'node:path';

const [src, out] = process.argv.slice(2);
const dir = path.dirname(path.resolve(src));
const tipos = { '.woff2': 'font/woff2', '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg' };

// Troca url(...) relativas de um CSS por data URIs, resolvidas a partir da pasta do CSS.
// Caminhos que não existem (como os exemplos nos comentários) ficam como estão.
const embutir = (css, base) => css.replace(/url\((?!data:)['"]?([^'")]+)['"]?\)/g, (orig, rel) => {
  const arq = path.resolve(base, rel);
  if (!fs.existsSync(arq)) return orig;
  return `url(data:${tipos[path.extname(arq)]};base64,${fs.readFileSync(arq).toString('base64')})`;
});

let html = fs.readFileSync(src, 'utf8');
html = html.replace(/<link rel="stylesheet" href="([^"]+)">/g, (_, href) => {
  const arq = path.resolve(dir, href);
  return `<style>\n${embutir(fs.readFileSync(arq, 'utf8'), path.dirname(arq))}</style>`;
});
html = html.replace(/<style>([\s\S]*?)<\/style>/g, (_, css) => `<style>${embutir(css, dir)}</style>`);
html = html.replace(/<img src="(?!data:)([^"]+)"/g, (_, rel) => {
  const arq = path.resolve(dir, rel);
  return `<img src="data:${tipos[path.extname(arq)]};base64,${fs.readFileSync(arq).toString('base64')}"`;
});
html = html.replace(/<section class="slide/g, '<section data-document-role="page" class="slide');
// O bloco de ajustes só vale para o Canva: no slides.html ele fica desligado (media="canva").
html = html.replace('<style media="canva">', '<style>');
fs.writeFileSync(out, html);
console.log('ok', out, `${Math.round(fs.statSync(out).size / 1024)} KB`);
