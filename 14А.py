﻿import datetime
n = int(input("Введіть номер місяця(1-12): "))
if n ==0 or n > 12:
    print("0 днів")
elif n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    print("31 днів")
elif n == 4 or n == 6 or n == 9 or n == 11:
    print("30 днів")
elif n == 2:
    print("28 або 29 днів")

import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Хоменко Андірй"

printTimeStamp(name)

