import RPi.GPIO as GPIO
from time import sleep

# GPIO pin numbers
SWITCH_PIN = 11
LED_PIN = 13

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin as input, with pull-down resistor
GPIO.setup(LED_PIN, GPIO.OUT)  # Set pin as output

try:
    while True:  # Infinite loop to continuously check switch state
        switch_state = GPIO.input(SWITCH_PIN)  # Read the state of the switch
        GPIO.output(LED_PIN, switch_state)     # Set LED state to match switch state
        sleep(0.1)  # Small delay to reduce CPU usage

except KeyboardInterrupt:
    pass

GPIO.cleanup()  # Clean up GPIO on normal exit

