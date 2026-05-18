from Pessoa import Pessoa
class Lista:

    def __init__(self):
        self.inicio = None

    def add(self, novaPessoa = Pessoa( "Sem Nome" , 0 ) ):
        if self.inicio is None:
            self.inicio = novaPessoa
        else:
            if novaPessoa.idade > self.inicio.idade:
                novaPessoa.prox = self.inicio
                self.inicio = novaPessoa
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux :
                    if novaPessoa.idade > aux.idade:
                        novaPessoa.prox = aux
                        ant.prox = novaPessoa
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if aux == None:
                    ant.prox = novaPessoa
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Lista Encadeada decrescente por Idade")
        if self.inicio is None:
            print("\nLista Vazia")
            return
        aux = self.inicio
        while aux :
            print(  aux.nome , " - Idade: ", aux.idade )
            aux = aux.prox

    def remover(self, valor):
        removeu = False
        if self.inicio == None:
            print("Lista Vazia")
        else:
            if valor == self.inicio.nome:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux: 
                    if valor == aux.nome:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removeu:
                print("\n", valor , " removido!" )
            else:
                print( "\n", valor , " não encontrado na lista!")
            self.imprimir()


