var1 = 'Hello world!'
var2 = 'Python Programming!'

print(f'var1[0]: {var1[0]}')
print(f'var2[1:5]: {var2[1:5]}')

print(f'Update string: {var1[:6]}Python \n Goodbye Python')
print('\n')
print(f'Update string: {var1[:6]}Python \110\151 Goodbye Python')

print(var1 * 2)
print(var1 + var2)

letra = input(f"A string é {var1}... Digite uma letra para busca...") 
if len(letra) ==1: 
    if letra in var1: 
        print(f"A letra {letra} existe") 
    else: print(f"A letra {letra} não existe") 
elif len(letra) > 1: print("Você digitou mais que um caractere. A busca será cancelada!") 
else: print("Você não digitou uma letra!") 

var = "hello python" 
letra = input(f"A string é {var}... Digite uma letra para busca...") 
if len(letra) ==1: 
    if letra in var: 
        print(f"A letra {letra} existe") 
    elif letra.isdigit():
        print(f"Você digitou um número, não uma letra!") 
    elif not letra.isprintable():
        print(f"Você alguma coisa, não uma letra!") 
    else: print(f"A letra {letra} não existe") 
elif len(letra) > 1: 
    print("Você digitou mais que um caractere. A busca será cancelada!") 
else: print("Você não digitou uma letra!") 