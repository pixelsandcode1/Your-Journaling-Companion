"""#Test file to verify the button press is be registered successfully - case 1
from hardware.button import ButtonManager
import time

print("Testing button...")

while True:
    if ButtonManager.button_pressed():
        print("Button pressed!")
    
    else:
        print("Button is Not pressed!")

    time.sleep(0.1)"""

#Tester file to see if button press can help cycle to the different screens - case 2
from screen_states.welcome import WelcomeScreen
from screen_states.prompts import PromptScreen
from screen_states.encouragement import EncouragementScreen
from hardware.button import ButtonManager
import time


def test_journaling_flow():

    print("Starting journaling flow test")

    # Show welcome screen
    WelcomeScreen.show()

    print("Waiting for button press...")

    # Wait for a single button press
    while True:

        if ButtonManager.button_pressed():

            print("Button pressed!")

            break

        time.sleep(0.05)


    # Show prompt screen
    print("Showing prompt screen")

    PromptScreen.showAM()

    time.sleep(5)


    # Show encouragement screen
    print("Showing encouragement screen")

    EncouragementScreen.showAM()

    time.sleep(5)


    print("Test complete")


test_journaling_flow()

#test file to see if button press changes to prompt screen, shows prompt + starts LED animation, before showing encouragment screen & powering down