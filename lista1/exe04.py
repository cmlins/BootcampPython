# 4. Elabore um algoritmo em Python que leia, calcule e escreva a média aritmética entre quatro números;
print('--- Exercício 4 ---\n')

# função que retorna a média aritmética de 4 números
def media (x, y, z, t):
    return (x + y + z + t) / 4

print('\nVamos calcular a média aritmética de 4 números: \n')

num1 = float(input('Insira um número: '))
num2 = float(input('Insira um número: '))
num3 = float(input('Insira um número: '))
num4 = float(input('Insira um número: '))

print(f'A média aritmética de {num1}, {num2}, {num3} e {num4} é: {media(num1, num2, num3, num4)}')
