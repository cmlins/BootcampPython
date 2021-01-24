from viajante import Viajante
from destino import Destino

# instanciando um objeto da classe Destino
destino = Destino()

destino.display_destinos()

# instanciando um objeto da classe Viajante
nome = Viajante(input("\nInsira seu nome: "))

while True:

    escolha = int(input("Digite o número do destino que escolheu: "))

    if (escolha in range(1, 11)):
        print(f"\n{nome.nome}, você escolheu o destino: {destino.display_destino_escolhido(escolha)}!\n")
        break
    else: 
        print("\nVocê não escolheu uma opção válida\n")        