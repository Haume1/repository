import datetime
import math
s = float(input("Довжина сторони: "))
n = float(input("Кількість сторiн: "))
с = n*s**2
h = float(math.pi/n)
s = 4 * math.tan(h)

print ("Площа: ",s ,"см^2")


def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Хоменко Андірй"

printTimeStamp(name)
