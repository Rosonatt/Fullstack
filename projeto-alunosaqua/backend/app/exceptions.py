class ErroValidacao(ValueError):
    def __init__(self, campos: dict[str, str]) -> None:
        super().__init__("Dados invalidos")
        self.campos = campos


class ChamadoNaoEncontrado(LookupError):
    def __init__(self, chamado_id: int) -> None:
        super().__init__(f"Nenhum chamado foi encontrado com o id {chamado_id}.")
