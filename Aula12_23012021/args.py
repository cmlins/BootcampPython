def titulos (pais, *anos):
    print(f'pais: {pais}')

    for ano in anos:
        print(f'ano: {ano}')

titulos('Brasil', '1958', '1962', '1970', '1994', '2002')

# def titulos (*paises, *anos):

#     for pais in paises:
#         print(f'pais: {pais}')

#     for ano in anos:
#         print(f'ano: {ano}')


# output:
# país: Brasil
# ano: 1958
# ano: 1962
# ano: 1970
# ano: 1994
# ano: 2002