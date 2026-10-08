# Série "Quem cuida": um post (carrossel de 3 slides) por integrante do time.
# Gera individuais.html. Uso:
#   python3 instagram/posts/time/individuais.py
#   node instagram/ferramentas/render.mjs instagram/posts/time/individuais.html instagram/posts/time/png-individuais
# Textos-base: stories "Conheça nosso time" (destaques do perfil). A resposta a
# "O que é importante para você?" ainda precisa ser pedida a cada pessoa.
import pathlib

AQUI = pathlib.Path(__file__).parent

# ordem da série no calendário (M1-04, M1-07, M1-13, M1-16, M2-03)
TIME = [
    dict(id='marilia', nome='Marília', art='a', foto='../../marca/time/marilia-story.jpg', pos='center 18%',
         bio='Médica formada pela Universidade de Santo Amaro (OSEC) e pós-graduanda em Medicina do Exercício e do Esporte pela Faculdade Israelita de Ciências da Saúde Albert Einstein.',
         frase='Também é atriz e cantora, e acredita que arte e cuidado caminham juntos.'),
    dict(id='nina', nome='Nina', art='a', foto='fotos/nina.jpg', pos='center 22%',
         bio='Formada em Análise e Desenvolvimento de Sistemas e estudante de Nutrição na Universidade São Camilo.',
         frase='Acredita que tecnologia e saúde caminham juntas, e que a inovação no cuidado nasce desse encontro.'),
    dict(id='ronald', nome='Ronald', art='o', foto='../../marca/time/ronald-story.jpg', pos='center 15%',
         bio='Médico pela Escola Paulista de Medicina (UNIFESP) e formado em Direito pela PUC. Pediatra, hebiatra e médico do esporte pela UNIFESP, doutor em Ciências da Saúde e há 20 anos na gestão hospitalar.',
         frase='Fundou o Escritório do Paciente e acredita numa medicina humanizada.'),
    dict(id='floriana', nome='Floriana', art='a', foto='fotos/floriana.jpg', pos='center 20%',
         bio='Médica pela UNISA, com residência em Clínica Médica no HC-FMUSP e em Cardiologia no InCor. Especialista em Cardiologia (SBC) e em Saúde e Bem-estar (Hospital Alemão Oswaldo Cruz), ergometrista no Fleury e no Einstein e docente de pós-graduação na USCS e no Einstein.',
         frase='Fala sobre Medicina do Estilo de Vida, longevidade e saúde integral.'),
    dict(id='renata', nome='Renata', art='a', foto='fotos/renata.jpg', pos='center 25%',
         bio='Psicóloga e administradora, doutora e mestra em Administração, com especialização em gestão de saúde corporativa e em psicologia clínica. Professora da Fundação Dom Cabral.',
         frase='Palestrante e mentora em saúde, bem-estar e cultura, e conselheira consultiva em comitês de RH e NR-01.'),
]

SETA = '<svg viewBox="0 0 24 24" fill="none" stroke="#1F3A36" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" width="46" height="46"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'

CSS = """
@font-face{font-family:Raleway;font-weight:400;src:url(../../marca/fontes/raleway-latin-400-normal.woff2)}
@font-face{font-family:Raleway;font-weight:500;src:url(../../marca/fontes/raleway-latin-500-normal.woff2)}
@font-face{font-family:Raleway;font-weight:700;src:url(../../marca/fontes/raleway-latin-700-normal.woff2)}
@font-face{font-family:Raleway;font-weight:800;font-style:italic;src:url(../../marca/fontes/raleway-latin-800-italic.woff2)}
:root{--t:#9FC5BD;--td:#5FA89A;--c:#F0F0E9;--k:#1F3A36}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Raleway,sans-serif;background:#ccc}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 40px;color:var(--k)}
.slide>*{position:absolute}
.t{background:var(--t)} .c{background:var(--c)}
.lbl{font-size:24px;font-weight:700;letter-spacing:5px;padding:14px 28px;border-radius:40px}
.foto{background-size:cover;background-repeat:no-repeat}
.handle{left:96px;bottom:80px;font-size:28px;font-weight:700}
h1{font-weight:400;letter-spacing:-1.5px;line-height:1.05}
h1 b{font-weight:800;font-style:italic}
.sub{font-size:38px;line-height:1.38}
"""


def slides(i, p):
    n, a = p['nome'], p['art']
    foto = f"background-image:url(../../marca/time/{p['id']}-capa.jpg);background-position:center"
    rosto = f"background-image:url(../../marca/time/{p['id']}-quadrado.jpg);background-position:center"
    capa = f'''<section class="slide t" id="{p['id']}-1">
  <div class="foto" style="left:300px;top:96px;width:684px;height:880px;border-radius:48px;{foto}"></div>
  <div class="lbl" style="left:96px;top:120px;background:var(--c)">QUEM CUIDA</div>
  <h1 style="left:96px;top:1000px;font-size:150px"><b>{n}</b></h1>
  <p class="sub" style="left:96px;top:1172px;width:700px;font-size:34px">Conheça quem cuida de você no Escritório do Cuidado.</p>
  <div style="right:96px;top:1150px;width:104px;height:104px;border-radius:52px;background:var(--c);display:flex;align-items:center;justify-content:center">{SETA}</div>
</section>'''
    bio = f'''<section class="slide c" id="{p['id']}-2">
  <div class="lbl" style="left:96px;top:150px;background:var(--t)">QUEM CUIDA</div>
  <div class="foto" style="right:96px;top:120px;width:150px;height:150px;border-radius:36px;{rosto}"></div>
  <h1 style="left:96px;top:310px;width:888px;font-size:96px">Quem é {a}<br><b>{n}</b></h1>
  <div style="left:96px;top:560px;width:888px">
    <p class="sub" style="font-size:36px">{p['bio']}</p>
    <div style="margin-top:56px;background:var(--t);border-radius:44px;padding:48px 56px">
      <p style="font-size:38px;line-height:1.35;font-weight:800;font-style:italic">{p['frase']}</p>
    </div>
  </div>
  <div class="handle">@fairhealth.br</div>
</section>'''
    perg = f'''<section class="slide t" id="{p['id']}-3">
  <h1 style="left:96px;top:200px;font-size:88px;white-space:nowrap">A mesma pergunta<br>que fazemos a quem<br><b>cuidamos.</b></h1>
  <div style="left:96px;right:96px;top:600px;background:var(--c);border-radius:44px;padding:44px 48px;box-shadow:0 16px 40px rgba(31,58,54,.12)">
    <p style="font-size:22px;font-weight:700;letter-spacing:4px">PERGUNTAMOS {'AO' if a == 'o' else 'À'} {n.upper()}</p>
    <p style="font-size:50px;font-weight:700;line-height:1.2;margin-top:20px">O que é importante para você?</p>
  </div>
  <div class="foto" style="left:96px;top:930px;width:96px;height:96px;border-radius:28px;{rosto}"></div>
  <div style="left:216px;right:96px;top:910px;background:var(--td);border-radius:36px;padding:32px 40px">
    <p style="font-size:36px;line-height:1.35;font-weight:500">“[resposta {'do' if a == 'o' else 'da'} {n}]”</p>
  </div>
  <p class="sub" style="left:96px;top:1140px;font-size:34px">E para você, <b style="font-weight:800;font-style:italic">o que é importante?</b></p>
  <div class="handle">@fairhealth.br</div>
</section>'''
    return capa + bio + perg


html = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Série Quem cuida: um post por integrante</title><style>'
        + CSS + '</style></head><body>' + ''.join(slides(i, p) for i, p in enumerate(TIME)) + '</body></html>')
(AQUI / 'individuais.html').write_text(html)
print('ok')
