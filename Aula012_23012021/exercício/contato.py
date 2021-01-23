class Contato:

    def __init__(self, nome, telefone, endereco):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def display_nome(self):
        return print(self.nome)

    def display_telefone(self):
        return print(self.telefone)

    def display_endereco(self):
        return print(self.endereco)