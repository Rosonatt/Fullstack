const chamadosController = require("../controllers/chamadosController");

async function chamadosRoutes(req, res) {
  const url = new URL(req.url, `http://${req.headers.host || "localhost"}`);

  if (url.pathname === "/chamados" && req.method === "GET") {
    chamadosController.listarChamados(req, res);
    return true;
  }

  if (url.pathname === "/chamados" && req.method === "POST") {
    await chamadosController.cadastrarChamado(req, res);
    return true;
  }

  return false;
}

module.exports = {
  chamadosRoutes
};
