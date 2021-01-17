import math
import random

# 1. Algoritmo para ligar um carro (Imprimir a sequência para ligar um carro)
passo1 = 'passo 1 - Pegar a chave'
passo2 = 'passo 2 - Desligar o alarme no controle'
passo3 = 'passo 3 - Inserir a chave na porta'
passo4 = 'passo 4 - Girar a chave e destravar o carro'
passo5 = 'passo 5 - Retirar a chave da porta'
passo6 = 'passo 6 - Sentar no carro'
passo7 = 'passo 7 - Inserir a chave na ignição'
passo8 = 'passo 8 - Pisar na embreagem e colocar o carro em ponto morto'
passo9 = 'passo 9 - Girar a chave na ignição e ligar o carro'

passos = [passo1, passo2, passo3, passo4,passo5, passo6, passo7, passo8, passo9]

for passo in passos:
    print(passo)

print('\n')

# 2. Algoritmo para ir ao banco para sacar dinheiro (Imprimir a sequência para ir ao banco e sacar dinheiro)
passo1 = 'passo 1 - Pegar a chave'
passo2 = 'passo 2 - Desligar o alarme no controle'
passo3 = 'passo 3 - Inserir a chave na porta'
passo4 = 'passo 4 - Girar a chave e destravar o carro'
passo5 = 'passo 5 - Retirar a chave da porta'
passo6 = 'passo 6 - Sentar no carro'
passo7 = 'passo 7 - Inserir a chave na ignição'
passo8 = 'passo 8 - Pisar na embreagem e colocar o carro em ponto morto'
passo9 = 'passo 9 - Girar a chave na ignição e ligar o carro'

passos = [passo1, passo2, passo3, passo4,passo5, passo6, passo7, passo8, passo9]

for passo in passos:
    print(passo)

print('\n')    

# 3. Algoritmo para trocar o pneu do carro (Imprimir a sequência para trocar o pneu do carro)
passo1 = 'passo 1 - Pegar a chave'
passo2 = 'passo 2 - Desligar o alarme no controle'
passo3 = 'passo 3 - Inserir a chave na porta'
passo4 = 'passo 4 - Girar a chave e destravar o carro'
passo5 = 'passo 5 - Retirar a chave da porta'
passo6 = 'passo 6 - Sentar no carro'
passo7 = 'passo 7 - Inserir a chave na ignição'
passo8 = 'passo 8 - Pisar na embreagem e colocar o carro em ponto morto'
passo9 = 'passo 9 - Girar a chave na ignição e ligar o carro'

passos = [passo1, passo2, passo3, passo4,passo5, passo6, passo7, passo8, passo9]

for passo in passos:
    print(passo)

print('\n')

# 4. Elabore um algoritmo em Python que leia, calcule e escreva a média aritmética entre quatro números;
def media (x, y, z, t):
    return (x + y + z + t) / 4

num1 = int(input('Insira um número: '))
num2 = int(input('Insira um número: '))
num3 = int(input('Insira um número: '))
num4 = int(input('Insira um número: '))

print(f'A média aritmética de {num1}, {num2}, {num3} e {num4} é: {media(num1, num2, num3, num4)}')

print('\n')

# 5. Algoritmo para calcular a média do aluno (Deve colocar o nome do aluno, colocar 4 notas e imprimir sua média)
nome = input("Insira o nome do aluno: ")
num1 = int(input('Insira a primeira nota: '))
num2 = int(input('Insira a segunda nota: '))
num3 = int(input('Insira a terceira nota: '))
num4 = int(input('Insira a quarta nota: '))

print(f'A média do aluno {nome} é: {media(num1, num2, num3, num4)}')

print('\n')

# 6. Algoritmo para criar uma lista usando range com 100 elementos e imprimi-la

lista = [i for i in range(100)]

print(lista)

print('\n')

# 7. Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto aleatório de número (de 0 a 100) e dizer se o usuário advinhou)

nome = input('Olá, jogadore!! Digite seu nome: ')

num = int(input('Agora, digite um número entre 0 e 100 e vamos tentar adivinhá-lo: '))

aleatorio = random.randint(0,100)

if (num >= 0 and num <= 100):
    if (num == aleatorio):
        print(f'Parabéns!!! Você adivinhou o número que escolhemos. Será que {num} é seu número da sorte?')
    else:
        print(f'Não foi dessa vez! Nosso número era {aleatorio} e você escolheu {num}. Mais sorte na próxima vez!!')
else:
    print(f'Você não inseriu um valor válido!')

print('\n')

# 8. Elabore um algoritmo em Python que receba um número inteiro e escreva na tela o número fornecido, o antecessor desse número e o sucessor desse número;

# 9. Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.

def area(r):
    return round(math.pi * math.pow(r,r), 2)

def perimetro(r):
    return round(2 * (math.pi) * r)
    
print(f'A área do círculo de raio = 3 é: {area(3)}')
print(f'A área do círculo de raio = 3 é: {perimetro(3)}')

print('\n')

# 10. Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca) retornando o índice do elemento

# 11. Fazer uma busca sequencial em uma matriz (Criar uma matriz 10 linhas e 10 colunas e pedir para o usuário fazer uma busca)

# 12. Elabore um algoritmo em Python que:
# a) Primeiro exiba uma mensagem de boas vindas;
# b) Pergunte o nome do usuário;
# c) Exiba uma mensagem dizendo uma mensagem de olá seguida pelo nome do usuário seguida por outra mensagem fazendo um elogio.

print('Olá! Bem vinde ao Elogiator!')

nome = input('Insira seu nome: ')

elogios = ['espetacular', 'incrível', 'inteligente', 'sagaz', '']

print(f'Olá, {nome}!! Você é {random.choice(elogios)}!!!')

print('\n')

# 13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada)

# 14. Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)

# 15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)

# 16. Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)

# 17. Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, nome do proprietário, data e hora da revisão. Depois deve guardar os dados em um dicionário e mostrar a lista de dicionários (agendamentos) na tela)

# 18. Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), pedir o nome do usuário e fazer com o que o usuário selecione um objeto e imprimir a compra na tela)