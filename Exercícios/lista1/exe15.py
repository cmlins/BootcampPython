# 15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)
print('--- Exercício 15 ---\n')
frutas = {
    1 : "Pera",
    2 : "Uva",
    3 : "Maçã", 
    4 : "Melão",
    5 : "Mamão",
    6 : "Banana",
    7 : "Carambola",
    8 : "Melancia",
    9 : "Ameixa",
    10 : "Caju"
}

print("As frutas disponíveis são:\n")

for opcao in frutas:
    print(f'{opcao} - {frutas[opcao]}')

nome = input("\nInsira seu nome: ")

fruta = int(input("Digite o número do fruta que escolheu: "))

if (fruta in range(len(frutas) + 1)):
    print(f"{nome}, você escolheu {frutas[fruta]}!")
else: 
    print("Você não escolheu uma opção válida")