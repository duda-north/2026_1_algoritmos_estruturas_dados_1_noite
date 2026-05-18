from Apartamento import Apartamento
from Torre import Torre

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, ap):
        if self.inicio is None:
            self.inicio = ap
        else:
            self.fim.proximo = ap
        self.fim = ap
        print( "\nAp " , ap.numero , " adicionado na fila!" )

    def imprimir(self):
        print("\n----------------------")
        print("Fila de Apartamentos")

        if self.inicio is None:
            print("\nFila Vazia")
            return
        aux = self.inicio
        while aux :
            print( aux )
            print("-------------------")
            aux = aux.proximo
        print("---Fim da Fila---")


    def remover(self, vaga):
        if self.inicio is not None:
            aux = self.inicio
            self.inicio = self.inicio.proximo
            aux.proximo = None
            aux.vaga = vaga
            if self.inicio is None:
                self.fim = None 
            print( "\nAp ", aux.numero , " removido da Fila")
            return aux
        return None