"""Gera o projeto HyperFrames da camada de legendas (palavra por palavra, no estilo do perfil).

legendas.py <video>

Lê transcricao_palavras.json e o bloco `plano.legendas` do estado:
  {"palavras_chave": [tempo_inicio, ...], "ocultar": [[ini, fim], ...], "correcoes": {"tempo": "palavra"}}
Escreve _CLAUDE/<video>/motion/legendas/index.html (fundo transparente, duração do vídeo aparado).
A linha inteira aparece apagada e cada palavra acende quando é dita (ofício §5); a palavra-chave ganha
marca-texto Tiffany e punch leve.
"""
import html, json, os, shutil, sys
from comum import RAIZ, carregar, pasta_trabalho, salvar

MAX_PALAVRAS, MAX_CHARS = 4, 24
# Palavras que não fecham uma linha: passam para a linha seguinte.
LIGACAO = {"a", "o", "as", "os", "e", "de", "da", "do", "das", "dos", "no", "na", "nos", "nas", "em", "um", "uma",
           "que", "para", "por", "com", "pelos", "pelas", "ao", "à"}
FONTES = os.path.join(RAIZ, "instagram", "marca", "fontes")


def blocos(ws, ocultar):
    res, atual = [], []
    def fecha(forcado=False):
        resto = []
        while forcado and len(atual) > 1 and atual[-1]["palavra"].lower() in LIGACAO:
            resto.insert(0, atual.pop())
        if atual: res.append(list(atual))
        atual[:] = resto
    for i, w in enumerate(ws):
        if any(a <= w["inicio"] < b for a, b in ocultar):
            fecha(); continue
        texto = " ".join(x["palavra"] for x in atual + [w])
        if atual and w["inicio"] - atual[-1]["fim"] > 0.35:
            fecha()
        elif atual and (len(atual) >= MAX_PALAVRAS or len(texto) > MAX_CHARS):
            fecha(forcado=True)
        atual.append(w)
        if w["palavra"][-1] in ".?!,":
            fecha()
    fecha()
    return res


def main(video):
    e, pasta = carregar(video), pasta_trabalho(video)
    cfg = e["plano"]["legendas"]
    ws = json.load(open(os.path.join(pasta, "transcricao_palavras.json")))
    for w in ws:
        c = cfg.get("correcoes", {}).get(f"{w['inicio']:.2f}")
        if c: w["palavra"] = c
    corte = e["cortes"]
    t0, dur = corte["inicio"], corte["duracao"]
    fps = corte["fps"]
    chaves = {round(t, 2) for t in cfg["palavras_chave"]}
    bs = blocos(ws, cfg.get("ocultar", []))
    proj = os.path.join(pasta, "motion", "legendas")
    os.makedirs(os.path.join(proj, "fontes"), exist_ok=True)
    for f in []:  # Nunito vem do Google Fonts no @import
        if os.path.exists(os.path.join(FONTES, f)):
            shutil.copy(os.path.join(FONTES, f), os.path.join(proj, "fontes", f))
    divs, js = [], []
    for n, b in enumerate(bs):
        ini = max(0, b[0]["inicio"] - t0 - 0.12)
        prox = bs[n + 1][0]["inicio"] - t0 - 0.12 if n + 1 < len(bs) else dur
        fim = min(b[-1]["fim"] - t0 + 0.45, prox)
        spans = []
        for k, w in enumerate(b):
            chave = round(w["inicio"], 2) in chaves
            txt = html.escape(w["palavra"].rstrip(",.") if chave else w["palavra"])
            spans.append(f'<span class="p{" k" if chave else ""}" id="b{n}w{k}">{txt}</span>')
            tw = round(w["inicio"] - t0, 3)
            js.append(f'tl.fromTo("#b{n}w{k}",{{opacity:.55}},{{opacity:1,duration:.12,ease:"power2.out",lazy:false,immediateRender:false}},{tw});')
            if chave:
                js.append(f'tl.fromTo("#b{n}w{k}",{{"--m":0,scale:1}},{{"--m":1,scale:1.08,duration:.18,ease:"expo.out",lazy:false,immediateRender:false}},{tw});')
                js.append(f'tl.to("#b{n}w{k}",{{scale:1,duration:.3,ease:"power2.out",lazy:false}},{tw + 0.18:.3f});')
        divs.append(f'<div class="bloco clip" id="b{n}" data-start="{ini:.3f}" data-duration="{fim - ini:.3f}"><div class="linha">{" ".join(spans)}</div></div>')
        js.append(f'tl.fromTo("#b{n} .linha",{{opacity:0,y:14,scale:.97}},{{opacity:1,y:0,scale:1,duration:.22,ease:"expo.out",lazy:false,immediateRender:false}},{ini:.3f});')
        js.append(f'tl.to("#b{n} .linha",{{opacity:0,y:-8,duration:.12,ease:"power3.in",lazy:false}},{max(ini + 0.25, fim - 0.12):.3f});')
    raiz = (round(dur * fps) - 0.5) / fps
    doc = f"""<!doctype html>
<html lang="pt-BR" data-resolution="portrait">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400..900;1,400..900&display=block");
:root {{ --tiffany: #9FC5BD; --verde: #1F3A36; --creme: #F0F0E9; }}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: transparent; }}
#root {{ position: relative; width: 1080px; height: 1920px; font-family: "Nunito", sans-serif; }}
.bloco {{ position: absolute; left: 0; top: 1240px; width: 940px; display: flex; justify-content: center; }}
.linha {{ color: #FFFFFF; font-weight: 800; font-size: 62px; line-height: 1; letter-spacing: -.005em;
  padding: 16px 20px 20px; white-space: nowrap; opacity: 0;
  text-shadow: 0 2px 4px rgba(13, 24, 22, .6), 0 4px 22px rgba(13, 24, 22, .5); }}
.p {{ display: inline-block; opacity: .55; }}
.k {{ --m: 0; position: relative; font-weight: 900; font-style: italic; padding: 0 .14em; margin: 0 .06em; text-shadow: none; }}
.k::before {{ content: ""; position: absolute; inset: -6px -2px -8px; background: var(--tiffany); border-radius: 10px;
  transform: scaleX(var(--m)); transform-origin: left center; z-index: -1; }}
.k {{ z-index: 0; color: var(--verde); }}
</style>
</head>
<body>
<div id="root" data-composition-id="legendas" data-start="0" data-duration="{raiz:.4f}" data-width="1080" data-height="1920">
{chr(10).join(divs)}
</div>
<script>
document.fonts.ready.then(() => {{
const tl = gsap.timeline({{ paused: true }});
{chr(10).join(js)}
window.__timelines = window.__timelines || {{}};
window.__timelines["legendas"] = tl;
tl.seek(0);
}});
</script>
</body>
</html>
"""
    open(os.path.join(proj, "index.html"), "w").write(doc)
    e.setdefault("motions", {})["legendas"] = {"projeto": proj, "blocos": len(bs)}
    salvar(video, e)
    for n, b in enumerate(bs):
        print(f"lg{n + 1:02} {b[0]['inicio']:6.2f}  " + " ".join(("*" + w["palavra"] + "*") if round(w["inicio"], 2) in chaves else w["palavra"] for w in b))


if __name__ == "__main__":
    main(sys.argv[1])
