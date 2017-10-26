import RPi.GPIO as gpio
import time
from curtsies import Input


# PIN CONSTANTS 
pwm_pin = 40 
positive_pin = 2
ground_pin = 9

# POSITION CONSTANTS
START = 2.0
CENTER = 6.0
END = 12.0
position = CENTER

def move(direction, current_position):
    global position
    step_size = 0.125
    
    # set movement
    if direction > 0:
        current_position += step_size
        
    if direction < 0:
        current_position -= step_size

    # normalize boundaries
    if current_position >= END:
        current_position = END
        return
    if current_position <= START:
        current_position = START
        return

    # set global position variable and move
    position = current_position 
    p.ChangeDutyCycle(current_position)

def keyboard_handler(p):
    with Input(keynames='curses') as input_gen:
        for e in input_gen:
            if repr(e) == "u'KEY_LEFT'":
                move(1, position)

            if repr(e) == "u'KEY_RIGHT'":
                move(-1, position)

# Initialize gpio
gpio.setmode(gpio.BOARD)
gpio.setup(pwm_pin, gpio.OUT)
p = gpio.PWM(pwm_pin, 50)


print("Centering servo...")
p.start(7.5)

p.ChangeDutyCycle(position)

try:
    keyboard_handler(p)

except KeyboardInterrupt:
    print("END... and cleanup.")
    p.stop()
    gpio.cleanup()
