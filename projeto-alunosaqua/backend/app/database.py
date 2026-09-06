import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
SCRIPT_BANCO = BASE_DIR / "banco" / "001_criar_tabela_chamados.sql"
CAMINHO_BANCO_PADRAO = BASE_DIR / "database" / "alunosaqua.db"


def abrir_conexao() -> sqlite3.Connection:
    caminho = caminho_banco()

    if caminho != ":memory:":
        Path(caminho).parent.mkdir(parents=True, exist_ok=True)

    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    return conexao


@contextmanager
def conectar():
    conexao = abrir_conexao()

    try:
        yield conexao
    finally:
        conexao.close()


def inicializar_banco() -> None:
    with conectar() as conexao:
        conexao.executescript(SCRIPT_BANCO.read_text(encoding="utf-8"))


def caminho_banco() -> str:
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        return str(CAMINHO_BANCO_PADRAO)

    if database_url == "sqlite:///:memory:":
        return ":memory:"

    prefixo = "sqlite:///"

    if database_url.startswith(prefixo):
        return database_url.removeprefix(prefixo)

    raise RuntimeError("Use DATABASE_URL no formato sqlite:///caminho/do/banco.db")
