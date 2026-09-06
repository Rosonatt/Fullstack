const http = require("node:http");
const { chamadosRoutes } = require("./routes/chamadosRoutes");
const { responderJson } = require("./utils/http");

function createApp() {
  return http.createServer(async (req, res) => {
    configurarCors(res);

    if (req.method === "OPTIONS") {
      res.writeHead(204);
      res.end();
      return;
    }

    try {
      const rotaEncontrada = await chamadosRoutes(req, res);

      if (!rotaEncontrada) {
        responderJson(res, 404, {
          erro: "RECURSO_NAO_ENCONTRADO",
          mensagem: "Rota nao encontrada."
        });
      }
    } catch (error) {
      responderJson(res, 500, {
        erro: "ERRO_INTERNO",
        mensagem: "Nao foi possivel processar a requisicao."
      });
    }
  });
}

function configurarCors(res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET,POST,OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, Accept");
}

module.exports = {
  createApp
};
