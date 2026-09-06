import os
import tempfile
import unittest
from pathlib import Path

from fastapi.testclient import TestClient

from app.database import inicializar_banco
from main import app


class ChamadosFastAPITest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        banco_teste = Path(self.temp_dir.name) / "alunosaqua_test.db"
        os.environ["DATABASE_URL"] = f"sqlite:///{banco_teste}"
        inicializar_banco()
        self.client_context = TestClient(app)
        self.client = self.client_context.__enter__()

    def tearDown(self) -> None:
        self.client_context.__exit__(None, None, None)
        self.temp_dir.cleanup()
        os.environ.pop("DATABASE_URL", None)

    def test_rota_inicial_funciona(self) -> None:
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["mensagem"], "API do AlunoSaqua ativa")

    def test_lista_inicial_retorna_vazia(self) -> None:
        response = self.client.get("/chamados")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_cria_consulta_e_persiste_chamado(self) -> None:
        response = self.client.post(
            "/chamados",
            json={
                "titulo": "Acesso bloqueado",
                "descricao": "Nao consigo acessar o painel do aluno.",
                "prioridade": "alta",
                "status": "aberto",
            },
        )
        criado = response.json()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(criado["id"], 1)
        self.assertEqual(criado["status"], "aberto")
        self.assertIn("criado_em", criado)

        lista = self.client.get("/chamados")
        self.assertEqual(lista.status_code, 200)
        self.assertEqual(lista.json(), [criado])

        por_id = self.client.get(f"/chamados/{criado['id']}")
        self.assertEqual(por_id.status_code, 200)
        self.assertEqual(por_id.json(), criado)

        with TestClient(app) as novo_cliente:
            consulta_persistida = novo_cliente.get(f"/chamados/{criado['id']}")
            self.assertEqual(consulta_persistida.status_code, 200)
            self.assertEqual(consulta_persistida.json(), criado)

    def test_filtro_por_status_funciona(self) -> None:
        self.client.post(
            "/chamados",
            json={
                "titulo": "Duvida sobre frequencia",
                "descricao": "Minha frequencia apareceu diferente.",
                "prioridade": "media",
                "status": "aberto",
            },
        )

        response = self.client.get("/chamados/status/aberto")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_titulo_ausente_retorna_400(self) -> None:
        response = self.client.post(
            "/chamados",
            json={
                "descricao": "Preciso de ajuda com uma informacao da escola.",
                "prioridade": "baixa",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["erro"], "DADOS_INVALIDOS")
        self.assertEqual(
            response.json()["campos"]["titulo"], "O titulo e obrigatorio."
        )

    def test_prioridade_invalida_retorna_400(self) -> None:
        response = self.client.post(
            "/chamados",
            json={
                "titulo": "Problema no acesso",
                "descricao": "Nao consigo entrar no portal.",
                "prioridade": "urgente",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["campos"]["prioridade"], "Use baixa, media ou alta.")

    def test_id_inexistente_retorna_404(self) -> None:
        response = self.client.get("/chamados/999")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["erro"], "RECURSO_NAO_ENCONTRADO")


if __name__ == "__main__":
    unittest.main()
