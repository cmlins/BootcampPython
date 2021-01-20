# 7. Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto aleatório de número (de 0 a 100) e dizer se o usuário advinhou)
import random

print('--- Exercício 7 ---\n')

nome = input('Olá, jogadore!! Digite seu nome: ')

num = int(input('Agora, digite um número inteiro entre 0 e 100 e vamos tentar adivinhá-lo: '))

aleatorio = random.randint(0,100)

if (num >= 0 and num <= 100):
    if (num == aleatorio):
        print(f'Parabéns!!! Você adivinhou o número que escolhemos. Será que {num} é seu número da sorte?')
    else:
        print(f'Não foi dessa vez! Nosso número era {aleatorio} e você escolheu {num}. Mais sorte na próxima vez!!')
else:
    print(f'Você não inseriu um valor válido!')
