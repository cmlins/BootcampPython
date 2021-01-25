class Dados:

    def __init__(self, escolha):
        self.escolha = escolha

    colecoes = {
        1 : ['Paris', 'Londres', 'Bruxelas', 'Amsterdam', 'Buenos Aires', 'Rio de Janeiro', 'Montreal', 'Maldivas', 'Tóquio', 'Pequim'],
        2 : ['Iluminadas por Lauren Beukes', 'Comer, rezar, amar por Elizabeth Gilbert', 'Outros Jeitos de Usar a Boca por Rupi Kaur', 'Meu corpo minha casa  por Rupi Kaur', 'Tudo nela brilha e queima por Ryane Leão', 'Pequeno manual antirracista por Djamila Ribeiro', 'Sejamos todos feministas por Chimamanda Ngozi Adichie', 'Labirinto por Kate Mosse', 'Cracking the coding interview por Gayle Laakmann McDowell', 'O momento de voar por Melinda Gates'],
        3 : ['Pera', 'Uva', 'Maçã', 'Melão', 'Mamão', 'Banana', 'Carambola', 'Melancia', 'Ameixa', 'Caju']
    }
    
    dict_item = {}

    def keys_numbers(self):
        return [i + 1 for i in range(len(self.colecoes.get(self.escolha)))]


    def create_dict (self):
        key = 1
        for (self.key, self.item) in zip(self.keys_numbers(), self.show_list()):
            self.dict_item[self.key] = self.item
            key += 1
        return self.dict_item


    def show_list(self):
        return (self.colecoes.get(self.escolha))
    

# um = Dados(1)

# print(um.show_list())
# print(um.keys_numbers())
# print(um.create_dict ())