import serial
from Adafruit_IO import Client


def serialTest(pin):
    pin = str(pin)
    # establsihing connection with Arduino
    s = serial.Serial('/dev/tty.usbmodem14201', baudrate=115200)
    print(s)
    # code run by Arduino 
    code = '''from board_func import *
ledTest('''+pin+''')'''

    CtrlC = '\x03'
    CtrlD = '\x04'
    CtrlE = '\x05'
    
    s.write(CtrlE.encode())
    code = code.replace('\n','\r\n').encode()
    print(code)
    s.write(code)
    s.write(CtrlD.encode())
    print(s.read_all())
    s.close()
    
    
def checkState():
    aio = Client('aadrien', 'aio_NXDg78rzNSl6qPWrFx0ObfGVmMOD') # REST API connection setup 
    data = aio.receive('leg-state') # get current data of "leg state" feed
    value = data[3] # extracting value of feed
    return value

def sendCode():
    # establshing connection with Arduino
    s = serial.Serial('/dev/tty.usbmodem14101', baudrate=115200)
    print(s)
    # code run by Arduino
    code = '''from board_func import * 
ledStart()
main()
ledEnd()'''
    
    CtrlC = '\x03'
    CtrlD = '\x04'
    CtrlE = '\x05'
    s.write(CtrlE.encode())
    code = code.replace('\n','\r\n').encode()
    print(code)
    s.write(code)
    s.write(CtrlD.encode())
    print(s.read_all())

    s.close()

    
