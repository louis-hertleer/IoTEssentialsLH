import time 
import wiringpi 
import sys

pin = [2,3,4,6]

def fulldrive():
    for i in range(4):
        wiringpi.digitalWrite(pin[i], 1)
        time.sleep(0.01) # adjust delay based on motor specifications
        wiringpi.digitalWrite(pin[i], 0)
        time.sleep(0.01) # adjust delay based on motor specifications
        wiringpi.digitalWrite(pin[(i+1)%4], 1)
        time.sleep(0.01) # adjust delay based on motor specifications

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
    fulldrive()