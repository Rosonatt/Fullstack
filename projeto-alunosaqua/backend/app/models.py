from pydantic import BaseModel, Field


class ChamadoEntrada(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=120)
    descricao: str = Field(..., min_length=1)
    prioridade: str = Field(..., min_length=1)
    status: str = "aberto"


class ChamadoSaida(BaseModel):
    id: int
    titulo: str
    descricao: str
    prioridade: str
    status: str
    criado_em: str
