#test file to validate the leds light up and can change color - case 1
"""
from machine import Pin
import neopixel
import time

NUM_LEDS = 65      # Change to however many LEDs you want to test
PIN = 16

pixels = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# White
for i in range(NUM_LEDS):
    pixels[i] = (3, 2, 0)
pixels.write()
time.sleep(1)

# Off
for i in range(NUM_LEDS):
    pixels[i] = (0, 0, 0)
pixels.write()
"""

#for 10 seconds, led 1 - 65 will each turn on to represent a timer passing time
# 7 leds turn on at a time until all are lit represnting the timer being complete -- case 2

from machine import Pin
import neopixel
import time

# ----- Configuration -----
NUM_LEDS = 65
PIN = 16

pixels = neopixel.NeoPixel(Pin(PIN), NUM_LEDS)

# Turn everything off
for i in range(NUM_LEDS):
    pixels[i] = (0, 0, 0)
pixels.write()

# Seconds per LED
DELAY = 10 / NUM_LEDS

# Fill the strip
for i in range(NUM_LEDS):
    # If your colors appear wrong, swap to (GREEN, RED, BLUE)
    pixels[i] = (13, 6, 1)
    pixels.write()
    time.sleep(DELAY)

# Hold completed timer
time.sleep(2)

# Turn off
for i in range(NUM_LEDS):
    pixels[i] = (0, 0, 0)
pixels.write()