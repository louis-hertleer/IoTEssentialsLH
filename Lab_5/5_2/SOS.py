import time
import wiringpi
import sys

def SOS(_pin):
    x= True
    while x:
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

print("start")
pinSwitch = 1
pin = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin, 1)
wiringpi.pinMode(pinSwitch, 0)


while True:
    if(wiringpi.digitalRead(pinSwitch) == 1):
        print("Help!")
        time.sleep(0.3)
        SOS()
    else:
        print("No help required")
        time.sleep(0.3)
        wiringpi.digitalWrite(pin, 0)