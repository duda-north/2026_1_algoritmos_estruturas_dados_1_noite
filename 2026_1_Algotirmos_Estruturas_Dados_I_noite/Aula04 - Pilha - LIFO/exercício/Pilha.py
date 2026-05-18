from Livro import Livro

class Pilha: 

    def __init__(self):
        self.topo = None
    
    def add(self, livro):
        livro.prox = self.topo
        self.topo = livro
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Pilha de Livros")
        if self.topo is None:
            print("\nPilha Vazia")
            return
        aux = self.topo
        while aux :
            print(  aux )
            aux = aux.prox

    def remover(self):
        if self.topo is not None:
            aux = self.topo
            self.topo = self.topo.prox
            del(aux)
        self.imprimir()
    
    def contLivros(self, valor):
        if self.topo is not None:
            cont = 0
            aux = self.topo
            while aux:
                if aux.autor.getNome() == valor:
                    cont += 1
                aux = aux.prox
            if cont == 0:
                print( "Nenum livro encontrado!")
            elif cont == 1:
                print("Encontrado 1 livro" )
            else: 
                print("Encontrados ", cont , " livros" )


