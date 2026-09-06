# Evidências dos testes da API de chamados

## Objetivo

Registrar uma evidência reproduzível da Atividade 3, cobrindo os endpoints `GET /chamados` e `POST /chamados`, além das validações obrigatórias.

## Como executar

Na pasta do backend:

```bash
cd C:\Users\Rosonatt\Documents\GitHub\Fullstack\projeto-alunosaqua\backend
npm test
```

## Resultado obtido

```text
✔ GET /chamados retorna 200 e uma lista vazia
✔ POST /chamados cadastra um chamado valido e ele aparece na consulta
✔ POST /chamados valida titulo obrigatorio
✔ POST /chamados valida descricao obrigatoria
✔ POST /chamados rejeita prioridade invalida
ℹ tests 5
ℹ pass 5
ℹ fail 0
```

## Casos verificados

| Caso | Resultado esperado |
|---|---|
| `GET /chamados` sem registros | `200 OK` com lista vazia |
| `POST /chamados` com dados válidos | `201 Created` com o chamado criado |
| `POST /chamados` sem título | `400 Bad Request` |
| `POST /chamados` sem descrição | `400 Bad Request` |
| `POST /chamados` com prioridade inválida | `400 Bad Request` |

## Teste manual

Também há um arquivo com requisições reproduzíveis em [`backend/requests/chamados.http`](../backend/requests/chamados.http). Ele pode ser executado por extensões de cliente HTTP no editor ou usado como referência para montar as chamadas em outra ferramenta.
