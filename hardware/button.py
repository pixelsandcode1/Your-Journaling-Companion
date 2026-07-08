from machine import Pin
import time

class ButtonManager:
    button = Pin(15, Pin.IN, Pin.PULL_UP) #pull up means released
    _last_state = 1

    #if the button is pressed it returns true. if the button is held down (multiple presses) it is false
    @staticmethod
    def button_pressed():
        current_state = ButtonManager.button.value()

        pressed = (ButtonManager._last_state == 1 and current_state == 0)

        ButtonManager._last_state = current_state

        return pressed
