from No import No
#Lista Duplamente Encadeada por ordem de chegada
class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.proximo = nodo
            nodo.anterior = self.fim
        self.fim = nodo
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Lista Duplamente Encadeada por ordem de chegada")
        if self.inicio is None:
            print("\nLista Vazia")
            return
        aux = self.inicio
        while aux :
            print(  aux.dado )
            aux = aux.proximo

    def imprimirReverso(self):
        print("\n----------------------")
        print("Lista Duplamente Encadeada por ordem reversa de chegada")
        if self.inicio is None:
            print("\nLista Vazia")
            return
        aux = self.fim
        while aux :
            print(  aux.dado )
            aux = aux.anterior

    def remover(self, valor):
        removeu = False
        if self.inicio == None:
            print("Lista Vazia")
        else:
            if valor == self.inicio.dado:
                self.inicio = self.inicio.proximo
                if self.inicio != None:
                    self.inicio.anterior = None
                else:
                    self.fim = None
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux: 
                    if valor == aux.dado:
                        ant.proximo = aux.proximo
                        if ant.proximo != None:
                            aux.proximo.anterior = ant
                        else:
                            self.fim = ant
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
            if removeu:
                print("\n", valor , " removido!" )
            else:
                print( "\n", valor , " não encontrado na lista!")
            self.imprimir()