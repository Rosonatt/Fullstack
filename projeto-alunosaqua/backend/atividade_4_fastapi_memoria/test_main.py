from fastapi.testclient import TestClient

from main import app, chamados


client = TestClient(app)


def setup_function():
    chamados.clear()


def test_rota_inicial_funciona():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "API de Chamados do AlunoSaqua ativa"
    }


def test_lista_inicial_vazia():
    response = client.get("/chamados")

    assert response.status_code == 200
    assert response.json() == []


def test_criar_chamado_retorna_201_e_aparece_na_lista():
    response = client.post(
        "/chamados",
        json={
            "titulo": "Duvida sobre frequencia",
            "descricao": "Minha frequencia apareceu diferente no sistema.",
            "prioridade": "media",
        },
    )

    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["status"] == "aberto"

    lista = client.get("/chamados")
    assert lista.status_code == 200
    assert lista.json() == [response.json()]


def test_buscar_chamado_por_id():
    criado = client.post(
        "/chamados",
        json={
            "titulo": "Acesso ao portal",
            "descricao": "Nao consigo acessar a area do aluno.",
            "prioridade": "alta",
        },
    ).json()

    response = client.get("/chamados/1")

    assert response.status_code == 200
    assert response.json() == criado


def test_id_inexistente_retorna_404():
    response = client.get("/chamados/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Chamado nao encontrado"


def test_post_invalido_retorna_validacao_automatica():
    response = client.post(
        "/chamados",
        json={
            "descricao": "Preciso de ajuda com uma informacao da escola.",
            "prioridade": "baixa",
        },
    )

    assert response.status_code == 422
    assert "detail" in response.json()


def test_desafio_filtro_por_status():
    client.post(
        "/chamados",
        json={
            "titulo": "Problema no boletim",
            "descricao": "Nao encontrei minhas notas no portal.",
            "prioridade": "baixa",
        },
    )

    response = client.get("/chamados/status/aberto")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_documentacao_docs_abre():
    response = client.get("/docs")

    assert response.status_code == 200
