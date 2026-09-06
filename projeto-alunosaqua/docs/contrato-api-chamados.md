# Contrato da API do AlunoSaqua

## Integrantes

- Bruno Oliveira
- Natalia Cardoso
- Raissa Queiroz
- Rosonatt Ferreira
- Ryan Guiwison

## 1. Para que serve

A API do AlunoSaqua será usada para registrar e acompanhar solicitações da escola. Ela ajuda a interface e o back-end a seguirem o mesmo formato de dados.

Uma solicitação pode ser uma dúvida, um pedido de informação ou um problema que precisa ser visto pela equipe da escola.

As mensagens usam JSON e as rotas são `/chamados` e `/chamados/{id}`, como definido na atividade.

Na Atividade 3, a primeira versão executável da API cobriu `GET /chamados` e `POST /chamados` com dados em memória. Nas Atividades 4 e 5, a API foi adaptada para FastAPI e passou a usar persistência local com SQLite.

## 2. Dados de uma solicitação

| Campo | Tipo | Obrigatório ao criar? | O que significa |
|---|---|---:|---|
| `id` | número inteiro | Não | Número gerado pelo sistema. |
| `titulo` | texto | Sim | Resumo do que a pessoa precisa. |
| `descricao` | texto | Sim | Explicação da solicitação. |
| `prioridade` | texto | Sim | `baixa`, `media` ou `alta`. |
| `status` | texto | Não | `aberto`, `em_andamento` ou `fechado`. |
| `criado_em` | texto/data | Não | Data e hora gerada pelo banco. |

### Regras

- O `id` é criado automaticamente.
- `titulo`, `descricao` e `prioridade` precisam ser enviados na criação.
- Se o status não for informado, ele começa como `aberto`.
- Os campos de texto não podem ficar vazios.
- A prioridade e o status devem usar apenas os valores indicados.
- O `criado_em` é preenchido pelo banco de dados.

## 3. Rotas implementadas

| O que fazer | Método | URI | Resposta de sucesso |
|---|---|---|---|
| Ver funcionamento da API | `GET` | `/` | `200 OK` |
| Ver solicitações | `GET` | `/chamados` | `200 OK` |
| Criar uma solicitação | `POST` | `/chamados` | `201 Created` |
| Ver uma solicitação | `GET` | `/chamados/{id}` | `200 OK` |
| Filtrar por status | `GET` | `/chamados/status/{status_chamado}` | `200 OK` |

### Rotas planejadas para as próximas etapas

| O que fazer | Método | URI | Resposta de sucesso |
|---|---|---|---|
| Alterar uma solicitação | `PATCH` | `/chamados/{id}` | `200 OK` |
| Remover uma solicitação | `DELETE` | `/chamados/{id}` | `204 No Content` |

## 4. Exemplos

### Ver solicitações

```http
GET /chamados?status=aberto
Accept: application/json
```

```json
[
  {
    "id": 1,
    "titulo": "Dúvida sobre a frequência",
    "descricao": "Minha frequência apareceu diferente no sistema.",
    "prioridade": "media",
    "status": "aberto",
    "criado_em": "2026-09-06 10:30:00"
  }
]
```

Na implementação atual, a consulta retorna uma lista JSON diretamente, inclusive quando estiver vazia.

### Ver uma solicitação

```http
GET /chamados/42
Accept: application/json
```

```json
{
  "id": 1,
  "titulo": "Dúvida sobre a frequência",
  "descricao": "Minha frequência apareceu diferente no sistema.",
  "prioridade": "media",
  "status": "aberto",
  "criado_em": "2026-09-06 10:30:00"
}
```

### Criar uma solicitação

```http
POST /chamados
Content-Type: application/json
```

```json
{
  "titulo": "Dúvida sobre a frequência",
  "descricao": "Minha frequência apareceu diferente no sistema.",
  "prioridade": "media",
  "status": "aberto"
}
```

Resposta `201 Created`:

```json
{
  "id": 1,
  "titulo": "Dúvida sobre a frequência",
  "descricao": "Minha frequência apareceu diferente no sistema.",
  "prioridade": "media",
  "status": "aberto",
  "criado_em": "2026-09-06 10:30:00"
}
```

### Alterar uma solicitação

A alteração pode ser feita só no campo que precisa mudar.

```http
PATCH /chamados/42
Content-Type: application/json
```

```json
{
  "status": "em_atendimento"
}
```

Resposta `200 OK`:

```json
{
  "id": 42,
  "titulo": "Dúvida sobre a frequência",
  "descricao": "Minha frequência apareceu diferente no sistema.",
  "prioridade": "media",
  "status": "em_atendimento"
}
```

### Remover uma solicitação

```http
DELETE /chamados/42
```

A resposta será `204 No Content` e não terá conteúdo.

### Filtrar por status

```http
GET /chamados/status/aberto
Accept: application/json
```

```json
[
  {
    "id": 1,
    "titulo": "Dúvida sobre a frequência",
    "descricao": "Minha frequência apareceu diferente no sistema.",
    "prioridade": "media",
    "status": "aberto",
    "criado_em": "2026-09-06 10:30:00"
  }
]
```

## 5. Respostas da API

| Código | Quando aparece |
|---:|---|
| `200` | Consulta ou alteração feita corretamente. |
| `201` | Solicitação criada. |
| `204` | Solicitação removida. |
| `400` | Algum dado está faltando ou foi enviado errado. |
| `404` | A solicitação não foi encontrada. |

## 6. Persistência

A persistência da Atividade 5 usa SQLite. O script SQL versionado está em:

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
- criado_em: data e hora
```

A API usa `DATABASE_URL` apenas quando for necessário trocar o caminho do banco. Sem essa variável, o banco local fica em `backend/database/alunosaqua.db`.

## 7. Exemplos de erro

### Dados incompletos — `400 Bad Request`

```json
{
  "descricao": "Preciso de ajuda com uma informação da escola.",
  "prioridade": "baixa"
}
```

```json
{
  "erro": "DADOS_INVALIDOS",
  "mensagem": "Não foi possível cadastrar o chamado.",
  "campos": {
    "titulo": "O título é obrigatório."
  }
}
```

### Prioridade inválida — `400 Bad Request`

```json
{
  "titulo": "Problema no acesso",
  "descricao": "Não consigo entrar no portal.",
  "prioridade": "urgente"
}
```

```json
{
  "erro": "DADOS_INVALIDOS",
  "mensagem": "Não foi possível cadastrar o chamado.",
  "campos": {
    "prioridade": "Use baixa, media ou alta."
  }
}
```

### Solicitação não encontrada — `404 Not Found`

```http
GET /chamados/9999
Accept: application/json
```

```json
{
  "erro": "RECURSO_NAO_ENCONTRADO",
  "mensagem": "Nenhum chamado foi encontrado com o id 9999."
}
```

## 8. Decisões do grupo

- A API usa JSON nas requisições e respostas.
- As rotas usam `/chamados` e `/chamados/{id}`.
- A criação usa `POST`.
- A alteração parcial usa `PATCH`.
- A remoção usa `DELETE`.
- O status inicial é `aberto`.
- O filtro por status foi implementado como desafio adicional da Atividade 4.
- Os exemplos foram feitos pensando em situações da escola.
- Na implementação atual, `GET /chamados` retorna uma lista JSON diretamente.
- O SQLite foi adotado na Atividade 5 por ser local, simples e sem credenciais sensíveis.
- As consultas SQL ficam na camada de repositório e usam parâmetros.

## 9. Dúvidas para depois

- A solicitação será ligada ao cadastro de um aluno ou responsável?
- Como será escolhido o setor que vai atender cada pedido?
- A remoção será definitiva ou apenas mudará para `cancelado`?
- Será preciso colocar paginação quando houver muitos registros?
- O AlunoSaqua terá uma API separada para denúncias?

> **Comentário do grupo:** deixamos essas perguntas anotadas para decidir com mais calma quando a parte prática começar.

## 10. Checklist

- [x] Recurso e campos definidos.
- [x] Rotas de consulta, criação, alteração e remoção.
- [x] Filtro por status.
- [x] Exemplos de requisição e resposta.
- [x] Exemplos de erro `400` e `404`.
- [x] Códigos `200`, `201`, `204`, `400` e `404`.
- [x] Decisões e dúvidas registradas.
- [x] Implementação inicial de `GET /chamados` e `POST /chamados`.
- [x] Evidência reproduzível dos testes automatizados.
- [x] Implementação FastAPI com `main.py`.
- [x] `GET /chamados/{id}` implementado.
- [x] Script SQL versionado.
- [x] Persistência local com SQLite.
- [x] Consulta por id inexistente retornando `404`.
- [x] Testes da persistência e validações.

---

**Projeto:** AlunoSaqua  
**Atividade:** 2 — Contrato da API / Atividades 3, 4 e 5 — Implementação
