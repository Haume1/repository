import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Хоменко Андірй"

printTimeStamp(name)

import math

r = float(input('Введіть радіус:'))
s = math.pi*(r**2)
print ('Площа кругу', s)
v = (4*math.pi*(r**3))/3
print ("Об`єм кулі", v)
