from gpiozero import Servo
from time import sleep

servoPin = 17

corrections = .99 #0.45
maxPW = (2.0+corrections)/1000
minPW = (1.0-corrections)/1000
servo = Servo(servoPin, min_pulse_width = minPW, max_pulse_width = maxPW)

delay = .02
def testServo():
    for degree in range(0,180):
        setPos(degree)
    sleep(.5)
    for degree in range(180, 0, -1):
        setPos(degree)
        
def setPos(value):
    value = float(value) / 90
    servo.value = (float(value)-10/10)
    sleep(delay)
    
while True:
    testServo()
    
    

        
