from pessoa import Pessoa
from displays import Displays


# instanciando um objeto da classe Pessoa
nome = Pessoa(input("\nOlá!! Insira seu nome: "))


# escolher qual programa vai ser executado

while True:
    programa = int(input("""\nEscolha o programa que deseja executar:

1 - Cadastro de viagem
2 - Reserva de livros
3 - Lista de compras
\n"""))

    if (programa == 1):
        print('\nVocê escolheu fazer um cadastro de viagem')
        # instanciando uma lista dos produtos escolhidos
        itens = Displays(programa)
        itens.display_itens()
        break
    elif (programa == 2):
        print('\nVocê escolheu fazer um cadastro de viagem')
        # instanciando uma lista dos produtos escolhidos
        itens = Displays(programa)
        itens.display_itens()
        break
    elif (programa == 3):
        print('\nVocê escolheu fazer um cadastro de viagem')
        # instanciando uma lista dos produtos escolhidos
        itens = Displays(programa)
        itens.display_itens()
        break
    else:
        print("\nVocê não escolheu uma opção válida\n")  


while True:

    escolha = int(input("\nDigite o número do produto que escolheu: "))

    if (escolha in range(1, 11)):
        print(f"\n{nome.pessoa}, você vai levar o seguinte produto: {itens.display_item_escolhido(escolha)}!\n")
        break
    else: 
        print("\nVocê não escolheu uma opção válida\n")  
