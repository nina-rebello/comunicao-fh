import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import path from 'node:path'; import fs from 'node:fs';
const require = createRequire(import.meta.url);
const pw = require(path.join(execSync('npm root -g').toString().trim(), 'playwright'));
const [src,out]=process.argv.slice(2);
const b = await pw.chromium.launch(); const p = await b.newPage({viewport:{width:1200,height:1400}});
await p.goto('file://'+path.resolve(src)); await p.evaluate(()=>document.fonts.ready);
const r = await p.evaluate(()=>[...document.querySelectorAll('section.slide')].map(s=>{
  const sr=s.getBoundingClientRect(); let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
  s.querySelectorAll('h1,.sub,.passo,.pill,.vidro').forEach(e=>{const r=e.getBoundingClientRect();
    x0=Math.min(x0,r.left-sr.left);y0=Math.min(y0,r.top-sr.top);x1=Math.max(x1,r.right-sr.left);y1=Math.max(y1,r.bottom-sr.top);});
  return {id:s.id,x0,y0,x1,y1};}));
fs.writeFileSync(out,JSON.stringify(r,null,1)); await b.close();
