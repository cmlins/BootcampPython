# 16. Fazer um sistema de Agenda de contatos (Deve 
# criar um dicionário com nome, telefone e endereco, 
# Imprimir os dados do dicionário, ser 
# capaz de inserir e excluir um contato)
print('--- Exercício 16 ---\n')

def add_contato (agenda_dict):
    nome = input('Insira o nome do novo contato: ')
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
    indice = int(input('Digite o número do contato que deseja excluir:\n'))
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

print("""Olá! Esta é sua agenda. Digite o que você opção que você gostaria de fazer:

1 - Listar sua agenda
2 - Inserir novo contato
3 - Excluir um contato
4 - Encerrar a sessão
""")

opcao = int(input())

while (opcao != 4):
    if (opcao == 1):
        listar_agenda (agenda)
    elif (opcao == 2):
        add_contato (agenda)
    elif (opcao == 3):    
        excluir_contato(agenda)
    elif (opcao not in (1,2,3,4)):
        print('Você não escolheu uma opção válida!')
else:
    print('Até a próxima!')




# # acessando valores
# print(f'dict1[1]: {dict1[1]} \n')

# # atualizando dicionário
# dict1[5] = "Isabel"
# print(f'dict1[5]: {dict1[5]} \n')

# # del() e copy() 
# dict1copy = dict1.copy()

# del dict1copy[1] #remove chave 1 do dict1

# dict1copy.clear() #remove as entradas do dict1

# del dict1copy #exclui dict1