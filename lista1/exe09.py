# 9. Elabore um algoritmo em Python que calcule a área e o perímetro de um círculo, sabendo que A = πr² e P=2πr.
import math

print('--- Exercício 9 ---\n')

def area(r):
    return round(math.pi * math.pow(r,r), 2)

def perimetro(r):
    return round(2 * (math.pi) * r)
    
print(f'A área do círculo de raio = 3 é: {area(3)}')
print(f'A área do círculo de raio = 3 é: {perimetro(3)}')
