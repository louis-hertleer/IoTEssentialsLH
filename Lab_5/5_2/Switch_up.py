import time
import wiringpi
import sys

# SETUP
print("start ")
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup ()
wiringpi.pinMode (pinLed, 1)
wiringpi.pinMode (pinSwitch, 0)

#infinite loop stop using CTRL-C
while True:
    if (wiringpi.digitalRead (pinSwitch) == 0):  
        print("Button Released")
        time.sleep (0.3) 
        wiringpi.digitalWrite (pinLed, 0)
    else:
        print("Button Pressed ")
        time.sleep (0.3) #anti bouncing
        wiringpi.digitalWrite (pinLed, 1)