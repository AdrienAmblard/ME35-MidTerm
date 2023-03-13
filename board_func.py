import time
import machine
from machine import Pin
from secrets import Tufts_eecs as wifi
import mqtt_CBR

# -------------------LED functions------------------- # 
def ledTest(pin):
    led = Pin(pin,Pin.OUT)
    led.on()
    time.sleep(2)
    led.off()
    
green = Pin(6,Pin.OUT)
top = Pin(26,Pin.OUT)
left = Pin(27,Pin.OUT)
right = Pin(15,Pin.OUT)
bottom= Pin(25,Pin.OUT)

def ledStart():
    
    green.on()
    time.sleep(0.5)
    top.on()
    time.sleep(0.5)
    right.on()
    time.sleep(0.5)
    bottom.on()
    time.sleep(0.5)
    left.on()
    time.sleep(0.5)

    green.off()
    top.on()
    right.off()
    bottom.off()
    left.off()

    for i in range(3):
        green.on()
        top.on()
        right.on()
        bottom.on()
        left.on()
        time.sleep(0.3)

        green.off()
        top.off()
        right.off()
        bottom.off()
        left.off()
        time.sleep(0.3)

def ledEnd():
    for i in range(3):
        green.on()
        top.on()
        right.on()
        bottom.on()
        left.on()
        time.sleep(0.3)

        green.off()
        top.off()
        right.off()
        bottom.off()
        left.off()
        time.sleep(0.3)

    green.on()
    top.on()
    right.on()
    bottom.on()
    left.on()
    
    left.off()
    time.sleep(0.5)
    bottom.off()
    time.sleep(0.5)
    right.off()
    time.sleep(0.5)
    top.off()
    time.sleep(0.5)
    green.off()

# -------------------functions for MQTT connection------------------- # 
mqtt_broker = '10.245.155.186' 
topic_sub = 'angles'
topic_pub = 'angles'
client_id = 'Adrien'

mqtt_CBR.connect_wifi(wifi)
led = machine.Pin(6, machine.Pin.OUT) 

def blink(delay = 0.1):
    led.on()
    time.sleep(delay)
    led.off()
    
def whenCalled(topic, msg):
    print((topic.decode(), msg.decode()))
    blink()
    time.sleep(0.01)
    blink()
        
def main():
    fred = mqtt_CBR.mqtt_client(client_id, mqtt_broker, whenCalled)
    fred.subscribe(topic_sub)

    armData = open('armData.csv','r')
    contents = armData.read()
    lines = contents.split('\n')
    data = []

    for line in lines:
        values = line.split(',')
        data.append(values)
    armData.close()
    data.pop(0)
    print(len(data))
    
    for index in range(len(data)-1):
        try:
            fred.check()
            msg = '('+data[index][0]+','+data[index][1]+')'
            fred.publish(topic_pub, msg)
            time.sleep(0.05)
                
        except OSError as e:
            print(e)
            fred.connect()
        except KeyboardInterrupt as e:
            fred.disconnect()
            print('done')
            break