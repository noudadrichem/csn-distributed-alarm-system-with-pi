import socket
import RPi.GPIO as GPIO
from time import sleep

HOST = '192.168.42.1'
PORT = 6677

btnPin = 8
def setup():
GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)                                           
print('setup')

def aanOfUitMan(ch):
	print('alarm gaat af')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                                           
	s.connect((HOST, PORT))
	s.sendall('True')



def start():
	GPIO.add_event_detect(btnPin, GPIO.FALLING, callback=aanOfUitMan)                               

setup()

try:
	start()
	input()
except:
	print('doeiiii')
