class Destino:

    def __init__(self) -> None:
        pass

    destinos = {
    1 : "Paris",
    2 : "Londres",
    3 : "Bruxelas", 
    4 : "Amsterdam",
    5 : "Buenos Aires",
    6 : "Rio de Janeiro",
    7 : "Montreal",
    8 : "Maldivas",
    9 : "Tóquio",
    10 : "Pequim"
    }

    def display_destinos(self):
        print("\nOs destinos disponíveis são:\n")
        index = 1
        for self.destino in self.destinos:
            print (index, self.destinos.get(self.destino))
            index += 1

    
    def display_destino_escolhido(self, escolha):
        return self.destinos.get(escolha)
