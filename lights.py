import RPi.GPIO as GPIO
import threading
from time import sleep

alarmPin= 8
startPin = 12
btnPin = 10
interval = 0.5
isBlinking = True 

def setInterval(function, interval):
    event = threading.Event()
    while not event.wait(interval):
        function(True)
        print('interval')

BUTTON_PRESSED = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(alarmPin, GPIO.OUT, initial=False)
GPIO.setup(startPin, GPIO.OUT, initial=True)

def toggleLight(state):
    if state:
        GPIO.output(alarmPin, True)
        # setInterval(toggleLight, 1)
    else:
        GPIO.output(alarmPin, False)

def toggleButtonValue(c):
    global BUTTON_PRESSED
    BUTTON_PRESSED = not BUTTON_PRESSED
    toggleLight(BUTTON_PRESSED)



GPIO.add_event_detect(btnPin, GPIO.RISING, callback=toggleButtonValue)

input()

