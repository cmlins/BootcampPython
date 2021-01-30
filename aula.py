import os
clear = lambda: os.system('clear')
clear()

# Função é um pedaço de função que pode ser reutilizado
def soma(a, b):
    return print(a + b)

soma(3,4)

# Function definition is here 
def changeme( mylist ): 
    "This changes a passed list into this function" 
    mylist.append([1,2,3,4]) 
    print("Values inside the function: ", mylist) 
    
# Now you can call changeme function
minha_lista = [10,20,30] 
changeme( mylist=minha_lista ) 
print("Values outside the function: ", minha_lista)

# Function definition is here 
def changeme( mylist ): 
    "This changes a passed list into this function" 
    mylist = ([1,2,3,4]) 
    print("Values inside the function: ", mylist)
    return
    
# Now you can call changeme function
minha_lista = [10,20,30] 
changeme( mylist = minha_lista ) 
print("Values outside the function: ", minha_lista) 

# Funções anonimas --> lambda
soma = lambda x, y: x + y

print(soma(2,3))


