from dados import Dados

class Displays:

    def __init__(self, escolha):
        self.escolha = escolha
        

    def display_itens(self):
        # instanciando um conjunto de dados da classe Dados
        dado = Dados(self.escolha)
        self.opcoes = dado.create_dict()
        # imprimir lista com as opções disponpiveis nas listas
        print("\nAs opcoes disponíveis são:\n")
        index = 1
        for self.opcao in self.opcoes:
            print (index, self.opcoes.get(self.opcao))
            index += 1

    
    def display_item_escolhido(self, item_escolhido):
        return self.opcoes.get(item_escolhido)


# itens = Displays(2)

# itens.display_itens()

# print(itens.display_item_escolhido(2))