class Fruta:

    def __init__(self) -> None:
        pass

    frutas = {
    1 : "Pera",
    2 : "Uva",
    3 : "Maçã", 
    4 : "Melão",
    5 : "Mamão",
    6 : "Banana",
    7 : "Carambola",
    8 : "Melancia",
    9 : "Ameixa",
    10 : "Caju"
    }

    def display_frutas(self):
        print("\nAs frutas disponíveis são:\n")
        index = 1
        for self.fruta in self.frutas:
            print (index, self.frutas.get(self.fruta))
            index += 1

    
    def display_fruta_escolhido(self, escolha):
        return self.frutas.get(escolha)
