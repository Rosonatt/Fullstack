const { createApp } = require("./app");

const port = process.env.PORT || 3000;

createApp().listen(port, () => {
  console.log(`API do AlunoSaqua rodando em http://localhost:${port}`);
});
