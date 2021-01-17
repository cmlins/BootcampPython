num = int(input('Insira um número: '))
matriz = [list(range(i, i+10)) for i in range(1, 100, 10)]

print(matriz)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if (num == matriz[linha][coluna]):
            print(f'O número {num} está na linha {linha} e na coluna {coluna}')

