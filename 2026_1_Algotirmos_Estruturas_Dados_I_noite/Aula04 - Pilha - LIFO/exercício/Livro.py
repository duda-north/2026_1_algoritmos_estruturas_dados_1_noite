from Autor import Autor

class Livro:

    def __init__(self, titulo = "Sem Título", paginas = 0, autor = Autor() ):
        self.titulo = titulo
        self.paginas = paginas
        self.autor = autor
        self.prox = None
    
    def __str__(self):
        txt = "Título: " + self.titulo + "\n"
        txt += "Páginas: " + str(self.paginas) + "\n"
        txt += "Autor: " + str( self.autor )
        return txt