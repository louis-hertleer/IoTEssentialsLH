import time 
import wiringpi 
import sys

pin = [2,3,4,6]

def wavedrive():
    for i in range(4):
        wiringpi.digitalWrite(pin[i], 1)
        time.sleep(0.01) # shorter delay time
        wiringpi.digitalWrite(pin[i], 0)
        time.sleep(0.01) # shorter delay time

# The motor does 1 tick every second with a 1000ms. With 10ms it turns faster

# SETUP
print("Start") 

wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin[0], 1) 
wiringpi.pinMode(pin[1], 1) 
wiringpi.pinMode(pin[2], 1) 
wiringpi.pinMode(pin[3], 1)

#MAIN
while 1 < 2: 
    wavedrive()