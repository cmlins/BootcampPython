import time

# ticks => segundos passados desde 00:00:00 de 1 janeiro de 1970
# epoch só vê passado

ticks = time.time()
print(f'ticks: {ticks}\n')

# timeTuple => tuplas de 9 números
# data e hora atual:

localtime = time.localtime(time.time())
print(f'localtime: {localtime}\n')
print(f'mês: {localtime[1]}\n')

# formatando data e hora
localtime = time.asctime(time.localtime(time.time()))
print(f'localtime asctime: {localtime}\n')

# obtendo um calendário
import calendar

cal = calendar.month(1983, 8)
print(f'calendário: {cal}')

# thread

