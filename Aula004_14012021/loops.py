'''
- while loop
- for loop
- nested loop

controle de loops:
- break --> termina o loop
- continue --> pula se der erro no loop
- pass --> 
'''
##################################################
## while loop
nome = 'Cinthya'
isPessoa = True
count = 0

while isPessoa:
    print(f'Meu nome é {nome}')
    isPessoa = False

while count <= 10:
    print(f'{count} - Meu nome é {nome}')
    count += 1

print('##################################################')

print('Começo do programa com break')

count = 0

while count <= 10:
    count += 1
    if count == 4:
        break
    print(f'{count} - Meu nome é {nome}')

print('Fim do programa')

print('##################################################')

print('Começo do programa com continue')

count = 0

while count <= 10:
    count += 1
    if count == 4:
        continue
    print(f'{count} - Meu nome é {nome}')

print('Fim do programa')

print('##################################################')
## for loop

frutas = ['banana', 'maçã', 'limão']

for fruta in frutas:
    print(f'A fruta do dia é {fruta}')

print('##################################################')
## for loop

i = 0
tam = len(frutas) - 1

while i <= tam:
    print(f'A fruta do dia é {frutas[i]}')
    i += 1

print('##################################################')

print('Começo do programa for com continue')

count = 0

for fruta in frutas:    
    if fruta == 'maçã':
        continue
    print(f'A fruta do dia é {fruta}')

print('Fim do programa')

print('##################################################')

print('Começo do programa for com break')

count = 0

for fruta in frutas:
    if fruta == 'maçã':
        break
    print(f'A fruta do dia é {fruta}')

print('Fim do programa')

print('##################################################')
# for com range

print('Começo do programa for com range')

for fruta in range(len(frutas)):
    if fruta == 'maçã':
        break
    print(f'A fruta do dia é {fruta}')

print('Fim do programa')

#Começa do 0 e vai até o 10 
for numero in range(11): 
    print(f"Número {numero}")

print('##################################################')

#Começa do 4 e faz até 10 
for numero in range(4, 11): 
    print(f"Número {numero}")

print('##################################################')

matriz_bidim = [['a','b','c'],
                ['d','e','f'],
                ['g','h','i']]

for it1 in matriz_bidim:
    for it2 in it1:
        print(f'O item é: {it2}')




