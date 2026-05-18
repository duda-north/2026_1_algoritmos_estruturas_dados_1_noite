class Autor:

    def __init__(self, nome = "Não Informado", ano = None):
        self._nome = nome
        self.__ano = ano

    def __str__(self):
        return  self._nome + " - Ano: " + str(self.__ano)
    
    def setNome(self, valor):
        if valor != "":
            self._nome = valor

    def getNome(self):
        return self._nome

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, valor):
        if valor != "" and valor < 2026:
            self.__ano = valor
