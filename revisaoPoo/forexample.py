class Carro:
    def __init__(self, nome, modelo):
        self.nome = nome
        self.modelo = modelo

c1 = Carro("Ford", "KA")
c2 = Carro("VW", "Fox")
c3 = Carro("GM", "Celta")
c4 = Carro("BMW", "320i")

lista_carros = [c1, c2, c3, c4]

valor = input("selecione um número")
#validação para verificar se não é um número fora do Range
indice_selecionado = int(valor)

for carro in lista_carros:
    #Para comparar objetos, use os atributos (Nesse caso, nome)
    if carro.nome == lista_carros[indice_selecionado].nome:
        print(f"O carro {carro.nome} - {carro.modelo} está na posição {indice_selecionado}")
        break
 

