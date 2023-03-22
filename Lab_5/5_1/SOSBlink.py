import time 
import wiringpi 
import sys

pin = 1

def blink():
    wiringpi.digitalWrite(pin, 1) 
    time.sleep(0.5)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(0.5)
    wiringpi.digitalWrite(pin, 1)
    time.sleep(1.5)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(0.5)
    wiringpi.digitalWrite(pin, 1) 
    time.sleep(0.5)
    wiringpi.digitalWrite(pin, 0)
    time.sleep(3)


#SETUP
print("Start") 

wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin, 1) 


#MAIN
while 1 < 2: 
    blink()