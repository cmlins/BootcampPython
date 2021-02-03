import os
os.system('cls||clear')

money = 2000

def addMoney():
    global money
    money += 1

print(money)
addMoney()
print(money)

# dir()
import time

print(f'dir(time): {dir(time)}')