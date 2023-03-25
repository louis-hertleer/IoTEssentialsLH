import time 
import wiringpi 
import sys

pin = [2,3,4,6]
pinSwitch = 1

def blinkyright():
    while True:
        wiringpi.digitalWrite(pin[0], 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin[0], 0) 
        wiringpi.digitalWrite(pin[1], 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin[1], 0)
        wiringpi.digitalWrite(pin[2], 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin[2], 0)
        wiringpi.digitalWrite(pin[3], 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin[3], 0)
        time.sleep(0.1)

def blinkyleft(): 
    while True:
        wiringpi.digitalWrite(pin[3], 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin[3], 0) 
        wiringpi.digitalWrite(pin[2], 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin[2], 0)
        wiringpi.digitalWrite(pin[1], 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin[1], 0)
        wiringpi.digitalWrite(pin[0], 1)
        time.sleep(0.1)
        wiringpi.digitalWrite(pin[0], 0)
        time.sleep(0.1)

#SETUP
print("Start") 

wiringpi.wiringPiSetup() 
wiringpi.pinMode(2, 1)
wiringpi.pinMode(3, 1)
wiringpi.pinMode(4, 1)
wiringpi.pinMode(6, 1)
wiringpi.pinMode(pinSwitch, 0)

#MAIN
while True: 
    if(wiringpi.digitalRead(pinSwitch) == 1):
        time.sleep(0.3)
        blinkyleft()
        

    else:
        time.sleep(0.3)
        blinkyright()