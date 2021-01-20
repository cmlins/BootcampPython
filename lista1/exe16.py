# 16. Fazer um sistema de Agenda de contatos (Deve 
# criar um dicionário com nome, telefone e endereco, 
# Imprimir os dados do dicionário, ser 
# capaz de inserir e excluir um contato)
print('--- Exercício 16 ---\n')

def add_contato (agenda_dict):
    nome = input('\nInsira o nome do novo contato: ')
    tel = input('Insira o telefone do novo contato: ')
    endereco = input('Insira o endereco do novo contato: ')
    contato = {"nome" : nome, "telefone" : tel, "endereco" : endereco}
    agenda_dict.append(contato)
    print('\nContato adicionado. Verifique abaixo.\n')
    listar_agenda (agenda)

    return agenda_dict

def listar_agenda (agenda_dict):
    index = 0
    for contato in agenda_dict:
        print(index, contato)
        index += 1

def excluir_contato(agenda_dict):
    listar_agenda (agenda)
    indice = int(input('\nDigite o número do contato que deseja excluir:\n'))
    del agenda_dict[indice]

    return (listar_agenda (agenda))

agenda = [
    {
        "nome" : "Maria",
        "telefone" : "8155558787",
        "endereco" : "Rua dos Bobos, 0"
    },
    {
        "nome" : "José",
        "telefone" : "8155558987",
        "endereco" : "Rua dos Tolos, 1"
    },
    {
        "nome" : "João",
        "telefone" : "8155558789",
        "endereco" : "Rua dos Bobos, 6"
    }
]

while True:
    print("""\nOlá! Esta é sua agenda. Digite o que você opção que você gostaria de fazer:

1 - Listar sua agenda
2 - Inserir novo contato
3 - Excluir um contato
4 - Encerrar a sessão
""")

    opcao = int(input())

    if (opcao == 1):
        listar_agenda (agenda)
    elif (opcao == 2):
        add_contato (agenda)
    elif (opcao == 3):    
        excluir_contato(agenda)
    elif (opcao == 4):
        print ("\nAté a próxima!")
        break
    else:
        print('\nVocê não escolheu uma opção válida!')