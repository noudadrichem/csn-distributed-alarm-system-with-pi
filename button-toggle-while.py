import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
latest_state = None


BUTTON_PRESSED = None

def toggle(c):
    global BUTTON_PRESSED
    BUTTON_PRESSED = not BUTTON_PRESSED


    print(BUTTON_PRESSED)


GPIO.add_event_detect(10, GPIO.RISING, callback=toggle)


input()

'''
while True:
    inputValue = GPIO.input(10)
    if inputValue != latest_state:
        latest_state = inputValue
        if latest_state:
            print('btn pressed')
            True
    time.sleep(0.3)
    print(latest_state)
'''
