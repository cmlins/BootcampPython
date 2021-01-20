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
