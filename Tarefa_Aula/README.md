# Atividade Prática — Primeira API de Chamados com FastAPI

**Aluno:** Rosonatt Ferreira Ramos  
**Curso:** Engenharia de Software  
**Aula:** Laboratório de Programação Full Stack  
**Professor:** Ralfh  

## Objetivo

Criar uma API para cadastrar e consultar chamados utilizando FastAPI, Uvicorn e Pydantic. Nesta atividade, os dados ficam armazenados temporariamente em memória.

## Como executar

Abra o terminal na pasta do projeto e execute os comandos:

    python -m venv .venv

    .venv\Scripts\activate

    pip install fastapi uvicorn

Depois, inicie a aplicação:

    uvicorn main:app --reload

Acesse a documentação interativa pelo navegador:

    http://127.0.0.1:8000/docs

## Endpoints implementados

- GET / — Verifica se a API está funcionando.
- GET /chamados — Lista todos os chamados.
- POST /chamados — Cadastra um novo chamado.
- GET /chamados/{id} — Consulta um chamado pelo ID.
- GET /chamados/status/{status} — Filtra chamados por status.

## Exemplo de cadastro

Para cadastrar um chamado, utilize o endpoint POST /chamados com os seguintes dados:

    {
      "titulo": "Computador com defeito",
      "descricao": "O computador não liga.",
      "prioridade": "alta"
    }

A resposta esperada será:

    {
      "id": 1,
      "titulo": "Computador com defeito",
      "descricao": "O computador não liga.",
      "prioridade": "alta",
      "status": "aberto"
    }

O cadastro deve retornar o status 201 Created.

## Testes realizados

- GET / retornando a mensagem de funcionamento;
- GET /chamados retornando uma lista vazia inicialmente;
- POST /chamados cadastrando um chamado com sucesso;
- GET /chamados exibindo o chamado cadastrado;
- GET /chamados/1 consultando o chamado pelo ID;
- GET /chamados/999 retornando o erro 404;
- POST /chamados sem um campo obrigatório retornando o erro de validação 422.

## Tecnologias utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic

## Observação

Os chamados são armazenados apenas em memória. Portanto, os dados serão apagados quando o servidor for encerrado.

## Gerando o arquivo requirements.txt

Com o ambiente virtual ativado, execute:

    pip freeze > requirements.txt
