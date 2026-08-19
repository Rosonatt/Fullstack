# Arquitetura do AlunoSaqua

O desenho mostra de forma simples como as partes do AlunoSaqua se conectam.

```mermaid
flowchart TD
    U[Aluno / responsável / professor / funcionário]
    UI[Site do AlunoSaqua\nInterface]
    API[API]
    BE[Back-end\nRegras do sistema]
    DB[(Banco de dados)]

    U -->|Acessa e envia informações| UI
    UI -->|Envia dados em JSON| API
    API -->|Faz as solicitações| BE
    BE -->|Salva e consulta dados| DB
```

## Como funciona

A pessoa usa o site para registrar uma solicitação ou consultar o andamento. A interface envia os dados para a API, o back-end confere tudo e o banco guarda as informações. Depois, o resultado volta para a tela.

## Função de cada parte

- **Pessoa usuária:** acessa o sistema e envia ou acompanha uma solicitação.
- **Interface:** mostra as telas, formulários e resultados.
- **API:** recebe os pedidos da interface e devolve as respostas.
- **Back-end:** cuida das validações e das regras do AlunoSaqua.
- **Banco de dados:** armazena usuários, solicitações e outras informações da escola.

> **Comentário do grupo:** separamos as partes dessa forma porque fica mais fácil entender o que cada uma faz. Também ajuda caso alguma parte precise mudar depois.
