import random

print('Olá! Bem vinde ao Elogiator!')

nome = input('Insira seu nome: ')

elogios = ['espetacular', 'incrível', 'inteligente', 'sagaz', '']

print(f'Olá, {nome}!! Você é {random.choice(elogios)}')