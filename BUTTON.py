import RPi.GPIO as GPIO
from time import sleep

ledPin = 11 
btnPin = 12


led_status = True

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print('Has been setup')

def switchLedLight(ev=None):
    global led_status
    led_status = not led_status

    if led_status:
        print('on')
    else:
        print('off')


def functionalityLoop():
    GPIO.add_event_detect(btnPin, GPIO.FALLING, callback=switchLedLight, bouncetime=200)
    while True:
        sleep(1)


def kapot():
    GPIO.output(ledPin, GPIO.HIGH)
    GPIO.cleanup()
    print('stopped')


setup()


try:
    functionalityLoop()
except KeyboardInterrupt:
    kapot()
