from Musica import Musica
#Lista Duplamente Encadeada de músicas ordenadas pelo título
class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, musica = Musica("Sem Título", "Desconhecido", 0) ):
        if self.inicio is None:
            self.inicio = musica
            self.fim = musica
        else:
            if musica.titulo < self.inicio.titulo:
                musica.proxima = self.inicio
                self.inicio.anterior = musica 
                self.inicio = musica
            else:
                ant = self.inicio
                aux = self.inicio.proxima
                while aux:
                    if musica.titulo < aux.titulo:
                        ant.proxima = musica
                        musica.anterior = ant
                        musica.proxima = aux
                        aux.anterior = musica
                        break
                    else:
                        ant = aux
                        aux = aux.proxima
                if aux == None:
                    ant.proxima = musica
                    musica.anterior = ant
                    self.fim = musica        
        self.imprimir()

    def imprimir(self):
        print("\n----------------------")
        print("Playlist por ordem de título")
        if self.inicio is None:
            print("\nPlaylist Vazia")
            return
        aux = self.inicio
        while aux :
            print(  aux )
            aux = aux.proxima

    def imprimirReverso(self):
        print("\n----------------------")
        print("Playlist por ordem de título reversa")
        if self.inicio is None:
            print("\nPlaylist Vazia")
            return
        aux = self.fim
        while aux :
            print(  aux )
            aux = aux.anterior

    def remover(self, valor):
        removeu = False
        if self.inicio == None:
            print("Playlist Vazia")
        else:
            if valor == self.inicio.titulo:
                self.inicio = self.inicio.proxima
                if self.inicio != None:
                    self.inicio.anterior = None
                else:
                    self.fim = None
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.proxima
                while aux: 
                    if valor == aux.titulo:
                        ant.proxima = aux.proxima
                        if ant.proxima != None:
                            aux.proxima.anterior = ant
                        else:
                            self.fim = ant
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.proxima
            if removeu:
                print("\n", valor , " removida!" )
            else:
                print( "\n", valor , " não encontrada na lista!")
            self.imprimir()