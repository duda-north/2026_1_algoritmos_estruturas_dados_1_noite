from Torre import Torre

class Apartamento: 
    def __init__(self, id, numero = "Sem Número", torre = Torre(nome = "Torre A"),
                  vaga = None):
        self.id = id
        self.numero = numero
        self.torre = torre
        self.vaga = vaga
        self.proximo = None

    def __str__(self):
        txt = "Apartamento: " + str(self.id)  + " - " + self.numero
        txt += "\n" + str( self.torre ) + "\nVaga: " + str( self.vaga )
        return txt
    
    def imprimir(self):
        print(self)