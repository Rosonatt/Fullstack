const assert = require("node:assert/strict");
const test = require("node:test");
const { createApp } = require("../src/app");
const chamadosService = require("../src/services/chamadosService");

async function iniciarApi(t) {
  const server = createApp();

  await new Promise((resolve) => {
    server.listen(0, "127.0.0.1", resolve);
  });

  t.after(() => server.close());

  const { port } = server.address();
  return `http://127.0.0.1:${port}`;
}

async function enviarJson(url, dados) {
  return fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(dados)
  });
}

test("GET /chamados retorna 200 e uma lista vazia", async (t) => {
  chamadosService.limparChamadosParaTeste();
  const baseUrl = await iniciarApi(t);

  const response = await fetch(`${baseUrl}/chamados`);
  const body = await response.json();

  assert.equal(response.status, 200);
  assert.deepEqual(body, []);
});

test("POST /chamados cadastra um chamado valido e ele aparece na consulta", async (t) => {
  chamadosService.limparChamadosParaTeste();
  const baseUrl = await iniciarApi(t);

  const response = await enviarJson(`${baseUrl}/chamados`, {
    titulo: "Nao consigo acessar o sistema",
    descricao: "A tela informa que minhas credenciais sao invalidas.",
    prioridade: "alta"
  });
  const criado = await response.json();

  assert.equal(response.status, 201);
  assert.equal(criado.id, 1);
  assert.equal(criado.status, "aberto");
  assert.equal(criado.prioridade, "alta");

  const consulta = await fetch(`${baseUrl}/chamados`);
  const chamados = await consulta.json();

  assert.equal(consulta.status, 200);
  assert.deepEqual(chamados, [criado]);
});

test("POST /chamados valida titulo obrigatorio", async (t) => {
  chamadosService.limparChamadosParaTeste();
  const baseUrl = await iniciarApi(t);

  const response = await enviarJson(`${baseUrl}/chamados`, {
    descricao: "Preciso de ajuda com uma informacao da escola.",
    prioridade: "baixa"
  });
  const body = await response.json();

  assert.equal(response.status, 400);
  assert.equal(body.erro, "DADOS_INVALIDOS");
  assert.equal(body.campos.titulo, "O titulo e obrigatorio.");
});

test("POST /chamados valida descricao obrigatoria", async (t) => {
  chamadosService.limparChamadosParaTeste();
  const baseUrl = await iniciarApi(t);

  const response = await enviarJson(`${baseUrl}/chamados`, {
    titulo: "Duvida sobre frequencia",
    prioridade: "baixa"
  });
  const body = await response.json();

  assert.equal(response.status, 400);
  assert.equal(body.erro, "DADOS_INVALIDOS");
  assert.equal(body.campos.descricao, "A descricao e obrigatoria.");
});

test("POST /chamados rejeita prioridade invalida", async (t) => {
  chamadosService.limparChamadosParaTeste();
  const baseUrl = await iniciarApi(t);

  const response = await enviarJson(`${baseUrl}/chamados`, {
    titulo: "Problema no acesso",
    descricao: "Nao consigo entrar no portal.",
    prioridade: "urgente"
  });
  const body = await response.json();

  assert.equal(response.status, 400);
  assert.equal(body.erro, "DADOS_INVALIDOS");
  assert.equal(body.campos.prioridade, "Use baixa, media ou alta.");
});
