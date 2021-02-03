from contato import Contato
# https://docs.python.org/3/tutorial/classes.html

class Funcoes:    

    def add_contato (agenda_dict):
        # entrada dos dados
        nome = input('\nInsira o nome do novo contato: ')
        tel = input('Insira o telefone do novo contato: ')
        endereco = input('Insira o endereco do novo contato: ')

        # inserção dos dados no dicionário e instaciação de um obj Contato
        contato = Contato(nome, tel, endereco)
        agenda_dict.append(contato)

        # confirma inserção e imprimi a lista dos contatos
        print('\nContato adicionado. Verifique abaixo.\n')
        Funcoes.listar_agenda (agenda_dict)

        return agenda_dict


    # função que lista os elementos do dicionário
    def listar_agenda (agenda_dict):
        if (len(agenda_dict) == 0):
            print('\nA agenda está vazia!\n')
        else:
            index = 0
            for item in agenda_dict:
                print(index, item.nome, item.telefone, item.endereco)
                index += 1
                

    # função que exclui um elemento dado um item.
    # o dicionário é exibido antes e depois da execução
    def excluir_contato(agenda_dict):
        while True:
            print(f'\nA agenda é:\n')
            Funcoes.listar_agenda (agenda_dict)    
            
            indice = int(input('\nDigite o número do contato que deseja excluir:\n'))
            
            if (len(agenda_dict) == 0):
                print('\nA agenda está vazia. Insira algum contato!\n')
                break
            elif (indice in range(len(agenda_dict))):
                print(f'\nContato excluído!\n')
                del agenda_dict[indice]
                print('\nA agenda agora é:\n')
                Funcoes.listar_agenda (agenda_dict)
                break
            else:
                print('\nEste contato não está na lista.\n')