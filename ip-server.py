import socket 
import RPi.GPIO as GPIO
import threading
from time import sleep

alarmPin= 8
startPin = 12
btnPin = 10
interval = 0.5
isBlinking = True 
port = 6677 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')
server.bind(('', port))
server.listen(4)
print('socket listening on 4')
client_socket, client_address = server.accept()
isAlarmRining = False

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(alarmPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(startPin, GPIO.OUT, initial=True)
print('has setup')

def init(): 
    print('je kan het alarm nu uitzetten')
    GPIO.add_event_detect(
        btnPin, 
        GPIO.RISING, 
        callback=zetAlarmUit
    )


def laatAlarmAfGaan():
    init()
    print('het alarm gaat zo af, je kan hem nog uitzetten')
    sleep(3)
    print('is alarm ringing', isAlarmRinging)

    if isAlarmRinging:
        print('DAAA DUUU DAA DUU')
        GPIO.output(alarmPin, GPIO.HIGH)
    else:
        print('ja hij is dus uit')


def zetAlarmUit(c):
    print('uit please') 
    global isAlarmRinging
    isAlarmRinging = False
    GPIO.output(alarmPin, GPIO.LOW)
    GPIO.output(startPin, GPIO.LOW)



while True:
    global isAlarmRinging
    client, addr = server.accept()
    client.send('True'.encode())
    isAlarmRinging = eval(client.recv(1024))
    
    if isAlarmRinging:
        laatAlarmAfGaan()
        break



input()
