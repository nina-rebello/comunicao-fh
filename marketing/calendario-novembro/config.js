// Programação de novembro de 2026. Em 23/11 o 30/11 passou a ser o carrossel sobre pedido de demissão. O reel de 02/12 é o primeiro corte do podcast do Seminário Mirix.
// d, formato, bloco, tipo, eixo, título curto (calendário), título, descrição, chamada
const POSTS = [
  [3, "carrossel", 3, "P", "Produto", "Como funciona o cuidado na prática?", "Como funciona o cuidado na prática?",
    "A jornada entre escuta, atendimento, plano individualizado e acompanhamento", "Comente CUIDADO"],
  [4, "reel", 3, "P", "Produto", "Quatro frentes, um cuidado conectado", "Quatro frentes, um cuidado conectado",
    "Medicina do Estilo de Vida, Escritório do Cuidado, plataforma e wearables", "Comente CUIDADO"],
  [6, "carrossel", 4, "I", "Cases", "Uma história de cuidado desde 2009", "Uma história de cuidado que começou em 2009",
    "Linha do tempo da metodologia e evolução até a fairhealth (validar com o Dr. Ronald)", "a definir"],
  [9, "reel", 4, "P", "Cases", "Cuidado na prática: resultados reais", "Cuidado na prática: experiências e resultados reais",
    "Evidências e resultados documentados, contados pelo Dr. Ronald", "a definir"],
  [11, "carrossel", 4, "P", "Cultura", "Estilo de vida também é tratamento sério", "Estilo de vida também é tratamento sério",
    "O que a ciência mostra sobre mudar a rotina, na semana do Dia Mundial do Diabetes", "a definir"],
  [13, "carrossel", 4, "P", "Produto", "Como levar a fairhealth para sua empresa?", "Como levar a fairhealth para sua empresa?",
    "Encerramento da apresentação inicial com orientação para o RH", "Comente CUIDADO (comercial)"],
  [16, "reel", 5, "E", "Cultura", "Novembro Azul: ele só vai ao médico quando dói", "Ele só vai ao médico quando dói",
    "Novembro Azul: o homem não deixa de se cuidar por descuido, e sim porque cuidar dá trabalho. Com o cuidado dentro da empresa, a barreira cai o ano todo", "Comente CUIDADO"],
  [18, "carrossel", 5, "P", "Notícias", "Afastamentos por saúde mental e a NR-01", "Recorde de afastamentos por saúde mental: o que a NR-01 cobra do RH",
    "546,2 mil licenças em 2025 e a gestão de riscos psicossociais além da planilha", "Comente CUIDADO e receba o guia de NR-01"],
  [19, "foto", 5, "P", "Cases", "Depoimentos: três vozes do Escritório do Cuidado", "Depoimentos: três vozes do Escritório do Cuidado",
    "A voz de quem é cuidado: hábito e cultura, sem promessa de resultado clínico. Entra na quinta porque sexta é feriado", "Comente CUIDADO"],
  [23, "reel", 5, "P", "Notícias", "O RH cuida de todo mundo. Quem cuida do RH?", "O RH cuida de todo mundo. Quem cuida do RH?",
    "Dados do Panorama da Saúde Emocional do RH 2026 e o cuidado que chega também a quem cuida", "Mande para alguém do RH"],
  [25, "carrossel", 5, "P", "Cultura", "Por que a Geração Z está tão desconectada do trabalho?", "Por que a Geração Z está tão desconectada do trabalho?",
    "Não é preguiça nem falta de compromisso. A resposta começa com a pergunta que quase ninguém faz: o que importa para você?", "Comente CUIDADO"],
  [27, "foto", 6, "P", "Cases", "Case: o relatório do Escritório do Cuidado", "Como ler o relatório do Escritório do Cuidado",
    "Post único em forma de relatório: adesão de 92,7%, retorno de 96,1% e 210 atendimentos numa indústria, de janeiro a novembro, e como levar ao CFO e ao RH", "Comente CUIDADO"],
  [30, "carrossel", 7, "P", "Cultura", "Por que as pessoas pedem demissão?", "Por que as pessoas pedem demissão?",
    "O motivo que o RH só descobre na entrevista de desligamento e o que existe por trás dele", "Comente CUIDADO"],
];
const DATAS = { 1: "Início do Novembro Azul", 2: "Finados", 14: "Dia Mundial do Diabetes", 15: "Proclamação da República", 20: "Consciência Negra (feriado)" };
const SEMANAS = [
  { n: 1, ini: 2, fim: 6, rotulo: "03 a 06/11", desc: "Compreensão e começo da confiança. O cuidado na prática, as quatro frentes conectadas e a trajetória do método." },
  { n: 2, ini: 9, fim: 13, rotulo: "09 a 13/11", desc: "Confiança. Resultados reais, a ciência por trás do cuidado e o convite para o RH." },
  { n: 3, ini: 16, fim: 20, rotulo: "16 a 19/11", desc: "Atualidade. Novembro Azul, NR-01 e a voz de quem é cuidado: temas do momento que levam ao Escritório do Cuidado. Sexta, 20/11, é feriado." },
  { n: 4, ini: 23, fim: 27, rotulo: "23 a 27/11", desc: "Atualidade e decisão. Quem cuida do RH, a desconexão dos jovens e a prova da Chemitec." },
  { n: 5, ini: 30, fim: 30, rotulo: "30/11", desc: "Passagem para dezembro, com o RH fechando o orçamento de 2027. Na quarta, 02/12, o primeiro reel do podcast do Seminário Mirix (os reels de dezembro intercalam o podcast e a Dra. Marília)." },
];
module.exports = {
  mes: 10, nomeMes: "Novembro", periodo: "01/11 a 30/11", sub: "3 posts por semana",
  gradeInicio: new Date(2026, 10, 2), semanasNaGrade: 5,
  objetivo: "Fechar a apresentação da fairhealth e abrir a conversa com o RH. Primeiro, mostramos o cuidado na prática e as provas de que ele funciona. Depois, usamos temas do momento (Novembro Azul, NR-01, saúde do RH, Geração Z) para mostrar que entendemos o que as empresas estão vivendo e terminamos com o convite para conhecer o Escritório do Cuidado, enquanto o RH fecha o orçamento de 2027.",
  POSTS, DATAS, SEMANAS,
  painel: { titulo: "Para novembro funcionar", itens: [
    "Até 13/11: guia de NR-01 pronto e validado",
    "Até 13/11: resposta automática da palavra CUIDADO no ar",
    "Até 27/11: pesquisa dos motivos de demissão achada e conferida (carrossel de 30/11)",
    "Revisão técnica dos posts de Novembro Azul, NR-01 e saúde mental",
    "Conferir na fonte original os dados do INSS, da Flash e da pesquisa sobre homens e saúde",
  ] },
};
