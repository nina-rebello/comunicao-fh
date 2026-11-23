# Detalhamento dos 13 posts de novembro de 2026 (03/11 a 30/11), usado por gerar_cronograma_simples.py (modelo padrão).
# Base: instagram/plan.md (03 a 13/11), marketing/calendario-novembro/calendario.html (o mês todo),
# instagram/carrossel-de-tendencia.md (pautas de 16 a 30/11), marketing/ferramentas/conteudo_posts_19-10_a_13-11.py
# (roteiros de 14/10), os README dos posts já feitos (cuidado-na-pratica, geracao-z), instagram/voice.md,
# instagram/referencias.md e instagram/depoimentos.md.
# Regras: "fairhealth" em minúsculas, sem travessão, 5 hashtags começando por #fairhealth, número só com fonte,
# sem promessa clínica, sem preço, comunicação B2B, carrossel de 5 a 8 slides, uma chamada só.
import datetime as dt

D = lambda d: dt.date(2026, 11, d)
REEL, CARR, FOTO = 'Reel', 'Carrossel', 'Foto única'
VIS = 'Direção visual'
ESP_REEL = 'Reel 9:16 (1080 × 1920), 30 a 45 s, texto na tela desde o 1º quadro, legendas sempre. Capa 4:5 para a grade.'

# Cada roteiro: lista de (parte, texto na tela ou no slide, fala (reels), visual e direção, observação)
POSTS = [
 dict(id='N01', data=D(3), semana=1, bloco='3 · Compreensão', eixo='Produto', fmt=CARR,
  titulo='Como funciona o cuidado na prática?',
  sub='A jornada entre escuta, atendimento, plano individualizado e acompanhamento',
  status='Arte para aprovação', resp='Nina (texto) · Dr. Ronald (revisão CFM)',
  espec='Carrossel 4:5 (1080 × 1350), 6 slides, com fotos.',
  gancho='O cuidado que todo mundo queria ter no trabalho. (rótulo: Por dentro do Escritório do Cuidado · pílula: Como isso funciona na prática, em 4 pontos →)',
  objetivo='Mostrar a jornada (escuta, atendimento, plano individualizado e acompanhamento) pelo que todo mundo deseja, sem repetir a apresentação do Escritório do Cuidado.',
  portras='Cada etapa responde a um desejo comum: ser ouvido, não perder o dia, ter um plano possível e não recomeçar do zero.',
  persona='RH; Colaboradores',
  fio='Vem de: 30/10 ("Na terça: como funciona o cuidado na prática"). Leva para: 04/11, as quatro frentes.',
  visual='Uma foto por ponto, com layouts alternados (foto inteira, metade de cima, faixa, ao lado do número, saindo pela lateral). Fundos foto, off, tinta, água, off e verde-escuro. Fotos de banco (Unsplash), ilustrativas.',
  material='Fotos do banco da marca (nenhum colaborador atendido). Depoimento A1.',
  cta='Slide 3: mande este post para quem cuida das pessoas · Slide 6: Comente CUIDADO (como funciona o Escritório do Cuidado)',
  stories='Repost do slide 2 com a caixa de perguntas "O que importa para você hoje?".',
  fonte='Executive Summary (plataforma com prontuário, histórico e metas); depoimento A1 (instagram/depoimentos.md).',
  validar='Formato do depoimento A1 com o Dr. Ronald; revisão do texto (CFM); alguém para responder as DMs do CUIDADO até a resposta automática ficar pronta.',
  arquivos='instagram/posts/cuidado-na-pratica/ (png/c-01 a c-06, canva.html, cuidado-na-pratica.pdf)',
  legenda='''O cuidado que todo mundo queria ter no trabalho tem endereço: o Escritório do Cuidado.

Ser ouvido, não perder o dia, ter um plano possível e não precisar recomeçar do zero. Na prática, funciona assim.

Às vezes, o que tira o sono é o turno, a conta do mês ou a casa. Por isso a primeira consulta começa por uma pergunta: o que importa para você? A rotina e o que anda pesando vêm antes de qualquer conduta.

O atendimento fica a poucos passos de quem trabalha. Médico, psicólogo e assistente social dentro da empresa, presencial ou remoto, sem meio período perdido entre trânsito e sala de espera.

O plano é combinado com a pessoa, tem base na Medicina do Estilo de Vida e cabe na rotina real. Como disse uma colaboradora atendida: "Não é aquela dieta impossível de fazer. É algo pra vida."

E o cuidado continua. Histórico e metas ficam registrados na plataforma, e a cada retorno o plano é revisto. O que é conversado fica no atendimento. Para cuidar da saúde corporativa, o RH recebe só indicadores do grupo, anonimizados.

Quer esse cuidado para o seu time? Comente CUIDADO e enviamos na DM como funciona o Escritório do Cuidado.

#fairhealth #saudecorporativa #medicinadoestilodevida #cuidadocentradonapessoa #gestaodepessoas''',
  roteiro=[
   ('Slide 1 · capa', 'Por dentro do Escritório do Cuidado\nO cuidado que todo mundo queria ter no trabalho.\nComo isso funciona na prática, em 4 pontos →', '', 'Foto colorida inteira (conversa no escritório), título no terço de baixo.', ''),
   ('Slide 2 · Ser ouvido', 'Todo mundo quer ser ouvido de verdade.\nÀs vezes, o que tira o sono é o turno, a conta do mês ou a casa. Por isso, no Escritório do Cuidado, a primeira consulta começa por uma pergunta: o que importa para você?\nCuidado começa pela história, não pelo sintoma.', '', 'Fundo claro, foto (mãos dadas) na metade de cima.', ''),
   ('Slide 3 · Cuidado por perto', 'Ninguém quer perder meio dia por uma consulta.\nPor isso o cuidado fica dentro da empresa: médico, psicólogo e assistente social a poucos passos de quem trabalha, presencial ou remoto.\nSem trânsito e sem sala de espera.', '', 'Fundo escuro, foto (profissional de capacete) numa faixa à direita.', 'CTA de envio: Conhece quem cuida das pessoas na sua empresa? Mande este post.'),
   ('Slide 4 · Um plano possível', 'Quem nunca recebeu uma dieta impossível?\nNo Escritório do Cuidado, o plano é combinado com a pessoa e cabe na rotina real: dormir meia hora mais cedo, almoçar longe da mesa. A base é a Medicina do Estilo de Vida.\n"Não é aquela dieta impossível de fazer. É algo pra vida." Colaboradora atendida pelo Escritório do Cuidado', '', 'Fundo água (virada), número grande e foto (prato) ao lado.', 'Depoimento A1.'),
   ('Slide 5 · Continuidade', 'Ninguém quer começar do zero a cada consulta.\nA equipe acompanha cada pessoa. Histórico e metas ficam na plataforma, e a cada retorno o plano é revisto. Sigilo. Pode falar: o que é conversado fica no atendimento. O RH recebe só indicadores do grupo, anonimizados.\nO plano muda quando a vida muda.', '', 'Fundo claro, foto (escada) saindo pela lateral.', ''),
   ('Slide 6 · convite', 'Quer esse cuidado para o seu time?\nComente CUIDADO e enviamos na DM como funciona o Escritório do Cuidado.\nNa quarta: quatro frentes, um cuidado conectado.', '', 'Verde-escuro, sem foto.', 'Ponte para o 04/11.'),
  ]),

 dict(id='N02', data=D(4), semana=1, bloco='3 · Compreensão', eixo='Produto', fmt=REEL,
  titulo='Quatro frentes, um cuidado conectado',
  sub='Medicina do Estilo de Vida, Escritório do Cuidado, wearables e o relatório para o RH',
  status='Roteiro proposto', resp='Nina · fairdata (relatório)',
  espec='Reel 9:16 (1080 × 1920), 25 a 30 s, motion (sem pessoas em cena). Capa 4:5.',
  gancho='Quatro frentes. Um cuidado só.',
  objetivo='Mostrar que Medicina do Estilo de Vida, Escritório do Cuidado, wearables e plataforma funcionam juntos e que, para o RH, o que a plataforma entrega é o relatório.',
  portras='Não são quatro produtos: é um cuidado só. Para o RH, menos sobre a plataforma e mais sobre o relatório que ela entrega.',
  persona='RH; RI e C-Level',
  fio='Vem de: 03/11, a jornada de uma pessoa. Leva para: 06/11, de onde vem esse método.',
  visual='Motion em Tiffany e verde. Um fio contínuo (creme) passa por quatro pontos; em cada ponto, um ícone linear fino e o nome da frente. No fim, o fio desenha a página de um relatório com barras simples (dados de exemplo, sem números reais).',
  material='Motion no Canva, ícones lineares finos, trilha calma. Sem pessoas em cena.',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  stories='Quiz: "Qual destas frentes acompanha a rotina entre as consultas?" (resposta: wearables).',
  fonte='Executive Summary e one-pager (11/10): as quatro peças. Nota do calendário: "Para o RH: a plataforma entrega relatório".',
  validar='Nomes das frentes iguais aos do one-pager. O que o relatório do RH mostra de fato (fairdata): não mostrar indicador que ainda não existe. Publicação hoje (04/11): o roteiro precisa de aprovação rápida.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/quatro-frentes/',
  legenda='''Não são quatro produtos soltos. É um cuidado só.

O Escritório do Cuidado leva médico, psicólogo e assistente social para dentro da empresa. O Programa de Medicina do Estilo de Vida leva informação para todos. Os wearables acompanham a rotina entre uma consulta e outra.

E a plataforma junta tudo num relatório para o RH, com indicadores do grupo, anonimizados. O que cada pessoa conta fica no atendimento. O que o RH recebe é a visão do todo, para decidir onde cuidar primeiro.

Quer ver como isso funciona na sua empresa? Comente CUIDADO e enviamos na DM como funciona o Escritório do Cuidado.

#fairhealth #saudecorporativa #medicinadoestilodevida #escritoriodocuidado #gestaodepessoas''',
  roteiro=[
   ('0 a 3 s', 'Quatro frentes. Um cuidado só.', '', 'O fio entra pela esquerda sobre fundo Tiffany.', 'Gancho.'),
   ('3 a 8 s', 'Escritório do Cuidado\nMédico, psicólogo e assistente social dentro da empresa.', '', 'Ponto 1 no fio, ícone de porta.', ''),
   ('8 a 13 s', 'Medicina do Estilo de Vida\nInformação e letramento para todo o time.', '', 'Ponto 2, ícone de folha.', ''),
   ('13 a 18 s', 'Wearables\nA rotina acompanhada entre uma consulta e outra.', '', 'Ponto 3, ícone de pulseira.', ''),
   ('18 a 24 s', 'Relatório para o RH\nIndicadores do grupo, anonimizados.', '', 'Ponto 4: o fio vira a página de um relatório com barras simples.', 'Foco no relatório, não na plataforma.'),
   ('24 a 27 s', 'O que cada pessoa conta fica no atendimento.', '', 'O relatório se fecha; o fio volta a ser linha.', 'Sigilo.'),
   ('27 a 30 s', 'fairhealth\nComente CUIDADO', '', 'Logo sobre Tiffany.', ''),
  ]),

 dict(id='N03', data=D(6), semana=1, bloco='4 · Confiança', eixo='Cases', fmt=CARR,
  titulo='Uma história de cuidado que começou em 2009',
  sub='A história do Escritório, do hospital em 2009 até as empresas',
  status='Roteiro proposto', resp='Nina · Dr. Ronald (validação da história)',
  espec='Carrossel 4:5 (1080 × 1350), 7 slides.',
  gancho='Antes de chegar às empresas, esse cuidado nasceu num hospital.',
  objetivo='Contar a história do Escritório (do Paciente ao Cuidado), e não da fairhealth, e mostrar que o método tem trajetória.',
  portras='O método não é novo: tem 15 anos de prática e acompanha as metas internacionais da saúde.',
  persona='RH; Medicina do Trabalho; RI e C-Level',
  fio='Vem de: 04/11, as quatro frentes. Leva para: 09/11, os resultados, com o Dr. Ronald.',
  visual='Linha do tempo no fio contínuo, um marco por slide, ano grande e fino. Capa com foto de corredor de hospital (banco, ilustrativa) ou fundo chapado; miolo alternando verde e Tiffany.',
  material='Tipografia, o fio e uma foto de banco na capa.',
  cta='Salve para mostrar a quem decide sobre saúde na sua empresa',
  stories='Slide 2 com a enquete "Você conhecia o Escritório do Paciente?".',
  fonte='instagram/essencia.md ("De onde veio"); IHI Triple Aim (2008); Quadruple Aim (2014); Quintuple Aim (2021); Hospital Dia Santo Amaro, 2025 (liberado em voice.md).',
  validar='Validar com o Dr. Ronald a história do Escritório (ano, hospital, como funcionava). Conferir a descrição de cada Aim. Caso do hospital: liberado em voice.md, mas a decisão de 30/10 tirou dados de clientes dos posts; confirmar se entra. "Validado no SUS" fica de fora.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/historia-2009/',
  legenda='''Antes de chegar às empresas, esse cuidado nasceu num hospital, em 2009.

O Escritório do Paciente começou como um espaço para ouvir quem estava sendo atendido e resolver o que travava o cuidado. Ao longo dos anos, acompanhou as grandes metas internacionais da saúde: a experiência do paciente, a saúde da população e o custo; depois o cuidado com quem cuida; depois a equidade.

Em 2025, num hospital-dia, as reclamações mensais caíram de 34 para cerca de 20. O estudo foi apresentado em congresso internacional.

Em 2024 e 2025, o mesmo método saiu do hospital e entrou nas empresas, como Escritório do Cuidado, com a Medicina do Estilo de Vida.

Salve para mostrar a quem decide sobre saúde na sua empresa.

#fairhealth #saudecorporativa #experienciadopaciente #cuidadocentradonapessoa #escritoriodocuidado''',
  roteiro=[
   ('Slide 1 · capa', 'Antes de chegar às empresas, esse cuidado nasceu num hospital.', '', 'Foto de corredor de hospital (banco) ou fundo chapado com "2009" grande.', 'Sem numeração de slide.'),
   ('Slide 2 · 2009', 'Escritório do Paciente\nDentro de um hospital, um espaço para ouvir quem estava sendo atendido e resolver o que travava o cuidado.', '', 'Fundo verde, ano grande em Tiffany.', 'Validar com o Dr. Ronald.'),
   ('Slide 3 · o contexto', 'Triple Aim\nNo mesmo período, a saúde passa a olhar junto para a experiência do paciente, a saúde da população e o custo.', '', 'Fundo Tiffany.', 'IHI, 2008. Conferir a descrição.'),
   ('Slide 4 · 2014 e 2021', 'Quadruple e Quintuple Aim\nEntram duas metas: cuidar de quem cuida (2014) e a equidade (2021).', '', 'Fundo verde, dois pontos no fio.', ''),
   ('Slide 5 · na prática', 'Num hospital-dia, as reclamações mensais caíram de 34 para cerca de 20.\nFonte: Hospital Dia Santo Amaro, 2025, estudo apresentado em congresso internacional.', '', 'Fundo Tiffany, número calmo.', 'Confirmar se entra (decisão de 30/10 sobre dados de clientes).'),
   ('Slide 6 · 2024 e 2025', 'Escritório do Cuidado\nO método sai do hospital e entra na empresa: médico, psicólogo e assistente social perto de quem trabalha, com a Medicina do Estilo de Vida.', '', 'Fundo verde, o fio chega ao logo.', ''),
   ('Slide 7 · chamada', 'Salve para mostrar a quem decide sobre saúde na sua empresa.\nNa segunda: o que o Dr. Ronald viu na prática.', '', 'Fundo Tiffany, logo.', 'Ponte para o 09/11.'),
  ]),

 dict(id='N04', data=D(9), semana=2, bloco='4 · Confiança', eixo='Cases', fmt=REEL,
  titulo='Cuidado na prática: experiências e resultados reais',
  sub='Evidências e resultados documentados, contados pelo Dr. Ronald',
  status='Roteiro proposto', resp='Dr. Ronald (gravação) · Nina',
  espec=ESP_REEL,
  gancho='Programa de saúde dá retorno?',
  objetivo='Responder, na voz de um médico, a pergunta que o RH faz ao fechar o orçamento de 2027: as pessoas usam, voltam, e os estudos mostram o que vem depois.',
  portras='Ninguém volta a um lugar onde não se sentiu cuidado. O primeiro retorno aparece antes de qualquer planilha.',
  persona='RH; Diretoria financeira',
  fio='Vem de: 06/11, a trajetória do método. Leva para: 11/11, a ciência por trás desse cuidado.',
  visual='Mesmo cenário e enquadramento do reel de 19/10, para a série ficar reconhecível. Números na tela em verde-escuro sobre Tiffany, com a fonte em texto pequeno. Legendas sempre.',
  material='Gravação vertical, microfone de lapela, luz natural. Autorização de uso de imagem do Dr. Ronald.',
  cta='Mande para quem está fechando o orçamento de 2027',
  stories='Repost com "8 em cada 10 voltaram" e a caixa de perguntas "O que você quer saber sobre o retorno de um programa de saúde?".',
  fonte='Dados internos de uma indústria atendida, 1º semestre de 2026 (voice.md): 81,3% voltaram para 2 ou mais atendimentos; 98% de adesão. Estudos oficiais: −28% de absenteísmo (Harvard Business Review, 2022) e −22% de custos com saúde (SHRM, 2023).',
  validar='Números de cliente: a decisão de 30/10 tirou dados de clientes dos posts; confirmar com os sócios se este reel pode usar os números (sempre sem o nome). Se não puder, o reel fica só com os estudos da HBR e da SHRM. Data de gravação com o Dr. Ronald.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/resultados-reais/',
  legenda='''Programa de saúde dá retorno? É a pergunta de quem está fechando o orçamento de 2027.

O Dr. Ronald responde pelo primeiro sinal, que aparece antes de qualquer planilha: as pessoas voltam. Numa indústria que atendemos, no primeiro semestre de 2026, 8 em cada 10 colaboradores voltaram para dois ou mais atendimentos, e a adesão chegou a 98%.

Ninguém volta a um lugar onde não se sentiu cuidado.

E os estudos mostram o que vem depois, quando a empresa cuida antes: menos 28% de absenteísmo (Harvard Business Review, 2022) e menos 22% de custos com saúde (SHRM, 2023).

Mande este reel para quem está fechando o orçamento de 2027 na sua empresa.

#fairhealth #saudecorporativa #medicinapreventiva #escritoriodocuidado #gestaodepessoas''',
  roteiro=[
   ('0 a 3 s', 'Programa de saúde dá retorno?', 'Toda empresa que fecha o orçamento de 2027 faz essa pergunta: programa de saúde dá retorno?', 'Plano médio, olhar na câmera.', 'Gancho.'),
   ('3 a 10 s', 'O primeiro sinal: as pessoas voltam.', 'O primeiro sinal aparece antes de qualquer planilha. As pessoas voltam. E ninguém volta a um lugar onde não se sentiu cuidado.', 'Plano mais fechado.', ''),
   ('10 a 20 s', '8 em cada 10 voltaram\n98% de adesão\n(uma indústria atendida, 1º semestre de 2026)', 'Numa indústria que a gente atende, 8 em cada 10 pessoas voltaram para mais de um atendimento. A adesão chegou a 98%.', 'Números entram na tela em Tiffany.', 'Depende da liberação dos dados de cliente.'),
   ('20 a 30 s', '−28% de absenteísmo (HBR, 2022)\n−22% de custos com saúde (SHRM, 2023)', 'E os estudos mostram o que vem depois: quando a empresa cuida antes, caem as faltas e cai o custo com saúde.', 'Números com a fonte em texto pequeno.', 'Números oficiais (decisão de 25/09).'),
   ('30 a 36 s', 'Perto · com escuta · para cada pessoa', 'Isso acontece porque o cuidado está perto, começa por uma conversa e é feito para cada pessoa.', 'Volta ao plano médio.', ''),
   ('36 a 40 s', 'Na quarta: a ciência por trás desse cuidado.', 'Na quarta, a gente mostra a ciência por trás desse jeito de cuidar.', 'Logo sobre Tiffany.', 'Ponte para o 11/11.'),
  ]),

 dict(id='N05', data=D(11), semana=2, bloco='4 · Confiança', eixo='Cultura', fmt=CARR,
  titulo='Estilo de vida também é tratamento sério',
  sub='O que a ciência mostra sobre mudar a rotina, na semana do Dia Mundial do Diabetes',
  status='Roteiro proposto', resp='Nina · responsável médica (leitura do estudo)',
  espec='Carrossel 4:5 (1080 × 1350), 7 slides.',
  gancho='Estilo de vida também é tratamento sério.',
  objetivo='Mostrar a base científica da Medicina do Estilo de Vida com um estudo clássico, na semana do Dia Mundial do Diabetes (sábado, 14/11).',
  portras='A rotina importa, e há ciência por trás disso. Por isso o cuidado começa nela.',
  persona='RH; Medicina do Trabalho; Colaboradores',
  fio='Vem de: 09/11, os resultados. Leva para: 13/11, como levar o cuidado para a empresa.',
  visual='Modelo de dado com fonte, suave, nos slides 3 e 4. Números em verde-escuro, sem alarme. Alternativa de capa (carrossel-de-tendencia.md): "Todo mundo fala das canetas. Pouca gente fala do que vem depois." (sem marca, dose ou indicação).',
  material='Tipografia e o fio. Uma foto de banco (refeição, caminhada) é opcional.',
  cta='Mande para quem cuida da saúde do seu time',
  stories='Sábado, 14/11: story do Dia Mundial do Diabetes com o slide 4 e o link para o post.',
  fonte='Diabetes Prevention Program Research Group. Reduction in the incidence of type 2 diabetes with lifestyle intervention or metformin. N Engl J Med. 2002;346(6):393-403. doi:10.1056/NEJMoa012512',
  validar='A responsável médica valida a leitura do estudo: adultos com risco aumentado, não é promessa individual. Se a capa for a das canetas, revisão do Dr. Ronald (CFM).',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/estilo-de-vida/',
  legenda='''Mudar a rotina faz diferença de verdade? A ciência responde.

Num estudo clássico, publicado no New England Journal of Medicine, 3.234 adultos com risco aumentado de diabetes tipo 2 foram acompanhados por quase 3 anos. Quem mudou a rotina, com alimentação e 150 minutos de atividade física por semana, teve 58% menos casos novos do que o grupo placebo. No grupo que recebeu medicamento, a queda foi de 31%.

Não é promessa individual. É a ciência mostrando que a rotina importa. No trabalho, isso vira um plano de cuidado combinado com cada pessoa, com base na Medicina do Estilo de Vida e revisto a cada retorno.

Neste sábado, 14/11, é o Dia Mundial do Diabetes. Mande este post para quem cuida da saúde do seu time.

Fonte: Diabetes Prevention Program Research Group, N Engl J Med, 2002.

#fairhealth #medicinadoestilodevida #diamundialdodiabetes #saudecorporativa #prevencao''',
  roteiro=[
   ('Slide 1 · capa', 'Estilo de vida também é tratamento sério.', '', 'Fundo Tiffany, título grande.', ''),
   ('Slide 2 · promessa', 'Neste sábado, 14/11, é o Dia Mundial do Diabetes.\nVale lembrar de um estudo que mudou a forma de cuidar.', '', 'Fundo verde.', 'Funciona sozinho.'),
   ('Slide 3 · o estudo', '3.234 adultos com risco aumentado de diabetes tipo 2, acompanhados por quase 3 anos.', '', 'Fundo Tiffany.', ''),
   ('Slide 4 · o dado', 'Quem mudou a rotina (alimentação e 150 minutos de atividade física por semana) teve 58% menos casos novos do que o grupo placebo.', '', 'Fundo verde, "58%" em Tiffany, calmo.', ''),
   ('Slide 5 · a comparação', 'No grupo que recebeu medicamento, a queda foi de 31%.', '', 'Texto menor, fundo claro.', ''),
   ('Slide 6 · no trabalho', 'No Escritório do Cuidado, isso vira um plano combinado com cada pessoa, com base na Medicina do Estilo de Vida, revisto a cada retorno.', '', 'Fundo Tiffany.', 'Sem slide-resumo explícito: o fato fala.'),
   ('Slide 7 · chamada', 'Mande para quem cuida da saúde do seu time.\nFonte: Diabetes Prevention Program, N Engl J Med, 2002.', '', 'Fundo verde, logo.', ''),
  ]),

 dict(id='N06', data=D(13), semana=2, bloco='4 · Confiança', eixo='Produto', fmt=CARR,
  titulo='Como levar a fairhealth para a sua empresa?',
  sub='Encerramento da apresentação inicial com orientação para o RH',
  status='Roteiro proposto', resp='Nina · Comunicação (DMs)',
  espec='Carrossel 4:5 (1080 × 1350), 6 slides. Post comercial.',
  gancho='O orçamento de 2027 está fechando. Onde entra o cuidado?',
  objetivo='Fechar a apresentação inicial com um caminho claro para o RH: conversa, proposta e implementação.',
  portras='Começar é simples e não pede decisão grande: o primeiro passo é uma conversa.',
  persona='RH; Diretoria financeira',
  fio='Vem de: 11/11, a ciência. Fecha os 4 blocos de 19/10 a 13/11. Leva para: as pautas de atualidade (16/11 em diante).',
  visual='Três passos no fio contínuo. Capa com foto de mesa de reunião (banco) ou fundo verde-escuro. Último slide verde-escuro com a palavra CUIDADO em destaque.',
  material='Tipografia e o fio.',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  stories='Sequência com os 3 passos e o adesivo "Mande uma mensagem".',
  fonte='Executive Summary: entrada comercial (proposta personalizada, implementação com onboarding e primeiros atendimentos). O diagnóstico gratuito não existe (Nina, 12/11).',
  validar='Resposta automática da palavra CUIDADO no ar até 13/11. Quem responde as DMs. Sem prazos de etapa e sem preço. NR-1: "apoio na prevenção", nunca "conformidade".',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/como-levar/',
  legenda='''O orçamento de 2027 está fechando. Onde entra o cuidado?

Levar o Escritório do Cuidado para a sua empresa começa por uma conversa. São três passos.

Primeiro, uma conversa para entender o time, os turnos e o que mais pesa hoje. Depois, uma proposta personalizada, do tamanho e da rotina da sua empresa. Por fim, a implementação, com onboarding e os primeiros atendimentos: médico, psicólogo e assistente social perto de quem trabalha.

O RH acompanha tudo por indicadores do grupo, anonimizados, e ganha apoio na prevenção de riscos psicossociais (NR-1).

Comente CUIDADO e enviamos na DM como funciona o Escritório do Cuidado.

#fairhealth #saudecorporativa #gestaodepessoas #rh #escritoriodocuidado''',
  roteiro=[
   ('Slide 1 · capa', 'O orçamento de 2027 está fechando.\nOnde entra o cuidado?', '', 'Foto de mesa de reunião (banco) ou fundo verde-escuro.', ''),
   ('Slide 2 · conversa', 'Começa por uma conversa.\nPara entender o time, os turnos e o que mais pesa hoje.', '', 'Fundo claro, primeiro ponto no fio.', 'Funciona sozinho.'),
   ('Slide 3 · proposta', 'Proposta personalizada\nO programa desenhado para o tamanho e a rotina da sua empresa.', '', 'Fundo Tiffany, segundo ponto.', 'Sem preço.'),
   ('Slide 4 · implementação', 'Implementação\nOnboarding e primeiros atendimentos, com médico, psicólogo e assistente social perto de quem trabalha.', '', 'Fundo verde, terceiro ponto.', 'Sem prazos.'),
   ('Slide 5 · o que o RH acompanha', 'Indicadores do grupo, anonimizados.\nApoio na prevenção de riscos psicossociais (NR-1).', '', 'Fundo claro, página de relatório estilizada.', 'Nunca "conformidade".'),
   ('Slide 6 · chamada', 'Comente CUIDADO\ne enviamos na DM como funciona o Escritório do Cuidado.', '', 'Verde-escuro, CUIDADO em destaque, logo.', ''),
  ]),

 dict(id='N07', data=D(16), semana=3, bloco='5 · Atualidade', eixo='Cultura', fmt=REEL,
  titulo='Novembro Azul: ele só vai ao médico quando dói',
  sub='O homem adia o cuidado porque cuidar dá trabalho; com o cuidado na empresa, a barreira cai o ano todo',
  status='Pauta proposta (calendário de novembro)', resp='Nina · Dr. Ronald (revisão técnica)',
  espec=ESP_REEL + ' Tipografia animada, sem pessoas em cena.',
  gancho='Ele só vai ao médico quando dói.',
  objetivo='Entrar no Novembro Azul pelo ângulo do trabalho: o homem adia o cuidado porque cuidar dá trabalho, e o cuidado dentro da empresa tira essa barreira o ano todo.',
  portras='Não é descuido: é atrito. Quando a consulta cabe no intervalo, a barreira cai.',
  persona='RH; Colaboradores',
  fio='Vem de: 13/11, como levar o cuidado à empresa. Leva para: 18/11, afastamentos e NR-01.',
  visual='Tipografia animada sobre fundo azul-acinzentado da paleta (sem azul de campanha que fuja da marca), uma frase por vez. Fecho em Tiffany com o logo.',
  material='Canva (animação de texto), trilha calma. Opcional: imagens de banco de rotina de trabalho (capacete, crachá, relógio), sem rosto.',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  stories='Enquete: "Quando foi a última vez que você foi ao médico sem estar doente?" (Neste ano · Faz tempo).',
  fonte='{{dado sobre homens e consultas + fonte}}: buscar pesquisa recente (Ministério da Saúde, SBU ou Fiocruz) e conferir na fonte original.',
  validar='Revisão técnica do Dr. Ronald (CFM): nada sobre exame específico, diagnóstico ou promessa. Conferir o dado sobre homens e saúde na fonte original. Sem carona em caso de famoso.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/novembro-azul/',
  legenda='''Ele só vai ao médico quando dói. E quase nunca é descuido.

Cuidar dá trabalho: marcar, pedir para sair mais cedo, atravessar a cidade, esperar. Para quem trabalha em turno, isso pode custar meio dia. Então a consulta fica para depois, até virar urgência.

Quando o cuidado está dentro da empresa, a conta muda. Médico, psicólogo e assistente social a poucos passos de quem trabalha, e a consulta cabe no intervalo.

O Novembro Azul dura um mês. O cuidado pode durar o ano todo.

Comente CUIDADO e enviamos na DM como funciona o Escritório do Cuidado.

#fairhealth #novembroazul #saudedohomem #saudecorporativa #medicinapreventiva''',
  roteiro=[
   ('0 a 3 s', 'Ele só vai ao médico quando dói.', '', 'Frase única, grande, sobre fundo escuro.', 'Gancho.'),
   ('3 a 8 s', 'Não é descuido.\nÉ que cuidar dá trabalho.', '', 'Duas linhas, uma por vez.', ''),
   ('8 a 13 s', 'Marcar. Pedir para sair. Atravessar a cidade. Esperar.', '', 'Palavras entram em sequência, ritmo de lista.', ''),
   ('13 a 18 s', '{{dado sobre homens e consultas + fonte}}', '', 'Número calmo, fonte em texto pequeno.', 'Se não houver dado confiável, cortar a cena.'),
   ('18 a 24 s', 'Com o cuidado dentro da empresa,\na consulta cabe no intervalo.', '', 'Fundo muda para Tiffany.', 'Virada.'),
   ('24 a 28 s', 'O Novembro Azul dura um mês.\nO cuidado pode durar o ano todo.', '', 'Duas linhas.', ''),
   ('28 a 30 s', 'fairhealth\nComente CUIDADO', '', 'Logo sobre Tiffany.', ''),
  ]),

 dict(id='N08', data=D(18), semana=3, bloco='5 · Atualidade', eixo='Notícias + Mercado', fmt=CARR,
  titulo='Recorde de afastamentos por saúde mental: o que a NR-01 cobra do RH',
  sub='O dado mais recente de afastamentos e o que a NR-01 pede: medir e cuidar dos riscos psicossociais',
  status='Texto aprovado (04/11) · v5 em 6 slides e legenda (ig-caption) para aprovação', resp='Nina · Dr. Ronald (NR-01 e saúde mental)',
  espec='Carrossel 4:5 (1080 × 1350), 6 slides, estilo institucional.',
  gancho='546,2 mil afastamentos do trabalho por saúde mental no Brasil em 2025, concedidos pelo INSS. E agora, RH?',
  objetivo='Usar o dado mais recente de afastamentos para explicar o que a NR-01 pede sobre riscos psicossociais: medir e cuidar, com a fairdata no diagnóstico e o Escritório do Cuidado no cuidado.',
  portras='A própria NR-01 (item 1.5.3.2) pede os dois lados: identificar, avaliar e classificar os riscos, e implementar medidas e acompanhar. Sem desvalorizar o mapeamento, que a fairdata faz (pedido da Nina, 04/11).',
  persona='RH; Medicina do Trabalho; SST',
  fio='Vem de: 16/11, Novembro Azul. Leva para: 19/11, a voz de quem é cuidado.',
  visual='Padrão dos carrosséis de 03/11 e 11/11: papel e creme com brilho Tiffany, marca-texto com textura, gráfico desenhado com anotação à mão, print do texto oficial da NR-01, balão "E agora, RH?" na capa e no fim. Uma foto de banco (conversa) no slide 5. CVV 188 no slide final.',
  material='PDF oficial da NR-01 (MTE), guia do MTE sobre fatores de riscos psicossociais, uma foto de banco.',
  cta='Fale com a gente pelo link da bio e leve o Escritório do Cuidado para a sua empresa (escolha da Nina, 04/11)',
  stories='Caixa de perguntas: "Qual a sua maior dúvida sobre a NR-01?" (respostas viram conteúdo).',
  fonte='Ministério da Previdência Social (nota oficial na Agência Gov, jan/2026): 546.254 benefícios por incapacidade temporária concedidos pelo INSS por transtornos mentais e comportamentais em 2025, 15,66% acima de 2024 (472.328); também no g1. Segundo recorde seguido. NR-01: texto atualizado no gov.br (MTE), itens 1.5.3.1.4 e 1.5.3.2, redação da Portaria MTE nº 1.419/2024, em vigor desde 26/05/2026 (Portaria MTE nº 765/2025). Lista de fatores: Guia de informações sobre os fatores de riscos psicossociais relacionados ao trabalho (MTE, 2025), listagem exemplificativa de 13 fatores.',
  validar='Conferir com o Dr. Ronald a situação da NR-01 (vigência e o que é exigido). Menção à fairdata no slide 5. Legenda feita com a ig-caption e revisada com a ig-human (04/11). Sem alarmismo ("epidemia", "bomba-relógio"). Nunca prometer conformidade com a NR-01.',
  arquivos='instagram/posts/nr01-afastamentos/ (png/n-01 a n-06, canva.html, nr01-afastamentos.pdf; alternativa do slide 3 em png-alternativas/ e canva-alternativas.html)',
  legenda='''546,2 mil afastamentos do trabalho por saúde mental em 2025. É o segundo recorde seguido. E agora, RH?

Os dados são do Ministério da Previdência Social: o INSS concedeu 546,2 mil licenças por transtornos mentais e comportamentais em 2025, 15,7% a mais que em 2024.

Desde maio de 2026, a NR-01 pede que a empresa identifique e gerencie os riscos psicossociais junto com os outros riscos ocupacionais. O guia do Ministério do Trabalho e Emprego dá exemplos: sobrecarga, falta de apoio, assédio, baixa clareza de papel e baixo controle sobre o trabalho.

A norma trata a saúde mental no trabalho em duas frentes. Medir: identificar, avaliar e classificar os riscos. Cuidar: implementar medidas de prevenção e acompanhar o controle dos riscos.

Com a fairdata, a empresa tem o diagnóstico dos riscos do grupo. Com o Escritório do Cuidado, médico, psicólogo e assistente social ficam dentro da empresa, com escuta, acompanhamento e encaminhamento, e o RH recebe indicadores do grupo, anonimizados.

Quer levar o Escritório do Cuidado para a sua empresa? Fale com a gente pelo link da bio.

Se você precisa de ajuda agora, o CVV atende pelo 188, 24 horas.

#fairhealth #nr01 #saudemental #saudecorporativa #riscospsicossociais''',
  roteiro=[
   ('Slide 1 · capa', 'Saúde mental no trabalho\n546,2 mil afastamentos do trabalho por saúde mental\nno Brasil em 2025, concedidos pelo INSS.\nFonte: Ministério da Previdência Social.\nBalão: E agora, RH?', '', 'Creme com brilho Tiffany, número gigante, marca-texto em "por saúde mental", balão verde.', 'O número conta benefícios por incapacidade temporária (auxílio-doença) concedidos, não pessoas: não trocar por "546 mil trabalhadores".'),
   ('Slide 2 · o dado', 'O dado\n546,2 mil licenças por transtornos mentais em 2025, o segundo recorde seguido.\nGráfico: 472,3 mil (2024) e 546,2 mil (2025), +15,7%.\nFonte: Ministério da Previdência Social (nota oficial, jan/2026).', '', 'Papel, barras com textura na mesma escala, anotação à mão.', 'Se sustenta sozinho.'),
   ('Slide 3 · a norma', 'A norma\nNR-01\nDesde maio de 2026, a NR-01 pede que a empresa identifique e gerencie os riscos psicossociais, junto com os outros riscos ocupacionais.\nPrint do texto oficial: vigência (26/05/2026) e itens 1.5.3.1.4 e 1.5.3.2.', '', 'Verde-escuro, print do PDF do MTE colado com fita, marca-texto no trecho dos riscos psicossociais.', 'Alternativa: o recorte digitado (png-alternativas/).'),
   ('Slide 4 · o que é risco psicossocial', 'Exemplos da lista do Ministério do Trabalho e Emprego: os 13 fatores do guia, na ordem e com as palavras do guia.\nFonte: Guia de informações sobre os fatores de riscos psicossociais relacionados ao trabalho (MTE, 2025). A lista é exemplificativa.', '', 'Tiffany, folha com lista numerada.', ''),
   ('Slide 5 · medir e cuidar', 'Medir e cuidar: a norma pede os dois.\nMedir: b) identificar os perigos, c) avaliar os riscos, d) classificar os riscos. Com a fairdata: o diagnóstico dos riscos do grupo.\nCuidar: e) implementar medidas de prevenção, f) acompanhar o controle dos riscos. Com o Escritório do Cuidado: escuta, acompanhamento e encaminhamento.\nFonte: NR-01, item 1.5.3.2.', '', 'Foto de conversa no alto, dois cartões (claro e verde-escuro).', 'Ponte para o produto, sem desvalorizar o mapeamento (fairdata).'),
   ('Slide 6 · chamada', 'Balão: E agora, RH?\nFale com a gente pelo link da bio\ne leve o Escritório do Cuidado para a sua empresa.\nPrecisa de ajuda agora? CVV 188.', '', 'Creme com brilho, marca-texto em "pelo link da bio.", logo.', 'Retoma a capa. Escolha da Nina (04/11); "curta, comente e compartilhe" ficou como alternativa. Todo post de saúde mental termina com onde pedir ajuda.'),
  ]),

 dict(id='N09', data=D(19), semana=3, bloco='5 · Atualidade', eixo='Cases', fmt=FOTO,
  titulo='Depoimentos: três vozes do Escritório do Cuidado em balões de conversa',
  sub='A voz de quem é cuidado: mudança real, sem promessa de resultado clínico',
  status='Arte v1 para aprovação (04/11)', resp='Nina · Dr. Ronald (formato dos depoimentos)',
  espec='Foto única 4:5 (1080 × 1350). Depoimentos em balões de conversa (referência enviada pela Nina em 04/11). Quinta-feira, porque sexta (20/11) é feriado.',
  gancho='"Os meus hábitos mudaram, e não foi um sacrifício."',
  objetivo='Dar prova pela voz de quem é cuidado: mudança real de hábito, sem resultado clínico.',
  portras='O cuidado que funciona é o que cabe na vida. Quem diz isso não somos nós.',
  persona='Colaboradores; RH',
  fio='Vem de: 18/11, NR-01. Leva para: 23/11, quem cuida do RH.',
  visual='Fundo Tiffany com grade fina e brilho creme; título Depoimentos; três balões brancos (colaboradoras, avatar em pictograma) e um verde-escuro (equipe, logo); fecho em serif com o A5; rodapé branco com @fairhealth.br e o slogan. Sem foto de pessoa.',
  material='Tipografia, pictogramas e o logo.',
  cta='Nenhuma (post de prova)',
  stories='Repost com a pergunta "O que tornaria o cuidado mais fácil na sua rotina?".',
  fonte='instagram/depoimentos.md: A2 + A1 (vídeo), B2 + B1 (e-mail para a Dra. Marília), C1 + C2 (relato da equipe por WhatsApp, 04/11) e A5 no fecho.',
  validar='Formato dos depoimentos com o Dr. Ronald (o mesmo pendente do 03/11). Autorização por escrito da colaboradora do e-mail e ok da Dra. Marília para o relato. Sem nome, rosto, empresa ou condição de saúde. Legenda: refazer com a ig-caption.',
  arquivos='instagram/posts/depoimentos/ (png/d-01.png, canva.html)',
  legenda='''"Os meus hábitos mudaram, e não foi um sacrifício."

Quem disse foi uma colaboradora atendida pelo Escritório do Cuidado, num retorno de consulta.

O plano de cuidado é combinado com cada pessoa e cabe na rotina real. Quando a mudança não pesa, ela fica.

#fairhealth #escritoriodocuidado #medicinadoestilodevida #saudecorporativa #cuidadocentradonapessoa''',
  roteiro=[
   ('Imagem única', 'Escritório do Cuidado · Depoimentos\nBalão 1: Os meus hábitos mudaram, e não foi um sacrifício. [...] Não é aquela dieta impossível de fazer. É algo pra vida. (Colaboradora atendida pelo Escritório do Cuidado)\nBalão 2: Agradeço por me ajudar a olhar para as minhas conquistas com mais gentileza e reconhecer que o processo não precisa ser perfeito para estar funcionando. (Colaboradora atendida pelo Escritório do Cuidado)\nBalão 3: Ficamos bem felizes ao ouvir de uma paciente o quanto o que estamos fazendo mudou a cultura da empresa. [...] Todos estão se alimentando mais saudável, se movimentando mais e fazendo melhores escolhas. (Equipe do Escritório do Cuidado)\nFecho: "O que é bom a gente tem que compartilhar."\nRodapé: @fairhealth.br · Fazemos o certo pelos motivos certos.', '', 'Tiffany com grade, balões de conversa, avatar em pictograma.', 'Trechos de instagram/depoimentos.md (A, B e C).'),
  ]),

 dict(id='N10', data=D(23), semana=4, bloco='5 · Atualidade', eixo='Notícias + Cultura', fmt=REEL,
  titulo='O RH cuida de todo mundo. Quem cuida do RH?',
  sub='Dados do Panorama da Saúde Emocional do RH 2026 e o cuidado que chega também a quem cuida',
  status='Pauta proposta (calendário de novembro)', resp='Nina · Dr. Ronald (saúde mental)',
  espec=ESP_REEL + ' Tipografia animada com dados.',
  gancho='O RH cuida de todo mundo. Quem cuida do RH?',
  objetivo='Falar com o próprio RH: os dados mostram que quem cuida também está sobrecarregado, e o cuidado da empresa chega a ele também.',
  portras='O RH também é colaborador. Cuidar de quem cuida faz parte do cuidado.',
  persona='RH',
  fio='Vem de: 19/11, o depoimento. Leva para: 25/11, Geração Z e desconexão.',
  visual='Tipografia animada, um dado por cena, com a fonte em texto pequeno. Imagens de banco de mesa de trabalho e agenda cheia, sem rosto.',
  material='Canva (animação de texto), trilha calma.',
  cta='Mande para alguém do RH',
  stories='Enquete: "Você, que é de RH, tem com quem falar quando está sobrecarregado?" (Tenho · Não tenho).',
  fonte='Panorama da Saúde Emocional do RH 2026 (Flash e RH Summit, mais de mil profissionais de RH, lançado no CONARH): 64% sobrecarregados; 6 em cada 10 com algum problema de saúde mental; 17% dos coordenadores já tiveram burnout; 20% se sentem isolados.',
  validar='Conferir os quatro números no material original da Flash. Revisão do Dr. Ronald (saúde mental). CVV 188 na legenda.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/quem-cuida-do-rh/',
  legenda='''O RH cuida de todo mundo. Quem cuida do RH?

No Panorama da Saúde Emocional do RH 2026, da Flash com o RH Summit, mais de mil profissionais de RH responderam. 64% se dizem sobrecarregados. 6 em cada 10 relatam algum problema de saúde mental. E 20% se sentem isolados no trabalho.

Quem segura o clima da empresa também precisa de alguém para conversar. No Escritório do Cuidado, o RH é atendido como qualquer colaborador, com o mesmo sigilo.

Mande este reel para alguém do RH que cuida de todo mundo.

Se você precisa de ajuda agora, o CVV atende pelo 188, 24 horas.

#fairhealth #rh #saudemental #saudecorporativa #gestaodepessoas''',
  roteiro=[
   ('0 a 3 s', 'O RH cuida de todo mundo.\nQuem cuida do RH?', '', 'Duas linhas, a segunda entra depois.', 'Gancho.'),
   ('3 a 8 s', '64% dos profissionais de RH se dizem sobrecarregados.', '', 'Número grande, fonte embaixo: Panorama da Saúde Emocional do RH 2026 (Flash).', ''),
   ('8 a 13 s', '6 em cada 10 relatam algum problema de saúde mental.', '', 'Mesmo modelo.', ''),
   ('13 a 18 s', '17% dos coordenadores já tiveram burnout.\n20% se sentem isolados.', '', 'Duas linhas.', ''),
   ('18 a 24 s', 'Quem segura o clima da empresa\ntambém precisa de alguém para conversar.', '', 'Fundo muda para Tiffany.', 'Virada.'),
   ('24 a 28 s', 'No Escritório do Cuidado, o RH é atendido como qualquer colaborador. Com o mesmo sigilo.', '', '', ''),
   ('28 a 30 s', 'Mande para alguém do RH.', '', 'Logo sobre Tiffany.', ''),
  ]),

 dict(id='N11', data=D(25), semana=4, bloco='5 · Atualidade', eixo='Cultura + Produto', fmt=CARR,
  titulo='Por que a Geração Z está tão desconectada do trabalho?',
  sub='Não é preguiça: a desconexão tem causa, e a resposta começa por "o que importa para você?"',
  status='Arte em rascunho (faltam fotos nos slides 1 a 4)', resp='Nina · Dr. Ronald (saúde mental, NR-01)',
  espec='Carrossel 4:5 (1080 × 1350), 7 slides (sem o slide do meme, a pedido da Nina em 23/11). Tom editorial, série "Cuidado em números".',
  gancho='Geração Z desconectada do trabalho: não é preguiça.',
  objetivo='Mostrar com dados que a desconexão da Geração Z tem causa, e que a resposta começa pela pergunta "o que importa para você?".',
  portras='Geração Z não é o problema. Falta de cuidado é.',
  persona='RH; Lideranças',
  fio='Vem de: 23/11, quem cuida do RH. Leva para: 27/11, o case de adesão.',
  visual='Manchete sem serifa, texto em Instrument Serif, foto real em tela cheia (banco com licença comercial ou sessão de fotos). Cores e logo da fairhealth.',
  material='Fotos dos slides 1 a 4 (vagas descritas no slides.html). Foto do espaço no slide 6.',
  cta='Comente CUIDADO',
  stories='Enquete: "Seu time tem com quem contar na hora difícil?".',
  fonte='Mapa da Felicidade Real dos Brasileiros 2026 (Renata Rivetti e Instituto Ideia; 1.500 entrevistas; 20/02 a 01/03/2026; margem de 2,5 pontos), via Metrópoles e Grupo Amanhã.',
  validar='Conferir os números no material original. O que o relatório do RH mostra de fato (slide 6). Revisão do Dr. Ronald. A @brandsdecoded_ já publicou os mesmos dados: o nosso se diferencia pelo que vem depois.',
  arquivos='instagram/posts/geracao-z/ (slides.html, png/, previa.png, README.md)',
  legenda='''Geração Z e saúde mental no trabalho: o olhar vazio na reunião não é preguiça.

No Mapa da Felicidade Real dos Brasileiros 2026, da pesquisadora Renata Rivetti com o Instituto Ideia, só 33% dos jovens de 16 a 24 anos disseram estar muito satisfeitos com a vida. Dos 25 anos para cima, foram 47,9%.

No trabalho, a distância passa do dobro: 46,7% dos jovens dizem que o trabalho os deixa mais infelizes, contra 20,5% nas outras idades. Mais de 1 em cada 5 diz não ter com quem contar na hora difícil.

É fácil rotular uma geração inteira. Mas sobrecarga, falta de sentido, ansiedade, sono ruim e solidão não têm idade, e vários desses são riscos psicossociais que a NR-01 agora pede para a empresa gerenciar.

No Escritório do Cuidado, todo atendimento começa com a mesma pergunta: o que importa para você? Médico, psicólogo e assistente social dentro da empresa, com um plano de cuidado para cada pessoa. O RH recebe só indicadores do grupo, anonimizados.

Comente CUIDADO e mostramos como funciona na sua empresa.

#fairhealth #saudecorporativa #geracaoz #saudemental #gestaodepessoas''',
  roteiro=[
   ('Slide 1 · capa', 'O olhar vazio na reunião não é preguiça.', '', 'Foto em tela cheia (jovem em reunião, olhar distante), manchete sem serifa.', 'Foto pendente.'),
   ('Slide 2 · promessa', 'Só 33% dos jovens de 16 a 24 anos se dizem muito satisfeitos com a vida. Dos 25 para cima, 47,9%.', '', 'Foto + dado com nome da pesquisa e da autora.', 'Foto pendente.'),
   ('Slide 3 · dado', '46,7% dos jovens dizem que o trabalho os deixa mais infelizes (20,5% nas outras idades).', '', 'Dado grande.', 'Foto pendente.'),
   ('Slide 4 · dado', 'Mais de 1 em cada 5 não tem com quem contar. 27% preocupados; 71,1% tristes com as redes.', '', 'Dado em lista.', '"Mais de 1 em cada 5" vem de 79% que têm com quem contar.'),
   ('Slide 5 · causas', 'Desconexão tem causa, e nenhuma delas é a idade: sobrecarga, falta de sentido, ansiedade, sono ruim, solidão. Vários são riscos psicossociais que a NR-01 pede para a empresa gerenciar.', '', 'Lista numerada.', ''),
   ('Slide 6 · produto', 'No Escritório do Cuidado, todo atendimento começa com a mesma pergunta: o que importa para você?', '', 'Foto do espaço.', ''),
   ('Slide 6b · RH', 'O RH recebe só indicadores do grupo, anonimizados.', '', 'No slide do produto.', 'Conferir o que o relatório mostra.'),
   ('Slide 7 · para o líder e chamada', 'Geração Z não é o problema. Falta de cuidado é.\nComente CUIDADO.\nFonte completa da pesquisa.', '', 'Verde-escuro, logo.', ''),
  ]),

 dict(id='N12', data=D(27), semana=4, bloco='6 · Atualidade', eixo='Notícias + Institucional', fmt=CARR,
  titulo='Seminário Mirix: a felicidade no trabalho pode ser medida',
  sub='Dr. Ronald Maia Filho e Fernando Brancaccio em Belo Horizonte e o que isso muda para quem cuida de gente',
  inspiracao='Repostagem da matéria do BH Ao Vivo (21/11/2026) sobre o Seminário Internacional Mirix (05/11). Layout institucional, card nosso.',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='BH Ao Vivo, 21/11/2026: "Especialistas apresentam metodologia que mede a felicidade e coloca o ser humano no centro das organizações durante o Seminário Internacional Mirix". Evento "ELO do Cuidado", Belo Horizonte, 05/11/2026. Citações curtas das falas marcadas com aspas na matéria: "Às vezes uma conversa resolve" (Ronald) e "Não é eu contra você, nós juntos" (Fernando). O resto é paráfrase da matéria. Sem os 73,9 pontos da Clínica Mirix (dado de terceiro).',
  validar='Ok de Fernando e Dr. Ronald para o texto. Foto do evento nossa ou frames do vídeo (não usar as fotos do portal sem autorização). Crédito "Fonte: BH Ao Vivo, 21/11/2026" na arte e link da matéria no primeiro comentário. A matéria não cita fairhealth nem fairjob: a ligação com a marca é só do nosso texto.',
  roteiro=[
   ('Slide 1 · capa', 'Seminário Mirix: a felicidade no trabalho pode ser medida.\nDr. Ronald Maia Filho e Fernando Brancaccio, em Belo Horizonte.', '', '', ''),
   ('Slide 2 · o encontro', 'O encontro\nSeminário Internacional Mirix, ELO do Cuidado. Belo Horizonte, 5 de novembro. O tema: do consultório à rede.', '', '', ''),
   ('Slide 3 · Dr. Ronald', 'Dr. Ronald Maia Filho\nO cuidado começa por entender o que importa para a pessoa, em vez de decidir sozinho o que é melhor para ela.\n"Às vezes uma conversa resolve."', '', '', 'Citação literal da matéria.'),
   ('Slide 4 · Fernando', 'Fernando Brancaccio\nA felicidade pode ser medida, acompanhada e estimulada com ações concretas. Percepção vira indicador, indicador vira decisão.', '', '', 'Paráfrase da matéria, sem aspas.'),
   ('Slide 5 · gestão', 'Cuidar de quem trabalha é estratégia de gestão, e não iniciativa assistencial.\n"Não é eu contra você, nós juntos."', '', '', 'Citação literal da matéria (Fernando).'),
   ('Slide 6 · Escritório + convite', 'No Escritório do Cuidado, a pergunta que abre cada atendimento é a mesma: o que importa para você? O plano é pela Medicina do Estilo de Vida, com bioimpedância e smartwatch, e o RH recebe só indicadores do grupo, anonimizados.\nQuer ver como funciona na sua empresa? Comente CUIDADO.\nFonte: BH Ao Vivo, 21/11/2026.', '', '', 'Chamada única; fonte em letra miúda.'),
   (VIS, 'Carrossel 4:5, 6 slides, fundo creme/papel, Raleway, um bloco por slide, sem numeração. Slides 3 e 4 com foto do evento ou frame do vídeo em faixa (sem a foto do portal), nome em Tiffany. Citações em Instrument Serif itálico, só a frase. Fonte da matéria em letra miúda no slide 6.', '', '', ''),
  ],
  legenda='''Cuidar de quem trabalha é estratégia de gestão, e dá para medir.

No Seminário Internacional Mirix, em Belo Horizonte, o Dr. Ronald Maia Filho e o Fernando Brancaccio apresentaram o mesmo caminho por dois lados. O cuidado começa por entender o que importa para a pessoa. E o que importa, como a felicidade no trabalho, pode virar indicador, e o indicador, decisão.

É o que fazemos no Escritório do Cuidado: a primeira pergunta do atendimento é "o que importa para você?", o plano é feito com a pessoa, com base na Medicina do Estilo de Vida, e a bioimpedância e o smartwatch acompanham a rotina. O RH recebe só indicadores do grupo, anonimizados.

Matéria completa no BH Ao Vivo (21/11/2026), com o link no primeiro comentário.

Quer ver como funciona na sua empresa? Comente CUIDADO.

#fairhealth #saudecorporativa #felicidadenotrabalho #escritoriodocuidado #gestaodepessoas''',
  palavras='felicidade no trabalho,Seminário Internacional Mirix,Escritório do Cuidado'),
 dict(id='N13', data=D(30), semana=5, bloco='6 · Atualidade', eixo='Cultura + Produto', fmt=CARR,
  titulo='Como se mede a felicidade no trabalho?',
  sub='As 9 dimensões da Felicidade Interna Bruta do Butão e o questionário anônimo que nasceu delas',
  inspiracao='Print "O que influencia sua saúde financeira" (lista com marcadores e destaque numérico), agora com as 9 dimensões da FIB no lugar de percentuais. Fonte: matéria do BH Ao Vivo (21/11/2026).',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='BH Ao Vivo, 21/11/2026: Fernando Brancaccio foi ao Butão conhecer a Felicidade Interna Bruta (FIB); a matéria lista as 9 dimensões (bem-estar psicológico, saúde, uso do tempo, vitalidade comunitária, educação, cultura, meio ambiente, governança, padrão de vida) e descreve um questionário anônimo, que busca fatores como saúde emocional, relações sociais, condições financeiras, segurança e qualidade da gestão. Conferir as 9 dimensões na fonte original da FIB (Centre for Bhutan and GNH Studies). Sem números.',
  validar='Confirmar com Fernando se o questionário faz parte da oferta da fairhealth (a matéria só diz que ele nasceu da parceria com o Dr. Ronald e foi aplicado na Clínica Mirix) e quais dimensões ele usa. Conferir as 9 dimensões da FIB na fonte original. Sem os 73,9 pontos da Clínica Mirix.',
  roteiro=[
   ('Slide 1 · capa', 'Como se mede a felicidade no trabalho?\nA metodologia do Butão que inspirou um questionário para empresas.', '', 'Verde da marca, grade de 9 pontos em Tiffany.', ''),
   ('Slide 2 · promessa (funciona sozinho)', 'Felicidade parece subjetiva demais para ser medida.\nMas ela pode ser medida, acompanhada e estimulada com ações concretas.\nFoi o tema do Seminário Internacional Mirix, em Belo Horizonte, em novembro.', '', 'Papel.', ''),
   ('Slide 3 · as 9 dimensões', 'Felicidade Interna Bruta, no Butão\nO bem-estar além da renda, em 9 dimensões: bem-estar psicológico · saúde · uso do tempo · vitalidade comunitária · educação · cultura · meio ambiente · governança · padrão de vida.\nFernando Brancaccio foi ao Butão estudar a metodologia.', '', 'Verde, grade 3 × 3 com marcador Tiffany.', 'Conferir as 9 dimensões na fonte original.'),
   ('Slide 4 · no trabalho', 'No trabalho\nA pergunta muda.\nNão é só "você está satisfeito com a empresa?". O questionário procura fatores como: saúde emocional · relações sociais · condições financeiras · segurança · qualidade da gestão.', '', 'Papel, lista com marcador (a referência).', ''),
   ('Slide 5 · anônimo', 'Anônimo, para dizer a verdade.\nAs respostas mostram pontos fortes e fragilidades e orientam ações de melhoria.\nPercepção vira indicador. Indicador vira decisão.', '', 'Verde.', ''),
   ('Slide 6 · Escritório', 'No Escritório do Cuidado\nO ponto de partida é o mesmo: o que importa para você?\nMédicos, psicólogos, assistentes sociais e felicitologistas dentro da empresa, com um plano pela Medicina do Estilo de Vida, bioimpedância e smartwatch.\nO RH recebe só indicadores do grupo, anonimizados.', '', 'Papel; a pergunta em Instrument Serif.', ''),
   ('Slide 7 · convite', 'Quer ver como funciona na sua empresa?\nComente CUIDADO e mostramos como o Escritório do Cuidado funciona.\nFonte: BH Ao Vivo (21/11/2026), sobre o Seminário Internacional Mirix. As 9 dimensões são as da Felicidade Interna Bruta do Butão.', '', 'Tiffany, logo.', 'Chamada única.'),
   (VIS, 'Sistema aprovado em 23/11 (carrossel de 25/11): verde da marca nos slides escuros, papel nos claros e o fecho em Tiffany. Raleway; Instrument Serif só na pergunta. Sem foto. Arte em instagram/posts/felicidade-medida/.', '', '', ''),
  ],
  legenda='''Como se mede a felicidade no trabalho? Ela pode ser medida, acompanhada e estimulada com ações concretas.

No Butão, a Felicidade Interna Bruta olha o bem-estar além da renda, em nove dimensões: bem-estar psicológico, saúde, uso do tempo, vitalidade comunitária, educação, cultura, meio ambiente, governança e padrão de vida. O Fernando Brancaccio foi até lá estudar a metodologia, e ela inspirou um questionário anônimo para empresas.

No trabalho, a pergunta deixa de ser só se a pessoa está satisfeita com a empresa. O questionário procura fatores como saúde emocional, relações sociais, condições financeiras, segurança e qualidade da gestão. As respostas mostram pontos fortes e fragilidades. Percepção vira indicador. Indicador vira decisão.

No Escritório do Cuidado, o ponto de partida é o mesmo: o que importa para você? Médicos, psicólogos, assistentes sociais e felicitologistas atendem dentro da empresa, com um plano pela Medicina do Estilo de Vida, bioimpedância e smartwatch. O RH recebe só indicadores do grupo, anonimizados.

Fonte: BH Ao Vivo (21/11/2026), sobre o Seminário Internacional Mirix.

Quer ver como funciona na sua empresa? Comente CUIDADO.

#fairhealth #felicidadenotrabalho #saudecorporativa #bemestarcorporativo #gestaodepessoas''',
  palavras='felicidade no trabalho,Felicidade Interna Bruta,questionário anônimo'),
]

PENDENCIAS = [
    ('N02', 'Publicação hoje (04/11): aprovar o roteiro do reel e produzir o motion. Definir com a fairdata o que o relatório do RH mostra.', 'Nina e fairdata', 'Urgente'),
    ('N01, N09', 'Formato dos depoimentos (A1 no 03/11, A2 no 19/11) com o Dr. Ronald.', 'Dr. Ronald', 'Aberta'),
    ('N03', 'Validar a história do Escritório (2009, hospital, como funcionava) e a descrição dos Aims.', 'Dr. Ronald', 'Aberta'),
    ('N03, N04', 'Dados de clientes: a decisão de 30/10 tirou os números de cliente dos posts. Confirmar se o caso do hospital (06/11) e os números da indústria (09/11) podem entrar.', 'Sócios', 'Aberta'),
    ('N04', 'Data de gravação do reel com o Dr. Ronald e autorização de uso de imagem.', 'Dr. Ronald e Comunicação', 'Aberta'),
    ('N05', 'Leitura do Diabetes Prevention Program pela responsável médica. Escolher a capa (estudo ou canetas).', 'Responsável médica', 'Aberta'),
    ('N06', 'Resposta automática da palavra CUIDADO pronta até 13/11 (o diagnóstico gratuito não existe: CUIDADO envia como funciona o Escritório do Cuidado). Quem responde as DMs até lá.', 'Comunicação', 'Aberta'),
    ('N07', 'Achar e conferir um dado sobre homens e consultas (fonte oficial). Revisão técnica do Dr. Ronald.', 'Comunicação e Dr. Ronald', 'Aberta'),
    ('N08', 'Número conferido na nota oficial da Previdência e texto da NR-01 conferido no PDF do MTE (04/11). Falta a leitura do Dr. Ronald e o ok da Nina para citar a fairdata.', 'Comunicação e Dr. Ronald', 'Aberta'),
    ('N10', 'Conferir os números do Panorama da Saúde Emocional do RH 2026 no material da Flash.', 'Comunicação', 'Aberta'),
    ('N11', 'Fotos dos slides 1 a 4, corte para 8 slides e conferência dos números do Mapa da Felicidade.', 'Nina', 'Aberta'),
    ('N12, N13', 'Seminário Mirix: ok de Fernando e Dr. Ronald, foto do evento (nossa) e conferir as 9 dimensões da FIB na fonte original. Link da matéria no primeiro comentário.', 'Nina', 'Aberta'),
    ('Todos', 'Legendas novas (04/11 em diante) passam pela ig-caption e pela ig-human antes de publicar; fotos com licença e origem confirmadas.', 'Comunicação', 'Aberta'),
]

DATAS = [
    (D(2), 'Finados (feriado, sem post)'),
    (D(14), 'Dia Mundial do Diabetes (sábado)'),
    (D(15), 'Proclamação da República (domingo)'),
    (D(20), 'Consciência Negra (feriado): o post da semana vai para quinta, 19/11'),
    (D(27), 'Black Friday: sem linguagem de promoção'),
    (D(30), 'Novembro Azul o mês todo; 30/11 (segunda) abre a passagem para dezembro. O reel "Dezembro chegou" virou story e o reel de 02/12 é o do seminário Mirix'),
]
