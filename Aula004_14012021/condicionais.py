'''
- if
- elif
- nested if
'''

var = 1000
if ( var == 100 ) : print ("Value of expression is 100") 
print ("Good bye!" )

nome = 'Cinthya'
if nome == 'Cinthya':
    print(f'Olá, meu nome é {nome}')
else:
    print('Digaêêê')

##################################################
## elif

nome = "Jeff" 
pessoa = "Aluno" 
ispessoa = True 

if pessoa == "Aluno" and ispessoa == True: 
    print(f"Olá {nome}!") 
elif pessoa == "Professor": 
    print("Olá Professor") 
elif pessoa == "Aprendiz": 
    print("Olá Aprendiz")

##################################################
## Nested if

nome = "Jeff" 
pessoa = "Professor" 
ispessoa = True 

if pessoa == "Aluno": 
    print("É aluno") 
    if ispessoa == True: 
        print(f"Olá {nome}!") 
    else: print("Olá Alguém!") 
elif pessoa == "Professor": 
    print("É professor") 
    if ispessoa: print(f"Olá {nome}!") 
    else: print("Olá Alguém!") 
elif pessoa == "Aprendiz": print("Olá Aprendiz")

##################################################
## Condicional com número

num = int(input('Escolha um número: '))

if num > 0 and num < 3:
    print(f'O número {num} está entre 0 e 3')
elif num > 3 and num < 6:
    print(f'O número {num} está entre 4 e 6')
elif num > 5 and num < 10:
    print(f'O número {num} está entre 6 e 9')
else:
    print(f'O número {num} não está entre 0 e 9')

