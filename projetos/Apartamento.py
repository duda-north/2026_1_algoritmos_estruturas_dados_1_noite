from Torre import Torre

class Apartamento:
    def __init__(self, id, numero, torre: Torre, vaga=0):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None  # Este é o "ponteiro" para o próximo nó da lista

    def cadastrar(self):
        print(f"Apartamento {self.numero} cadastrado.")

    def imprimir(self):
        status = f"Vaga: {self.vaga}" if self.vaga > 0 else "Na fila de espera"
        print(f"ID: {self.id} | Ap: {self.numero} | {status} | Torre: {self.torre.nome}")