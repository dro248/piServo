import RPi.GPIO as gpio
import time

# PIN CONSTANTS 
pwm_pin = 40 
positive_pin = 2
ground_pin = 9

# POSITION CONSTANTS
START = 2.0
MID = 6.0
END = 12.0

gpio.setmode(gpio.BOARD)
gpio.setup(pwm_pin, gpio.OUT)
p = gpio.PWM(pwm_pin, 50)

print("Centering servo...")
p.start(7.5)

try:
    print("BEGIN")

    while True:
        # turn towards 0 degrees 
	print("Turn to START...")
        p.ChangeDutyCycle(START)    
	time.sleep(3)

        # turn towards 90 degrees 
        print("Turn to MID...")  
	p.ChangeDutyCycle(MID)	    
	time.sleep(3)

        # turn towards 180 degrees	
        print("Turn to END...")
	p.ChangeDutyCycle(END)	    
	time.sleep(3)

except KeyboardInterrupt:
    print("END")
    p.stop()
    gpio.cleanup()
