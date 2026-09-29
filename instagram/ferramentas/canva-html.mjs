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
     .replace(/<section class="slide/g, '<section data-document-role="page" class="slide')
     // listas como divs (o Canva adiciona marcadores próprios a <li>)
     .replace(/<ul class="lista">/g, '<div class="lista">').replace(/<\/ul>/g, '</div>')
     .replace(/<li>/g, '<div class="li">').replace(/<\/li>/g, '</div>')
     // texto da caixa num bloco interno, para o Canva respeitar o respiro
     .replace(/<div class="caixa">([\s\S]*?)<\/div>/g, '<div class="caixa"><p>$1</p></div>')
     // borda do círculo da seta desenhada no próprio SVG
     .replace(/<path d="M4 12h15M13 6l6 6-6 6"\/>/g, '<circle cx="12" cy="12" r="11.2" stroke-width=".9"/><path transform="translate(6 6) scale(.5)" d="M4 12h15M13 6l6 6-6 6"/>');
h = h.replace('</style></head>', '.lista .li{padding:22px 0;border-bottom:3px solid color-mix(in srgb,var(--acento) 35%,transparent)}.lista .li:last-child{border:0}.lista .li span{font-weight:800;font-style:italic;color:var(--acento);margin-right:18px}.flecha{border:0!important}.flecha svg{width:110px!important;height:110px!important}\n</style></head>');
fs.writeFileSync(out, h);
console.log('ok', out);
