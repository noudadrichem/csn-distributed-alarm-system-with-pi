import RPi.GPIO as GPIO
import threading
from time import sleep

alarmPin= 8
startPin = 12
btnPin = 10
interval = 0.5
isBlinking = True 



BUTTON_PRESSED = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(alarmPin, GPIO.OUT, initial=False)
GPIO.setup(startPin, GPIO.OUT, initial=True)

def setInterval(function, intervalDuration):
    event = threading.Event()
    while not event.wait(intervalDuration):
        function()



def sendOutSignal(pin):
    sleep(.1)
    state = not GPIO.input(alarmPin)

    if GPIO.input(pin):
        BUTTON_PRESSED = True
    else:
        BUTTON_PRESSED = False

    if state:
        if isBlinking:
            # setInterval(blink, interval)
            GPIO.output(alarmPin, GPIO.HIGH)
        else:
            GPIO.output(alarmPin, GPIO.LOW)
    else:
        GPIO.output(alarmPin, GPIO.LOW)



def blink():
    global isBlinking
    isBlinking = not isBlinking


def start():
    GPIO.add_event_detect(
        btnPin,
        GPIO.RISING,
        callback=sendOutSignal
    )



try:
    start()
    input('entor\n')

except:
    GPIO.cleanup()


