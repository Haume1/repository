import datetime
print("""
       xxx
    xxxxxxxxx
  xxxxxxxxxxxxx
 xxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxx
 xxxxxxxxxxxxxxx
  xxxxxxxxxxxxx
    xxxxxxxxx
       xxx
""")
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = "Хоменко Андірй"

printTimeStamp(name)
