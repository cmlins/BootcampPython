from cliente import Cliente
from fruta import Fruta

# instanciando um objeto da classe Fruta
fruta = Fruta()

fruta.display_frutas()

# instanciando um objeto da classe Cliente
nome = Cliente(input("\nInsira seu nome: "))

while True:

    escolha = int(input("Digite o número da fruta que escolheu: "))

    if (escolha in range(1, 11)):
        print(f"\n{nome.cliente}, você vai levar a fruta: {fruta.display_fruta_escolhido(escolha)}!\n")
        break
    else: 
        print("\nVocê não escolheu uma opção válida\n")  
