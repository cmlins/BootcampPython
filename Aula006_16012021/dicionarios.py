'''
- conjunto de chave:valor limitada com {}
- chaves são imutáveis
'''

dict1 = {   1 : 'Fabio',
            2 : 'Maria', 
            3 : 'João', 
            4 : 'José'}
print(dict1)

dict2 = {  1 : 'Pedro', 
            2 : 'Tiago', 
            3 : 'João', 
            4 : 'Galiléia'}
print(type(dict2))


# acessando valores
print(f'dict1[1]: {dict1[1]} \n')

# atualizando dicionário
dict1[5] = "Isabel"
print(f'dict1[5]: {dict1[5]} \n')

# modificar valor em dicionários
dict1[2] = 'Bia'
print(f'dict1[2]: {dict1[2]} \n')

# del() e copy() 
dict1copy = dict1.copy()

del dict1copy[1] #remove chave 1 do dict1

dict1copy.clear() #remove as entradas do dict1

del dict1copy #exclui dict1

# len()
print(f'len dict1: {len(dict1)} \n')

# str() converte para string
print(f'str dict1: {str(dict1)} \n')

# type()
print(f'tipo de dado dict1: {type(dict1)} \n')

# fromkeys() --> cria um dicionário só com chaves
dict_chaves = dict.fromkeys(dict1)
print(f'dict_chaves: {(dict_chaves)} \n')

# get()
print(f'get() dict1: {dict1.get(1)} \n')

# items()
print(f'items() dict1: {dict1.items()} \n')

# values()
print(f'values() dict1: {dict1.values()} \n')



