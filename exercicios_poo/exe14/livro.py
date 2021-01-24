class Livro:

    def __init__(self) -> None:
        pass

    livros = {
    1 : "Iluminadas por Lauren Beukes",
    2 : "Comer, rezar, amar por Elizabeth Gilbert",
    3 : "Outros Jeitos de Usar a Boca por Rupi Kaur", 
    4 : "Meu corpo minha casa  por Rupi Kaur",
    5 : "Tudo nela brilha e queima por Ryane Leão",
    6 : "Pequeno manual antirracista por Djamila Ribeiro",
    7 : "Sejamos todos feministas por Chimamanda Ngozi Adichie",
    8 : "Labirinto por Kate Mosse",
    9 : "Cracking the coding interview por Gayle Laakmann McDowell",
    10 : "O momento de voar por Melinda Gates"
    }

    def display_livros(self):
        print("\nOs livros disponíveis são:\n")
        index = 1
        for self.livro in self.livros:
            print (index, self.livros.get(self.livro))
            index += 1

    
    def display_livro_escolhido(self, escolha):
        return self.livros.get(escolha)
