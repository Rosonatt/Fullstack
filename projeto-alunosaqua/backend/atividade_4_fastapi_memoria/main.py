from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Professor: o enunciado fala em chamados de suporte; aqui adaptei para o AlunoSaqua,
# usando os chamados como solicitacoes feitas por alunos, responsaveis e equipe escolar.
app = FastAPI(title="API de Chamados do AlunoSaqua")


class ChamadoEntrada(BaseModel):
    titulo: str
    descricao: str
    prioridade: str


chamados = []


@app.get("/")
def inicio():
    return {"mensagem": "API de Chamados do AlunoSaqua ativa"}


@app.get("/chamados")
def listar_chamados():
    return chamados


@app.post("/chamados", status_code=status.HTTP_201_CREATED)
def criar_chamado(dados: ChamadoEntrada):
    # Mantive a estrutura pedida na aula, mudando apenas o contexto para a rotina escolar.
    chamado = {
        "id": len(chamados) + 1,
        **dados.model_dump(),
        "status": "aberto",
    }

    chamados.append(chamado)
    return chamado


@app.get("/chamados/{chamado_id}")
def buscar_chamado(chamado_id: int):
    for chamado in chamados:
        if chamado["id"] == chamado_id:
            return chamado

    raise HTTPException(
        status_code=404,
        detail="Chamado nao encontrado",
    )


@app.get("/chamados/status/{status_chamado}")
def listar_chamados_por_status(status_chamado: str):
    # Desafio adicional do PDF aplicado aos status dos chamados do AlunoSaqua.
    return [
        chamado
        for chamado in chamados
        if chamado["status"] == status_chamado
    ]
