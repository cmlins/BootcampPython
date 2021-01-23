class JustCounter: 
    __secretCount = 0 
    
    def count(self): 
        self.__secretCount += 1 
        print(self.__secretCount) 


counter = JustCounter() #instanciando o objeto 
counter.count() #incrementando o contador 
counter.count() #incrementando o contador 
# counter._JustCounter__secretCount = 5 #<==Acessando a variável de outra forma 
counter.__secretCount = 5
print(counter._JustCounter__secretCount) #Mostrando na tela


# output:
# 1
# 2
# 2