# 10. Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca) retornando o índice do elemento
print('--- Exercício 10 ---\n')

num = int(input('Insira um número inteiro entre 0 e 20, inclusive 0 e 20: '))

lista = tuple([i for i in range(0,21)])

if (num in lista):---->>>>> não usar isso
    indice = [i for i in range(len(lista)) if lista[i] == num]
    print(f'O número {num} está no índice {indice[0]} lista')
else:
    print('O número digitado não está na lista')

print('\n')