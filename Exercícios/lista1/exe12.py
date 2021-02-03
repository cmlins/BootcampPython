# 12. Elabore um algoritmo em Python que:
# a) Primeiro exiba uma mensagem de boas vindas;
# b) Pergunte o nome do usuário;
# c) Exiba uma mensagem dizendo uma mensagem de olá seguida pelo nome do usuário seguida por outra mensagem fazendo um elogio.
import random

print('--- Exercício 12 ---\n')

print('Olá! Bem vinde ao Elogiator!')

nome = input('Insira seu nome: ')

# lista de exercícios
elogios = ['espetacular', 'incrível', 'inteligente', 'sagaz', 'uma perfeição']

# random.choice() retorna um valor aleatório em uma lista
print(f'Olá, {nome}!! Você é {random.choice(elogios)}!!!')
