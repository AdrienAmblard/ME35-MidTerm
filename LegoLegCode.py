import time
from funcTest import *

i = 0

# checks if switch is on or off, stops if off after 30s
while i < 10:
    val = checkState()
    print(i,val)
    if val == '1':
        sendCode()
        time.sleep(10)
    time.sleep(1)
    i +=  1

