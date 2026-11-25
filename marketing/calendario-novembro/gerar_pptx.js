// Uso: NODE_PATH=<pasta com pptxgenjs, react, react-dom, react-icons e sharp> node gerar_pptx.js
// Depois: soffice --headless --convert-to pdf Programacao_Instagram_LinkedIn_Novembro_2026.pptx
const path = require("path");
const { build } = require("../ferramentas/programacao_pdf.js");
build(Object.assign({ out: path.join(__dirname, "Programacao_Instagram_LinkedIn_Novembro_2026.pptx") }, require("./config.js")));
