# 17. Fazer um sistema de Agenda de revisão do Carro
# Deve pedir o nome do carro, ano e modelo, nome do proprietário, data e hora da revisão. 
# Depois deve guardar os dados em um dicionário e mostrar a lista de dicionários (agendamentos) na tela)
print('--- Exercício 17 ---\n')

# função para inserir elementos
def add_agendamento (agendamentos):
    # entrada dos dados
    carro_nome = input('\nInsira o nome do carro: ')
    carro_ano = input('Insira o ano do carro: ')
    carro_modelo = input('Insira o modelo do carro: ')
    prop_nome = input('Insira o nome do proprietário: ')
    revisao_data = input('Insira data da revisão: ')
    revisao_hora = input('Insira a hora da revisão: ')

    # inserção dos dados na agenda de revisão
    dados = {"carro" : carro_nome, 
            "ano" : carro_ano, 
            "modelo" : carro_modelo, 
            "proprietario" : prop_nome, 
            "data" : revisao_data,
            "hora" : revisao_hora}
    agendamentos.append(dados)

    # exibe uma mensagem com confirmação da inserção e e imprime a lista de agendamentos
    print('\nAgendamento feito. Verifique abaixo.\n')
    listar_agendamento (agendamentos)

    return agendamentos

# função que lista os elementos do dicionário
def listar_agendamento (agendamentos):
    index = 0
    for contato in agendamentos:
        print(index, contato)
        index += 1


# função que exclui um elemento dado um item.
# o dicionário é exibido antes e depois da execução
def excluir_agendamento(agendamentos):
    while True:
        listar_agendamento (agendamentos)
        
        indice = int(input('\nDigite o número do agendamento que deseja excluir:\n'))
        
        if (len(agendamentos) == 0):
            print('A agenda está vazia. Insira algum agendamento!')
            break
        elif (indice in range(len(agendamentos))):
            print(f'\nO item {agendamentos[indice]} vai ser excluído!\n')
            del agendamentos[indice]
            print('\nA agenda agora está:\n')
            listar_agendamento (agendamentos)
            break
        else:
            print('\nEste agendamento não está na lista.\n')
        

# inicializa uma lista vazia de agendamentos
agenda = []

# loop que executa as tarefas do agendamento
while True:
    
    print("""\nOlá! Esta é uma agenda de revisão de carros. Digite o que você opção que você gostaria de fazer:

1 - Listar agendamentos
2 - Inserir novo agendamento
3 - Excluir um agendamento
4 - Encerrar a sessão
""")

    opcao = int(input())

    if (opcao == 1):
        listar_agendamento (agenda)
    elif (opcao == 2):
        add_agendamento (agenda)
    elif (opcao == 3):    
        excluir_agendamento (agenda)
    elif (opcao == 4):
        print ("\nAté a próxima!")
        break
    else:
        print('\nVocê não escolheu uma opção válida!')