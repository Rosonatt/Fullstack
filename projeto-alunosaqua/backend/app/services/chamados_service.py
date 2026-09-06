from app.exceptions import ChamadoNaoEncontrado, ErroValidacao
from app.models import ChamadoEntrada
from app.repositories import chamados_repository

PRIORIDADES_PERMITIDAS = {"baixa", "media", "alta"}
STATUS_PERMITIDOS = {"aberto", "em_andamento", "fechado"}


def listar_chamados() -> list[dict]:
    return chamados_repository.listar_chamados()


def buscar_chamado_por_id(chamado_id: int) -> dict:
    chamado = chamados_repository.buscar_chamado_por_id(chamado_id)

    if not chamado:
        raise ChamadoNaoEncontrado(chamado_id)

    return chamado


def listar_chamados_por_status(status_chamado: str) -> list[dict]:
    status_normalizado = status_chamado.strip().lower()

    if status_normalizado not in STATUS_PERMITIDOS:
        raise ErroValidacao({"status": "Use aberto, em_andamento ou fechado."})

    return chamados_repository.listar_chamados_por_status(status_normalizado)


def criar_chamado(dados: ChamadoEntrada) -> dict:
    titulo = dados.titulo.strip()
    descricao = dados.descricao.strip()
    prioridade = dados.prioridade.strip().lower()
    status = dados.status.strip().lower()
    campos = {}

    # Adaptado para o AlunoSaqua: mantemos prioridades de atendimento escolar.
    if not titulo:
        campos["titulo"] = "O titulo e obrigatorio."

    if not descricao:
        campos["descricao"] = "A descricao e obrigatoria."

    if not prioridade:
        campos["prioridade"] = "A prioridade e obrigatoria."
    elif prioridade not in PRIORIDADES_PERMITIDAS:
        campos["prioridade"] = "Use baixa, media ou alta."

    if not status:
        campos["status"] = "O status e obrigatorio."
    elif status not in STATUS_PERMITIDOS:
        campos["status"] = "Use aberto, em_andamento ou fechado."

    if campos:
        raise ErroValidacao(campos)

    return chamados_repository.criar_chamado(
        titulo=titulo,
        descricao=descricao,
        prioridade=prioridade,
        status=status,
    )
