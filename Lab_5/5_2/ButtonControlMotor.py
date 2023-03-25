import time 
import wiringpi 
import sys

pin = [2,3,4,6] 
pinSwitch = 9
pinSwitch2 = 10
wiringpi.wiringPiSetup ()
def Controlmode():
    while True:
        if (wiringpi.digitalRead (pinSwitch) == 0):
            pin = [2,3,4,6]  
            print("Motor turning Clockwise")
            time.sleep (0.3) 
            for i in range(4):
                wiringpi.digitalWrite(pin[i], 1)
                time.sleep(0.01) # shorter delay time
                wiringpi.digitalWrite(pin[i], 0)
                time.sleep(0.01) # shorter delay time
        elif(wiringpi.digitalRead (pinSwitch2) == 0):
            pin = [6,4,3,2]
            print("Motor turning Counter-Clockwise")
            time.sleep (0.3) 
            for i in range(4):
                wiringpi.digitalWrite(pin[i], 0)
                time.sleep(0.01) # shorter delay time
                wiringpi.digitalWrite(pin[i], 1)
                time.sleep(0.01) # shorter delay time
        else:
             time.sleep(1)
             print("Idle")

# SETUP
print("Start") 

wiringpi.wiringPiSetup() 
wiringpi.pinMode(pin[0], 1) 
wiringpi.pinMode(pin[1], 1) 
wiringpi.pinMode(pin[2], 1) 
wiringpi.pinMode(pin[3], 1)
wiringpi.pinMode(pinSwitch,0)
wiringpi.pinMode(pinSwitch2,0)
#MAIN
while 1 < 2: 
    Controlmode()