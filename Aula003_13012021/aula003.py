'''
variável:
- espaço ocupado em memória
- tem um tipo

String slice
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

# multiplas definições
a = b = c = 1
x,y,z = 1,2,'john'

print("a:{} - b:{} - c:{} - x:{} - y:{} - z:{}".format(a,b,c,x,y,z))

# string

str = 'Hello World!' 

print(str) # Prints complete string 
print(str[0]) # Prints first character of the string 
print(str[2:5]) # Prints characters starting from 3rd to 5th 
print(str[2:]) # Prints string starting from 3rd character 
print(str * 2) # Prints string two times 
print(str + "TEST") # Prints concatenated string 
