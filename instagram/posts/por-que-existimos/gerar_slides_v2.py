# Arte v2 (19/10) do post de qua 21/10, "Por que a fairhealth existe?", conteúdo v3 (README.md desta pasta).
# Pedido da Nina: "algo totalmente diferente" da arte v1, "mais rabiscado, com elementos mais divertidos que
# humanizam os slides". Referências dela: um carrossel de "processo de trabalho" (papel com textura, um fio fino que
# faz curvas e laços entre os slides, números grandes ao lado das bolinhas, anotações à mão) e uma linha do tempo em
# espiral com pessoinhas caminhando.
#   - Papel com textura: creme nos slides 2 a 6, Tiffany na capa e no final.
#   - Um fio verde, desenhado à mão, atravessa os sete slides: nasce na capa, marca 2009 e hoje, faz um laço na
#     conversa (slide 4) e termina no logo.
#   - Desenhos à mão (rough.js, licença MIT, em ../../ferramentas/vendor/roughjs/): pessoinhas, o hospital, o prédio
#     da empresa, balões de fala, setas, coração, brilhos e marca-texto Tiffany nas palavras de destaque.
#   - Anotações em Raleway itálico, levemente inclinadas (a regra é só Raleway: nada de fonte manuscrita).
#   Todo texto vem do conteúdo v3; as anotações vêm do material base (README).
# A arte v1 (gerar_slides.py, png/) fica guardada.
# Uso: python3 gerar_slides_v2.py slides-v2.html && node ../../ferramentas/render.mjs slides-v2.html png-v2
import json
import sys

SAIDA = sys.argv[1]
N = 7
W = 1080

CSS = r'''
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:400;font-style:italic;src:url(../../marca/fontes/raleway-latin-400-italic.woff2)}
@font-face{font-family:Raleway;font-weight:800;src:url(../../marca/fontes/raleway-latin-800-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--tif:#96C5BD;--verde:#1F3A36;--creme:#F0F0E9;--tclaro:#BFE0D9;--vlogo:#2F6B64}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#888;display:flex;flex-wrap:wrap;gap:40px;padding:40px}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;font-variant-numeric:lining-nums;color:var(--verde)}
.slide>*{position:absolute}
.C{background:var(--creme)}
.T{background:var(--tif)}
.papel{inset:0;opacity:.28;mix-blend-mode:multiply;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='360' height='360'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 .55 0 0 0 0 .55 0 0 0 0 .52 0 0 0 -1.1 .9'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>"),
    repeating-linear-gradient(0deg,rgba(31,58,54,.035) 0 1px,transparent 1px 5px),
    repeating-linear-gradient(90deg,rgba(31,58,54,.03) 0 1px,transparent 1px 5px)}
svg.cheia{left:0;top:0;width:1080px;height:1350px;overflow:visible}
.k{font-weight:800;font-style:italic}
.rot{left:96px;top:96px;font-size:22px;line-height:28px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--vlogo)}
.T .rot{color:var(--verde)}
.tit{left:96px;width:888px;font-size:70px;line-height:80px;letter-spacing:-0.01em}
.corpo{left:96px;width:888px;font-size:32px;line-height:44px}
.anota{font-size:30px;line-height:36px;font-style:italic;color:var(--vlogo);transform:rotate(-4deg);transform-origin:left top}
.T .anota{color:var(--verde)}
.grande{font-size:156px;line-height:150px;font-weight:800;letter-spacing:-0.03em}
.balao{font-size:36px;line-height:44px;font-weight:800;font-style:italic;text-align:center}
.handle{left:96px;top:1238px;font-size:24px;line-height:32px}
.pg{right:96px;top:1238px;font-size:24px;line-height:32px;letter-spacing:.08em}
'''

# O fio: pontos por onde ele passa, em coordenadas do carrossel inteiro (7 × 1080 de largura).
# Nomes marcam onde ficam a bolinha, as pessoinhas e o laço.
FIO = [
    (150, 930),                                    # 1 · começo (bolinha)
    (430, 990),                                    # 1 · pessoinha andando
    (760, 950), (1080, 1030),
    (1340, 900),                                   # 2 · bolinha de 2009
    (1600, 1060), (1900, 1120), (2160, 1090),
    (2560, 1110), (2920, 1080), (3240, 1100),
    (3500, 1110),                                  # 4 · pessoinha A
    (3700, 1110), (3820, 1080), (3830, 1010), (3770, 985), (3720, 1020), (3745, 1090), (3860, 1115),  # 4 · o laço
    (4040, 1110),                                  # 4 · pessoinha B
    (4320, 1080),
    (4620, 1060),                                  # 5 · pessoinha andando
    (4940, 980), (5160, 925),                      # 5 · base do prédio
    (5400, 880),
    (5660, 900),                                   # 6 · bolinha de hoje
    (5960, 1050), (6200, 1100), (6480, 1080),
    (6780, 1100), (7000, 1060),                    # 7 · pessoinha comemorando
    (7160, 960),                                   # 7 · chega ao logo
]

S = []
# 1 · capa (Tiffany)
S.append(('r01', 'T', 'capa: a história começa num hospital; o fio nasce aqui', '''<p class="rot">Nossa história</p>
  <p class="tit" style="top:200px;font-size:84px;line-height:96px">Antes de chegar às empresas, nossa história começou <span class="k mk">em um hospital</span>.</p>
  <p class="anota" style="left:150px;top:760px">há quase 20 anos…</p>'''))
# 2 · 2009, no hospital
S.append(('r02', 'C', '2009, no hospital: o Escritório do Paciente', '''<p class="rot">No hospital</p>
  <p class="tit" style="top:170px;font-size:64px;line-height:74px">Dentro de um hospital, surgiu o <span class="k mk">Escritório do Paciente</span>.</p>
  <p class="corpo" style="top:420px;font-size:30px;line-height:42px">Um modelo de cuidado criado para trazer o paciente de volta ao centro, com a escuta, o acolhimento e as necessidades de cada pessoa em primeiro lugar.</p>
  <p class="grande" style="left:300px;top:775px">2009</p>
  <p class="anota" style="left:330px;top:1130px">onde tudo começou</p>'''))
# 3 · a essência: uma pessoa e o que ela traz
S.append(('r03', 'C', 'a essência: a pessoa por trás de cada atendimento', '''<p class="rot">A essência</p>
  <p class="tit" style="top:170px">Por trás de cada atendimento, existe <span class="k mk">uma pessoa</span>.</p>
  <p class="anota" style="left:120px;top:560px">a sua história</p>
  <p class="anota" style="left:740px;top:560px">seus hábitos</p>
  <p class="anota" style="left:96px;top:770px">suas necessidades</p>
  <p class="anota" style="left:730px;top:770px">suas prioridades</p>
  <p class="corpo" style="top:920px;font-size:36px;line-height:48px">Por isso, escutar sempre foi parte essencial da nossa maneira de cuidar.</p>'''))
# 4 · o acolhimento: duas pessoinhas, a pergunta e o laço da conversa
S.append(('r04', 'C', 'o acolhimento: antes de qualquer exame, uma conversa', '''<p class="rot">O acolhimento</p>
  <p class="tit" style="top:170px">Antes de qualquer exame, <span class="k mk">uma conversa</span>.</p>
  <p class="corpo" style="top:370px">Um espaço seguro e confidencial para contar a própria história e decidir junto o próprio cuidado.</p>
  <p class="balao" style="left:200px;top:716px;width:360px">O que é importante para você?</p>
  <p class="anota" style="left:690px;top:585px;width:330px">sem pressa e sem julgamento</p>'''))
# 5 · evolução: a pessoinha caminha até o trabalho
S.append(('r05', 'C', 'evolução: o conceito chega ao trabalho', '''<p class="rot">Evolução</p>
  <p class="tit" style="top:170px">Com o tempo, essa forma de cuidar <span class="k mk">evoluiu</span>.</p>
  <p class="corpo" style="top:370px">E o conceito chegou a um lugar que faz parte da rotina das pessoas: <b style="font-weight:800">o trabalho</b>. Porque, quando o cuidado está perto, ele acontece.</p>
  <p class="anota" style="left:470px;top:680px">o trabalho!</p>'''))
# 6 · hoje, nas empresas: o Escritório do Cuidado
S.append(('r06', 'C', 'hoje, nas empresas: o Escritório do Cuidado', '''<p class="rot">Hoje · Nas empresas</p>
  <p class="tit" style="top:170px;font-size:64px;line-height:74px">Assim surgiu o <span class="k mk">Escritório do Cuidado</span>, da fairhealth.</p>
  <p class="corpo" style="top:360px;font-size:30px;line-height:42px">Um projeto novo, inspirado no Escritório do Paciente e pensado para as empresas: um espaço de acolhimento e de medicina preventiva, com cuidado individualizado e acompanhamento.</p>
  <p class="grande" style="left:300px;top:770px">hoje</p>
  <p class="anota" style="left:690px;top:610px">dentro da empresa</p>'''))
# 7 · o propósito (Tiffany): o fio chega ao logo
S.append(('r07', 'T', 'o propósito: os lugares mudaram, a essência permanece', '''<p class="rot">O propósito</p>
  <p class="tit" style="top:170px">Os lugares mudaram. <span class="k mk">A essência do cuidado permanece.</span></p>
  <p class="corpo" style="top:450px">Do hospital às empresas, seguimos com um mesmo princípio: <b style="font-weight:800">o cuidado começa pela pessoa.</b></p>
  <p class="anota" style="left:110px;top:720px">a gente tá aqui pra te ouvir</p>
  <img src="../../marca/logo-circulo.png" alt="fairhealth" style="left:685px;top:865px;width:150px;height:150px;z-index:2">'''))

# Desenhos de cada slide, em coordenadas do slide (JavaScript, com o rough.js). Cada um recebe o "g", que desenha
# no fundo do slide. Ordem: o que vem antes fica atrás.
DESENHOS = r'''
const VERDE = '#1F3A36', TIF = '#96C5BD', CREME = '#F0F0E9', VLOGO = '#2F6B64', BRANCO = '#FBFBF8';
const DESENHOS = {
  r01: g => {
    g.bolinha(150, 930);
    g.seta([[205, 815], [175, 860], [158, 905]]);
    g.pessoa(430, 988, 1.6, 'anda', CREME);
    g.brilho(940, 610, 22); g.brilho(985, 560, 13);
  },
  r02: g => {
    g.mancha(290, 805, 400, 120);
    g.hospital(740, 790);
    g.bolinha(260, 900);
    g.seta([[600, 1140], [680, 1110], [745, 1030]]);
  },
  r03: g => {
    g.pessoa(540, 830, 1.75, 'pe', TIF);
    g.coracao(540, 700, 0.55, CREME);
    g.seta([[260, 612], [360, 640], [462, 650]]);
    g.seta([[830, 612], [720, 630], [622, 650]]);
    g.seta([[300, 822], [390, 790], [470, 760]]);
    g.seta([[790, 822], [700, 790], [612, 760]]);
  },
  r04: g => {
    g.balao(380, 760, 520, 200, [300, 892], BRANCO);
    g.balao(880, 820, 150, 100, [825, 900], BRANCO);
    g.coracao(880, 818, 0.7, TIF);
    g.pessoa(260, 1108, 1.45, 'fala', TIF, 1);
    g.pessoa(800, 1108, 1.45, 'pe', VLOGO, -1);
    g.seta([[860, 660], [880, 700], [880, 770]]);
  },
  r05: g => {
    g.predio(740, 925, 200, 280, false);
    g.pessoa(300, 1058, 1.35, 'anda', TIF);
    g.seta([[640, 725], [690, 735], [728, 770]]);
    g.brilho(990, 640, 18);
  },
  r06: g => {
    g.mancha(290, 800, 330, 120);
    g.predio(700, 1100, 200, 280, true);
    g.bolinha(260, 900);
    g.pessoa(630, 1086, 1.0, 'anda', VLOGO);
    g.seta([[850, 660], [860, 720], [810, 880]]);
  },
  r07: g => {
    g.circulo(760, 940, 200, CREME);
    g.pessoa(520, 1058, 1.35, 'viva', CREME);
    g.brilho(440, 900, 20); g.brilho(610, 880, 14); g.brilho(900, 820, 18);
    g.seta([[520, 790], [610, 820], [670, 880]]);
  },
};
'''

JS = r'''
(function () {
  const gen = rough.generator();
  const NS = 'http://www.w3.org/2000/svg';
  let semente = 7;
  const op = o => Object.assign({ stroke: VERDE, strokeWidth: 3, roughness: 1.2, bowing: 1.2, seed: semente++ }, o || {});

  function poe(svg, drawable) {
    for (const p of gen.toPaths(drawable)) {
      const el = document.createElementNS(NS, 'path');
      el.setAttribute('d', p.d);
      el.setAttribute('stroke', p.stroke);
      el.setAttribute('stroke-width', p.strokeWidth);
      el.setAttribute('fill', p.fill || 'none');
      el.setAttribute('stroke-linecap', 'round');
      el.setAttribute('stroke-linejoin', 'round');
      svg.appendChild(el);
    }
  }

  function helpers(svg, fundoTif) {
    const g = {};
    g.bolinha = (x, y) => poe(svg, gen.circle(x, y, 26, op({ fill: VERDE, fillStyle: 'solid', roughness: .6 })));
    g.seta = pts => {
      poe(svg, gen.curve(pts, op({ strokeWidth: 2.5, roughness: .9 })));
      const [a, b] = [pts[pts.length - 2], pts[pts.length - 1]];
      const ang = Math.atan2(b[1] - a[1], b[0] - a[0]);
      for (const d of [2.6, -2.6]) {
        poe(svg, gen.line(b[0], b[1], b[0] - 20 * Math.cos(ang + d / 6), b[1] - 20 * Math.sin(ang + d / 6), op({ strokeWidth: 2.5, roughness: .6 })));
      }
    };
    g.brilho = (x, y, r) => {
      poe(svg, gen.line(x - r, y, x + r, y, op({ strokeWidth: 2.5, roughness: .5 })));
      poe(svg, gen.line(x, y - r, x, y + r, op({ strokeWidth: 2.5, roughness: .5 })));
      poe(svg, gen.line(x - r * .55, y - r * .55, x + r * .55, y + r * .55, op({ strokeWidth: 2, roughness: .5 })));
      poe(svg, gen.line(x - r * .55, y + r * .55, x + r * .55, y - r * .55, op({ strokeWidth: 2, roughness: .5 })));
    };
    g.mancha = (x, y, w, h) => poe(svg, gen.rectangle(x, y, w, h, op({ stroke: 'none', fill: fundoTif ? CREME : TIF, fillStyle: 'hachure', hachureGap: 9, fillWeight: 5, hachureAngle: -32, roughness: 1.6 })));
    g.coracao = (x, y, s, cor) => {
      const d = `M${x} ${y - 10 * s} C${x - 14 * s} ${y - 34 * s} ${x - 44 * s} ${y - 12 * s} ${x} ${y + 26 * s} C${x + 44 * s} ${y - 12 * s} ${x + 14 * s} ${y - 34 * s} ${x} ${y - 10 * s} Z`;
      poe(svg, gen.path(d, op({ fill: cor, fillStyle: 'solid', strokeWidth: 2.5, roughness: .8 })));
    };
    g.circulo = (x, y, d, cor) => poe(svg, gen.circle(x, y, d, op({ fill: cor, fillStyle: 'solid', strokeWidth: 3, roughness: 1.4 })));
    g.balao = (x, y, w, h, ponta, cor) => {
      const ang0 = Math.atan2(ponta[1] - y, ponta[0] - x);
      const borda = (a) => [x + (w / 2) * Math.cos(a), y + (h / 2) * Math.sin(a)];
      const [p1, p2] = [borda(ang0 - .16), borda(ang0 + .16)];
      const dentro = ([a, b]) => [x + (a - x) * .9, y + (b - y) * .9];
      poe(svg, gen.ellipse(x, y, w, h, op({ fill: cor, fillStyle: 'solid', roughness: 1.1 })));
      poe(svg, gen.polygon([dentro(p1), ponta, dentro(p2)], op({ stroke: 'none', fill: cor, fillStyle: 'solid', roughness: 0 })));
      poe(svg, gen.line(p1[0], p1[1], ponta[0], ponta[1], op({ roughness: .6 })));
      poe(svg, gen.line(p2[0], p2[1], ponta[0], ponta[1], op({ roughness: .6 })));
    };
    g.pessoa = (x, y, s, pose, cor, olha) => {
      olha = olha || 0;
      const L = (x1, y1, x2, y2) => poe(svg, gen.line(x + x1 * s, y + y1 * s, x + x2 * s, y + y2 * s, op({ strokeWidth: 3.2, roughness: .9 })));
      // pernas
      if (pose === 'anda') { L(-6, -50, -24, 0); L(6, -50, 22, -2); }
      else { L(-8, -50, -12, 0); L(8, -50, 12, 0); }
      // braços
      if (pose === 'anda') { L(16, -92, 36, -64); L(-16, -92, -34, -68); }
      else if (pose === 'viva') { L(-16, -94, -40, -140); L(16, -94, 40, -140); }
      else if (pose === 'fala') { L(-16, -92, -28, -56); L(16, -92, 46, -112); }
      else { L(-16, -92, -30, -56); L(16, -92, 30, -56); }
      // tronco
      const t = [[-19, -98], [19, -98], [15, -48], [-15, -48]].map(([a, b]) => [x + a * s, y + b * s]);
      poe(svg, gen.polygon(t, op({ fill: cor, fillStyle: 'solid', strokeWidth: 3, roughness: .9 })));
      // cabeça, olhos e sorriso
      const hx = x + olha * 2 * s, hy = y - 118 * s;
      poe(svg, gen.circle(hx, hy, 36 * s, op({ fill: fundoTif ? TIF : CREME, fillStyle: 'solid', strokeWidth: 3, roughness: .7 })));
      const ox = olha * 5 * s;
      for (const dx of [-6, 6]) poe(svg, gen.circle(hx + ox + dx * s, hy - 3 * s, 3.2 * s, op({ fill: VERDE, fillStyle: 'solid', strokeWidth: 1, roughness: .2 })));
      poe(svg, gen.arc(hx + ox, hy + 3 * s, 14 * s, 10 * s, .25, Math.PI - .25, false, op({ strokeWidth: 2.2, roughness: .4 })));
    };
    g.hospital = (x, y) => {
      poe(svg, gen.rectangle(x, y, 240, 200, op({ fill: BRANCO, fillStyle: 'solid' })));
      poe(svg, gen.rectangle(x + 90, y - 62, 60, 62, op({ fill: TIF, fillStyle: 'solid' })));
      poe(svg, gen.line(x + 120, y - 50, x + 120, y - 12, op({ strokeWidth: 5, roughness: .4, stroke: BRANCO })));
      poe(svg, gen.line(x + 101, y - 31, x + 139, y - 31, op({ strokeWidth: 5, roughness: .4, stroke: BRANCO })));
      for (const [cx, cy] of [[x + 22, y + 28], [x + 96, y + 28], [x + 170, y + 28], [x + 22, y + 92], [x + 170, y + 92]])
        poe(svg, gen.rectangle(cx, cy, 48, 40, op({ strokeWidth: 2.2, fill: TIF, fillStyle: 'hachure', hachureGap: 7, roughness: 1 })));
      poe(svg, gen.rectangle(x + 96, y + 120, 48, 80, op({ strokeWidth: 2.5 })));
    };
    g.predio = (x, base, w, h, cuidado) => {
      const y = base - h;
      poe(svg, gen.rectangle(x, y, w, h, op({ fill: BRANCO, fillStyle: 'solid' })));
      for (let i = 0; i < 4; i++) for (let j = 0; j < 3; j++) {
        if (cuidado && i < 2 && j === 1) continue;
        poe(svg, gen.rectangle(x + 22 + j * 58, y + 26 + i * 52, 40, 32, op({ strokeWidth: 2.2, fill: TIF, fillStyle: 'hachure', hachureGap: 7, roughness: 1 })));
      }
      poe(svg, gen.rectangle(x + w / 2 - 24, base - 64, 48, 64, op({ strokeWidth: 2.5 })));
      if (cuidado) g.coracao(x + w / 2, y + 66, 1.05, TIF);
    };
    return g;
  }

  function desenha() {
    let k = 0;
    for (const sec of document.querySelectorAll('section.slide')) {
      const tif = sec.classList.contains('T');
      const fundo = sec.querySelector('svg.fundo');
      const sr = sec.getBoundingClientRect();
      // marca-texto nas palavras de destaque (uma faixa por linha)
      for (const sp of sec.querySelectorAll('.mk')) {
        for (const r of sp.getClientRects()) {
          const x = r.left - sr.left - 8, y = r.top - sr.top + r.height * .52, w = r.width + 16, h = r.height * .42;
          poe(fundo, gen.rectangle(x, y, w, h, op({ stroke: 'none', fill: tif ? CREME : TIF, fillStyle: 'hachure', hachureGap: 6, fillWeight: 5, hachureAngle: -24, roughness: 1.4 })));
        }
      }
      // o fio do carrossel, deslocado para este slide
      const gf = document.createElementNS(NS, 'g');
      gf.setAttribute('transform', `translate(${-k * 1080} 0)`);
      fundo.appendChild(gf);
      for (const p of FIO_D) {
        const el = document.createElementNS(NS, 'path');
        el.setAttribute('d', p); el.setAttribute('stroke', VERDE); el.setAttribute('stroke-width', 3.5);
        el.setAttribute('fill', 'none'); el.setAttribute('stroke-linecap', 'round');
        gf.appendChild(el);
      }
      DESENHOS[sec.id](helpers(fundo, tif));
      k++;
    }
  }

  // o fio é desenhado uma vez só (mesma semente), para emendar certinho de um slide para o outro
  const FIO_D = gen.toPaths(gen.curve(FIO, { stroke: VERDE, strokeWidth: 3.5, roughness: .7, bowing: .8, seed: 3, disableMultiStroke: true })).map(p => p.d);
  document.fonts.ready.then(desenha);
})();
'''


def html(slides):
    out = ['<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Por que a fairhealth existe? (v2, rabiscada)</title><style>'
           + CSS + '</style><script src="../../ferramentas/vendor/roughjs/rough.js"></script></head><body>\n']
    for k, (sid, cls, nota, corpo) in enumerate(slides, 1):
        if k == 1:
            fim = '\n  <p class="handle">@fairhealth.br</p>\n  <p class="pg">Arraste para o lado →</p>'
        else:
            fim = '\n  <p class="handle">@fairhealth.br</p>\n  <p class="pg">%02d / %02d</p>' % (k, N)
        out.append('<!-- %d · %s -->\n<section class="slide %s" id="%s">\n  <div class="papel"></div>\n  <svg class="cheia fundo" viewBox="0 0 1080 1350" aria-hidden="true"></svg>\n  %s%s\n</section>\n\n'
                   % (k, nota, cls, sid, corpo, fim))
    out.append('<script>\nconst FIO = ' + json.dumps(FIO) + ';\n' + DESENHOS + JS + '</script>\n</body></html>\n')
    return ''.join(out)


open(SAIDA, 'w').write(html(S))
print('ok', len(S))
