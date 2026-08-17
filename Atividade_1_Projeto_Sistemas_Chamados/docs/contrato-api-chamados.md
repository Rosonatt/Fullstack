# Contrato inicial — API de Chamados

## 1. Contexto

Este documento define o contrato inicial da API do sistema de chamados de suporte interno. A proposta é criar uma referência comum para as equipes de front-end e back-end, evitando interpretações diferentes durante a implementação.

O contrato foi elaborado como parte do planejamento acadêmico do projeto **Sistema de Chamados**. Neste momento, o foco está na definição das operações, dos dados e das respostas esperadas da API. A implementação do código e a criação do banco de dados ficam para uma etapa posterior.

## 2. Recurso `chamados`

### Finalidade

O recurso `chamados` representa solicitações de suporte feitas por pessoas usuárias. Cada chamado registra o problema informado, sua prioridade e o andamento do atendimento.

### Formato das mensagens

- Formato das requisições e respostas: `JSON`
- Tipo de conteúdo esperado: `application/json`
- Identificadores: números inteiros positivos
- Nomes dos campos: será utilizado o padrão `snake_case`.

## 3. Atributos do chamado

| Campo | Tipo | Obrigatório na criação? | Descrição | Valores ou exemplo |
|---|---|---:|---|---|
| `id` | número inteiro | Não | Identificador único do chamado, gerado pela API. | `42` |
| `titulo` | texto | Sim | Resumo objetivo do problema ou solicitação. | `"Tela sem acesso"` |
| `descricao` | texto | Sim | Detalhamento do problema relatado pela pessoa usuária. | `"Não consigo acessar a tela de consultas."` |
| `prioridade` | texto | Sim | Nível de urgência do chamado. | `"baixa"`, `"media"` ou `"alta"` |
| `status` | texto | Não | Situação atual do chamado. | `"aberto"`, `"em_atendimento"`, `"resolvido"` ou `"cancelado"` |

### Regras iniciais dos atributos

- O campo `id` é criado automaticamente pela API e não deve ser enviado na criação.
- Os campos `titulo`, `descricao` e `prioridade` são obrigatórios no `POST`.
- O campo `status` será iniciado com o valor `aberto` quando não for informado.
- O campo `prioridade` aceita somente `baixa`, `media` e `alta`.
- O campo `status` aceita somente `aberto`, `em_atendimento`, `resolvido` e `cancelado`.
- Os textos não devem ser vazios ou compostos apenas por espaços.

## 4. Endpoints

A API utilizará a versão inicial no caminho `/api/v1`.

| Operação | Método | URI | Parâmetros | Status de sucesso |
|---|---|---|---|---|
| Listar chamados | `GET` | `/api/v1/chamados` | Consulta opcional `status` | `200 OK` |
| Consultar um chamado | `GET` | `/api/v1/chamados/{id}` | `id` na URI | `200 OK` |
| Criar chamado | `POST` | `/api/v1/chamados` | Corpo JSON | `201 Created` |
| Atualizar chamado | `PATCH` | `/api/v1/chamados/{id}` | `id` na URI e corpo JSON | `200 OK` |
| Remover chamado | `DELETE` | `/api/v1/chamados/{id}` | `id` na URI | `204 No Content` |

### Listar chamados

```http
GET /api/v1/chamados?status=aberto
Accept: application/json
```

Resposta `200 OK`:

```json
{
  "dados": [
    {
      "id": 42,
      "titulo": "Tela sem acesso",
      "descricao": "Não consigo acessar a tela de consultas.",
      "prioridade": "alta",
      "status": "aberto"
    }
  ],
  "total": 1
}
```

### Consultar um chamado

```http
GET /api/v1/chamados/42
Accept: application/json
```

Resposta `200 OK`:

```json
{
  "id": 42,
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "alta",
  "status": "aberto"
}
```

### Criar um chamado

```http
POST /api/v1/chamados
Content-Type: application/json
```

Requisição:

```json
{
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "alta"
}
```

Resposta `201 Created`:

```json
{
  "id": 42,
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "alta",
  "status": "aberto"
}
```

### Atualizar um chamado

A atualização será parcial, por isso somente os campos alterados precisam ser enviados.

```http
PATCH /api/v1/chamados/42
Content-Type: application/json
```

```json
{
  "status": "em_atendimento",
  "prioridade": "media"
}
```

Resposta `200 OK`:

```json
{
  "id": 42,
  "titulo": "Tela sem acesso",
  "descricao": "Não consigo acessar a tela de consultas.",
  "prioridade": "media",
  "status": "em_atendimento"
}
```

### Remover um chamado

```http
DELETE /api/v1/chamados/42
```

Resposta `204 No Content`, sem corpo na resposta.

## 5. Códigos HTTP previstos

| Código | Nome | Quando será utilizado |
|---:|---|---|
| `200` | `OK` | Listagem, consulta individual ou atualização realizada com sucesso. |
| `201` | `Created` | Chamado criado com sucesso. |
| `204` | `No Content` | Chamado removido com sucesso, sem conteúdo na resposta. |
| `400` | `Bad Request` | Dados inválidos, campos obrigatórios ausentes ou valores não permitidos. |
| `404` | `Not Found` | Chamado não encontrado para o identificador informado. |

## 6. Exemplos de erros

### Erro 400 — dado inválido

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

### Erro 404 — chamado inexistente

```json
{
  "erro": "Recurso não encontrado",
  "detalhes": [
    {
      "campo": "id",
      "mensagem": "Nenhum chamado foi encontrado com o identificador 9999."
    }
  ]
}
```

## 7. Decisões e dúvidas

### Decisões técnicas

1. Foi adotado o nome plural `/chamados` para representar a coleção do recurso.
2. Foi escolhido `POST` para criação, `PATCH` para atualização parcial e `DELETE` para remoção.
3. O status inicial será `aberto`.
4. Foi incluído o filtro opcional `status` na listagem.
5. A versão inicial da API será identificada por `/api/v1`.

### Revisão por outra equipe

**Alteração feita após a revisão:** a URI foi padronizada para utilizar nomes de recursos no plural, como `/api/v1/chamados` e `/api/v1/chamados/{id}`, sem verbos como `/criarChamado` ou `/listarChamados`.

Essa alteração torna o contrato mais coerente com os métodos HTTP e facilita a compreensão para quem desenvolverá o front-end.

### Dúvidas pendentes

- Em uma próxima versão, o chamado deverá ser vinculado a uma pessoa usuária, setor ou atendente específico?
- A remoção será física ou o sistema apenas alterará o status para `cancelado`?
- A paginação será necessária quando o volume de chamados aumentar?

## 8. Checklist

- [x] Finalidade e atributos do recurso definidos.
- [x] Endpoints obrigatórios documentados.
- [x] Parâmetro `id` presente nas URIs individuais.
- [x] Filtro opcional por `status` documentado.
- [x] Exemplos de criação, sucesso `201`, erro `400` e erro `404` incluídos.
- [x] Códigos HTTP previstos registrados.
- [x] Decisões, dúvidas e revisão por outra equipe registrados.

---

**Projeto:** Sistema de Chamados  
**Atividade:** 2 — Contrato inicial da API
