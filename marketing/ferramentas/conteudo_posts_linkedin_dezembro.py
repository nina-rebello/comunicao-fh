# Cronograma do LinkedIn da fairhealth: 1 post por semana, toda quarta (pedido da Nina, 24/11), de 25/11 a 30/12.
# Substitui o calendário de quintas do linkedin/README.md. Usado por gerar_cronograma_simples.py (modelo padrão):
#   python3 marketing/ferramentas/gerar_cronograma_simples.py marketing/Cronograma_Posts_LinkedIn_25-11_a_30-12.xlsx marketing/ferramentas/conteudo_posts_linkedin_dezembro.py
# Regras do LinkedIn (linkedin/README.md): a primeira frase se sustenta sozinha antes do "ver mais", link só no primeiro comentário,
# uma chamada por post (pergunta aberta ou convite), 3 hashtags no fim, sem emoji, sem travessão, "colaborador", "fairhealth" em minúsculas.
# Regras da marca (CLAUDE.md): sem diagnóstico gratuito, programa de 4 meses, MEV dentro do Escritório do Cuidado, bioimpedância e
# smartwatch ao falar de atendimento ou medição, número só com fonte, sem promessa clínica, sem preço, comunicação B2B.
import datetime as dt

D = lambda m, d: dt.date(2026, m, d)
TXT = 'Texto'
PRIM, DESE, CHAM, COM, TIME, FONTE = ('Primeira linha (antes do "ver mais")', 'Desenvolvimento', 'Chamada (pergunta final)',
                                       'Primeiro comentário (da página, logo depois de publicar)', 'Para o time compartilhar', 'Fontes')
H3 = '#fairhealth #saudecorporativa #gestaodepessoas'

POSTS = [
 dict(id='L05', data=D(12, 16), semana=4, bloco='Compreensão', fmt=TXT, eixo='Produto',
  titulo='Entre a medicina do trabalho e o plano de saúde',
  sub='O espaço do dia a dia que nenhum dos dois foi feito para ocupar',
  validar='Dr. Ronald valida o trecho sobre o papel da medicina do trabalho (pendência do post de 26/11 do plano antigo). Quem publica: página da fairhealth ou perfil da FairJob (decidir).',
  roteiro=[
   (PRIM, 'Toda empresa tem medicina do trabalho e plano de saúde. Mesmo assim, falta alguém no meio.', '', '', ''),
   (DESE, 'A medicina do trabalho olha o risco da empresa; o plano de saúde olha o tratamento. Entre os dois fica o dia a dia: o sono ruim, a ansiedade que ainda não virou crise, o hábito que escorrega. O Escritório do Cuidado ocupa esse espaço (médico, psicólogo, assistente social e felicitologista dentro da empresa, plano pela MEV, bioimpedância e smartwatch) e complementa os dois, sem substituir.', '', '', ''),
   (CHAM, 'Na sua empresa, quem cuida do colaborador antes de ele precisar do plano?', '', '', 'Uma chamada só.'),
   (COM, 'Sem link neste post.', '', '', ''),
   (TIME, '"Muitas vezes, a pessoa só precisa de alguém que escute e diga para onde ir. Esse é o espaço que a gente ocupa." (serviço social)', '', '', ''),
   (FONTE, 'Descrição do Escritório do Cuidado conforme o site da fairjob (referencias.md). Sem números.', '', '', ''),
  ],
  legenda='''Toda empresa tem medicina do trabalho e plano de saúde. Mesmo assim, falta alguém no meio.

A medicina do trabalho olha para o risco da empresa: exames, ambiente, segurança, o que a lei exige.

O plano de saúde olha para o tratamento: entra quando a pessoa já está doente e procura atendimento.

Entre os dois fica quase tudo o que acontece no dia a dia. O colaborador que dorme mal há meses. A ansiedade que ainda não virou crise. O hábito que começou a escorregar. A pessoa que só precisava de alguém para ouvir e saber para onde ir.

É nesse espaço que o Escritório do Cuidado trabalha. Médico, psicólogo, assistente social e felicitologista dentro da empresa, com um plano individual de cuidado pela Medicina do Estilo de Vida e com bioimpedância e smartwatch para acompanhar a rotina entre uma consulta e outra.

Não substituímos a medicina do trabalho nem o plano de saúde. Complementamos os dois, no espaço que nenhum deles foi feito para ocupar.

Na sua empresa, quem cuida do colaborador antes de ele precisar do plano?

#fairhealth #saudecorporativa #gestaodepessoas'''),

 dict(id='L06', data=D(12, 2), semana=2, bloco='Atualidade', fmt=TXT, eixo='Notícias + Institucional',
  titulo='Seminário Mirix: a felicidade no trabalho pode ser medida',
  sub='O que Fernando Brancaccio e Dr. Ronald Maia Filho apresentaram em Belo Horizonte, com a matéria do BH Ao Vivo',
  validar='Ok de Fernando e Dr. Ronald para o texto. Autorização da Mirix para citar o seminário. Conferir as 9 dimensões da Felicidade Interna Bruta na fonte original. Sem os 73,9 pontos da Clínica Mirix (dado de terceiro) e sem a história de burnout do Fernando. Combina com o reel do podcast (Instagram, 30/11 e 16/12).',
  roteiro=[
   (PRIM, 'Felicidade no trabalho não é sorte nem clima de festa. Dá para medir e dá para agir.', '', '', ''),
   (DESE, 'No Seminário Internacional Mirix (Belo Horizonte, 5 de novembro), Fernando Brancaccio mostrou como a percepção das pessoas vira indicador e o indicador vira decisão, com um questionário anônimo inspirado na Felicidade Interna Bruta do Butão (9 dimensões). O Dr. Ronald Maia Filho mostrou o outro lado: o cuidado começa por entender o que importa para a pessoa. Para o RH, a conclusão prática é medir o que importa e cuidar com a pessoa no centro, com indicadores do grupo, anonimizados, no lugar de opinião.', '', '', ''),
   (CHAM, 'Na sua empresa, a felicidade do time é medida ou só presumida?', '', '', 'Uma chamada só.'),
   (COM, 'Matéria completa do BH Ao Vivo (21/11/2026): https://bhaovivo.com.br/saude/mirix/especialistas-apresentam-metodologia-que-mede-a-felicidade/', '', '', 'Sem UTM (link de terceiro).'),
   (TIME, 'Fernando: "Percepção vira indicador, indicador vira decisão. Foi isso que levei ao seminário." Dr. Ronald: "Às vezes uma conversa resolve."', '', '', 'Conferir as frases com eles antes.'),
   (FONTE, 'BH Ao Vivo, 21/11/2026, sobre o Seminário Internacional Mirix (05/11/2026). Falas e conceitos parafraseados da matéria.', '', '', ''),
  ],
  legenda='''Felicidade no trabalho não é sorte nem clima de festa. Dá para medir e dá para agir.

No Seminário Internacional Mirix, em Belo Horizonte, no dia 5 de novembro, o Fernando Brancaccio e o Dr. Ronald Maia Filho apresentaram dois lados do mesmo caminho.

O Fernando mostrou como a percepção das pessoas pode virar indicador, e o indicador, decisão. A metodologia se inspira na Felicidade Interna Bruta do Butão, que olha o bem-estar além da renda, em nove dimensões, e inspirou um questionário anônimo para o ambiente corporativo. Ele não pergunta só se a pessoa está satisfeita com a empresa: procura saúde emocional, relações, condições financeiras, segurança e qualidade da gestão.

O Dr. Ronald mostrou o outro lado: o cuidado começa por entender o que importa para a pessoa, em vez de decidir sozinho o que é melhor para ela. É a pergunta que abre cada atendimento no Escritório do Cuidado, onde o plano é feito com a pessoa, pela Medicina do Estilo de Vida, com bioimpedância e smartwatch na rotina.

Para o RH, a conclusão prática é a mesma: medir o que importa e cuidar com a pessoa no centro. Indicadores do grupo, anonimizados, no lugar de opinião.

A matéria completa do BH Ao Vivo está no primeiro comentário.

Na sua empresa, a felicidade do time é medida ou só presumida?

#fairhealth #felicidadenotrabalho #gestaodepessoas'''),

 dict(id='L07', data=D(12, 9), semana=3, bloco='Compreensão', fmt=TXT, eixo='Produto',
  titulo='Como o cuidado entra na rotina sem atrapalhar o trabalho',
  sub='Escuta, atendimento, plano e acompanhamento, num programa de 4 meses',
  validar='Descrição conforme o site (jornada em 4 passos) e o programa de 4 meses (Nina, 13/11). Se o carrossel "Como funciona o cuidado na prática" (Instagram, 03/11) for refeito em quadrado, pode ir como documento em PDF.',
  roteiro=[
   (PRIM, 'Como o cuidado entra na rotina de uma empresa sem atrapalhar o trabalho?', '', '', ''),
   (DESE, 'Quatro passos: escuta (o que importa para você?), atendimento (médico, psicólogo, assistente social e felicitologista, dentro da empresa ou a distância), plano individual pela Medicina do Estilo de Vida e acompanhamento entre as consultas, com bioimpedância e smartwatch. No programa de 4 meses: diagnóstico do grupo no 1º mês, Escritório do Cuidado do 1º ao 4º e mensuração no 4º. O RH recebe só indicadores do grupo, anonimizados.', '', '', ''),
   (CHAM, 'O que mais dificulta o cuidado com a saúde no dia a dia da sua empresa?', '', '', 'Uma chamada só.'),
   (COM, 'Sem link neste post.', '', '', ''),
   (TIME, '"Quatro passos, e o mais importante é o primeiro: ouvir."', '', '', ''),
   (FONTE, 'Site da fairjob (página fairhealth) e referencias.md. Sem números.', '', '', ''),
  ],
  legenda='''Como o cuidado entra na rotina de uma empresa sem atrapalhar o trabalho?

No Escritório do Cuidado, funciona assim:

1. Escuta. O primeiro encontro é uma conversa. Rotina, trabalho, o que pesa. E a pergunta que guia tudo: o que importa para você?

2. Atendimento. Médico, psicólogo, assistente social e felicitologista, dentro da empresa ou a distância, em horários que conversam com o expediente.

3. Plano. Cada colaborador sai com um plano individual, feito para a vida dele, com base na Medicina do Estilo de Vida: sono, alimentação, movimento, estresse, relações.

4. Acompanhamento. O cuidado continua entre uma consulta e outra, com bioimpedância e smartwatch mostrando como foram as últimas semanas.

No programa de quatro meses, isso começa por um diagnóstico do grupo no primeiro mês e termina com a mensuração dos indicadores no quarto. O RH acompanha o que muda no grupo, com indicadores anonimizados. Nenhum dado individual sai do atendimento.

Para a empresa, o cuidado passa a acontecer no meio da rotina, e não apesar dela.

O que mais dificulta o cuidado com a saúde no dia a dia da sua empresa?

#fairhealth #saudecorporativa #RH'''),

 dict(id='L08', data=D(11, 25), semana=1, bloco='Confiança', fmt='Foto única', eixo='Cases',
  titulo='O primeiro resultado é adesão: como ler o relatório do Escritório do Cuidado',
  sub='A arte do relatório (post do Instagram de 27/11) com o texto para o CFO e o RH: indústria química atendida, janeiro a novembro de 2026',
  validar='Os sócios liberam os dados de cliente (decisão de 30/10); o nome Chemitec fica de fora ("uma indústria química atendida"), como no Instagram de 27/11. Mesma base do relatório conferido pela Nina em 23/11. Passou para 25/11 a pedido da Nina (24/11), trocando de data com o L05.',
  roteiro=[
   ('Imagem', 'A arte do relatório do Instagram de 27/11 (1080 × 1350): linkedin/posts/relatorio-case/relatorio-linkedin.png', '', '', 'A mesma do Instagram.'),
   (PRIM, 'Programa de bem-estar que ninguém usa é custo, não cuidado. Por isso, o primeiro número que o CFO e o RH deveriam olhar é a adesão.', '', '', ''),
   (DESE, 'Relatório de uma indústria química atendida (01/01 a 23/11/2026, indicadores baseados no modelo Quintuple Aim, IHI), número a número: 92,7% de adesão (51 de 55 ativos); 96,1% de retorno (49 de 51), "vir uma vez pode ser curiosidade, voltar é sinal de que o cuidado fez sentido"; 210 atendimentos, mais de 4 por pessoa; 94,3% presenciais; médico, psicólogo, felicitologista e assistente social, bioimpedância e 48 smartwatches. O RH recebe só indicadores do grupo.', '', '', ''),
   (CHAM, 'Na sua empresa, qual indicador mostra hoje se o programa de saúde está sendo usado?', '', '', 'Uma chamada só.'),
   (COM, 'Sem link neste post.', '', '', ''),
   (TIME, '"Voltar é o número de que mais me orgulho este ano."', '', '', ''),
   (FONTE, 'Relatório do Escritório do Cuidado de uma indústria química atendida, 01/01 a 23/11/2026 (indicadores baseados no modelo Quintuple Aim, IHI). Sempre agregado; sem gênero (veio vazio).', '', '', ''),
  ],
  legenda='''Programa de bem-estar que ninguém usa é custo, não cuidado. Por isso, o primeiro número que o CFO e o RH deveriam olhar é a adesão.

Este é o relatório do Escritório do Cuidado de uma indústria química que atendemos, de janeiro a novembro de 2026, com indicadores baseados no modelo Quintuple Aim, do Institute for Healthcare Improvement. E o que cada número diz para quem decide:

→ 92,7% de adesão: 51 de 55 colaboradores ativos foram atendidos. O cuidado chegou a quase todo o time.
→ 96,1% de retorno: 49 das 51 pessoas voltaram para dois ou mais atendimentos. Vir uma vez pode ser curiosidade. Voltar é sinal de que o cuidado fez sentido.
→ 210 atendimentos, mais de quatro por pessoa. Uso contínuo, mês a mês, e não um evento isolado.
→ 94,3% presenciais, dentro da empresa. Tempo e acesso deixam de ser barreira.
→ Médico, psicólogo, felicitologista e assistente social no mesmo lugar, com bioimpedância nas consultas e 48 smartwatches acompanhando a rotina.

Tudo isso chega ao RH como indicador do grupo, agregado e anonimizado. Nunca o que cada pessoa contou no atendimento.

Na sua empresa, qual indicador mostra hoje se o programa de saúde está sendo usado?

#fairhealth #saudecorporativa #gestaodepessoas'''),

 dict(id='L09', data=D(12, 23), semana=5, bloco='Confiança', fmt=TXT, eixo='Produto',
  titulo='Como levar o cuidado para a sua empresa em janeiro',
  sub='Conversa, proposta personalizada e implementação, para quem fecha o planejamento de 2027',
  validar='Página de contato do Escritório do Cuidado no ar até 23/12, com UTM do LinkedIn (sem diagnóstico gratuito). Véspera de Natal: alcance menor; se preferir, antecipar para terça, 22/12. Só o que está no site: conversa, proposta personalizada, implementação. Sem preço e sem prazo além do que está no site.',
  roteiro=[
   (PRIM, 'Começar a cuidar do seu time em janeiro é mais simples do que parece.', '', '', ''),
   (DESE, 'Três passos: uma conversa para entender o time e o que pesa hoje; uma proposta personalizada, sob medida; implementação, com onboarding e primeiros atendimentos. O programa dura 4 meses: diagnóstico do grupo no 1º mês, Escritório do Cuidado do 1º ao 4º e mensuração dos indicadores no 4º.', '', '', ''),
   (CHAM, 'Se a saúde do time está nos planos de 2027, o link para falar com a gente está no primeiro comentário.', '', '', 'Uma chamada só (convite).'),
   (COM, 'Para conversar com a gente sobre o Escritório do Cuidado na sua empresa: https://www.fairhealth.com.br/?utm_source=linkedin&utm_medium=organico&utm_campaign=post-09 [CONFIRMAR o endereço antes de publicar]', '', '', ''),
   (TIME, '"Se você é de RH e está fechando o planejamento do ano, esse é um bom momento para conversarmos."', '', '', ''),
   (FONTE, 'Executive Summary (conversa, proposta, implementação), site da fairjob e programa de 4 meses (Nina, 13/11).', '', '', ''),
  ],
  legenda='''Começar a cuidar do seu time em janeiro é mais simples do que parece.

Nas últimas semanas, contamos aqui o que é o Escritório do Cuidado, como ele entra na rotina de quem trabalha e o que os números de uma indústria atendida mostram. Para levar isso à sua empresa, são três passos:

1. Uma conversa. Para entender o seu time, a rotina da empresa e o que mais pesa hoje.

2. Proposta personalizada. Um programa sob medida para o seu time.

3. Implementação. Onboarding e primeiros atendimentos, com acompanhamento do RH desde o início.

O programa dura quatro meses: diagnóstico do grupo no primeiro mês, Escritório do Cuidado do primeiro ao quarto mês, com Medicina do Estilo de Vida, bioimpedância e smartwatch, e mensuração dos indicadores no quarto.

Se a saúde do seu time está nos planos de 2027, o link para falar com a gente está no primeiro comentário.

#fairhealth #saudecorporativa #RH'''),

 dict(id='L10', data=D(12, 30), semana=6, bloco='Atualidade', fmt=TXT, eixo='Notícias + Produto',
  titulo='O cansaço constante não é fraqueza',
  sub='Os 3 sinais de esgotamento que a OMS descreve e o que o líder pode fazer',
  validar='Conferir o texto da OMS (CID-11) e a redação sobre a NR-01 nos originais. Revisão do Dr. Ronald ou da psicóloga (sem rótulo de diagnóstico). Última quarta do ano: pode ser adiantado para 29/12 se a página tiver menos movimento no dia 30.',
  roteiro=[
   (PRIM, 'O cansaço constante não é fraqueza. É um sinal que o gestor precisa saber ler.', '', '', ''),
   (DESE, 'A OMS trata o burnout como fenômeno ligado ao trabalho: estresse crônico que não foi bem gerenciado, com três sinais (exaustão, distanciamento do trabalho e sensação de menor eficácia). Rotular não ajuda; perguntar o que está pesando ajuda. Sobrecarga, pouca autonomia e conflito estão entre os fatores de risco psicossocial que a NR-01 trata como de gestão. O Escritório do Cuidado escuta e acompanha, e o RH recebe só indicadores do grupo. CVV 188.', '', '', ''),
   (CHAM, 'Na sua empresa, o gestor sabe o que fazer quando percebe um desses sinais?', '', '', 'Uma chamada só.'),
   (COM, 'Sem link neste post.', '', '', ''),
   (TIME, '"Perguntar o que está pesando muda a conversa. Rotular, não."', '', '', ''),
   (FONTE, 'OMS, CID-11 (burnout como fenômeno ocupacional). NR-01: gov.br/MTE. Guia "Saúde mental: o cuidado no dia a dia" (OMS, APA, IPq-USP). CVV 188.', '', '', ''),
  ],
  legenda='''O cansaço constante não é fraqueza. É um sinal que o gestor precisa saber ler.

A OMS trata o burnout como um fenômeno ligado ao trabalho: estresse crônico que não foi bem gerenciado. Os três sinais que ela descreve são exaustão, distanciamento do trabalho e sensação de menor eficácia.

Para quem lidera, rotular alguém não ajuda. Perguntar o que está pesando ajuda. Sobrecarga, pouca autonomia e conflito estão entre os fatores de risco psicossocial que a NR-01 trata como de gestão, e a saúde mental no trabalho é parte disso.

No Escritório do Cuidado, psicólogo, médico e assistente social escutam e acompanham, com plano individual pela Medicina do Estilo de Vida. O RH recebe só indicadores do grupo, anonimizados.

Se alguém do seu time precisa de ajuda agora, o CVV atende 24 horas pelo 188.

Na sua empresa, o gestor sabe o que fazer quando percebe um desses sinais?

#fairhealth #saudementalnotrabalho #gestaodepessoas'''),
]
POSTS.sort(key=lambda p: p['data'])
