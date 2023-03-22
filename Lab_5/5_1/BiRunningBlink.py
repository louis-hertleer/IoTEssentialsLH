import time 
import wiringpi 
import sys

pin = [2,3,4,6]

def blink():
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
wiringpi.pinMode(pin[0], 1) 
wiringpi.pinMode(pin[1], 1) 
wiringpi.pinMode(pin[2], 1) 
wiringpi.pinMode(pin[3], 1)

#MAIN
while 1 < 2: 
    blink()