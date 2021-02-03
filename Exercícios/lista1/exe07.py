# 7. Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto aleatório de número (de 0 a 100) e dizer se o usuário advinhou)
import random

print('--- Exercício 7 ---\n')

nome = input('\nOlá, jogadore!! Digite seu nome: ')

num = int(input('\nAgora, digite um número inteiro entre 0 e 100 e vamos tentar adivinhá-lo: '))

# gera um número aleatório entre 0 e 100
aleatorio = random.randint(0,100)

if (num >= 0 and num <= 100):
    if (num == aleatorio):
        print(f'\nParabéns!!! Você adivinhou o número que escolhemos. Será que {num} é seu número da sorte?\n')
    else:
        print(f'\nNão foi dessa vez! Nosso número era {aleatorio} e você escolheu {num}. Mais sorte na próxima vez!!\n')
else:
    print(f'\nVocê não inseriu um valor válido!')
