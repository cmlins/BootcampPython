import math
import random

# 1. Algoritmo para ligar um carro (Imprimir a sequência para ligar um carro)
print('--- Exercício 1 ---\n')

print('Como ligar um carro: \n')

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
print('--- Exercício 2 ---\n')

print('Como sacar dinheiro: \n')

passo1 = 'passo 1 - Pegar o cartão;'
passo2 = 'passo 2 - Inserir o cartão no caixa eletrônico;'
passo3 = 'passo 3 - Digitar a senha;'
passo4 = 'passo 4 - EScolher a opção de saque no menu;'
passo5 = 'passo 5 - Digitar ou escolher o valor a ser sacado e apertar o valor para confirmar o valor;'
passo6 = 'passo 6 - Se não tiver saldo suficiente em conta, o saque não será possível e a operação termina. Caso contrário, a operação segue para o próximo passo;'
passo7 = 'passo 7 - Digitar a senha para sacar o dinheiro;'
passo8 = 'passo 8 - Esperar a contagem das notas pela máquina;'
passo9 = 'passo 9 - Retirar o dinheiro da máquina e encerrar a sessão.'

passos = [passo1, passo2, passo3, passo4,passo5, passo6, passo7, passo8, passo9]

for passo in passos:
    print(passo)

print('\n')    

# 3. Algoritmo para trocar o pneu do carro (Imprimir a sequência para trocar o pneu do carro)
print('--- Exercício 3 ---\n')

print('Como trocar o pneu do carro: \n')

passo1 = 'passo 1 - Encostar o carro;'
passo2 = 'passo 2 - Abrir o porta malas;'
passo3 = 'passo 3 - Pegar a chave de roda, o macaco e o estepe na mala do carro;'
passo4 = 'passo 4 - Pegar o macaco;'
passo5 = 'passo 5 - Pegar o estepe;'
passo6 = 'passo 6 - Com a chave de roda, afrouxar os parafusos do pneu a ser trocado;'
passo7 = 'passo 7 - Encaixar o macaco e levantar o carro para tirar o pneu a ser trocado;'
passo8 = 'passo 8 - Retirar os parafusos já afrouxados e tirar o pneu;'
passo9 = 'passo 9 - Encaixar o estepe no lugar do pneu danificado e colocar os parafusos;'
passo10 = 'passo 10 - Abaixar o carro;'
passo11 = 'passo 11 - Desencaixar o estepe;'
passo12 = 'passo 12 - Com a chave de roda, apertar os parafusos do pneu;'
passo13 = 'passo 13 - Guardar o pneu no lugar do estepe;'
passo14 = 'passo 14 - Guardar o macaco e a chave de roda;'
passo15 = 'passo 15 - Fechar o porta malas.'

passos = [passo1, passo2, passo3, passo4,passo5, passo6, passo7, passo8, passo9, passo10, passo11, passo12, passo13, passo14, passo15]

for passo in passos:
    print(passo)

print('\n')

# 4. Elabore um algoritmo em Python que leia, calcule e escreva a média aritmética entre quatro números;
print('--- Exercício 4 ---\n')

def media (x, y, z, t):
    return (x + y + z + t) / 4

num1 = int(input('Insira um número: '))
num2 = int(input('Insira um número: '))
num3 = int(input('Insira um número: '))
num4 = int(input('Insira um número: '))

print(f'A média aritmética de {num1}, {num2}, {num3} e {num4} é: {media(num1, num2, num3, num4)}')

print('\n')

# 5. Algoritmo para calcular a média do aluno (Deve colocar o nome do aluno, colocar 4 notas e imprimir sua média)
print('--- Exercício 5 ---\n')

nome = input("Insira o nome do aluno: ")
num1 = int(input('Insira a primeira nota: '))
num2 = int(input('Insira a segunda nota: '))
num3 = int(input('Insira a terceira nota: '))
num4 = int(input('Insira a quarta nota: '))

print(f'A média do aluno {nome} é: {media(num1, num2, num3, num4)}')

print('\n')

# 6. Algoritmo para criar uma lista usando range com 100 elementos e imprimi-la
print('--- Exercício 6 ---\n')

lista = [i for i in range(100)]

print(lista)

print('\n')

# 7. Fazer um sistema de Loteria (Deve pedir o nome do usuário, pedir um número e comparar com um conjunto aleatório de número (de 0 a 100) e dizer se o usuário advinhou)
print('--- Exercício 7 ---\n')

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
print('--- Exercício 8 ---\n')

num = int(input('Insira um número: '))

print(f'O número digitado foi {num}, seu antecessor é {num - 1} e seu sucessor é {num + 1}')

print('\n')

# 9. Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.
print('--- Exercício 9 ---\n')

def area(r):
    return round(math.pi * math.pow(r,r), 2)

def perimetro(r):
    return round(2 * (math.pi) * r)
    
print(f'A área do círculo de raio = 3 é: {area(3)}')
print(f'A área do círculo de raio = 3 é: {perimetro(3)}')

print('\n')

# 10. Fazer uma busca sequencial em uma lista (Criar uma tupla [0....20] e pedir para o usuário fazer uma busca) retornando o índice do elemento
print('--- Exercício 10 ---\n')

num = int(input('Insira um número entre 0 e 20, inclusive 0 e 20: '))

lista = [i for i in range(0,21)]

if (num in lista):
    indice = [i for i in range(len(lista)) if lista[i] == num]
    print(f'O número {num} está no índice {indice[0]} lista')
else:
    print('O número digitado não está na lista')

print('\n')

# 11. Fazer uma busca sequencial em uma matriz (Criar uma matriz 10 linhas e 10 colunas e pedir para o usuário fazer uma busca)
print('--- Exercício 11 ---\n')

num = int(input('Insira um número: '))

matriz = [list(range(i, i+10)) for i in range(1, 100, 10)]

print(matriz)

for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        if (num == matriz[linha][coluna]):
            print(f'O número {num} está na linha {linha} e na coluna {coluna}')

print('\n')

# 12. Elabore um algoritmo em Python que:
# a) Primeiro exiba uma mensagem de boas vindas;
# b) Pergunte o nome do usuário;
# c) Exiba uma mensagem dizendo uma mensagem de olá seguida pelo nome do usuário seguida por outra mensagem fazendo um elogio.
print('--- Exercício 12 ---\n')

print('Olá! Bem vinde ao Elogiator!')

nome = input('Insira seu nome: ')

elogios = ['espetacular', 'incrível', 'inteligente', 'sagaz', '']

print(f'Olá, {nome}!! Você é {random.choice(elogios)}!!!')

print('\n')

# 13. Fazer um cadastro de viagem (Deve pedir o nome do viajante, dar as opções de destino e imprimir a selecionada)
print('--- Exercício 1 3---\n')

# 14. Fazer um sistema de biblioteca (Deve imprimir uma lista com 10 livros, pedir o nome do solicitante do empréstimo, pedir para selecionar um livro e imprimir o livro selecionado)
print('--- Exercício 14 ---\n')

# 15. Fazer um sistema de Feira Livre(Deve imprimir uma lista com as frutas e pedir para o solicitante colocar o nome e selecionar a fruta e depois deve imprimir o nome do solicitante e a fruta)
print('--- Exercício 15 ---\n')

# 16. Fazer um sistema de Agenda de contatos (Deve criar um dicionário com Nome, Telefone e Endereço, Imprimir os dados do dicionário, ser capaz de inserir e excluir um contato)
print('--- Exercício 16 ---\n')

# 17. Fazer um sistema de Agenda de revisão do Carro (Deve pedir o nome do carro, ano e modelo, nome do proprietário, data e hora da revisão. Depois deve guardar os dados em um dicionário e mostrar a lista de dicionários (agendamentos) na tela)
print('--- Exercício 17 ---\n')

# 18. Fazer um sistema de compras (Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), pedir o nome do usuário e fazer com o que o usuário selecione um objeto e imprimir a compra na tela)
print('--- Exercício 18 ---\n')