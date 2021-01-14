'''
variável:
- espaço ocupado em memória
- tem um tipo

String slice
multiplas definições
interpolação de string
listas
tuplas
dicionários
'''

counter = 100 # An integer assignment 
miles = 1000.0 # A floating point 
name = "John" # A string print(counter) 

print(name)
print(miles) 
print(name)
print(type(name))
print(type(miles))
print(type(name))

print('#########################################################################################')
# multiplas definições
a = b = c = 1
x,y,z = 1,2,'john'

print("a:{} - b:{} - c:{} - x:{} - y:{} - z:{}".format(a,b,c,x,y,z))

print('#########################################################################################')
# string

str = 'Hello World! ' 

print(str) # Prints complete string 
print(str[0]) # Prints first character of the string 
print(str[2:5]) # Prints characters starting from 3rd to 5th 
print(str[2:]) # Prints string starting from 3rd character 
print(str * 2) # Prints string two times 
print(str + " TEST") # Prints concatenated string

print('#########################################################################################')
# interpolação de string
nome = 'Cinthya'
sobrenome = 'Lins'
nome_completo = f'Meu nome completo é {nome} {sobrenome}'
print(nome_completo)

print('#########################################################################################')
# listas
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ] 
tinylist = [123, 'john'] 

print(list) # Prints complete list 
print(list[0]) # Prints first element of the list 
print(list[1:3]) # Prints elements starting from 2nd till 3rd 
print(list[2:]) # Prints elements starting from 3rd element 
print(tinylist * 2) # Prints list two times 
print(list + tinylist) # Prints concatenated lists 

print('#########################################################################################')
# tuplas --> não podem ser alteradas
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 ) 
tinytuple = (123, 'john') 

print(tuple) # Prints the complete tuple 
print(tuple[0]) # Prints first element of the tuple 
print(tuple[1:3]) # Prints elements of the tuple starting from 2nd till 3rd 
print(tuple[2:]) # Prints elements of the tuple starting from 3rd element 
print(tinytuple * 2) # Prints the contents of the tuple twice 
print(tuple + tinytuple) # Prints concatenated tuples 

print('#########################################################################################')
# dicionários
dict = {} 
dict['one'] = "This is one" 
dict[2] = "This is two" 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'} 

print(dict['one']) # Prints value for 'one' key 
print(dict[2]) # Prints value for 2 key 
print(tinydict) # Prints complete dictionary 
print(tinydict.keys()) # Prints all the keys 
print(tinydict.values()) # Prints all the values 