from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.database import inicializar_banco
from app.exceptions import ChamadoNaoEncontrado, ErroValidacao
from app.routers.chamados import router as chamados_router


@asynccontextmanager
async def lifespan(_app: FastAPI):
    inicializar_banco()
    yield


# Adaptado para o AlunoSaqua: os chamados representam solicitacoes da rotina escolar.
app = FastAPI(title="API do AlunoSaqua", lifespan=lifespan)


@app.get("/")
def inicio() -> dict[str, str]:
    return {"mensagem": "API do AlunoSaqua ativa"}


app.include_router(chamados_router)


@app.exception_handler(ErroValidacao)
async def tratar_erro_validacao(_request: Request, exc: ErroValidacao) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={
            "erro": "DADOS_INVALIDOS",
            "mensagem": "Nao foi possivel cadastrar o chamado.",
            "campos": exc.campos,
        },
    )


@app.exception_handler(ChamadoNaoEncontrado)
async def tratar_chamado_nao_encontrado(
    _request: Request, exc: ChamadoNaoEncontrado
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={
            "erro": "RECURSO_NAO_ENCONTRADO",
            "mensagem": str(exc),
        },
    )


@app.exception_handler(RequestValidationError)
async def tratar_validacao_pydantic(
    _request: Request, exc: RequestValidationError
) -> JSONResponse:
    campos = {}

    for erro in exc.errors():
        loc = erro.get("loc", [])
        campo = loc[-1] if loc else "corpo"
        campos[str(campo)] = mensagem_validacao(str(campo), erro.get("type", ""))

    return JSONResponse(
        status_code=400,
        content={
            "erro": "DADOS_INVALIDOS",
            "mensagem": "Nao foi possivel cadastrar o chamado.",
            "campos": campos,
        },
    )


def mensagem_validacao(campo: str, tipo: str) -> str:
    mensagens_obrigatorias = {
        "titulo": "O titulo e obrigatorio.",
        "descricao": "A descricao e obrigatoria.",
        "prioridade": "A prioridade e obrigatoria.",
    }

    if "missing" in tipo:
        return mensagens_obrigatorias.get(campo, "Campo obrigatorio.")

    return "Valor invalido."
