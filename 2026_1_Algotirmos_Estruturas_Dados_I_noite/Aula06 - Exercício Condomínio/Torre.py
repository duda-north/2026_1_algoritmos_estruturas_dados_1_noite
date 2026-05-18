class Torre:

    def __init__(self, id = 0, nome = "Sem Nome", end = None):
        self.id = id
        self.nome = nome
        self.endereco = end

    def __str__(self):
        txt = "Torre: " + str( self.id ) 
        txt += " - " + self.nome
        txt += "\nEndereço: " + self.endereco
        return txt
    
    def imprimir(self):
        print( self )
        
        