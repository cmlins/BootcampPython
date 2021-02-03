# 10. Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca) retornando o índice do elemento
print('--- Exercício 10 ---\n')

num = int(input('Insira um número inteiro entre 0 e 20, inclusive 0 e 20: '))

# cria uma lista de 0 a 20 usando list comprehension e faz a conversão para tupla
lista = tuple([i for i in range(0,21)])


if (num in lista):
    # faz uma busca e retorna o índice do número se ele estiver na lista
    indice = [i for i in range(len(lista)) if lista[i] == num]
    print(f'O número {num} está no índice {indice[0]} lista')
else:
    print('O número digitado não está na lista')

# a lista começa do 0, então o índice retornado acaba sendo o mesmo do índice.
