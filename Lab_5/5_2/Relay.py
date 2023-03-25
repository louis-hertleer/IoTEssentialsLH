import time
import wiringpi
import sys

# SETUP
print("start")
SPin = [1, 2]
RPin = [3, 4]
wiringpi.wiringPiSetup()

for PinR in RPin:
    wiringpi.pinMode(PinR, 1)
for PinS in SPin:
    wiringpi.pinMode(PinS, 0)

while True:
    if wiringpi.digitalRead(SPin[0]) == 0:
        print("OFF")
        wiringpi.digitalWrite(RPin[0], 0)
    elif wiringpi.digitalRead(SPin[0]) != 0:
        print("ON")
        wiringpi.digitalWrite(RPin[0], 1)



    if wiringpi.digitalRead(SPin[1]) == 0:
        print("OFF")
        wiringpi.digitalWrite(RPin[1], 0)
    elif wiringpi.digitalRead(SPin[1]) != 0:
        print("ON")
        wiringpi.digitalWrite(RPin[1], 1)