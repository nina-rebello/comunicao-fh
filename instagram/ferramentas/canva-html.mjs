// Gera um HTML autocontido para importar no Canva (cada <section> vira uma página).
// Uso: node instagram/ferramentas/canva-html.mjs caminho/slides.html saida.html
import fs from 'node:fs';
import path from 'node:path';
const [src, out] = process.argv.slice(2);
const RAW = 'https://raw.githubusercontent.com/nina-rebello/Comunica-o-FH/claude/eager-bell-tblhnh/';
const repo = path.resolve(path.dirname(new URL(import.meta.url).pathname), '../..');
const dir = path.dirname(path.resolve(src));
const abs = p => RAW + path.relative(repo, path.resolve(dir, p));
let h = fs.readFileSync(src, 'utf8');
const css = fs.readFileSync(path.join(repo, 'instagram/marca/base.css'), 'utf8').replace(/@font-face[^}]*}\n?/g, '');
h = h.replace(/<link rel="stylesheet"[^>]*>/,
  '<link href="https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,400;0,500;0,700;0,800;1,400;1,700;1,800&display=swap" rel="stylesheet">\n<style>' + css + '</style>');
h = h.replace(/url\(([^)]+)\)/g, (m, p) => p.startsWith('http') ? m : `url(${abs(p)})`)
     .replace(/src="([^"]+)"/g, (m, p) => p.startsWith('http') ? m : `src="${abs(p)}"`)
     .replace(/<section class="slide/g, '<section data-document-role="page" class="slide');
fs.writeFileSync(out, h);
console.log('ok', out);
