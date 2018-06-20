import datetime

def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
printTimeStamp('Прокопчук Б. Ю.')

a = input('Вихідний (ТАК/НІ)? ')
b = input('Відпустка (ТАК/НІ)? ')

if a == 'ТАК' or b == 'ТАК':
    print('Не вмикати.')
else:
    print('Вмикати.')

import datetime

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Хоменко Андірй"

printTimeStamp(name)