import RPi.GPIO as GPIO
from time import sleep

ledPin = 8
btnPin = 10
interval = 0.5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.LOW)


def sendOutSignal(chan):
    state = not GPIO.input(ledPin)

    if state:
        while True:
            GPIO.output(ledPin, GPIO.HIGH)
            sleep(1)
            GPIO.output(ledPin, GPIO.LOW)
            sleep(1)
    else:
        GPIO.output(ledPin, GPIO.LOW)



def start():
    GPIO.add_event_detect(
        btnPin,
        GPIO.RISING,
        callback=sendOutSignal
    )


try:
    start()

except KeyboardInterrupt:
    GPIO.cleanup()


