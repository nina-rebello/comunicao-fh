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
  cta='Slide 3: mande este post para quem cuida das pessoas · Slide 6: Comente CUIDADO (diagnóstico gratuito)',
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

Quer esse cuidado para o seu time? Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #medicinadoestilodevida #cuidadocentradonapessoa #gestaodepessoas''',
  roteiro=[
   ('Slide 1 · capa', 'Por dentro do Escritório do Cuidado\nO cuidado que todo mundo queria ter no trabalho.\nComo isso funciona na prática, em 4 pontos →', '', 'Foto colorida inteira (conversa no escritório), título no terço de baixo.', ''),
   ('Slide 2 · Ser ouvido', 'Todo mundo quer ser ouvido de verdade.\nÀs vezes, o que tira o sono é o turno, a conta do mês ou a casa. Por isso, no Escritório do Cuidado, a primeira consulta começa por uma pergunta: o que importa para você?\nCuidado começa pela história, não pelo sintoma.', '', 'Fundo claro, foto (mãos dadas) na metade de cima.', ''),
   ('Slide 3 · Cuidado por perto', 'Ninguém quer perder meio dia por uma consulta.\nPor isso o cuidado fica dentro da empresa: médico, psicólogo e assistente social a poucos passos de quem trabalha, presencial ou remoto.\nSem trânsito e sem sala de espera.', '', 'Fundo escuro, foto (profissional de capacete) numa faixa à direita.', 'CTA de envio: Conhece quem cuida das pessoas na sua empresa? Mande este post.'),
   ('Slide 4 · Um plano possível', 'Quem nunca recebeu uma dieta impossível?\nNo Escritório do Cuidado, o plano é combinado com a pessoa e cabe na rotina real: dormir meia hora mais cedo, almoçar longe da mesa. A base é a Medicina do Estilo de Vida.\n"Não é aquela dieta impossível de fazer. É algo pra vida." Colaboradora atendida pelo Escritório do Cuidado', '', 'Fundo água (virada), número grande e foto (prato) ao lado.', 'Depoimento A1.'),
   ('Slide 5 · Continuidade', 'Ninguém quer começar do zero a cada consulta.\nA equipe acompanha cada pessoa. Histórico e metas ficam na plataforma, e a cada retorno o plano é revisto. Sigilo. Pode falar: o que é conversado fica no atendimento. O RH recebe só indicadores do grupo, anonimizados.\nO plano muda quando a vida muda.', '', 'Fundo claro, foto (escada) saindo pela lateral.', ''),
   ('Slide 6 · convite', 'Quer esse cuidado para o seu time?\nComente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.\nNa quarta: quatro frentes, um cuidado conectado.', '', 'Verde-escuro, sem foto.', 'Ponte para o 04/11.'),
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
  cta='Comente CUIDADO (diagnóstico gratuito)',
  stories='Quiz: "Qual destas frentes acompanha a rotina entre as consultas?" (resposta: wearables).',
  fonte='Executive Summary e one-pager (11/10): as quatro peças. Nota do calendário: "Para o RH: a plataforma entrega relatório".',
  validar='Nomes das frentes iguais aos do one-pager. O que o relatório do RH mostra de fato (fairdata): não mostrar indicador que ainda não existe. Publicação hoje (04/11): o roteiro precisa de aprovação rápida.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/quatro-frentes/',
  legenda='''Não são quatro produtos soltos. É um cuidado só.

O Escritório do Cuidado leva médico, psicólogo e assistente social para dentro da empresa. O Programa de Medicina do Estilo de Vida leva informação para todos. Os wearables acompanham a rotina entre uma consulta e outra.

E a plataforma junta tudo num relatório para o RH, com indicadores do grupo, anonimizados. O que cada pessoa conta fica no atendimento. O que o RH recebe é a visão do todo, para decidir onde cuidar primeiro.

Quer ver como isso funciona na sua empresa? Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

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
  objetivo='Fechar a apresentação inicial com um caminho claro para o RH: diagnóstico, proposta e implementação.',
  portras='Começar é simples e não pede decisão grande: o primeiro passo é uma conversa.',
  persona='RH; Diretoria financeira',
  fio='Vem de: 11/11, a ciência. Fecha os 4 blocos de 19/10 a 13/11. Leva para: as pautas de atualidade (16/11 em diante).',
  visual='Três passos no fio contínuo. Capa com foto de mesa de reunião (banco) ou fundo verde-escuro. Último slide verde-escuro com a palavra CUIDADO em destaque.',
  material='Tipografia e o fio.',
  cta='Comente CUIDADO (diagnóstico gratuito)',
  stories='Sequência com os 3 passos e o adesivo "Mande uma mensagem".',
  fonte='Executive Summary: entrada comercial (diagnóstico gratuito, proposta personalizada, implementação com onboarding e primeiros atendimentos).',
  validar='Resposta automática da palavra CUIDADO e página do diagnóstico no ar até 13/11. Quem responde as DMs. Sem prazos de etapa e sem preço. NR-1: "apoio na prevenção", nunca "conformidade".',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/como-levar/',
  legenda='''O orçamento de 2027 está fechando. Onde entra o cuidado?

Levar o Escritório do Cuidado para a sua empresa começa por uma conversa. São três passos.

Primeiro, um diagnóstico gratuito para entender o time, os turnos e o que mais pesa hoje. Depois, uma proposta personalizada, do tamanho e da rotina da sua empresa. Por fim, a implementação, com onboarding e os primeiros atendimentos: médico, psicólogo e assistente social perto de quem trabalha.

O RH acompanha tudo por indicadores do grupo, anonimizados, e ganha apoio na prevenção de riscos psicossociais (NR-1).

Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #gestaodepessoas #rh #escritoriodocuidado''',
  roteiro=[
   ('Slide 1 · capa', 'O orçamento de 2027 está fechando.\nOnde entra o cuidado?', '', 'Foto de mesa de reunião (banco) ou fundo verde-escuro.', ''),
   ('Slide 2 · diagnóstico', 'Começa por uma conversa.\nDiagnóstico gratuito: entender o time, os turnos e o que mais pesa hoje.', '', 'Fundo claro, primeiro ponto no fio.', 'Funciona sozinho.'),
   ('Slide 3 · proposta', 'Proposta personalizada\nO programa desenhado para o tamanho e a rotina da sua empresa.', '', 'Fundo Tiffany, segundo ponto.', 'Sem preço.'),
   ('Slide 4 · implementação', 'Implementação\nOnboarding e primeiros atendimentos, com médico, psicólogo e assistente social perto de quem trabalha.', '', 'Fundo verde, terceiro ponto.', 'Sem prazos.'),
   ('Slide 5 · o que o RH acompanha', 'Indicadores do grupo, anonimizados.\nApoio na prevenção de riscos psicossociais (NR-1).', '', 'Fundo claro, página de relatório estilizada.', 'Nunca "conformidade".'),
   ('Slide 6 · chamada', 'Comente CUIDADO\ne enviamos na DM como funciona o diagnóstico gratuito.', '', 'Verde-escuro, CUIDADO em destaque, logo.', ''),
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
  cta='Comente CUIDADO (diagnóstico gratuito)',
  stories='Enquete: "Quando foi a última vez que você foi ao médico sem estar doente?" (Neste ano · Faz tempo).',
  fonte='{{dado sobre homens e consultas + fonte}}: buscar pesquisa recente (Ministério da Saúde, SBU ou Fiocruz) e conferir na fonte original.',
  validar='Revisão técnica do Dr. Ronald (CFM): nada sobre exame específico, diagnóstico ou promessa. Conferir o dado sobre homens e saúde na fonte original. Sem carona em caso de famoso.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/novembro-azul/',
  legenda='''Ele só vai ao médico quando dói. E quase nunca é descuido.

Cuidar dá trabalho: marcar, pedir para sair mais cedo, atravessar a cidade, esperar. Para quem trabalha em turno, isso pode custar meio dia. Então a consulta fica para depois, até virar urgência.

Quando o cuidado está dentro da empresa, a conta muda. Médico, psicólogo e assistente social a poucos passos de quem trabalha, e a consulta cabe no intervalo.

O Novembro Azul dura um mês. O cuidado pode durar o ano todo.

Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

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
  status='Texto aprovado (04/11) · v4 em 6 slides para aprovação', resp='Nina · Dr. Ronald (NR-01 e saúde mental)',
  espec='Carrossel 4:5 (1080 × 1350), 6 slides, estilo institucional.',
  gancho='546,2 mil afastamentos do trabalho por saúde mental no Brasil em 2025, concedidos pelo INSS. E agora, RH?',
  objetivo='Usar o dado mais recente de afastamentos para explicar o que a NR-01 pede sobre riscos psicossociais: medir e cuidar, com a fairdata no diagnóstico e o Escritório do Cuidado no cuidado.',
  portras='A própria NR-01 (item 1.5.3.2) pede os dois lados: identificar, avaliar e classificar os riscos, e implementar medidas e acompanhar. Sem desvalorizar o mapeamento, que a fairdata faz (pedido da Nina, 04/11).',
  persona='RH; Medicina do Trabalho; SST',
  fio='Vem de: 16/11, Novembro Azul. Leva para: 19/11, a voz de quem é cuidado.',
  visual='Padrão dos carrosséis de 03/11 e 11/11: papel e creme com brilho Tiffany, marca-texto com textura, gráfico desenhado com anotação à mão, print do texto oficial da NR-01, balão "E agora, RH?" na capa e no fim. Uma foto de banco (conversa) no slide 5. CVV 188 no slide final.',
  material='PDF oficial da NR-01 (MTE), guia do MTE sobre fatores de riscos psicossociais, uma foto de banco.',
  cta='Curta, comente e compartilhe com quem cuida das pessoas na sua empresa (alternativa: fale com a gente pelo link da bio)',
  stories='Caixa de perguntas: "Qual a sua maior dúvida sobre a NR-01?" (respostas viram conteúdo).',
  fonte='Ministério da Previdência Social (nota oficial na Agência Gov, jan/2026): 546.254 benefícios por incapacidade temporária concedidos pelo INSS por transtornos mentais e comportamentais em 2025, 15,66% acima de 2024 (472.328); também no g1. Segundo recorde seguido. NR-01: texto atualizado no gov.br (MTE), itens 1.5.3.1.4 e 1.5.3.2, redação da Portaria MTE nº 1.419/2024, em vigor desde 26/05/2026 (Portaria MTE nº 765/2025). Lista de fatores: Guia de informações sobre os fatores de riscos psicossociais relacionados ao trabalho (MTE, 2025), listagem exemplificativa de 13 fatores.',
  validar='Conferir com o Dr. Ronald a situação da NR-01 (vigência e o que é exigido). Menção à fairdata no slide 5. Legenda: passar pela ig-caption e pela ig-human. Sem alarmismo ("epidemia", "bomba-relógio"). Nunca prometer conformidade com a NR-01.',
  arquivos='instagram/posts/nr01-afastamentos/ (png/n-01 a n-06, canva.html, nr01-afastamentos.pdf; alternativa do slide 3 em png-alternativas/ e canva-alternativas.html)',
  legenda='''Recorde de afastamentos por saúde mental: o que a NR-01 cobra do RH.

Em 2025, foram 546,2 mil licenças por transtornos mentais no Brasil, o segundo recorde seguido, segundo o Ministério da Previdência Social.

Desde maio de 2026, a NR-01 pede que a empresa identifique e gerencie os riscos psicossociais junto com os outros riscos ocupacionais. O guia do Ministério do Trabalho e Emprego dá exemplos: sobrecarga, falta de apoio, assédio, baixa clareza de papel e baixo controle sobre o trabalho.

A norma pede medir e cuidar: identificar, avaliar e classificar os riscos, e também implementar medidas de prevenção e acompanhar o controle dos riscos. Com a fairdata, o diagnóstico dos riscos do grupo. Com o Escritório do Cuidado, escuta, acompanhamento e encaminhamento, e o RH recebe indicadores do grupo, anonimizados.

Curta, comente e compartilhe com quem cuida das pessoas na sua empresa.

Se você precisa de ajuda agora, o CVV atende pelo 188, 24 horas.

#fairhealth #nr01 #saudemental #saudecorporativa #riscospsicossociais''',
  roteiro=[
   ('Slide 1 · capa', 'Saúde mental no trabalho\n546,2 mil afastamentos do trabalho por saúde mental\nno Brasil em 2025, concedidos pelo INSS.\nFonte: Ministério da Previdência Social.\nBalão: E agora, RH?', '', 'Creme com brilho Tiffany, número gigante, marca-texto em "por saúde mental", balão verde.', 'O número conta benefícios por incapacidade temporária (auxílio-doença) concedidos, não pessoas: não trocar por "546 mil trabalhadores".'),
   ('Slide 2 · o dado', 'O dado\n546,2 mil licenças por transtornos mentais em 2025, o segundo recorde seguido.\nGráfico: 472,3 mil (2024) e 546,2 mil (2025), +15,7%.\nFonte: Ministério da Previdência Social (nota oficial, jan/2026).', '', 'Papel, barras com textura na mesma escala, anotação à mão.', 'Se sustenta sozinho.'),
   ('Slide 3 · a norma', 'A norma\nNR-01\nDesde maio de 2026, a NR-01 pede que a empresa identifique e gerencie os riscos psicossociais, junto com os outros riscos ocupacionais.\nPrint do texto oficial: vigência (26/05/2026) e itens 1.5.3.1.4 e 1.5.3.2.', '', 'Verde-escuro, print do PDF do MTE colado com fita, marca-texto no trecho dos riscos psicossociais.', 'Alternativa: o recorte digitado (png-alternativas/).'),
   ('Slide 4 · o que é risco psicossocial', 'Exemplos da lista do Ministério do Trabalho e Emprego: os 13 fatores do guia, na ordem e com as palavras do guia.\nFonte: Guia de informações sobre os fatores de riscos psicossociais relacionados ao trabalho (MTE, 2025). A lista é exemplificativa.', '', 'Tiffany, folha com lista numerada.', ''),
   ('Slide 5 · medir e cuidar', 'Medir e cuidar: a norma pede os dois.\nMedir: b) identificar os perigos, c) avaliar os riscos, d) classificar os riscos. Com a fairdata: o diagnóstico dos riscos do grupo.\nCuidar: e) implementar medidas de prevenção, f) acompanhar o controle dos riscos. Com o Escritório do Cuidado: escuta, acompanhamento e encaminhamento.\nFonte: NR-01, item 1.5.3.2.', '', 'Foto de conversa no alto, dois cartões (claro e verde-escuro).', 'Ponte para o produto, sem desvalorizar o mapeamento (fairdata).'),
   ('Slide 6 · chamada', 'Balão: E agora, RH?\nCurta, comente e compartilhe com quem cuida das pessoas na sua empresa.\nPrecisa de ajuda agora? CVV 188.', '', 'Creme com brilho, ícones de curtir, comentar e compartilhar, logo.', 'Retoma a capa. Sem "Comente CUIDADO" (pedido da Nina, 04/11). Alternativa: Fale com a gente pelo link da bio e leve o Escritório do Cuidado para a sua empresa. Todo post de saúde mental termina com onde pedir ajuda.'),
  ]),

 dict(id='N09', data=D(19), semana=3, bloco='5 · Atualidade', eixo='Cases', fmt=FOTO,
  titulo='Depoimento: "Os meus hábitos mudaram, e não foi um sacrifício."',
  sub='A voz de quem é cuidado: mudança real, sem promessa de resultado clínico',
  status='Pauta proposta (calendário de novembro)', resp='Nina · Dr. Ronald (formato dos depoimentos)',
  espec='Foto única 4:5 (1080 × 1350). Card de citação. Quinta-feira, porque sexta (20/11) é feriado.',
  gancho='"Os meus hábitos mudaram, e não foi um sacrifício."',
  objetivo='Dar prova pela voz de quem é cuidado: mudança real de hábito, sem resultado clínico.',
  portras='O cuidado que funciona é o que cabe na vida. Quem diz isso não somos nós.',
  persona='Colaboradores; RH',
  fio='Vem de: 18/11, NR-01. Leva para: 23/11, quem cuida do RH.',
  visual='Card de citação: aspas grandes em Instrument Serif, frase em verde-escuro sobre fundo creme, logo coração. Sem foto de pessoa.',
  material='Só tipografia e o logo coração.',
  cta='Nenhuma (post de prova)',
  stories='Repost com a pergunta "O que tornaria o cuidado mais fácil na sua rotina?".',
  fonte='Depoimento A2 (instagram/depoimentos.md), trecho aprovado, transcrição limpa.',
  validar='Formato dos depoimentos com o Dr. Ronald (o mesmo pendente do 03/11). Sem nome, rosto, empresa ou condição de saúde. Assinatura padrão.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/depoimento-a2/',
  legenda='''"Os meus hábitos mudaram, e não foi um sacrifício."

Quem disse foi uma colaboradora atendida pelo Escritório do Cuidado, num retorno de consulta.

O plano de cuidado é combinado com cada pessoa e cabe na rotina real. Quando a mudança não pesa, ela fica.

#fairhealth #escritoriodocuidado #medicinadoestilodevida #saudecorporativa #cuidadocentradonapessoa''',
  roteiro=[
   ('Imagem única', '"Os meus hábitos mudaram, e não foi um sacrifício."\nColaboradora atendida pelo Escritório do Cuidado', '', 'Fundo creme, aspas grandes em Tiffany, frase em verde-escuro, logo coração embaixo.', 'Depoimento A2.'),
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
  status='Arte em rascunho (faltam fotos; reduzir de 9 para 8 slides)', resp='Nina · Dr. Ronald (saúde mental, NR-01)',
  espec='Carrossel 4:5 (1080 × 1350), 8 slides (o rascunho tem 9; juntar os slides 5 e 6). Tom editorial, série "Cuidado em números".',
  gancho='O olhar vazio na reunião não é preguiça.',
  objetivo='Pegar a tendência (Gen Z stare, task masking) e mostrar que a desconexão tem causa, e que a resposta começa pela pergunta "o que importa para você?".',
  portras='Geração Z não é o problema. Falta de cuidado é.',
  persona='RH; Lideranças',
  fio='Vem de: 23/11, quem cuida do RH. Leva para: 27/11, o case de adesão.',
  visual='Manchete sem serifa, texto em Instrument Serif, foto real em tela cheia (banco com licença comercial ou sessão de fotos). Cores e logo da fairhealth.',
  material='Fotos dos slides 1 a 4 (vagas descritas no slides.html). Foto do espaço no slide 6.',
  cta='Comente CUIDADO',
  stories='Enquete: "Você já viu o gen Z stare na sua empresa?".',
  fonte='Mapa da Felicidade Real dos Brasileiros 2026 (Renata Rivetti e Instituto Ideia; 1.500 entrevistas; 20/02 a 01/03/2026; margem de 2,5 pontos), via Metrópoles e Grupo Amanhã.',
  validar='Conferir os números no material original. O que o relatório do RH mostra de fato (slide 7). Revisão do Dr. Ronald. A @brandsdecoded_ já publicou os mesmos dados: o nosso se diferencia pelo que vem depois. Cortar para 8 slides (regra da marca).',
  arquivos='instagram/posts/geracao-z/ (slides.html, png/, previa.png, README.md)',
  legenda='''Geração Z e saúde mental no trabalho: o olhar vazio na reunião não é preguiça.

No Mapa da Felicidade Real dos Brasileiros 2026, da pesquisadora Renata Rivetti com o Instituto Ideia, só 33% dos jovens de 16 a 24 anos disseram estar muito satisfeitos com a vida. Dos 25 anos para cima, foram 47,9%.

No trabalho, a distância passa do dobro: 46,7% dos jovens dizem que o trabalho os deixa mais infelizes, contra 20,5% nas outras idades. Mais de 1 em cada 5 diz não ter com quem contar na hora difícil.

Na internet, isso virou meme. Gen Z stare, task masking, o olhar vazio na reunião. É fácil rotular uma geração inteira. Mas sobrecarga, falta de sentido, ansiedade, sono ruim e solidão não têm idade, e vários desses são riscos psicossociais que a NR-01 agora pede para a empresa gerenciar.

No Escritório do Cuidado, todo atendimento começa com a mesma pergunta: o que importa para você? Médico, psicólogo e assistente social dentro da empresa, com um plano de cuidado para cada pessoa. O RH recebe só indicadores do grupo, anonimizados.

Comente CUIDADO e mostramos como funciona na sua empresa.

#fairhealth #saudecorporativa #geracaoz #saudemental #gestaodepessoas''',
  roteiro=[
   ('Slide 1 · capa', 'O olhar vazio na reunião não é preguiça.', '', 'Foto em tela cheia (jovem em reunião, olhar distante), manchete sem serifa.', 'Foto pendente.'),
   ('Slide 2 · promessa', 'Só 33% dos jovens de 16 a 24 anos se dizem muito satisfeitos com a vida. Dos 25 para cima, 47,9%.', '', 'Foto + dado com nome da pesquisa e da autora.', 'Foto pendente.'),
   ('Slide 3 · dado', '46,7% dos jovens dizem que o trabalho os deixa mais infelizes (20,5% nas outras idades).', '', 'Dado grande.', 'Foto pendente.'),
   ('Slide 4 · dado', 'Mais de 1 em cada 5 não tem com quem contar. 27% preocupados; 71,1% tristes com as redes.', '', 'Dado em lista.', '"Mais de 1 em cada 5" vem de 79% que têm com quem contar.'),
   ('Slide 5 · tendência e causa', 'Gen Z stare, task masking: o meme descreve um sintoma. As causas (sobrecarga, falta de sentido, ansiedade, sono ruim, solidão) não têm idade, e várias são riscos psicossociais da NR-01.', '', 'Texto em serif.', 'Junta os slides 5 e 6 do rascunho.'),
   ('Slide 6 · produto', 'No Escritório do Cuidado, todo atendimento começa com a mesma pergunta: o que importa para você?', '', 'Foto do espaço.', ''),
   ('Slide 7 · produto RH e salvamento', 'O RH recebe só indicadores do grupo, anonimizados.\nTrês perguntas para o líder fazer ao time.', '', 'Checklist.', 'Conferir o que o relatório mostra.'),
   ('Slide 8 · chamada', 'Geração Z não é o problema. Falta de cuidado é.\nComente CUIDADO.\nFonte completa da pesquisa.', '', 'Verde-escuro, logo.', ''),
  ]),

 dict(id='N12', data=D(27), semana=4, bloco='6 · Decisão', eixo='Cases + Produto', fmt=CARR,
  titulo='Case Chemitec: como 98% do time aceitou ser cuidado',
  sub='Adesão e continuidade num case real, com o convite ao diagnóstico antes do orçamento de 2027',
  status='Pauta proposta (calendário de novembro)', resp='Nina · Sócios (liberação do case)',
  espec='Carrossel 4:5 (1080 × 1350), 8 slides, estilo institucional. Sexta de Black Friday: sem linguagem de promoção.',
  gancho='98% do time aceitou ser cuidado. O que essa empresa fez diferente?',
  objetivo='Provar adesão e continuidade com um case real e convidar o RH ao diagnóstico antes do orçamento de 2027.',
  portras='Adesão não se impõe: acontece quando o cuidado está perto, começa pela escuta e cabe na rotina.',
  persona='RH; Diretoria financeira',
  fio='Vem de: 25/11, Geração Z. Leva para: 30/11, a virada para dezembro.',
  visual='Estilo institucional, um número por slide, calmo, sempre com "1º semestre de 2026". Fotos de banco de indústria (capacete, linha de produção), sem rosto de colaborador.',
  material='Tipografia e fotos de banco. Logo da Chemitec só com autorização.',
  cta='Comente CUIDADO (diagnóstico gratuito)',
  stories='Sequência com os 4 números e o adesivo "Mande uma mensagem".',
  fonte='Chemitec, 1º semestre de 2026 (voice.md, LIBERADO): 161 atendimentos; 48 colaboradores atendidos (98% de adesão); 81,3% voltaram para 2 ou mais atendimentos; 46 smartbands em uso. Sempre agregado.',
  validar='Decisão de 30/10 tirou dados de clientes dos posts: confirmar com os sócios se o case sai e se pode citar o nome Chemitec (autorização escrita do cliente). Se não puder, "uma indústria que atendemos". Conferir como foi a implantação (slide 2) antes de descrever.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/case-adesao/',
  legenda='''98% do time aceitou ser cuidado. O que essa empresa fez diferente?

Na Chemitec, no primeiro semestre de 2026, o Escritório do Cuidado atendeu 48 colaboradores, 98% de adesão. Foram 161 atendimentos, e 81,3% das pessoas voltaram para dois ou mais. Entre uma consulta e outra, 46 smartbands acompanham a rotina de quem é cuidado.

O que estava por trás: o cuidado perto de quem trabalha, a primeira consulta começando por "o que importa para você?" e um plano que cabe no turno. O RH recebe só indicadores do grupo, anonimizados.

Antes de fechar o orçamento de 2027, comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #escritoriodocuidado #gestaodepessoas #medicinadoestilodevida''',
  roteiro=[
   ('Slide 1 · capa', '98% do time aceitou ser cuidado.\nO que essa empresa fez diferente?', '', 'Foto de banco de indústria, número em destaque.', 'Nome do cliente só com autorização.'),
   ('Slide 2 · contexto', 'Uma indústria, primeiro semestre de 2026. O Escritório do Cuidado dentro da empresa.', '', 'Fundo claro.', 'Conferir como foi a implantação antes de detalhar.'),
   ('Slide 3 · adesão', '48 colaboradores atendidos\n98% de adesão', '', 'Fundo verde, número em Tiffany.', ''),
   ('Slide 4 · volume', '161 atendimentos no semestre', '', 'Fundo Tiffany.', ''),
   ('Slide 5 · continuidade', '81,3% voltaram para dois ou mais atendimentos.\nNinguém volta a um lugar onde não se sentiu cuidado.', '', 'Fundo verde.', ''),
   ('Slide 6 · entre as consultas', '46 smartbands acompanham a rotina de quem é cuidado.\nO RH recebe só indicadores do grupo.', '', 'Foto de pulseira (banco).', ''),
   ('Slide 7 · o que estava por trás', 'Cuidado perto de quem trabalha · a primeira consulta começa por "o que importa para você?" · um plano que cabe no turno', '', 'Fundo claro, três pontos no fio.', 'Fatos do método, sem frase-resumo.'),
   ('Slide 8 · chamada', 'Antes de fechar o orçamento de 2027:\ncomente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.', '', 'Verde-escuro, logo.', 'Sem "oferta", "promoção" ou "Black Friday".'),
  ]),

 dict(id='N13', data=D(30), semana=5, bloco='6 · Decisão', eixo='Cultura', fmt=REEL,
  titulo='Dezembro chegou: a corrida das metas também adoece',
  sub='Uma prática de 1 minuto para o fim de ano e o convite para cuidar antes de 2027',
  status='Pauta proposta (calendário de novembro)', resp='Nina · psicóloga ou Dr. Ronald (prática de 1 minuto)',
  espec=ESP_REEL + ' Tipografia animada com contagem de 1 minuto.',
  gancho='Dezembro chegou. E a corrida das metas também.',
  objetivo='Abrir dezembro com uma prática simples de 1 minuto para o time e o convite para a empresa cuidar antes de 2027.',
  portras='O fim de ano aperta todo mundo. Uma pausa pequena não resolve tudo, mas lembra que o cuidado cabe no dia.',
  persona='Colaboradores; RH; Lideranças',
  fio='Vem de: 27/11, o case. Leva para: o calendário de dezembro.',
  visual='Tipografia animada sobre Tiffany e verde, com um círculo que se fecha em 60 segundos durante a prática. Sem pessoas em cena.',
  material='Canva (animação de texto), trilha calma, sem locução ou com voz em off.',
  cta='Comente CUIDADO (diagnóstico gratuito)',
  stories='Contagem regressiva para 2027 e a pergunta "O que você quer levar de cuidado para o ano que vem?".',
  fonte='Prática de respiração e pausa: conteúdo educativo do guia "Saúde mental: o cuidado no dia a dia" (referencias.md). Sem número.',
  validar='A psicóloga ou o Dr. Ronald valida a prática (sem promessa de efeito). Sem número sem fonte.',
  arquivos='Ainda sem pasta. Sugestão: instagram/posts/dezembro-metas/',
  legenda='''Dezembro chegou. E a corrida das metas também.

Fechamento, entrega, confraternização, férias para organizar. O fim de ano aperta todo mundo ao mesmo tempo, e o cuidado costuma ficar para janeiro.

Uma pausa de um minuto não resolve tudo, mas lembra que o cuidado cabe no dia. Pare, solte os ombros, respire devagar cinco vezes e escolha uma coisa que importa hoje.

Para a empresa, o convite é o mesmo, numa escala maior: cuidar antes de 2027 começar. Comente CUIDADO e enviamos na DM como funciona o diagnóstico gratuito.

#fairhealth #saudecorporativa #saudemental #bemestarnotrabalho #gestaodepessoas''',
  roteiro=[
   ('0 a 3 s', 'Dezembro chegou.\nE a corrida das metas também.', '', 'Duas linhas, ritmo rápido.', 'Gancho.'),
   ('3 a 8 s', 'Fechamento. Entrega. Confraternização. Férias para organizar.', '', 'Palavras em sequência, aceleradas.', ''),
   ('8 a 12 s', 'Antes de seguir: 1 minuto.', '', 'O ritmo desacelera; aparece um círculo.', 'Virada.'),
   ('12 a 22 s', 'Pare. Solte os ombros.\nRespire devagar, cinco vezes.', '', 'O círculo se fecha devagar.', 'Prática validada pela psicóloga.'),
   ('22 a 26 s', 'Escolha uma coisa que importa hoje.', '', 'Frase única.', ''),
   ('26 a 30 s', 'Para a empresa: cuidar antes de 2027 começar.\nComente CUIDADO', '', 'Logo sobre Tiffany.', ''),
  ]),
]

PENDENCIAS = [
    ('N02', 'Publicação hoje (04/11): aprovar o roteiro do reel e produzir o motion. Definir com a fairdata o que o relatório do RH mostra.', 'Nina e fairdata', 'Urgente'),
    ('N01, N09', 'Formato dos depoimentos (A1 no 03/11, A2 no 19/11) com o Dr. Ronald.', 'Dr. Ronald', 'Aberta'),
    ('N03', 'Validar a história do Escritório (2009, hospital, como funcionava) e a descrição dos Aims.', 'Dr. Ronald', 'Aberta'),
    ('N03, N04, N12', 'Dados de clientes: a decisão de 30/10 tirou os números de cliente dos posts. Confirmar se o caso do hospital (06/11), os números da indústria (09/11) e o case Chemitec com nome (27/11) podem entrar.', 'Sócios', 'Aberta'),
    ('N04', 'Data de gravação do reel com o Dr. Ronald e autorização de uso de imagem.', 'Dr. Ronald e Comunicação', 'Aberta'),
    ('N05', 'Leitura do Diabetes Prevention Program pela responsável médica. Escolher a capa (estudo ou canetas).', 'Responsável médica', 'Aberta'),
    ('N06', 'Resposta automática da palavra CUIDADO e página do diagnóstico prontas até 13/11. Quem responde as DMs até lá.', 'Comunicação', 'Aberta'),
    ('N07', 'Achar e conferir um dado sobre homens e consultas (fonte oficial). Revisão técnica do Dr. Ronald.', 'Comunicação e Dr. Ronald', 'Aberta'),
    ('N08', 'Número conferido na nota oficial da Previdência e texto da NR-01 conferido no PDF do MTE (04/11). Falta a leitura do Dr. Ronald e o ok da Nina para citar a fairdata.', 'Comunicação e Dr. Ronald', 'Aberta'),
    ('N10', 'Conferir os números do Panorama da Saúde Emocional do RH 2026 no material da Flash.', 'Comunicação', 'Aberta'),
    ('N11', 'Fotos dos slides 1 a 4, corte para 8 slides e conferência dos números do Mapa da Felicidade.', 'Nina', 'Aberta'),
    ('N13', 'Validar a prática de 1 minuto.', 'Psicóloga ou Dr. Ronald', 'Aberta'),
    ('Todos', 'Legendas novas (04/11 em diante) passam pela ig-caption e pela ig-human antes de publicar; fotos com licença e origem confirmadas.', 'Comunicação', 'Aberta'),
]

DATAS = [
    (D(2), 'Finados (feriado, sem post)'),
    (D(14), 'Dia Mundial do Diabetes (sábado)'),
    (D(15), 'Proclamação da República (domingo)'),
    (D(20), 'Consciência Negra (feriado): o post da semana vai para quinta, 19/11'),
    (D(27), 'Black Friday: sem linguagem de promoção'),
    (D(30), 'Novembro Azul o mês todo; 30/11 abre a passagem para dezembro'),
]
