#by ateeq72@xda
import RPi.GPIO as gpio

#PIR SENSOR GPIO Pin
P_IN = 26

def initialSetup():
   gpio.setmode(gpio.BCM)

   gpio.setup(P_IN, gpio.IN)         #Read output from PIR motion sensor

def checkObs():
    initialSetup()
    obs = gpio.input(P_IN)
    if(obs == 1):
       return True
    elif(obs == 0):
       return False

