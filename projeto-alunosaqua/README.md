# AlunoSaqua

## Integrantes

- Bruno Oliveira
- Natalia Cardoso
- Raissa Queiroz
- Rosonatt Ferreira
- Ryan Guiwison

## Sobre o projeto

O AlunoSaqua é uma ideia de sistema para ajudar a escola a organizar melhor sua rotina. A proposta é reunir em um só lugar informações e pedidos de alunos, responsáveis, professores e funcionários.

A escola costuma receber dúvidas e solicitações por vários lugares. Às vezes isso acaba dificultando o acompanhamento. Com o AlunoSaqua, a pessoa poderia registrar o que precisa e acompanhar o andamento até receber uma resposta.

O projeto também pode crescer com o tempo e receber outras áreas, como notas, frequência, comunicados, cadastro de usuários e comunicação com a equipe pedagógica.

> **Comentário do grupo:** escolhemos esse tema porque ele faz sentido para o dia a dia de uma escola e dá espaço para criar várias funções úteis sem deixar a ideia confusa.

## Objetivo

Criar uma aplicação web simples para organizar solicitações da comunidade escolar e facilitar o contato com a equipe responsável.

## Atualizações das atividades

### Atividade 1 — Planejamento e estruturação do projeto

Na primeira atividade, o grupo definiu a ideia do AlunoSaqua e o problema que o sistema pretende resolver: organizar o registro e o acompanhamento de solicitações da comunidade escolar.

Também foram realizados:

- definição do público do sistema: alunos, responsáveis, professores, funcionários, coordenação e direção;
- delimitação do escopo inicial do projeto;
- levantamento dos requisitos funcionais;
- identificação das principais informações que serão armazenadas;
- definição do fluxo principal de uma solicitação, desde o cadastro até o encerramento;
- planejamento da divisão do sistema em **frontend, backend, API e banco de dados**;
- registro das funcionalidades que poderão ser incluídas em versões futuras, como notas, frequência, notificações e relatórios.

A documentação dessa atividade está disponível em [`docs/planejamento-semana-1.md`](docs/planejamento-semana-1.md).

### Atividade 2 — Contrato da API de chamados

Na segunda atividade, o grupo definiu e documentou o contrato da API responsável pelo registro e acompanhamento das solicitações escolares.

Foram especificados:

- o formato das mensagens da API, utilizando JSON;
- os dados de uma solicitação: `id`, `titulo`, `descricao`, `prioridade` e `status`;
- as regras de preenchimento dos campos obrigatórios;
- as rotas para consultar, criar, alterar e remover solicitações;
- os métodos HTTP `GET`, `POST`, `PATCH` e `DELETE`;
- o filtro opcional por status;
- os códigos de resposta `200`, `201`, `204`, `400` e `404`;
- exemplos de requisições, respostas de sucesso e mensagens de erro;
- o status inicial `aberto` e os demais status possíveis: `em_atendimento`, `resolvido` e `cancelado`.

As principais rotas definidas foram:

- `GET /chamados` — consultar solicitações;
- `GET /chamados/{id}` — consultar uma solicitação específica;
- `POST /chamados` — criar uma solicitação;
- `PATCH /chamados/{id}` — alterar uma solicitação;
- `DELETE /chamados/{id}` — remover uma solicitação.

A documentação dessa atividade está disponível em [`docs/contrato-api-chamados.md`](docs/contrato-api-chamados.md).

### Atividade 3 — Primeira implementação da API

Na terceira atividade, o grupo iniciou a parte prática da API de chamados, mantendo os dados em memória e separando o código em rota, controlador e serviço.

Foram implementados:

- `GET /chamados` para consultar a lista de chamados cadastrados;
- `POST /chamados` para cadastrar um novo chamado;
- validação de `titulo`, `descricao` e `prioridade`;
- regra de prioridade permitida: `baixa`, `media` ou `alta`;
- resposta padronizada para dados inválidos;
- testes automatizados cobrindo cadastro válido e casos de erro.

O código dessa atividade está em [`backend/`](backend/) e as evidências de teste estão em [`docs/evidencias-testes-api-chamados.md`](docs/evidencias-testes-api-chamados.md).

### Atividade 4 — Primeira API com FastAPI

Na quarta atividade, o back-end foi adaptado para FastAPI, seguindo o enunciado da aula prática. A API agora possui `main.py`, pode ser iniciada com Uvicorn e expõe a documentação interativa em `/docs`.

Foram implementados:

- aplicação FastAPI em [`backend/main.py`](backend/main.py);
- `GET /` para confirmar que a API está ativa;
- `GET /chamados` para consultar chamados;
- `POST /chamados` para cadastrar chamados;
- `GET /chamados/{id}` para consultar um chamado específico;
- validação do corpo da requisição com Pydantic;
- desafio adicional `GET /chamados/status/{status_chamado}`.

> **Comentário do grupo:** a proposta da aula falava em chamados de suporte. Adaptamos para o AlunoSaqua, então os chamados representam solicitações da comunidade escolar.

### Atividade 5 — Persistência de chamados

Na quinta atividade, a API deixou de depender apenas de dados em memória e passou a usar persistência local com SQLite.

Foram implementados:

- script SQL versionado em [`backend/banco/001_criar_tabela_chamados.sql`](backend/banco/001_criar_tabela_chamados.sql);
- tabela `chamados` com `id`, `titulo`, `descricao`, `prioridade`, `status` e `criado_em`;
- conexão configurada sem credenciais expostas;
- variável opcional `DATABASE_URL` para trocar o caminho do banco;
- camada de repositório com consultas SQL parametrizadas;
- `POST /chamados`, `GET /chamados` e `GET /chamados/{id}` usando banco de dados;
- erro `400` para dados inválidos e erro `404` para id inexistente;
- testes automatizados comprovando criação, consulta, persistência, validação e erro.

As evidências estão em [`docs/evidencias-testes-fastapi-persistencia.md`](docs/evidencias-testes-fastapi-persistencia.md).

### Status das atividades

- [x] Atividade 1 — planejamento do AlunoSaqua.
- [x] Atividade 2 — contrato da API.
- [x] Atividade 3 — API inicial com dados em memória.
- [x] Atividade 4 — API FastAPI.
- [x] Atividade 5 — persistência com SQLite.

## O que a primeira versão faz

- registra uma solicitação feita por aluno, responsável ou funcionário;
- permite consultar as solicitações registradas;
- mostra o andamento de cada solicitação;
- permite que a equipe responsável atualize o status;
- permite encerrar uma solicitação resolvida;
- guarda título, descrição, prioridade e situação do atendimento.

## O que pode entrar depois

- notas e médias;
- controle de frequência;
- envio de arquivos e imagens;
- notificações;
- relatórios para a direção;
- comunicação com outras plataformas da escola;
- organização por unidade, turma ou setor.

## Organização

- `docs/planejamento-semana-1.md`: planejamento, problema, usuários, requisitos e fluxo principal.
- `docs/diagrama-arquitetura.md`: visão de como as partes do sistema se comunicam.
- `docs/contrato-api-chamados.md`: regras e exemplos das solicitações da aplicação.
- `docs/evidencias-testes-api-chamados.md`: registros reproduzíveis dos testes da API.
- `docs/evidencias-testes-fastapi-persistencia.md`: evidências das atividades 4 e 5.
- `frontend/`: parte visual do sistema.
- `backend/`: API de chamados.
- `backend/main.py`: aplicação FastAPI atual.
- `backend/app/`: rotas, modelos, serviços, repositórios e conexão com o banco.
- `backend/banco/`: scripts SQL versionados.
- `backend/requirements.txt`: dependências Python do backend.
- `backend/src/routes/`: rotas da aplicação.
- `backend/src/controllers/`: controladores que recebem as requisições.
- `backend/src/services/`: regras de negócio e dados em memória.
- `backend/tests/`: testes automatizados da API FastAPI.
- `backend/test/`: testes da implementação inicial em Node.
- `backend/requests/`: requisições HTTP para testar manualmente.
- `database/`: dados que serão armazenados.

## Como executar a API atual das Partes 4 e 5

Entre na pasta do backend:

```bash
cd C:\Users\Rosonatt\Documents\GitHub\Fullstack\projeto-alunosaqua\backend
```

Crie e ative o ambiente virtual, caso ainda não esteja criado:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Para rodar os testes:

```bash
python -m pytest
```

Para iniciar a API FastAPI:

```bash
uvicorn main:app --reload
```

A API fica disponível em `http://localhost:8000` e a documentação interativa fica em `http://localhost:8000/docs`. As requisições de exemplo estão em [`backend/requests/chamados.http`](backend/requests/chamados.http).

Por padrão, o SQLite grava os dados em `backend/database/alunosaqua.db`. Se for necessário usar outro arquivo, configure a variável:

```bash
set DATABASE_URL=sqlite:///caminho/do/banco.db
```

## Como pensamos o sistema

A pessoa acessa o AlunoSaqua pelo site, preenche uma solicitação e envia. A aplicação confere os dados, registra a informação e mostra o status para quem fez o pedido. A equipe da escola consegue consultar as solicitações e atualizar o atendimento.

A parte visual conversa com a API, o back-end cuida das regras e o banco guarda os dados.

## Projeto de referência

O AlunoSaqua foi pensado a partir do projeto disponível em [github.com/Rosonatt/PEI5](https://github.com/Rosonatt/PEI5), que apresenta diferentes áreas para a administração escolar, direção, professores, alunos, responsáveis e equipe pedagógica.

Nesta etapa, o grupo focou em uma parte menor para deixar a proposta mais clara e possível de desenvolver. As outras funções podem ser adicionadas aos poucos.

> **Comentário do grupo:** a ideia é começar com algo simples, mas que realmente ajude a escola. Depois, outras funções podem ser encaixadas sem precisar refazer tudo.
