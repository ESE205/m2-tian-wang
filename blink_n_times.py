import RPi.GPIO as GPIO
from time import sleep
import sys

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED_PIN = 13  # LED pin
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

# Default number of blinks
DEFAULT_BLINK_COUNT = 5

# Get number of blinks from command line argument, default to 5 if not provided
blink_count = DEFAULT_BLINK_COUNT
if len(sys.argv) > 1:
    try:
        blink_count = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Using default blink count of 5.")

# Blinking loop
for _ in range(blink_count):
    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
    sleep(1)                         # Wait 1 second
    GPIO.output(LED_PIN, GPIO.LOW)   # Turn off LED
    sleep(1)                         # Wait 1 second

# Cleanup
GPIO.cleanup()

