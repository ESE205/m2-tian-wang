import RPi.GPIO as GPIO
from time import sleep, time
import argparse

# Setup GPIO
LED_PIN = 13  # LED Pin number
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

# Parse command line arguments
parser = argparse.ArgumentParser(description='LED Blink Program with Write Feature.')
parser.add_argument('--rate', type=float, default=1.0, help='Blink rate in seconds')
parser.add_argument('--duration', type=int, default=30, help='Duration to run the program in seconds')
parser.add_argument('--debug', action='store_true', help='Enable debug mode')
args = parser.parse_args()

# Initialize variables
blink_rate = args.rate
duration = args.duration
debug = args.debug
start_time = time()

# Main loop
with open('data.txt', 'w') as file:
    while time() - start_time < duration:
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED on
        if debug:
            print(f"{time()}\tON")
        file.write(f"{time()}\tON\n")
        sleep(blink_rate)

        GPIO.output(LED_PIN, GPIO.LOW)   # LED off
        if debug:
            print(f"{time()}\tOFF")
        file.write(f"{time()}\tOFF\n")
        sleep(blink_rate)

# Clean up
GPIO.cleanup()
