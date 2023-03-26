import wiringpi
import time
import sys

TRIG_PIN = 4
ECHO_PIN = 5

def measure_distance():
    # Send 10us pulse to trigger pin
    wiringpi.digitalWrite(TRIG_PIN, 1)
    time.sleep(0.00001)
    wiringpi.digitalWrite(TRIG_PIN, 0)
    
    # Wait for echo pin to go high
    pulse_start = time.time()
    while wiringpi.digitalRead(ECHO_PIN) == 0:
        pulse_start = time.time()
    
    # Wait for echo pin to go low
    pulse_end = time.time()
    while wiringpi.digitalRead(ECHO_PIN) == 1:
        pulse_end = time.time()
    
    # Calculate pulse duration and distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # speed of sound in cm/s
    distance = round(distance, 2)
    print(distance)
    time.sleep(1)    

wiringpi.wiringPiSetup()
wiringpi.pinMode(TRIG_PIN, 1)
wiringpi.pinMode(ECHO_PIN,0)
    
while True:
    print("Start")
    measure_distance()
    
