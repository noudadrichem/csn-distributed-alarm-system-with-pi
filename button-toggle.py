import RPi.GPIO as GPIO
from time import sleep

ledPin = 8
btnPin = 10


GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)




def sendOutMessage(chan):
    sleep(.1)
    state = not GPIO.input(ledPin)

    if state:
        GPIO.output(ledPin, GPIO.HIGH)
    else:
        GPIO.output(ledPin, GPIO.LOW)

def start():
    GPIO.add_event_detect(
        btnPin,
        GPIO.RISING,
        callback=sendOutMessage
    )


try:
    start()
    input('press enter to stop')

except KeyboardInterrupt:
    GPIO.cleanup()


