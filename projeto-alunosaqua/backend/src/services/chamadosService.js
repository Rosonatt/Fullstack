const prioridadesPermitidas = new Set(["baixa", "media", "alta"]);

let chamados = [];
let proximoId = 1;

function listarChamados() {
  return chamados;
}

function cadastrarChamado(dados = {}) {
  const titulo = normalizarTexto(dados.titulo);
  const descricao = normalizarTexto(dados.descricao);
  const prioridade = normalizarTexto(dados.prioridade).toLowerCase();
  const campos = {};

  if (!titulo) {
    campos.titulo = "O titulo e obrigatorio.";
  }

  if (!descricao) {
    campos.descricao = "A descricao e obrigatoria.";
  }

  if (!prioridade) {
    campos.prioridade = "A prioridade e obrigatoria.";
  } else if (!prioridadesPermitidas.has(prioridade)) {
    campos.prioridade = "Use baixa, media ou alta.";
  }

  if (Object.keys(campos).length > 0) {
    throw criarErroValidacao(campos);
  }

  const chamado = {
    id: proximoId,
    titulo,
    descricao,
    prioridade,
    status: "aberto"
  };

  proximoId += 1;
  chamados.push(chamado);

  return chamado;
}

function normalizarTexto(valor) {
  return typeof valor === "string" ? valor.trim() : "";
}

function criarErroValidacao(campos) {
  const error = new Error("Dados invalidos");
  error.codigo = "DADOS_INVALIDOS";
  error.campos = campos;
  return error;
}

function limparChamadosParaTeste() {
  chamados = [];
  proximoId = 1;
}

module.exports = {
  listarChamados,
  cadastrarChamado,
  limparChamadosParaTeste
};
