from No import No

class Pilha: 

    def __init__(self):
        self.topo = None
    
    def add(self, valor):
        nodo = No(valor)
        nodo.prox = self.topo
        self.topo = nodo
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Pilha - LIFO")
        if self.topo is None:
            print("\nPilha Vazia")
            return
        aux = self.topo
        while aux :
            print(  aux.dado )
            aux = aux.prox

    def remover(self):
        if self.topo is not None:
            aux = self.topo
            self.topo = self.topo.prox
            del(aux)
        self.imprimir()