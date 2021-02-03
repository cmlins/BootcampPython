# 5. Algoritmo para calcular a média do aluno (Deve colocar o nome do aluno, colocar 4 notas e imprimir sua média)
print('--- Exercício 5 ---\n')

# função que retorna a média aritmética de 4 números
def media (x, y, z, t):
    return (x + y + z + t) / 4

print('\nVamos calcular a média das notas de um alune: \n')

nome = input("Insira o nome do alune: ")
num1 = float(input('Insira a primeira nota: '))
num2 = float(input('Insira a segunda nota: '))
num3 = float(input('Insira a terceira nota: '))
num4 = float(input('Insira a quarta nota: '))

print(f'A média do aluno {nome} é: {media(num1, num2, num3, num4)}')
