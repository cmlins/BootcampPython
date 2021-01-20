# 9. Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.
import math

print('--- Exercício 9 ---\n')

# função que calcula a área de um círculo
def area(r):
    return round(math.pi * math.pow(r,r), 2)

# função que calcula o perímetro de um círculo
def perimetro(r):
    return round(2 * (math.pi) * r)
    
print(f'A área do círculo de raio = 3 é: {area(3)}')
print(f'A área do círculo de raio = 3 é: {perimetro(3)}')
