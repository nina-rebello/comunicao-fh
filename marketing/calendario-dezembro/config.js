// Programação de dezembro de 2026. Reels sempre na quarta (desde 23/11), intercalando o podcast do Seminário Mirix e os vídeos da Dra. Marília (23/11).
// O corte 1 do podcast saiu em 30/11 (novembro); 02/12 é o reel "Dezembro chegou". Ordem e datas iguais a ferramentas/conteudo_posts_dezembro.py.
// d, formato, bloco, tipo, eixo, título curto (calendário), título, descrição, chamada
const POSTS = [
  [2, "reel", 7, "E", "Cultura", "Dezembro chegou: a corrida das metas também adoece", "Dezembro chegou: a corrida das metas também adoece",
    "Uma prática de 1 minuto para o fim de ano e o convite para cuidar antes de 2027", "Comente CUIDADO"],
  [4, "foto", 7, "P", "Produto", "Todo mundo precisa de alguém por perto", "Todo mundo precisa de alguém por perto",
    "Escuta, clareza e um plano possível, dentro da empresa", "Mande para quem cuida das pessoas"],
  [7, "carrossel", 8, "P", "Cultura", "Seu sono virou nota no relógio", "Seu sono virou nota no relógio. Por que o cansaço continua?",
    "O que o smartwatch mostra, o que ele não mostra e onde o cuidado começa", "Comente CUIDADO"],
  [9, "reel", 8, "P", "Cultura", "Marília: acordar toda hora", "Acordar toda hora: você dorme, mas não descansa",
    "Vídeo da Dra. Marília: por que oito horas na cama nem sempre são oito horas de descanso", "Mande para quem cuida do time"],
  [11, "carrossel", 8, "P", "Produto", "O número do dia não conta a história toda", "O número do dia não conta a história toda",
    "Bioimpedância e smartwatch: a tendência de semanas entra na consulta", "Mande para quem cuida do time"],
  [14, "carrossel", 9, "P", "Notícias", "3 sinais de esgotamento que a OMS descreve", "3 sinais de esgotamento no trabalho que a OMS descreve",
    "O cansaço constante não é fraqueza. O que o líder pode fazer e onde pedir ajuda", "Comente CUIDADO"],
  [16, "reel", 9, "I", "Notícias", "Podcast: o que o Butão ensina", "O que o Butão ensina sobre felicidade no trabalho",
    "Podcast, corte 2: o Fernando Brancaccio e a Felicidade Interna Bruta (trechos a escolher)", "Mande para quem cuida de gente"],
  [18, "carrossel", 9, "P", "Cultura", "O que influencia a felicidade dos colaboradores?", "O que influencia a felicidade dos seus colaboradores?",
    "Sono, relações, contas e propósito: o que pesa e quem cuida de cada parte", "Comente CUIDADO"],
  [21, "carrossel", 10, "P", "Produto", "O que o RH recebe do Escritório do Cuidado?", "O que o RH recebe do Escritório do Cuidado?",
    "Um relatório de indicadores do grupo, anonimizados, sem o nome de ninguém", "Comente CUIDADO"],
  [23, "reel", 10, "P", "Produto", "Marília: por onde o cuidado começa", "Janeiro está aí: por onde o cuidado começa na empresa",
    "Vídeo da Dra. Marília: conversa, proposta personalizada e implementação, num programa de 4 meses", "Comente CUIDADO"],
  [24, "foto", 10, "I", "Institucional", "Boas festas do time fairhealth", "Boas festas do time fairhealth",
    "Uma pausa de fim de ano para quem cuida de gente. Sem promoção", "nenhuma (post de agradecimento)"],
  [28, "carrossel", 11, "P", "Mercado", "5 perguntas para o RH levar ao planejamento de 2027", "5 perguntas para o RH levar ao planejamento de 2027",
    "Adesão, dados, prevenção, NR-01 e medição: o que perguntar antes de fechar o programa de saúde", "Comente CUIDADO"],
  [30, "reel", 11, "I", "Institucional", "Podcast: o cuidado começa pela escuta", "O cuidado começa pela escuta",
    "Podcast, corte 3: o Dr. Ronald Maia Filho e a pergunta \"o que importa para você?\" (trechos a escolher)", "Mande para quem cuida de gente"],
];
const DATAS = { 1: "Dezembro começa", 24: "Véspera de Natal", 25: "Natal (feriado)", 31: "Réveillon" };
const SEMANAS = [
  { n: 1, ini: 1, fim: 6, rotulo: "02 a 04/12", desc: "Causas. A segunda, 30/11, abre com o primeiro corte do podcast do Seminário Mirix; na quarta, a corrida das metas de dezembro; e todo mundo precisa de alguém por perto." },
  { n: 2, ini: 7, fim: 11, rotulo: "07 a 11/12", desc: "Sono e dados. A nota do relógio, o sono que não descansa (vídeo da Dra. Marília) e a tendência que a bioimpedância e o smartwatch mostram na consulta." },
  { n: 3, ini: 14, fim: 18, rotulo: "14 a 18/12", desc: "Esgotamento e felicidade. O que a OMS descreve, o que o Butão ensina sobre felicidade (podcast, corte 2) e o que pesa na vida de quem trabalha." },
  { n: 4, ini: 21, fim: 25, rotulo: "21 a 24/12", desc: "Começar. O que o RH recebe, como o programa de 4 meses começa (vídeo da Dra. Marília) e uma pausa de fim de ano. Sexta, 25/12, é feriado." },
  { n: 5, ini: 28, fim: 31, rotulo: "28 a 30/12", desc: "Virada do ano. O RH leva 5 perguntas para o planejamento de 2027 e o Dr. Ronald fecha o ano com a pergunta que abre cada atendimento (podcast, corte 3)." },
];
module.exports = {
  mes: 11, nomeMes: "Dezembro", periodo: "02/12 a 30/12", sub: "reels na quarta: podcast e Marília",
  gradeInicio: new Date(2026, 10, 30), semanasNaGrade: 5,
  objetivo: "Fechar o ano mostrando o cuidado por trás dos temas que o RH já tem na cabeça: a saída de pessoas, o sono, os dados, o esgotamento e a felicidade. Cada tema leva ao Escritório do Cuidado e ao que o RH recebe, indicadores do grupo e anonimizados. Terminamos com como o programa de 4 meses começa, enquanto o RH planeja 2027.",
  POSTS, DATAS, SEMANAS,
  painel: { titulo: "Para dezembro funcionar", itens: [
    "Até 27/11: pesquisa dos motivos de demissão achada e conferida (carrossel de 30/11)",
    "Até 27/11: autorização de BH Ao Vivo e da Mirix e ok de Fernando e Dr. Ronald para os cortes do podcast (o primeiro sai em 30/11)",
    "Até 01/12: prática de 1 minuto do reel de 02/12 validada",
    "Datas de gravação dos vídeos da Dra. Marília (09/12 e 23/12), com nome e CRM na tela",
    "Até 09/12: Dr. Ronald revisa o roteiro do sono e os dados do smartwatch e da bioimpedância",
    "Até 14/12: texto da OMS e da NR-01 conferidos nos originais",
    "Até 16/12: trechos dos cortes 2 e 3 do podcast escolhidos na transcrição",
    "Até 18/12: percentuais da felicidade com fonte",
    "Até 23/12: resposta automática da palavra CUIDADO no ar",
    "CRM do Dr. Ronald para a tela dos cortes do podcast",
  ] },
};
