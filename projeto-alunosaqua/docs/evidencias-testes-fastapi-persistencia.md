# Evidências das Atividades 4 e 5

## Objetivo

Registrar a execução da API FastAPI do AlunoSaqua e a integração com persistência em SQLite, conforme os enunciados das novas atividades.

## Atividade 4 — Primeira API com FastAPI

Foi criada uma API executável em `backend/main.py`, com documentação interativa em `/docs` quando iniciada com Uvicorn.

Endpoints implementados:

- `GET /`: confirma que a API está ativa.
- `GET /chamados`: lista chamados cadastrados.
- `POST /chamados`: cria chamado com validação por Pydantic e regra de negócio no serviço.
- `GET /chamados/{id}`: consulta um chamado pelo identificador.
- `GET /chamados/status/{status_chamado}`: desafio adicional para filtrar por status.

## Atividade 5 — Persistência de chamados

Foi adicionada persistência local com SQLite. O script versionado está em:

```text
backend/banco/001_criar_tabela_chamados.sql
```

Modelo simplificado:

```text
Chamado
- id: identificador único gerado pelo banco
- titulo: texto obrigatório
- descricao: texto obrigatório
- prioridade: baixa | media | alta
- status: aberto | em_andamento | fechado
- criado_em: data e hora gerada pelo banco
```

Variável de ambiente documentada:

```text
DATABASE_URL=sqlite:///caminho/do/banco.db
```

Se a variável não for informada, a API usa o banco local:

```text
backend/database/alunosaqua.db
```

## Comando executado

Na pasta `backend`:

```bash
.venv\Scripts\python.exe -m pytest
```

## Resultado obtido

```text
collected 7 items

tests\test_chamados_fastapi.py ....... [100%]

7 passed
0 failed
```

## Casos verificados

| Caso | Resultado esperado |
|---|---|
| `GET /` | `200 OK` com mensagem de funcionamento |
| `GET /chamados` sem registros | `200 OK` com lista vazia |
| `POST /chamados` válido | `201 Created` com o chamado criado |
| Consulta após criação | chamado continua disponível no banco |
| `GET /chamados/{id}` válido | `200 OK` com o registro correto |
| `GET /chamados/status/aberto` | `200 OK` com chamados filtrados |
| `POST /chamados` sem título | `400 Bad Request` |
| `POST /chamados` com prioridade inválida | `400 Bad Request` |
| `GET /chamados/999` | `404 Not Found` |

## Decisão técnica

O grupo adotou SQLite para a persistência local porque não exige serviço externo, permite script SQL versionado e atende ao pedido da atividade sem expor credenciais. As consultas usam parâmetros (`?`) na camada de repositório, evitando concatenação direta de dados recebidos na requisição.
