# 14. Fazer um sistema de biblioteca (Deve 
# imprimir uma lista com 10 livros, 
# pedir o nome do solicitante do empréstimo, 
# pedir para selecionar um livro e 
# imprimir o livro selecionado)

livros = {
    1 : " Iluminadas por Lauren Beukes",
    2 : " Comer, rezar, amar por Elizabeth Gilbert",
    3 : " Outros Jeitos de Usar a Boca por Rupi Kaur", 
    4 : " Meu corpo minha casa  por Rupi Kaur",
    5 : " Tudo nela brilha e queima por Ryane Leão",
    6 : " Pequeno manual antirracista por Djamila Ribeiro",
    7 : " Sejamos todos feministas por Chimamanda Ngozi Adichie",
    8 : " Labirinto por Kate Mosse",
    9 : " Cracking the coding interview por Gayle Laakmann McDowell",
    10 : " O momento de voar por Melinda Gates"
}

print("Os livros disponíveis são:\n")

for opcao in livros:
    print(f'{opcao} - {livros[opcao]}')

nome = input("\nInsira seu nome: ")

livro = int(input("Digite o número do livro que escolheu: "))

# print(f"{nome}, você escolheu o livro{livros[livro]}!")
# print(range(len(livros)))

if (livro in range(len(livros) + 1)):
    print(f"{nome}, você escolheu o livro{livros[livro]}!")
else: 
    print("Você não escolheu uma opção válida")