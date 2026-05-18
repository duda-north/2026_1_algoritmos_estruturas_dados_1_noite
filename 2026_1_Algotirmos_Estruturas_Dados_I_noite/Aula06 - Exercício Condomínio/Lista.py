from Apartamento import Apartamento
from Torre import Torre

class Lista:

    def __init__(self):
        self.inicio = None

    def add(self, ap ):
        if self.inicio is None:
            self.inicio = ap
        else:
            if ap.vaga < self.inicio.vaga:
                ap.proximo = self.inicio
                self.inicio = ap
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux :
                    if ap.vaga < aux.vaga:
                        ap.proximo = aux
                        ant.proximo = ap
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None:
                    ant.proximo = ap
        print( "\nAp " , ap.numero, " adicionado na Lista")

    def imprimir(self):
        print("\n----------------------")
        print("Lista de Apartamento com vaga")
        if self.inicio is None:
            print("\nLista Vazia")
            return
        aux = self.inicio
        while aux :
            print( aux )
            print("\n----------------------")
            aux = aux.proximo

    def remover(self, vaga):
        apRemovido = None
        if self.inicio == None:
            print("Lista Vazia")
        else:
            if vaga == self.inicio.vaga:
                apRemovido = self.inicio
                self.inicio = self.inicio.proximo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux: 
                    if vaga == aux.vaga:
                        ant.proximo = aux.proximo
                        apRemovido = aux
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
            if apRemovido:
                print("\nAp ", apRemovido.numero  , " removido da Lista!" )
                apRemovido.proximo = None
            else:
                print( "\nVaga ", vaga , " não encontrada na lista!")
        return apRemovido
