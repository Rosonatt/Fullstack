const chamadosService = require("../services/chamadosService");
const { lerJson, responderJson } = require("../utils/http");

function listarChamados(_req, res) {
  const chamados = chamadosService.listarChamados();
  responderJson(res, 200, chamados);
}

async function cadastrarChamado(req, res) {
  try {
    const dados = await lerJson(req);
    const chamado = chamadosService.cadastrarChamado(dados);

    responderJson(res, 201, chamado);
  } catch (error) {
    if (error.codigo === "DADOS_INVALIDOS") {
      responderJson(res, 400, {
        erro: "DADOS_INVALIDOS",
        mensagem: "Nao foi possivel cadastrar o chamado.",
        campos: error.campos
      });
      return;
    }

    throw error;
  }
}

module.exports = {
  listarChamados,
  cadastrarChamado
};
