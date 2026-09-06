function lerJson(req) {
  return new Promise((resolve, reject) => {
    let corpo = "";

    req.on("data", (chunk) => {
      corpo += chunk;
    });

    req.on("end", () => {
      if (!corpo.trim()) {
        resolve({});
        return;
      }

      try {
        resolve(JSON.parse(corpo));
      } catch (_error) {
        reject(criarErroValidacao({
          corpo: "Envie um JSON valido."
        }));
      }
    });

    req.on("error", reject);
  });
}

function responderJson(res, statusCode, corpo) {
  const conteudo = JSON.stringify(corpo);

  res.writeHead(statusCode, {
    "Content-Type": "application/json; charset=utf-8"
  });
  res.end(conteudo);
}

function criarErroValidacao(campos) {
  const error = new Error("Dados invalidos");
  error.codigo = "DADOS_INVALIDOS";
  error.campos = campos;
  return error;
}

module.exports = {
  lerJson,
  responderJson
};
