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


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(alarmPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(startPin, GPIO.OUT, initial=True)


while True:
    client, addr = server.accept()
    client.send('True'.encode())
    isAlarmRinging = client.recv(1024)
    

    if eval(isAlarmRinging):
        print('DAAA DUUU DAAA DUUU')
        GPIO.output(alarmPin, GPIO.HIGH)
        break

def toggleButtonValue(c):
    print('uit please')
    GPIO.output(alarmPin, GPIO.LOW)
    GPIO.output(startPin, GPIO.LOW)


GPIO.add_event_detect(btnPin, GPIO.RISING, callback=toggleButtonValue)


server.close()
input()


