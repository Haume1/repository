import datetime
import math

print("Ціле число: ")
a = float(input())
s = (a*(a + 1))/2


print ("Сума: ",s)


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Хоменко Андірй"

printTimeStamp(name)

