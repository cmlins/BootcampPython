# 16. Fazer um sistema de Agenda de contatos (Deve 
# criar um dicionário com nome, telefone e endereco,  ok
# Imprimir os dados do dicionário, ok
# ser capaz de inserir e excluir um contato) ok
print('--- Exercício 16 ---\n')

# função para inserir elementos
def add_contato (agenda_dict):
    # entrada dos dados
    nome = input('\nInsira o nome do novo contato: ')
    tel = input('Insira o telefone do novo contato: ')
    endereco = input('Insira o endereco do novo contato: ')

    # inserção dos dados no dicionário
    contato = {"nome" : nome, "telefone" : tel, "endereco" : endereco}
    agenda_dict.append(contato)

    # confirma inserção e imprimi a lista dos contatos
    print('\nContato adicionado. Verifique abaixo.\n')
    listar_agenda (agenda_dict)

    return agenda_dict

# função que lista os elementos do dicionário
def listar_agenda (agenda_dict):
    index = 0
    for contato in agenda_dict:
        print(index, contato)
        index += 1

# função que exclui um elemento dado um item.
# o dicionário é exibido antes e depois da execução
def excluir_contato(agenda_dict):
    while True:
        listar_agenda (agenda_dict)    
        
        indice = int(input('\nDigite o número do contato que deseja excluir:\n'))
        
        if (len(agenda_dict) == 0):
            print('A agenda está vazia. Insira algum contato!')
            break
        elif (indice in range(len(agenda_dict))):
            print(f'O contato {agenda_dict[indice]} vai ser excluído!\n')
            del agenda_dict[indice]
            print('A agenda agora é:\n')
            listar_agenda (agenda_dict)
            break
        else:
            print('Este contato não está na lista.')

# lista com contatos
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

# loop que executa as tarefas da agenda
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