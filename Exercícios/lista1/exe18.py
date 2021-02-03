# 18. Fazer um sistema de compras (
# Deve mostrar um dicionário com os objetos (Nome, Preço e Cor), 
# pedir o nome do usuário e 
# fazer com o que o usuário selecione um objeto e 
# imprimir a compra na tela)
print('--- Exercício 18 ---\n')

# função para inserir elementos
def add_item (lista_compra):
    # entrada dos dados
    item_nome = input('\nInsira o nome do item: ')
    item_preco = input('Insira o preço do item: ')
    item_cor = input('Insira cor do item: ')
    
    # inserção dos itens na lista de compras
    item = {
            "nome" : item_nome, 
            "preco" : item_preco, 
            "cor" : item_cor
            }
    lista_compra.append(item)

    # exibe uma mensagem com confirmação da inserção e e imprime a lista de compras
    print('\nItem adicionado. Verifique a lista de compras abaixo.\n')
    listar_itens (lista_compra)

    return lista_compra

# função que lista os elementos do dicionário
def listar_itens (lista_compra):
    index = 0
    for item in lista_compra:
        print(index, item)
        index += 1

# função que exclui um elemento dado um item.
# o dicionário é exibido antes e depois da execução
def excluir_item (lista_compra):
    while True:
        listar_itens (lista_compra)    
        
        indice = int(input('\nDigite o número do item que deseja excluir:\n'))
        
        if (len(lista_compra) == 0):
            print('A lista está vazia. Insira algum item!')
            break
        elif (indice in range(len(lista_compra))):
            print(f'O item {lista_compra[indice]} vai ser excluído!\n')
            del lista_compra[indice]
            print('A lista está de itens agora é:\n')
            listar_itens (lista_compra)
            break
        else:
            print('Este item não está na lista.')
            

# inicializa uma lista de agendamentos
lista = []

# loop que executa as tarefas da lista de compras
while True:
    
    print("""\nOlá! Esta é sua lista de compras. Digite o que você gostaria de fazer:

1 - Listar itens da lista   
2 - Inserir novo item na lista
3 - Excluir um item da lista
4 - Encerrar a sessão
""")

    opcao = int(input())

    if (opcao == 1):
        listar_itens (lista)
    elif (opcao == 2):
        add_item (lista)
    elif (opcao == 3):    
        excluir_item (lista)
    elif (opcao == 4):
        print ("\nAté a próxima!")
        break
    else:
        print('\nVocê não escolheu uma opção válida!')