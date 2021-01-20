# array = [1, 2, 3]

# matriz = [  [1, 2], 
#             [3, 4], 
#             [5, 6]]

# cubo = [[[1, 2], [3, 4]], [5, 6]]

print('--- Exercício 11 ---\n')

num = int(input('Insira um número: '))

matriz = [list(range(i, i+10)) for i in range(1, 100, 10)]

count = 0

print(matriz)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if (num == matriz[linha][coluna]):
            print(f'\nO número {num} está na linha {linha} e na coluna {coluna}')
            count += 1

if (count == 0): print(f'\nO número {num} não está na lista!')

print('\n')