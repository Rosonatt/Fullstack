# Evidencias da Aula 05 FastAPI em memoria

## Objetivo

Registrar a entrega da atividade de FastAPI com dados em memoria, adaptada para o tema AlunoSaqua.

PDF trabalhado:

```text
Aula_05_FastAPI_04_Atividade_Hands_On.pdf
```

## Local da atividade

```text
backend/atividade_4_fastapi_memoria
```

## Endpoints implementados

- `GET /`
- `GET /chamados`
- `POST /chamados`
- `GET /chamados/{chamado_id}`
- `GET /chamados/status/{status_chamado}`

## Como executar

Na pasta da atividade:

```bash
cd C:\Users\xxxx\xxxx\xxxx\Fullstack\projeto-alunosaqua\backend\atividade_4_fastapi_memoria
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

A API abre em:

```text
http://localhost:8000
```

A documentacao interativa abre em:

```text
http://localhost:8000/docs
```

## Casos testados

| Caso | Resultado esperado |
|---|---|
| `GET /` | API responde com mensagem de funcionamento |
| `GET /chamados` | Retorna lista vazia no inicio |
| `POST /chamados` | Cria chamado e retorna `201` |
| `GET /chamados` depois do cadastro | Mostra o chamado criado |
| `GET /chamados/1` | Retorna o chamado pelo id |
| `GET /chamados/999` | Retorna `404` |
| `POST /chamados` sem titulo | Retorna erro de validacao do Pydantic |
| `GET /chamados/status/aberto` | Filtra chamados pelo status |

## Observacao

Essa pasta mantem a versao em memoria pedida na Aula 05. A API principal do projeto, em `backend/main.py`, continua com SQLite porque representa a evolucao da atividade de persistencia feita no PDF seguinte.
