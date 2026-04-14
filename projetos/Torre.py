class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self):
        # Lógica para persistência de dados poderia vir aqui
        print(f"Torre {self.nome} cadastrada com sucesso.")

    def imprimir(self):
        print(f"ID: {self.id} | Nome: {self.nome} | Endereço: {self.endereco}")