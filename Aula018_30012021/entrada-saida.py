import os
os.system('cls||clear')

fo = open("colon.txt", "wb")

print(f"fo nome: {fo.name}")

print(f"fo nome: {fo.close}")

fo.close

# escrever um txt
import codecs

frutas = ['banana', 'limão', 'cereja']

fa = codecs.open('./Aula017_30012021/frutas.txt', 'w', 'utf-8')

for fruta in frutas:
    fa.write(f'{fruta}\n')

fa.close

# ler um txt
colon = open('./Aula017_30012021/colon.txt', 'r+')
# print(colon.read().splitlines())
with open("./Aula017_30012021/colon.txt", "r") as fd:
    lines = fd.read().splitlines()

for i in (range(10)):
    print(lines[i])

os.chdir('././Aula015_28012021')
