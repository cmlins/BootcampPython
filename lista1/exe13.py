# 13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada)
print('--- Exercício 13---\n')

nome = input('Insira seu nome: ')

print('\nDigite o número correspondente ao seu destino:\n1 - Paris;\n 2 - Londres;\n 3 - Bruxelas;\n 4 - Amsterdam')

destino = int(input())

if (destino == 1):
    print(f'{nome}, você escolheu visitar Paris!')
elif (destino == 2):
    print(f'{nome}, você escolheu visitar Londres!')
elif (destino == 3):
    print(f'{nome}, você escolheu visitar Bruxelas!')
elif (destino == 4):
    print(f'{nome}, você escolheu visitar Amsterdam!')
else: 
    print('Você não escolheu uma opção válida')