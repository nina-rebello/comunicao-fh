# Detalhamento dos 13 posts de dezembro de 2026 (02/12 a 30/12), usado por gerar_cronograma_simples.py (modelo padrão).
# Base: as inspirações que a Nina mandou em 18/11 (instagram/inspiracoes-dezembro.md), o ritmo de novembro
# (conteudo_posts_novembro.py), instagram/carrossel-de-tendencia.md (sleepmaxxing guardado para dezembro),
# instagram/voice.md, instagram/referencias.md (site da fairjob, programa de 4 meses) e o CLAUDE.md.
# Regras: "fairhealth" em minúsculas, sem travessão, 5 hashtags começando por #fairhealth, número só com fonte
# (sem fonte conferida, o roteiro sai com {{número + fonte}}), sem promessa clínica, sem preço, sem diagnóstico gratuito,
# comunicação B2B, carrossel de 5 a 8 slides sem numeração, uma chamada só, MEV dentro do Escritório do Cuidado,
# bioimpedância e smartwatch sempre que falar de atendimento ou medição, programa de 4 meses.
import datetime as dt

D = lambda d: dt.date(2026, 12, d)
REEL, CARR, FOTO = 'Reel', 'Carrossel', 'Foto única'
VIS = 'Direção visual'

POSTS = [
 dict(id='D01', data=D(2), semana=1, bloco='7 · Causas', eixo='Cultura + Produto', fmt=CARR,
  titulo='Por que as pessoas pedem demissão?',
  sub='O motivo que o RH só descobre na entrevista de desligamento e o que existe por trás dele',
  inspiracao='Print "Por que as contas atrasam?" (gráfico de barras em carrossel) + legenda da Nina: "por que as pessoas se demitem?"',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='{{4 motivos de pedido de demissão com percentuais + pesquisa e ano}} (buscar pesquisa brasileira recente e conferir no original). NR-01 e fatores psicossociais: gov.br/MTE (mesma conferência do 18/11).',
  validar='Achar e conferir a pesquisa dos motivos (sem ela, o slide 3 não sai com percentuais). Revisão do Dr. Ronald (NR-01).',
  roteiro=[
   ('Slide 1 · capa', 'Por que as pessoas pedem demissão?\nO que o RH só descobre na entrevista de desligamento.', '', '', ''),
   ('Slide 2 · contexto', 'A entrevista de desligamento chega tarde.\nQuando a pessoa já decidiu sair, o motivo começou antes. E quase sempre ficou sem ser dito.', '', '', ''),
   ('Slide 3 · dado (gráfico de barras)', 'Os motivos mais citados\n{{motivo 1 · %}} · {{motivo 2 · %}} · {{motivo 3 · %}} · {{outros · %}}\nFonte: {{pesquisa, ano, número de respondentes}}', '', '', 'Sem os percentuais conferidos, o slide não sai.'),
   ('Slide 4 · o que existe por trás', 'Por trás do motivo, quase sempre há uma causa de saúde: sobrecarga, sono ruim, ansiedade, conflito com a liderança.\nVários desses são fatores de risco psicossocial, tema que a NR-01 trata como de gestão.', '', '', ''),
   ('Slide 5 · produto', 'No Escritório do Cuidado, a primeira pergunta é: o que importa para você?\nMédico, psicólogo e assistente social dentro da empresa, presencial ou remoto. O plano é feito com a pessoa, com base na Medicina do Estilo de Vida, com bioimpedância e smartwatch acompanhando a rotina.', '', '', ''),
   ('Slide 6 · RH + convite', 'O RH não fica sabendo o que cada um conta. Recebe só indicadores do grupo, anonimizados, para agir antes que o desgaste vire saída ou afastamento.\nQuer ver como isso funciona na sua empresa? Comente CUIDADO.', '', '', 'Chamada única.'),
   (VIS, 'Fundo creme/papel, título em Raleway. No slide 3, barras horizontais como no print: percentual à esquerda, ícone linear à direita, a barra maior em verde-azulado escuro (#2F6B64) e as demais em Tiffany (#9FC5BD). Sem vermelho nem emoji. Slide 5 com foto do espaço ou de banco; fundo verde-azulado escuro só em um slide de contraste.', '', '', ''),
  ],
  legenda='''Por que as pessoas pedem demissão? O RH costuma descobrir só na entrevista de desligamento, quando a decisão já foi tomada.

No carrossel, os motivos mais citados em {{pesquisa + ano}} e o que costuma existir por trás deles: sobrecarga, sono ruim, ansiedade e conflito com a liderança. Vários são fatores de risco psicossocial, tema que a NR-01 trata como de gestão.

No Escritório do Cuidado, a conversa começa por uma pergunta: o que importa para você? Médico, psicólogo e assistente social dentro da empresa escutam, e o plano é feito com a pessoa, com base na Medicina do Estilo de Vida. A bioimpedância e o smartwatch acompanham a rotina entre uma consulta e outra.

O RH não fica sabendo o que cada um conta. Recebe só indicadores do grupo, anonimizados, para agir antes que o desgaste vire saída ou afastamento.

Quer entender como isso funcionaria na sua empresa? Comente CUIDADO e enviamos como funciona o Escritório do Cuidado.

#fairhealth #saudecorporativa #gestaodepessoas #turnover #medicinadoestilodevida''',
  palavras='pedem demissão,entrevista de desligamento,Escritório do Cuidado'),

 dict(id='D02', data=D(4), semana=1, bloco='7 · Causas', eixo='Produto', fmt=FOTO,
  titulo='Todo mundo precisa de alguém por perto',
  sub='Escuta, clareza e um plano possível, dentro da empresa',
  inspiracao='Post "Everyone needs someone in their corner" (Reality With PSJ): foto aérea de duas pessoas em poltronas, creme, verde e terracota.',
  cta='Mande esta imagem para quem cuida das pessoas na sua empresa',
  fonte='Sem número. Descrição do Escritório do Cuidado conforme o site da fairjob (referencias.md).',
  validar='Foto de banco com licença comercial (vista de cima, duas pessoas conversando, poltronas e piso claro). Nenhum colaborador atendido.',
  roteiro=[
   ('Imagem única 4:5', 'Todo mundo precisa de alguém por perto.\nEscuta, clareza e um plano possível, dentro da empresa.\nEscuta · Clareza · Plano', '', '', 'Sem telefone nem @ de outra marca.'),
   (VIS, 'Foto aérea de duas pessoas conversando em poltronas, piso claro, uma planta na mesinha. Aspas grandes em Tiffany claro no alto, título em Raleway 800 verde-azulado escuro (#2F6B64), as três palavras no canto de baixo, uma em Tiffany. Logo fairhealth no canto, sem rodapé de contato. Cuidar para o verde das poltronas combinar com o verde da marca.', '', '', ''),
  ],
  legenda='''Todo mundo precisa de alguém por perto. No trabalho também.

Alguém para escutar sem pressa, ajudar a enxergar com clareza o que pesa e montar um plano que caiba na rotina.

É isso que o Escritório do Cuidado leva para dentro da empresa: médico, psicólogo e assistente social, presencial ou remoto, e um plano individual de cuidado com base na Medicina do Estilo de Vida.

Mande esta imagem para quem cuida das pessoas na sua empresa.

#fairhealth #saudecorporativa #escritoriodocuidado #cuidadocentradonapessoa #gestaodepessoas''',
  palavras='Escritório do Cuidado,Medicina do Estilo de Vida,dentro da empresa'),

 dict(id='D03', data=D(7), semana=2, bloco='8 · Sono e dados', eixo='Cultura + Produto', fmt=CARR,
  titulo='Seu sono virou nota no relógio. Por que o cansaço continua?',
  sub='O que o smartwatch mostra, o que ele não mostra e onde o cuidado começa',
  inspiracao='Post "Responsible.fit" (dados de sono sobrepostos à foto de quem dorme) e a pauta sleepmaxxing guardada em carrossel-de-tendencia.md.',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='Sono reparador como pilar da MEV (Cartilha do Escritório do Cuidado). Sleepmaxxing: tendência citada sem número. Sem dado de cliente.',
  validar='Quais dados o smartwatch de vocês registra (mesma pendência dos posts de wearables). Revisão do Dr. Ronald. Foto da capa (pessoa dormindo, banco) com os dados sobrepostos marcados como exemplo.',
  roteiro=[
   ('Slide 1 · capa', 'Seu sono virou nota no relógio.\nPor que o cansaço continua?', '', '', 'Dados sobrepostos à foto são de exemplo.'),
   ('Slide 2 · promessa (funciona sozinho)', 'A nota mostra como você dormiu. Ela não mostra por quê. É aí que o cuidado começa.', '', '', ''),
   ('Slide 3 · a tendência', 'O sleepmaxxing viralizou: aparelhos, suplementos, rotinas de vinte passos e a busca por uma nota perfeita.\nMuita coisa sem comprovação. E tem gente perdendo o sono por causa da própria nota.', '', '', ''),
   ('Slide 4 · entrega técnica', 'O sono depende de horário, luz, cafeína, estresse, dor, turno e da cabeça que não desliga.\nNenhum aparelho resolve isso sozinho. Sono reparador é um dos sete pilares da Medicina do Estilo de Vida.', '', '', ''),
   ('Slide 5 · o que o relógio vê', 'O que o smartwatch vê: duração, regularidade, frequência cardíaca.\nO que ele não vê: o prazo, o filho pequeno, a dor no fim do dia, a escala da noite.', '', '', 'Confirmar os dados que o aparelho registra.'),
   ('Slide 6 · salvamento', 'Antes do próximo aparelho, três perguntas:\nO que mudou na minha rotina?\nO que me acorda ou não me deixa dormir?\nCom quem posso olhar isso?', '', '', ''),
   ('Slide 7 · produto', 'No Escritório do Cuidado, o smartwatch e a bioimpedância entram na consulta. "Acho que durmo mal" vira olhar, junto com o profissional, como foram as últimas semanas. E a causa define quem cuida: médico, psicólogo ou assistente social.', '', '', ''),
   ('Slide 8 · RH + convite', 'O RH não vê o sono de ninguém. Recebe só indicadores do grupo, anonimizados.\nQuer ver como funciona na sua empresa? Comente CUIDADO.', '', '', 'Chamada única.'),
   (VIS, 'Capa: foto de quem dorme com a leitura do relógio sobreposta (duração, fases do sono, recuperação), em branco fino e transparente, sobre tons escuros e quentes da foto. Atenção: fundo azul escuro só na foto, sem virar cor de destaque. Do slide 2 em diante, fundo creme e Raleway, o Tiffany nos destaques; o slide 5 em duas colunas (vê / não vê).', '', '', ''),
  ],
  legenda='''Seu sono virou nota no relógio. Por que o cansaço continua?

A nota mostra como você dormiu. Ela não mostra por quê. Prazo, filho pequeno, dor no fim do dia e a escala da noite não aparecem no aplicativo.

O sleepmaxxing viralizou com aparelhos, suplementos e rotinas de vinte passos. Mas o sono depende de horário, luz, cafeína, estresse e da cabeça que não desliga, e é um dos sete pilares da Medicina do Estilo de Vida.

No Escritório do Cuidado, o dado do smartwatch entra na consulta. Em vez de "acho que durmo mal", a conversa olha com a pessoa como foram as últimas semanas, e a causa define quem cuida: médico, psicólogo ou assistente social. O RH recebe só indicadores do grupo, anonimizados.

Quer ver como funciona na sua empresa? Comente CUIDADO.

#fairhealth #saudecorporativa #sono #wearables #medicinadoestilodevida''',
  palavras='smartwatch,cansaço,sleepmaxxing'),

 dict(id='D04', data=D(9), semana=2, bloco='8 · Sono e dados', eixo='Cultura', fmt=REEL,
  titulo='Acordar toda hora: você dorme, mas não descansa',
  sub='Por que oito horas na cama nem sempre são oito horas de descanso',
  inspiracao='Post do médico do sono (tipografia grande em duas camadas sobre foto de quem acorda cansado). O gancho foi reescrito, não copiado.',
  cta='Mande este reel para quem cuida do time na sua empresa',
  fonte='Sono reparador como pilar da MEV (Cartilha). A explicação sobre sono interrompido é conteúdo educativo geral e precisa da revisão médica antes de gravar.',
  validar='Revisão do roteiro pelo Dr. Ronald (sono interrompido, sinais de procurar um profissional). Se ele aparecer, nome e CRM na tela (regras do CFM). Data de gravação.',
  roteiro=[
   ('0 a 3 s', 'Acordar toda hora: você dorme, mas não descansa.', 'Acordar toda hora é diferente de dormir pouco: você dorme, mas não descansa.', 'Plano médio, olhar na câmera. Texto em duas camadas: a primeira frase pequena, "NÃO DESCANSA." enorme, em branco.', 'Gancho.'),
   ('3 a 12 s', 'Oito horas na cama não são oito horas de descanso.', 'Dá para passar oito horas na cama e acordar cansado. Quando o sono é interrompido várias vezes, ele deixa de ser contínuo, e o corpo descansa menos.', 'Plano mais fechado.', 'Validar a frase com o médico.'),
   ('12 a 22 s', 'Horário · luz · cafeína · estresse · dor · turno', 'O que interrompe a noite varia: horário, luz, cafeína, estresse, dor, turno de trabalho. Sono reparador é um dos sete pilares da Medicina do Estilo de Vida, e é por aí que o cuidado começa.', 'As seis palavras entram uma a uma na tela, em Tiffany.', ''),
   ('22 a 32 s', 'Escritório do Cuidado: o profissional olha a causa. O smartwatch mostra a rotina.', 'No Escritório do Cuidado, o médico e o psicólogo olham a causa com a pessoa. E o smartwatch mostra como foi a rotina entre uma consulta e outra, para a conversa partir de fatos.', 'Corte para o motion do relógio (sem dados reais).', ''),
   ('32 a 38 s', 'Cansaço constante pede um profissional de saúde.', 'Se o cansaço é constante, procure um profissional de saúde. E, se você cuida de um time, mande este reel para quem precisa ouvir isso.', 'Volta ao plano médio. Logo no fim.', 'Chamada única.'),
   (VIS, 'Reel 9:16, 35 a 40 s, para a câmera, legendas sempre. Cena em tons neutros e quentes (cabeceira, luz de abajur) ou o consultório do Escritório. Tipografia grande em Raleway 800 como no post de referência; fundo de destaque só Tiffany ou neutro. Capa 4:5 com a frase do gancho.', '', '', ''),
  ],
  legenda='''Acordar toda hora é diferente de dormir pouco. Mande este reel para quem cuida do time na sua empresa.

Dormir oito horas e acordar cansado acontece, e o motivo costuma estar na noite picada: o sono interrompido várias vezes descansa menos do que o contínuo.

Horário, luz, cafeína, estresse, dor e turno entram na conta. O sono reparador é um dos sete pilares da Medicina do Estilo de Vida e um bom ponto de partida para o cuidado.

No Escritório do Cuidado, o médico e o psicólogo olham a causa com a pessoa, e o smartwatch ajuda a ver como foi a rotina entre uma consulta e outra.

Se o cansaço é constante, vale procurar um profissional de saúde.

#fairhealth #saudecorporativa #sonoreparador #medicinadoestilodevida #gestaodepessoas''',
  palavras='sono reparador,acordar cansado,sono interrompido'),

 dict(id='D05', data=D(11), semana=2, bloco='8 · Sono e dados', eixo='Produto', fmt=REEL,
  titulo='O número do dia não conta a história toda',
  sub='Bioimpedância e smartwatch: a tendência de semanas entra na consulta',
  inspiracao='Imagem da balança com o aplicativo ao lado (tela com composição corporal e gráfico de tendência).',
  cta='Mande este reel para quem cuida do time na sua empresa',
  fonte='Site da fairjob (medições com tecnologia, bioimpedância e smartwatch). Sem número. Sem "por 48 horas" (não está no site).',
  validar='Quais dados o smartwatch e a bioimpedância registram de fato. Tela do aplicativo no motion é genérica, sem dados reais e sem peso na tela.',
  roteiro=[
   ('0 a 3 s', 'Um número isolado não é diagnóstico.', '', 'Motion: balança e celular com uma linha de tendência. Sem pessoas em cena.', 'Gancho.'),
   ('3 a 10 s', 'Bioimpedância: a composição corporal ao longo do tempo.', '', 'O gráfico mostra a linha, não um valor.', 'Evitar peso na tela.'),
   ('10 a 17 s', 'Smartwatch: sono, atividade e frequência cardíaca entre as consultas.', '', 'Ícones lineares finos em Tiffany.', 'Confirmar os dados que o aparelho registra.'),
   ('17 a 24 s', 'Na consulta, a conversa olha as últimas semanas. O plano é feito com a pessoa, pela Medicina do Estilo de Vida.', '', 'As duas linhas se juntam numa página de consulta.', ''),
   ('24 a 30 s', 'Os dados de cada pessoa ficam no atendimento. O RH recebe só indicadores do grupo, anonimizados.\nMande para quem cuida do time.', '', 'Logo e chamada no fim.', 'Chamada única.'),
   (VIS, 'Reel 9:16, 25 a 30 s, motion, sem fala, trilha calma. Fundo creme, linhas em verde-azulado escuro e Tiffany, tipografia Raleway. A balança e o celular do exemplo servem só de referência de composição: no motion, usar formas lisas e uma tela genérica.', '', '', ''),
  ],
  legenda='''Um número isolado não é diagnóstico. O que a consulta olha é a tendência. Mande este reel para quem cuida do time.

No Escritório do Cuidado, a bioimpedância mostra a composição corporal ao longo do tempo, e o smartwatch acompanha sono, atividade e frequência cardíaca entre uma consulta e outra.

Os dois entram na conversa com o profissional, que olha as últimas semanas e monta o plano com a pessoa, com base na Medicina do Estilo de Vida.

Nada disso vira vigilância. Os dados de cada pessoa ficam no atendimento, e o RH recebe só indicadores do grupo, anonimizados.

#fairhealth #saudecorporativa #bioimpedancia #smartwatch #medicinadoestilodevida''',
  palavras='bioimpedância,smartwatch,composição corporal'),

 dict(id='D06', data=D(14), semana=3, bloco='9 · Esgotamento', eixo='Notícias + Produto', fmt=CARR,
  titulo='3 sinais de esgotamento no trabalho que a OMS descreve',
  sub='O cansaço constante não é fraqueza',
  inspiracao='Posts "Esgotamento emocional" (colagem sobre papel, destaque na palavra) e "Bournout em mulheres multitarefas" ("sinal de burnout e não de fraqueza").',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='OMS, CID-11: burnout como fenômeno ocupacional, resultado de estresse crônico no trabalho que não foi bem gerenciado, com três dimensões (exaustão, distanciamento mental ou cinismo, menor eficácia profissional). Conferir o texto no site da OMS. Guia "Saúde mental: o cuidado no dia a dia" (OMS, APA, IPq-USP). NR-01: gov.br/MTE. CVV 188.',
  validar='Conferir o texto da OMS no original e a redação sobre a NR-01. Revisão do Dr. Ronald ou da psicóloga (sem rótulo de diagnóstico).',
  roteiro=[
   ('Slide 1 · capa', '3 sinais de esgotamento no trabalho que a OMS descreve.\nO cansaço constante não é fraqueza.', '', '', ''),
   ('Slide 2 · contexto', 'A OMS trata o burnout como um fenômeno ligado ao trabalho: estresse crônico que não foi bem gerenciado.\nNão é falta de caráter, e não é fraqueza.', '', '', 'Conferir a redação no original da OMS.'),
   ('Slide 3 · Exaustão', 'Exaustão\nA sensação de que a energia acabou, mesmo depois de descansar.', '', '', ''),
   ('Slide 4 · Distanciamento', 'Distanciamento\nO trabalho passa a pesar mais: a pessoa se afasta, perde o interesse ou fica cética.', '', '', ''),
   ('Slide 5 · Eficácia', 'Menor eficácia\nA sensação de que, por mais que se esforce, o resultado não aparece.', '', '', ''),
   ('Slide 6 · o que o líder pode fazer', 'Rotular não ajuda. Perguntar ajuda: o que está pesando?\nSobrecarga, pouca autonomia e conflito estão entre os fatores de risco psicossocial que a NR-01 trata como de gestão.', '', '', ''),
   ('Slide 7 · produto + convite', 'No Escritório do Cuidado, psicólogo, médico e assistente social escutam e acompanham. O RH recebe só indicadores do grupo, anonimizados.\nQuer ver como funciona na sua empresa? Comente CUIDADO.\nPrecisa de ajuda agora? CVV, 188, 24 horas.', '', '', 'Chamada única; CVV em texto pequeno.'),
   (VIS, 'Fundo de papel creme com textura leve. Título em Raleway 800; a palavra em destaque (exaustão, distanciamento, eficácia) em Instrument Serif itálico, só ela. Marca-texto em Tiffany (#9FC5BD) atrás da palavra, no lugar do azul do post de referência. Colagem em preto e branco de uma pessoa cansada (banco) com o rabisco desenhado em verde-azulado escuro. Sem foto de rosto identificável.', '', '', ''),
  ],
  legenda='''3 sinais de esgotamento no trabalho que a OMS descreve. O cansaço constante não é fraqueza.

A OMS trata o burnout como um fenômeno ligado ao trabalho: estresse crônico que não foi bem gerenciado. Os três sinais que ela descreve são exaustão, distanciamento do trabalho e sensação de menor eficácia.

Para quem lidera, rotular alguém não ajuda. Perguntar o que está pesando ajuda. Sobrecarga, pouca autonomia e conflito estão entre os fatores de risco psicossocial que a NR-01 trata como de gestão, e a saúde mental no trabalho é parte disso.

No Escritório do Cuidado, psicólogo, médico e assistente social escutam e acompanham. O RH recebe só indicadores do grupo, anonimizados.

Se você ou alguém do seu time precisa de ajuda agora, o CVV atende 24 horas pelo 188.

Quer entender como funciona na sua empresa? Comente CUIDADO.

#fairhealth #saudementalnotrabalho #burnout #nr01 #saudecorporativa''',
  palavras='saúde mental no trabalho,burnout,esgotamento'),

 dict(id='D07', data=D(16), semana=3, bloco='9 · Esgotamento', eixo='Cultura + Produto', fmt=CARR,
  titulo='O que influencia a felicidade dos seus colaboradores?',
  sub='Sono, relações, contas e propósito: o que pesa e quem cuida de cada parte',
  inspiracao='Print "O que influencia sua saúde financeira" (controles deslizantes com percentuais) + legenda da Nina: "o que influencia a felicidade de seus colaboradores".',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='{{percentuais dos fatores que mais influenciam a felicidade + pesquisa e ano}}. Candidata: Mapa da Felicidade Real dos Brasileiros 2026 (Renata Rivetti e Instituto Ideia), já usado em 25/11: conferir se traz os fatores. Pilares da MEV: Cartilha do Escritório do Cuidado. Felicitologista: site da fairjob.',
  validar='Os percentuais e a fonte (sem eles, os controles deslizantes não têm posição e o slide 3 não sai). Não repetir os números da Geração Z de 25/11.',
  roteiro=[
   ('Slide 1 · capa', 'O que influencia a felicidade dos seus colaboradores?\nÀs vezes, a resposta está na rotina e não no cargo.', '', '', ''),
   ('Slide 2 · contexto', 'Felicidade no trabalho não é clima de festa. É um conjunto de coisas que a empresa pode enxergar e cuidar.', '', '', ''),
   ('Slide 3 · dado (controles deslizantes)', 'O que mais pesa\nSono e energia · {{%}}\nRelações · {{%}}\nContas em dia · {{%}}\nPropósito · {{%}}\nFonte: {{pesquisa, ano}}', '', '', 'Sem percentuais conferidos, o slide não sai. Os fatores podem mudar conforme a pesquisa.'),
   ('Slide 4 · sono e energia', 'Sono e energia\nSono reparador é um dos sete pilares da Medicina do Estilo de Vida. Quem dorme mal sente o dia inteiro.', '', '', ''),
   ('Slide 5 · relações e propósito', 'Relações e propósito\nSentir que pertence e que o trabalho faz sentido também são pilares da MEV, e é onde a escuta da liderança mais pesa.', '', '', ''),
   ('Slide 6 · contas', 'Contas em dia\nFim de ano aperta a conta de muita gente. No Escritório do Cuidado, o assistente social ajuda a olhar o que pesa fora do trabalho.', '', '', ''),
   ('Slide 7 · produto + convite', 'No Escritório do Cuidado, médico, psicólogo, assistente social e felicitologista cuidam de cada parte. O RH recebe só indicadores do grupo, anonimizados.\nQuer ver como funciona na sua empresa? Comente CUIDADO.', '', '', 'Chamada única.'),
   (VIS, 'Fundo off-white leve. No slide 3, controles deslizantes como no print: linha fina em Tiffany claro, marcador em verde-azulado escuro (um coração só se combinar com a marca; senão, uma bolinha), percentual à direita. Sem verde de outra paleta: o verde do print vira o nosso Tiffany e o verde-azulado escuro (#2F6B64). Um slide pequeno de rosca no fim do slide 3 não é necessário.', '', '', ''),
  ],
  legenda='''O que influencia a felicidade de quem trabalha com você? Sono, relações, contas e propósito entram na conta.

No carrossel, os fatores que mais pesam segundo {{pesquisa + ano}}. Vários são pilares da Medicina do Estilo de Vida: sono reparador, relações sociais, saúde mental e propósito. Outros, como a conta que aperta no fim do ano, pedem a escuta do serviço social.

No Escritório do Cuidado, médico, psicólogo, assistente social e felicitologista cuidam de cada parte, presencial ou remoto, com um plano individual feito com a pessoa. O RH recebe só indicadores do grupo, anonimizados.

Quer ver como funciona na sua empresa? Comente CUIDADO.

#fairhealth #saudecorporativa #felicidadenotrabalho #medicinadoestilodevida #gestaodepessoas''',
  palavras='felicidade de quem trabalha,Medicina do Estilo de Vida,saúde mental'),

 dict(id='D08', data=D(18), semana=3, bloco='9 · Esgotamento', eixo='Notícias + Produto', fmt=REEL,
  titulo='A empresa acha que cuida. O time percebe?',
  sub='A distância entre querer um empregador que cuide e sentir que a empresa cuida',
  inspiracao='Post "The workplace wellness gap is growing" (número grande em branco, frase ao lado, chave e chamada com seta).',
  cta='Mande este reel para quem cuida de gente na sua empresa',
  fonte='{{% de colaboradores que querem um empregador que valorize o bem-estar + % que acreditam que o seu valoriza + pesquisa, ano e país}}. O post de referência traz 92% e 60%, sem fonte visível: não usar sem achar e conferir a pesquisa original, de preferência brasileira. 8 em cada 10 voltaram para mais de um atendimento: indústria atendida, 1º semestre de 2026 (depende da liberação dos sócios).',
  validar='Achar a pesquisa dos dois números. Liberação dos dados de cliente (decisão de 30/10). Quem fala no vídeo.',
  roteiro=[
   ('0 a 3 s', 'A empresa acha que cuida. O time percebe?', 'A empresa acha que cuida. Mas o time percebe?', 'Plano médio, para a câmera. Título em duas linhas, a segunda em destaque.', 'Gancho.'),
   ('3 a 12 s', '{{%}} querem um empregador que valorize o bem-estar.\nSó {{%}} acham que o seu valoriza.\nFonte: {{pesquisa, ano}}', 'Quase todo mundo quer trabalhar numa empresa que valoriza o bem-estar. Mas só uma parte acha que a sua realmente valoriza.', 'O primeiro número grande em branco na tela, a frase ao lado; o segundo número aparece embaixo, com a chave.', 'Sem números conferidos, esta cena não sai.'),
   ('12 a 22 s', 'Programa que ninguém usa não chega a quem precisa.', 'Entre a intenção da empresa e a percepção do time costuma ter um programa que ninguém usa. Adesão é o primeiro resultado a medir.', 'Plano mais fechado.', 'Posição da marca (voice.md).'),
   ('22 a 32 s', 'Perto do trabalho, o cuidado chega.\n8 em cada 10 voltaram para mais de um atendimento\n(uma indústria atendida, 1º semestre de 2026)', 'Quando o cuidado fica dentro da empresa, com escuta e um plano individual, as pessoas voltam. Numa indústria que atendemos, oito em cada dez voltaram para mais de um atendimento.', 'Números em Tiffany.', 'Depende da liberação dos dados de cliente.'),
   ('32 a 38 s', 'Mande para quem cuida de gente na sua empresa.', 'Se você cuida de gente na sua empresa, mande este reel para quem precisa ver.', 'Logo no fim.', 'Chamada única.'),
   (VIS, 'Reel 9:16, 35 a 40 s, para a câmera, legendas sempre. Os dois números como no post de referência: o primeiro grande e branco com a frase ao lado, o segundo menor logo abaixo, com uma chave fina e a chamada com seta. Fundo verde-azulado escuro (#2F6B64) só neste reel como contraste (não o verde-limão do post), texto branco e destaques em Tiffany.', '', '', ''),
  ],
  legenda='''Querer um empregador que cuide é uma coisa. Sentir que a empresa cuida é outra. Mande este reel para o RH.

{{% querem}} dos colaboradores querem trabalhar numa empresa que valorize o bem-estar, mas só {{% acham}} acham que a sua realmente valoriza ({{pesquisa + ano}}).

Programa que ninguém usa não chega a quem precisa. Adesão é o primeiro resultado a medir, e ela cresce quando o cuidado fica perto: numa indústria que atendemos, no primeiro semestre de 2026, 8 em cada 10 colaboradores voltaram para dois ou mais atendimentos no Escritório do Cuidado.

#fairhealth #saudecorporativa #bemestarcorporativo #gestaodepessoas #escritoriodocuidado''',
  palavras='bem-estar,Escritório do Cuidado,adesão'),

 dict(id='D09', data=D(21), semana=4, bloco='10 · Começar', eixo='Produto + Mercado', fmt=CARR,
  titulo='O que o RH recebe do Escritório do Cuidado?',
  sub='Um relatório de indicadores do grupo, anonimizados, sem o nome de ninguém',
  inspiracao='Post do case study (folha de relatório num fichário, com visão geral e três cartões de destaques).',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='Site da fairjob: "relatórios de tendências de saúde, anonimizados e agregados, no painel fairdata"; diagnóstico integrado no 1º mês e mensuração com ciclo de pesquisa fairdata. Programa de 4 meses (Nina, 13/11).',
  validar='O que o relatório do RH mostra de fato (fairdata). Mesma pendência do 04/11: não mostrar indicador que ainda não existe. Todos os números da folha são exemplo e vêm marcados assim.',
  roteiro=[
   ('Slide 1 · capa', 'O que o RH recebe do Escritório do Cuidado?\nIndicadores do grupo. Nunca de uma pessoa.', '', '', ''),
   ('Slide 2 · a folha', 'Exemplo de relatório\nVisão geral do grupo\nTrês destaques: {{indicador 1}} · {{indicador 2}} · {{indicador 3}}\n(dados de exemplo, sem números reais)', '', '', 'Marcar "dados de exemplo" na folha.'),
   ('Slide 3 · o que entra', 'O que entra\nIndicadores de tendência do grupo, anonimizados e agregados, no painel fairdata.', '', '', ''),
   ('Slide 4 · o que não entra', 'O que não entra\nNome, conversa de atendimento e histórico clínico de cada pessoa. O que é conversado fica no atendimento.', '', '', ''),
   ('Slide 5 · a jornada', 'Ao longo do programa de 4 meses\nNo 1º mês, diagnóstico integrado do grupo. Do 1º ao 4º mês, Escritório do Cuidado, com Medicina do Estilo de Vida, bioimpedância e smartwatch. No 4º mês, mensuração dos indicadores.', '', '', ''),
   ('Slide 6 · convite', 'Para que serve: o RH escolhe onde agir com base em evidência, e não em suposição.\nQuer ver um exemplo completo? Comente CUIDADO.', '', '', 'Chamada única.'),
   (VIS, 'Slide 2 é o centro do post: uma folha branca de relatório em perspectiva leve, sobre fundo neutro escuro ou pedra (sem o azul-bebê do post de referência), com visão geral e três cartões de destaque em Tiffany claro. Tudo em Raleway, ícones lineares, rodapé "dados de exemplo". Os demais slides, fundo creme, um bloco por slide.', '', '', ''),
  ],
  legenda='''O RH recebe um relatório do Escritório do Cuidado. Nele não há o nome de ninguém.

São indicadores do grupo, anonimizados e agregados, no painel fairdata. O que cada pessoa conta fica no atendimento.

No programa de quatro meses, o diagnóstico integrado do grupo acontece no primeiro mês. Do primeiro ao quarto mês, o Escritório do Cuidado atende, com a Medicina do Estilo de Vida, a bioimpedância e o smartwatch. No quarto mês, os indicadores são medidos de novo.

O objetivo é o RH escolher onde agir com base em evidência, e não em suposição.

Quer ver um exemplo completo? Comente CUIDADO e enviamos como funciona o Escritório do Cuidado.

#fairhealth #saudecorporativa #fairdata #gestaodepessoas #indicadoresdesaude''',
  palavras='indicadores do grupo,anonimizados,painel fairdata'),

 dict(id='D10', data=D(23), semana=4, bloco='10 · Começar', eixo='Produto', fmt=REEL,
  titulo='Janeiro está aí: por onde o cuidado começa na empresa',
  sub='Conversa, proposta personalizada e implementação, num programa de 4 meses',
  inspiracao='Fechamento do mês no mesmo estilo de motion de 04/11 (fio contínuo com pontos), mais a frase de apoio do post "Corporate wellness" (declaração curta, centralizada).',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='Executive Summary (entrada comercial: conversa, proposta, implementação) e site da fairjob (proposta personalizada, onboarding e primeiros atendimentos). Programa de 4 meses (Nina, 13/11). Sem diagnóstico gratuito, sem preço, sem prazo além do que está no site.',
  validar='Nada além do que está no site e em referencias.md. Resposta automática da palavra CUIDADO funcionando até 23/12.',
  roteiro=[
   ('0 a 3 s', 'Janeiro está aí. Por onde o cuidado começa?', '', 'Motion: fundo verde-azulado escuro (#2F6B64) só neste reel como contraste, texto creme. O fio entra pela esquerda.', 'Gancho.'),
   ('3 a 9 s', 'Uma conversa com o time', '', 'Ponto 1 no fio, ícone linear.', ''),
   ('9 a 15 s', 'Uma proposta personalizada\nUm programa sob medida para o seu time', '', 'Ponto 2.', 'Texto do site.'),
   ('15 a 21 s', 'Implementação\nOnboarding e primeiros atendimentos', '', 'Ponto 3.', 'Texto do site.'),
   ('21 a 27 s', 'Programa de 4 meses\nDiagnóstico no 1º mês · Escritório do Cuidado do 1º ao 4º · Mensuração no 4º', '', 'O fio vira uma linha do tempo de 4 marcos.', ''),
   ('27 a 30 s', 'Comente CUIDADO e enviamos como funciona.', '', 'Logo e chamada.', 'Chamada única.'),
   (VIS, 'Reel 9:16, 25 a 30 s, motion, sem pessoas em cena, trilha calma. Tipografia Raleway; frase de fechamento centralizada e curta, como no post de referência (mas sem prometer sucesso nem usar a igualdade "bem-estar = sucesso").', '', '', ''),
  ],
  legenda='''Janeiro está aí. Começar o cuidado na empresa tem três passos. Comente CUIDADO e enviamos como funciona.

Primeiro, uma conversa com o time. Depois, uma proposta personalizada, sob medida para a realidade da empresa. Em seguida, a implementação, com onboarding e os primeiros atendimentos do Escritório do Cuidado.

O programa dura quatro meses: diagnóstico integrado da população no primeiro mês, Escritório do Cuidado do primeiro ao quarto mês, com Medicina do Estilo de Vida, bioimpedância e smartwatch, e mensuração dos indicadores no quarto mês.

#fairhealth #saudecorporativa #escritoriodocuidado #medicinadoestilodevida #gestaodepessoas''',
  palavras='proposta personalizada,Escritório do Cuidado,programa dura quatro meses'),

 dict(id='D11', data=D(24), semana=4, bloco='10 · Começar', eixo='Institucional', fmt=FOTO,
  titulo='Boas festas do time fairhealth',
  sub='Uma pausa de fim de ano para quem cuida de gente',
  inspiracao='Post "Your health impacts how you feel" (rosto de perfil olhando para o céu, frase curta no alto) e a simplicidade do "Corporate wellness".',
  cta='Sem chamada (post de agradecimento)',
  fonte='Sem número.',
  validar='Foto de banco com licença comercial (pessoa de perfil olhando para cima, céu limpo, sem rosto identificável de colaborador atendido). Sem promoção.',
  roteiro=[
   ('Imagem única 4:5', 'Boas festas.\nQue a pausa de fim de ano chegue para todo mundo que cuida de gente.\nTime fairhealth', '', '', 'Sem preço, sem promoção.'),
   (VIS, 'Foto de perfil olhando para o céu (como no post de referência), com o céu em tons claros ou do entardecer; evitar o azul escuro do post, usar céu claro ou neutro. Texto curto no alto em Raleway, assinatura pequena em verde-azulado escuro. Logo fairhealth no canto.', '', '', ''),
  ],
  legenda='''Boas festas do time fairhealth. Que a pausa de fim de ano chegue para todo mundo que cuida de gente.

Obrigado a cada RH, líder e profissional de saúde que cuidou de pessoas em 2026. Voltamos em janeiro com o mesmo cuidado.

#fairhealth #boasfestas #saudecorporativa #gestaodepessoas #cuidado''',
  palavras='boas festas,fim de ano,cuida de gente'),

 dict(id='D12', data=D(28), semana=5, bloco='11 · Virada do ano', eixo='Institucional', fmt=REEL,
  titulo='O que é importante para você? O time responde',
  sub='A pergunta que abre cada atendimento, respondida por quem cuida',
  inspiracao='Série "Quem cuida" (voice.md): cada pessoa responde "O que é importante para você?", sem foco em cargo. Tom humano dos posts de rosto das referências.',
  cta='Responda nos comentários: o que é importante para você?',
  fonte='Sem número. Respostas gravadas com o time.',
  validar='Quem do time grava e quando (a apresentação do time foi adiada em 09/10: confirmar se já pode). Autorização de uso de imagem. Cada resposta sem foco em cargo.',
  roteiro=[
   ('0 a 3 s', 'O que é importante para você?', 'Em todo atendimento do Escritório do Cuidado, a primeira pergunta é a mesma: o que é importante para você?', 'Plano fechado, pessoa do time para a câmera.', 'Gancho.'),
   ('3 a 25 s', 'Quatro respostas, uma por pessoa.', '{{respostas do time}}', 'Cortes rápidos entre quatro pessoas, cada uma com a resposta na tela. Sem cargo, só o primeiro nome.', 'Gravar com quem estiver à vontade.'),
   ('25 a 33 s', 'E para você?', 'Neste fim de ano, a gente quer saber: o que é importante para você?', 'Tela com a pergunta em Raleway e a palavra "você" em Instrument Serif itálico.', ''),
   ('33 a 36 s', 'Responda nos comentários.', '', 'Logo no fim.', 'Chamada única.'),
   (VIS, 'Reel 9:16, 30 a 36 s, para a câmera, legendas sempre. Luz natural, fundo neutro do escritório; sem uniforme de cargo em destaque. Tipografia Raleway, o Tiffany nos destaques.', '', '', ''),
  ],
  legenda='''O que é importante para você? Responda nos comentários.

É a primeira pergunta de todo atendimento do Escritório do Cuidado, antes de qualquer conduta. Neste fim de ano, quem cuida respondeu também.

Escutar vem antes de tratar. Por isso a conversa começa pelo que pesa e pelo que importa para cada pessoa, e o plano é construído com ela, com base na Medicina do Estilo de Vida.

#fairhealth #saudecorporativa #escritoriodocuidado #cuidadocentradonapessoa #medicinadoestilodevida''',
  palavras='o que é importante para você,Escritório do Cuidado,Medicina do Estilo de Vida'),

 dict(id='D13', data=D(30), semana=5, bloco='11 · Virada do ano', eixo='Mercado + Produto', fmt=CARR,
  titulo='5 perguntas para o RH levar ao planejamento de 2027',
  sub='Adesão, dados, prevenção, NR-01 e medição: o que perguntar antes de fechar o programa de saúde',
  inspiracao='Post "Corporate wellness = corporate success" (declaração curta e centralizada) no fechamento, e os números oficiais em destaque, sem a igualdade do post.',
  cta='Comente CUIDADO (como funciona o Escritório do Cuidado)',
  fonte='Números oficiais (referencias.md): menos 28% de absenteísmo (Harvard Business Review, 2022) e menos 22% de custos com saúde (SHRM, 2023). NR-01: gov.br/MTE (mesma conferência do 18/11). Programa de 4 meses (Nina, 13/11).',
  validar='Redação sobre a NR-01 e o PGR conferida no texto do MTE. Revisão do Dr. Ronald.',
  roteiro=[
   ('Slide 1 · capa', '5 perguntas para o RH levar ao planejamento de 2027.\nAntes de fechar o programa de saúde.', '', '', ''),
   ('Slide 2 · Adesão', 'Adesão\nQuantas pessoas usam o programa de saúde hoje? Programa que ninguém usa não chega a quem precisa.', '', '', ''),
   ('Slide 3 · Dados', 'Dados\nO que a empresa sabe sobre a saúde do grupo, sem expor ninguém? Indicadores anonimizados dizem onde agir.', '', '', ''),
   ('Slide 4 · Prevenção', 'Prevenção\nQuem cuida antes do afastamento? Cuidado perto do trabalho, com médico, psicólogo e assistente social, tira a barreira do tempo e do acesso.', '', '', ''),
   ('Slide 5 · NR-01', 'NR-01\nOs riscos psicossociais estão no radar da gestão? A norma pede que sejam gerenciados.', '', '', 'Conferir a redação no texto do MTE.'),
   ('Slide 6 · Medição + convite', 'Medição\nComo saber, no fim, se mudou alguma coisa? No programa de 4 meses, a mensuração acontece no 4º mês.\nOs estudos mostram o que vem quando a empresa cuida antes: menos 28% de absenteísmo (HBR, 2022) e menos 22% de custos com saúde (SHRM, 2023).\nQuer ver como funciona na sua empresa? Comente CUIDADO.', '', '', 'Chamada única. Fonte completa no rodapé.'),
   (VIS, 'Fundo creme/papel, um bloco de texto por slide, a palavra-chave de cada pergunta em Raleway 800 verde-azulado escuro. Slide 6 em Tiffany claro, com os dois números grandes, e a frase de fechamento centralizada e curta, como no post de referência. Sem numeração dos slides e sem slide-resumo.', '', '', ''),
  ],
  legenda='''5 perguntas para o RH levar ao planejamento de 2027, antes de fechar o programa de saúde.

Adesão: quantas pessoas usam o programa de saúde hoje? Dados: o que a empresa sabe sobre a saúde do grupo, sem expor ninguém? Prevenção: quem cuida antes do afastamento? NR-01: os riscos psicossociais estão no radar da gestão? Medição: como saber, no fim, se algo mudou?

Os estudos mostram o que vem quando a empresa cuida antes: menos 28% de absenteísmo (Harvard Business Review, 2022) e menos 22% de custos com saúde (SHRM, 2023).

No programa de quatro meses do Escritório do Cuidado, o diagnóstico vem no primeiro mês e a mensuração dos indicadores, no quarto.

Quer ver como funciona na sua empresa? Comente CUIDADO.

#fairhealth #saudecorporativa #gestaodepessoas #planejamento2027 #medicinadoestilodevida''',
  palavras='planejamento de 2027,programa de saúde,absenteísmo'),
]

PENDENCIAS = [
 ('D01', 'Achar e conferir a pesquisa dos motivos de pedido de demissão (percentuais, ano, amostra). Sem ela, o slide 3 não sai.', 'Comunicação', 'Aberta'),
 ('D02, D11', 'Fotos de banco com licença comercial (aérea de duas pessoas em poltronas; perfil olhando para o céu).', 'Nina', 'Aberta'),
 ('D03, D05', 'Quais dados o smartwatch e a bioimpedância registram. Foto da capa do sono, com dados de exemplo marcados.', 'Dr. Ronald e fairdata', 'Aberta'),
 ('D04', 'Revisão do roteiro do sono pelo Dr. Ronald, data de gravação e, se ele aparecer, nome e CRM na tela (CFM).', 'Dr. Ronald e Comunicação', 'Aberta'),
 ('D06', 'Conferir o texto da OMS (CID-11) sobre burnout e a redação sobre a NR-01. Revisão médica ou da psicóloga.', 'Comunicação e Dr. Ronald', 'Aberta'),
 ('D07', 'Percentuais e fonte dos fatores da felicidade (candidata: Mapa da Felicidade Real, já usado em 25/11).', 'Comunicação', 'Aberta'),
 ('D08', 'Achar a pesquisa dos dois números da lacuna (querem x percebem). Liberação dos dados de cliente (decisão de 30/10).', 'Comunicação e Sócios', 'Aberta'),
 ('D09', 'O que o relatório do RH mostra de fato (fairdata). Não mostrar indicador que ainda não existe.', 'Nina e fairdata', 'Aberta'),
 ('D10', 'Resposta automática da palavra CUIDADO funcionando até 23/12.', 'Comunicação', 'Aberta'),
 ('D12', 'Quem do time grava, quando, e autorização de imagem. Confirmar se a apresentação do time já pode.', 'Nina', 'Aberta'),
 ('D13', 'Redação da NR-01 e do PGR conferida no texto do MTE. Revisão do Dr. Ronald.', 'Comunicação e Dr. Ronald', 'Aberta'),
]

DATAS = [
 (D(1), 'Dezembro começa; 30/11 (reel "Dezembro chegou") abre a passagem'),
 (D(24), 'Véspera de Natal: post leve de agradecimento, sem promoção'),
 (D(25), 'Natal (feriado, sem post)'),
 (D(31), 'Réveillon (sem post, a menos que a Nina queira um agradecimento extra)'),
]
