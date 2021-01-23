def calculo_preco(valor, **kwargs):
    imposto = kwargs.get('imposto')
    desconto = kwargs.get('desconto')
    if imposto:
        valor += valor * (imposto / 100)
    if desconto:
        valor -= desconto

    return valor

print(f'somente o valor = {calculo_preco(100)}')
print(f'desconto = {calculo_preco(100.00, desconto=2)}')
print(f'imposto = {calculo_preco(100.00, imposto=2)}')
print(f'desconto + imposto = {calculo_preco(100.00, desconto=2, imposto=5)}')