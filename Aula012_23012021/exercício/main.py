from funcoes import Funcoes

agenda = []

while True:

    print("""\nOlá! Esta é sua agenda. Digite o que você opção que você gostaria de fazer:

1 - Listar sua agenda
2 - Inserir novo contato
3 - Excluir um contato
4 - Encerrar a sessão
""")

    opcao = int(input())

    if (opcao == 1):
        Funcoes.listar_agenda (agenda)
    elif (opcao == 2):
        Funcoes.add_contato (agenda)
    elif (opcao == 3):    
        Funcoes.excluir_contato(agenda)
    elif (opcao == 4):
        print ("\nAté a próxima!")
        break
    else:
        print('\nVocê não escolheu uma opção válida!')