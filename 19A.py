import datetime
import time

print(time.asctime(), "\n")

def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Хоменко Андірй"

printTimeStamp(name)

