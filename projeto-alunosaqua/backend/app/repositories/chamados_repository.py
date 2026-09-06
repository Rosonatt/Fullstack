from app.database import conectar


def listar_chamados() -> list[dict]:
    with conectar() as conexao:
        linhas = conexao.execute(
            """
            SELECT id, titulo, descricao, prioridade, status, criado_em
            FROM chamados
            ORDER BY id
            """
        ).fetchall()

    return [dict(linha) for linha in linhas]


def buscar_chamado_por_id(chamado_id: int) -> dict | None:
    with conectar() as conexao:
        linha = conexao.execute(
            """
            SELECT id, titulo, descricao, prioridade, status, criado_em
            FROM chamados
            WHERE id = ?
            """,
            (chamado_id,),
        ).fetchone()

    return dict(linha) if linha else None


def listar_chamados_por_status(status_chamado: str) -> list[dict]:
    with conectar() as conexao:
        linhas = conexao.execute(
            """
            SELECT id, titulo, descricao, prioridade, status, criado_em
            FROM chamados
            WHERE status = ?
            ORDER BY id
            """,
            (status_chamado,),
        ).fetchall()

    return [dict(linha) for linha in linhas]


def criar_chamado(
    titulo: str,
    descricao: str,
    prioridade: str,
    status: str,
) -> dict:
    with conectar() as conexao:
        cursor = conexao.execute(
            """
            INSERT INTO chamados (titulo, descricao, prioridade, status)
            VALUES (?, ?, ?, ?)
            """,
            (titulo, descricao, prioridade, status),
        )
        conexao.commit()
        chamado_id = cursor.lastrowid

    return buscar_chamado_por_id(chamado_id)
