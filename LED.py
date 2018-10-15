import RPi.GPIO as GPIO
from time import sleep 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


interval = 1

while True:
    
    sleep(interval)
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    sleep(interval)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
