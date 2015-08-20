import socket
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)

#Motor 1 GPIO Pin
IC1_A = 27
IC1_B = 22

#Motor 2 GPIO Pin
IC2_A = 24
IC2_B = 23

gpio.setmode(gpio.BCM)

m1_epin = 17
m2_epin = 25

gpio.setup(m1_epin,gpio.OUT)
gpio.setup(m2_epin,gpio.OUT)
gpio.setup(IC1_A, gpio.OUT)
gpio.setup(IC1_B, gpio.OUT)
gpio.setup(IC2_A, gpio.OUT)
gpio.setup(IC2_B, gpio.OUT)


p1 = gpio.PWM(m1_epin,100)
p2 = gpio.PWM(m2_epin,100)

p1.start(0)
p2.start(0)

p1.ChangeDutyCycle(100)
p2.ChangeDutyCycle(100) 

UDP_IP = "0.0.0.0"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def forward():
    gpio.output(IC2_A, gpio.LOW)
    gpio.output(IC2_B, gpio.HIGH)

def backword():
    gpio.output(IC2_A, gpio.HIGH)
    gpio.output(IC2_B, gpio.LOW)

def turnRight():
    gpio.output(IC1_A, gpio.HIGH)
    gpio.output(IC1_B, gpio.LOW)

def turnLeft():
    gpio.output(IC1_A, gpio.LOW)
    gpio.output(IC1_B, gpio.HIGH)

def stopFB():
    gpio.output(IC2_A, gpio.LOW)
    gpio.output(IC2_B, gpio.LOW)

def stopLR():
    gpio.output(IC1_A, gpio.LOW)
    gpio.output(IC1_B, gpio.LOW)

try:
  while True:
     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
     print "received message:", data
     position = data.split(";")[0]
     acceleration = data.split(";")[1]
     print "position", position
     print "acceleration", acceleration
     if acceleration == "1":
       forward()
     if acceleration == "2":
       backword()
     if position == "15":
       turnLeft()
     if position == "-15":
       turnRight()
     if position == "0":
       stopLR()
     if acceleration == "0":
       stopFB()       
 
except KeyboardInterrupt:
       gpio.cleanup()
