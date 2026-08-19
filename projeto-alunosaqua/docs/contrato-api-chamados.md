# Contrato da API do AlunoSaqua

## Integrantes

- Bruno Oliveira
- Natalia Cardoso
- Rosonatt Ferreira
- Ryan Guiwison

## 1. Para que serve

A API do AlunoSaqua será usada para registrar e acompanhar solicitações da escola. Ela ajuda a interface e o back-end a seguirem o mesmo formato de dados.

Uma solicitação pode ser uma dúvida, um pedido de informação ou um problema que precisa ser visto pela equipe da escola.

As mensagens usam JSON e as rotas são `/chamados` e `/chamados/{id}`, como definido na atividade.

## 2. Dados de uma solicitação

| Campo | Tipo | Obrigatório ao criar? | O que significa |
|---|---|---:|---|
| `id` | número inteiro | Não | Número gerado pelo sistema. |
| `titulo` | texto | Sim | Resumo do que a pessoa precisa. |
| `descricao` | texto | Sim | Explicação da solicitação. |
| `prioridade` | texto | Sim | `baixa`, `media` ou `alta`. |
| `status` | texto | Não | `aberto`, `em_atendimento`, `resolvido` ou `cancelado`. |

### Regras

- O `id` é criado automaticamente.
- `titulo`, `descricao` e `prioridade` precisam ser enviados na criação.
- Se o status não for informado, ele começa como `aberto`.
- Os campos de texto não podem ficar vazios.
- A prioridade e o status devem usar apenas os valores indicados.

## 3. Rotas

| O que fazer | Método | URI | Resposta de sucesso |
|---|---|---|---|
| Ver solicitações | `GET` | `/chamados` | `200 OK` |
| Ver uma solicitação | `GET` | `/chamados/{id}` | `200 OK` |
| Criar uma solicitação | `POST` | `/chamados` | `201 Created` |
| Alterar uma solicitação | `PATCH` | `/chamados/{id}` | `200 OK` |
| Remover uma solicitação | `DELETE` | `/chamados/{id}` | `204 No Content` |

## 4. Exemplos

### Ver solicitações

```http
GET /chamados?status=aberto
Accept: application/json
```

```json
{
  "dados": [
    {
      "id": 42,
      "titulo": "Dúvida sobre a frequência",
      "descricao": "Minha frequência apareceu diferente no sistema.",
      "prioridade": "media",
      "status": "aberto"
    }
  ],
  "total": 1
}
```

O filtro `status` é opcional. Sem ele, a API lista as solicitações conforme a regra definida na aplicação.

### Ver uma solicitação

```http
GET /chamados/42
Accept: application/json
```

```json
{
  "id": 42,
  "titulo": "Dúvida sobre a frequência",
  "descricao": "Minha frequência apareceu diferente no sistema.",
  "prioridade": "media",
  "status": "aberto"
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
  "prioridade": "media"
}
```

Resposta `201 Created`:

```json
{
  "id": 42,
  "titulo": "Dúvida sobre a frequência",
  "descricao": "Minha frequência apareceu diferente no sistema.",
  "prioridade": "media",
  "status": "aberto"
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

## 5. Respostas da API

| Código | Quando aparece |
|---:|---|
| `200` | Consulta ou alteração feita corretamente. |
| `201` | Solicitação criada. |
| `204` | Solicitação removida. |
| `400` | Algum dado está faltando ou foi enviado errado. |
| `404` | A solicitação não foi encontrada. |

## 6. Exemplos de erro

### Dados incompletos — `400 Bad Request`

```json
{
  "descricao": "Preciso de ajuda com uma informação da escola.",
  "prioridade": "baixa"
}
```

```json
{
  "erro": "Dado inválido",
  "detalhes": [
    {
      "campo": "titulo",
      "mensagem": "O título é obrigatório."
    }
  ]
}
```

### Solicitação não encontrada — `404 Not Found`

```http
GET /chamados/9999
Accept: application/json
```

```json
{
  "erro": "Recurso não encontrado",
  "detalhes": [
    {
      "campo": "id",
      "mensagem": "Nenhuma solicitação foi encontrada com o identificador 9999."
    }
  ]
}
```

## 7. Decisões do grupo

- A API usa JSON nas requisições e respostas.
- As rotas usam `/chamados` e `/chamados/{id}`.
- A criação usa `POST`.
- A alteração parcial usa `PATCH`.
- A remoção usa `DELETE`.
- O status inicial é `aberto`.
- O filtro por status é opcional.
- Os exemplos foram feitos pensando em situações da escola.

## 8. Dúvidas para depois

- A solicitação será ligada ao cadastro de um aluno ou responsável?
- Como será escolhido o setor que vai atender cada pedido?
- A remoção será definitiva ou apenas mudará para `cancelado`?
- Será preciso colocar paginação quando houver muitos registros?
- O AlunoSaqua terá uma API separada para denúncias?

> **Comentário do grupo:** deixamos essas perguntas anotadas para decidir com mais calma quando a parte prática começar.

## 9. Checklist

- [x] Recurso e campos definidos.
- [x] Rotas de consulta, criação, alteração e remoção.
- [x] Filtro por status.
- [x] Exemplos de requisição e resposta.
- [x] Exemplos de erro `400` e `404`.
- [x] Códigos `200`, `201`, `204`, `400` e `404`.
- [x] Decisões e dúvidas registradas.

---

**Projeto:** AlunoSaqua  
**Atividade:** 2 — Contrato da API
