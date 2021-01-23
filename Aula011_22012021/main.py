import funcoes
from src import employee as em

soma = funcoes.soma(2,3)
print(soma)

empregado = em.Employee('cinthya', 235234)

print(f'nome = {empregado.name}')