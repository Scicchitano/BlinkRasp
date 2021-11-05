#import RPi.GPIO as GPIO
import time
import pigpio 

pi = pigpio.pi()

while(1):
    pi.set_mode(4, pigpio.OUTPUT)
    pi.write(4,1)
    time.sleep(5)
    pi.write(4,0)
    time.sleep(5)
