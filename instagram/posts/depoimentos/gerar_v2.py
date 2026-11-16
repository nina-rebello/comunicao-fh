"""Gera o slides.html da v2 dos depoimentos (16/11): balões de mensagem em SVG, fundo verde-escuro liso.
Uso: python3 instagram/posts/depoimentos/gerar_v2.py (rodar da raiz do repositório)"""
P='instagram/posts/depoimentos'
def balao(x,y,w,h,cor,lado,r=40,L=18):
    # balão de mensagem num SVG só (retângulo arredondado + rabicho embaixo), sem transformações, para o Canva
    W=w
    if lado=='esq':
        d=(f'M{L+r} 0 H{W-r} A{r} {r} 0 0 1 {W} {r} V{h-r} A{r} {r} 0 0 1 {W-r} {h} '
           f'H{L+26} C{L+12} {h},6 {h},0 {h} C{L-2} {h-8},{L} {h-20},{L} {h-38} V{r} A{r} {r} 0 0 1 {L+r} 0 Z')
    else:
        R=W-L
        d=(f'M{r} 0 H{R-r} A{r} {r} 0 0 1 {R} {r} V{h-38} C{R} {h-20},{R+2} {h-8},{W} {h} '
           f'C{W-6} {h},{R-12} {h},{R-26} {h} H{r} A{r} {r} 0 0 1 0 {h-r} V{r} A{r} {r} 0 0 1 {r} 0 Z')
    return (f'<div class="bal" style="left:{x}px;top:{y}px;width:{W}px;height:{h}px">'
            f'<svg width="{W}" height="{h}" viewBox="0 0 {W} {h}"><path d="{d}" fill="{cor}"/></svg></div>')
html=f'''<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Foto única 19/11: Depoimentos</title>
<link rel="stylesheet" href="../../marca/base.css">
<style>
/* Foto única de 19/11 (N09), v2 (16/11): pedido da Nina, mais elegante e menos formas (referências: balões de
   mensagem do iOS e o "Feedback de Cliente" em fundo verde chapado). Fundo verde-escuro liso; título centrado;
   três balões de mensagem com rabicho, sem avatar, sem grade e sem os tiques de lido: dois de colaboradoras
   (brancos, à esquerda) e a resposta da equipe (Tiffany, à direita); logo branco centrado no pé. Mesmo texto da v1
   (depoimentos.md: sem nome, sem condição de saúde, sem resultado clínico, cortes com [...]).
   Balões em SVG dentro de div posicionado; tudo em posição fixa, para o Canva. A v1 está em slides-v1.html. */
@font-face{{font-family:"Instrument Serif";font-style:italic;src:url(../../marca/fontes/instrument-serif-latin-400-italic.woff2)}}
.ed{{padding:0;text-align:left;align-items:stretch;justify-content:flex-start;background:#2A625B;color:#fff}}
.abs{{position:absolute;margin:0}}
.bal{{position:absolute}}
.bal svg{{display:block}}
.kicker{{position:absolute;margin:0;left:0;width:1080px;text-align:center !important;font-size:22px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:#BFE0D9}}
.tit{{position:absolute;margin:0;left:0;width:1080px;text-align:center !important;font-size:92px;font-weight:800;letter-spacing:-3.5px;line-height:1;color:#fff}}
.msg{{position:absolute;margin:0;font-size:28px;line-height:1.36;font-weight:500;color:#141B1B}}
.corte{{opacity:.45}}
.ass{{position:absolute;margin:0;font-size:16px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#2F6B64;white-space:nowrap}}
.fecho{{position:absolute;margin:0;left:0;width:1080px;text-align:center !important;font-family:"Instrument Serif",serif;font-style:italic;font-size:46px;line-height:1.1;color:#BFE0D9}}
.r-logo{{position:absolute;width:56px;height:56px;border-radius:50%}}
.r-t{{position:absolute;margin:0;font-size:26px;font-weight:700;color:#fff;white-space:nowrap}}
.miuda{{position:absolute;margin:0;left:0;width:1080px;text-align:center !important;font-size:15px;font-weight:500;line-height:1.35;color:#fff;opacity:.6}}
</style>
<style media="canva">
body{{background:none;margin:0}}
.slide{{margin:0}}
</style></head><body>

<section class="slide ed" id="d-01">
  <p class="kicker" style="top:112px">Escritório do Cuidado</p>
  <p class="tit" style="top:152px">Depoimentos</p>

  <!-- A: colaboradora (vídeo, A2 e A1) -->
  {balao(72,312,800,206,'#FFFFFF','esq')}
  <p class="msg" style="left:132px;top:340px;width:700px">Os meus hábitos mudaram, e não foi um sacrifício. <span class="corte">[...]</span><br>Não é aquela dieta impossível de fazer.<br>É algo pra vida.</p>
  <p class="ass" style="left:132px;top:470px">Colaboradora atendida</p>

  <!-- B: colaboradora (e-mail, B2 e B1) -->
  {balao(72,548,800,240,'#FFFFFF','esq')}
  <p class="msg" style="left:132px;top:576px;width:700px">Agradeço por me ajudar a olhar para as minhas conquistas com mais gentileza e reconhecer que o processo não precisa ser perfeito para estar funcionando.</p>
  <p class="ass" style="left:132px;top:742px">Colaboradora atendida</p>

  <!-- C: equipe (WhatsApp, C1 e C2) -->
  {balao(208,818,800,276,'#9FC5BD','dir')}
  <p class="msg" style="left:250px;top:846px;width:700px">Ficamos bem felizes ao ouvir de uma paciente o quanto o que estamos fazendo mudou a cultura da empresa. <span class="corte">[...]</span> Todos estão se alimentando mais saudável, se movimentando mais e fazendo melhores escolhas.</p>
  <p class="ass" style="left:250px;top:1050px">Equipe do Escritório do Cuidado</p>

  <p class="fecho" style="top:1136px">O que é bom a gente tem que compartilhar.</p>

  <img src="../../marca/logo-circulo.png" class="r-logo" alt="" style="left:422px;top:1218px">
  <p class="r-t" style="left:494px;top:1229px">@fairhealth.br</p>
  <p class="miuda" style="top:1298px">Trechos publicados com autorização e sem nomes. Cortes marcados com [...].</p>
</section>
</body></html>
'''
open(P+'/slides.html','w').write(html)
