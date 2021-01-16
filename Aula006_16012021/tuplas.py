'''
- são imutáveis
- usa parenteses (não são necessários)
- pode inicializar tupla vazia: tupla = ()
- fazer tupla com um valor e vírgula tupla = (50,)
'''

tupla1 = ('física', 'quimica', 1997, 2000)
tupla2 = (1,2,3,4,5,6,7,8)
tupla3 = 1,2,3,4,5
tupla4 = ()

print(f'tupla3: {tupla3}')

print(f'tupla 4: {tupla4}')
tupla4 = (43,3)
print(f'tupla 4: {tupla4}')

### acessar valores em Tuplas
print(tupla1[2])

### operação +
tupla5 = tupla1 + tupla2
print(f'tupla5: {tupla5}')

### del()
del tupla5
# print(tupla5)

# del tupla3[1]

### len()
print(f'len tupla1: {len(tupla1)}')

### operação *
print(f'Operação * em tupla1: {tupla1 * 2}')

### atribuição
tup = x,y,z,k = 1,2,8,9
print(f'x: {x}, y: {y}')

print(type(tup))

# compare two tuples
import operator
print(operator.eq(set(tupla2), set(tupla3)))

print(set(tupla2) & set(tupla3))

# converter lista pra tupla
l1 = [1,2,3,4,5,6]
t1 = tuple(l1)
print(t1)