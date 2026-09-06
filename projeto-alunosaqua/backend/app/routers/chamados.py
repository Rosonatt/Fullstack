from fastapi import APIRouter, status

from app.models import ChamadoEntrada, ChamadoSaida
from app.services import chamados_service

router = APIRouter(prefix="/chamados", tags=["Chamados"])


@router.get("", response_model=list[ChamadoSaida])
def listar_chamados() -> list[dict]:
    return chamados_service.listar_chamados()


@router.post("", response_model=ChamadoSaida, status_code=status.HTTP_201_CREATED)
def criar_chamado(dados: ChamadoEntrada) -> dict:
    return chamados_service.criar_chamado(dados)


@router.get("/status/{status_chamado}", response_model=list[ChamadoSaida])
def listar_chamados_por_status(status_chamado: str) -> list[dict]:
    return chamados_service.listar_chamados_por_status(status_chamado)


@router.get("/{chamado_id}", response_model=ChamadoSaida)
def buscar_chamado(chamado_id: int) -> dict:
    return chamados_service.buscar_chamado_por_id(chamado_id)
