# 11. Fazer uma busca sequencial em uma matriz (Criar uma matriz 10 linhas e 10 colunas e pedir para o usuário fazer uma busca)
print('--- Exercício 11 ---\n')

matriz = [list(range(i, i+10)) for i in range(1, 100, 10)]

print(matriz)

num = int(input('Insira um número: '))

count = 0

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if (num == matriz[linha][coluna]):
            print(f'\nO número {num} está na linha {linha} e na coluna {coluna}')
            count += 1

if (count == 0): print(f'\nO número {num} não está na lista!')
