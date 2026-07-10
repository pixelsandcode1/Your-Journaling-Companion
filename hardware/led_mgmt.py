#LED Management controls the LED state.

from machine import Pin
import neopixel
import time


class LEDManager:

    num_leds = 65
    data_pin = 16

    # Warm white at 5%
    color = (13, 6, 1)

    pixels = neopixel.NeoPixel(Pin(data_pin), num_leds)

    @classmethod
    def off(cls):
        for i in range(cls.num_leds):
            cls.pixels[i] = (0, 0, 0)
        cls.pixels.write()

    @classmethod
    def fill(cls):
        for i in range(cls.num_leds):
            cls.pixels[i] = cls.color
        cls.pixels.write()

    @classmethod
    def timer_fill(cls, seconds):
        cls.off()

        delay = seconds / cls.num_leds

        for i in range(cls.num_leds):
            cls.pixels[i] = cls.color
            cls.pixels.write()
            time.sleep(delay)