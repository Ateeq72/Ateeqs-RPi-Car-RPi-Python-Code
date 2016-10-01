#by ateeq72@xda
import RPi.GPIO as gpio

#Motor 1 GPIO Pin
IC1_A = 23
IC1_B = 24

#Motor 2 GPIO Pin
IC2_A = 25
IC2_B = 8

m1_epin = 20
m2_epin = 21


def initialSetup():
   gpio.setmode(gpio.BCM)

   gpio.setwarnings(False)

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

def done():
       gpio.cleanup()
