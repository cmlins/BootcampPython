'''
- Guarda múltiplos valores
- inicia do índice zero
- itens separados por ',' e entre colchetes
- itens não precisam ser do mesmo tipo
'''

frutas = ['banana','maçã','uva','limão']
nums = [1,2,3,4,5,6,7]

print(frutas[3])
print(nums[2:5])

# alterar valor de um elemento da lista
frutas[2] = 'mamão'
print(frutas)

# add item no fim da lista
frutas.append('carambola')
print(frutas)

# remover item com del
del frutas[0]
print(frutas)

# remove()
frutas.remove('carambola')
print(frutas)

# add item com insert(posição,valor)
frutas.insert(2, 'carambola')
print(frutas)

# Operação +
num = nums + frutas
print(num)

# Operação *
num = nums * 2
print(num)

# pegar elementos comuns entre duas listas
l1 = [1,2,3,4,5,6]
l2 = [2,4,6,8,10,12]
## 1 - for
for one in l1:
    for two in l2:
        if one == two:
            print(one)
        
## 2 - set
print(set(l1) & set(l2))

## 3 - list comprehension
print([i for (i,j) in zip(l1,l2) if i == j])

# max() min()
print(f'max nums: {max(nums)}')
print(f'max frutas: {max(frutas)}')

print(f'min nums: {min(nums)}')
print(f'min frutas: {min(frutas)}')

# count()
print(frutas.count('maçã'))

# extend()
l1.extend(l2)
print(l1)

# len()
print(f'len de l1: {len(l1)}')

# pop()
l1.pop()
print(f'pop de l1: {l1}')

l1.pop(3)
print(f'pop de l1: {l1}')