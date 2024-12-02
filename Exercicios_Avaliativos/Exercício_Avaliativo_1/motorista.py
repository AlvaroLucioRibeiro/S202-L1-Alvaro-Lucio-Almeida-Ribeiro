from typing import List


class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def dict(self):
        return {"nome": self.nome, "documento": self.documento}


class Corrida:
    def __init__(
        self, nota: int, distancia: float, valor: float, passageiro: Passageiro
    ):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro


class Motorista:
    def __init__(self, corridas: List[Corrida], nota: int):
        self.corridas = corridas
        self.nota = nota
