import time
armData = open('armData.csv','r')
contents = armData.read()
lines = contents.split('\n')
data = []

for line in lines:
    values = line.split(',')
    data.append(values)
armData.close()
data.pop(0)

for index in range(len(data)-1):
    print('('+data[index][0]+','+data[index][1]+')')
    time.sleep(0.1)