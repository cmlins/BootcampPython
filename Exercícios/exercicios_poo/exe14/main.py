from leitor import Leitor
from livro import Livro

# instanciando um objeto da classe Livro
livro = Livro()

livro.display_livros()

# instanciando um objeto da classe Leitor
nome = Leitor(input("\nInsira seu nome: "))

while True:

    escolha = int(input("Digite o número do livro que escolheu: "))

    if (escolha in range(1, 11)):
        print(f"\n{nome.leitor}, você escolheu o livro: {livro.display_livro_escolhido(escolha)}!\n")
        break
    else: 
        print("\nVocê não escolheu uma opção válida\n")        