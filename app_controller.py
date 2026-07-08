"""
App Controller functions as a state machine. Here, we generally follow this sequence:
welcome -> wait for button press -> journal -> encouragement message -> sleep
Journaling Window? : No = Sleep, Yes = Current State? -> Welcome -> Button -> Prompt -> Timer, etc.
"""

from hardware.time_mgmt import TimeManager
from screen_states.welcome import WelcomeScreen
from screen_states.prompts import PromptScreen
from screen_states.encouragement import EncouragementScreen
from hardware.button import ButtonManager
import time

class AppController:

    SLEEP = "Sleep"
    WELCOME = "Welcome"
    PROMPT = "Prompt"
    ENCOURAGEMENT = "Encouragement"
    current_session = None
    current_state = SLEEP
    encouragement_start_time = None

    @staticmethod
    def update():

        session = TimeManager.journaling_window() # are we in an AM or PM journaling window? 

    #Outside the journaling window
        if session is None:
            AppController.current_session = None

            if AppController.current_state != AppController.SLEEP:
                AppController.current_state = AppController.SLEEP
                #add DisplayManager.sleep()
                #Power off the LEDs
            return
    
    #Inside AM or PM journaling session
        if session != AppController.current_session:

            AppController.current_session = session
            AppController.current_state = AppController.WELCOME

            WelcomeScreen.show()
            return

    #On the welcome screen
        if AppController.current_state == AppController.WELCOME:
            if ButtonManager.button_pressed():
                if session == "AM":
                    PromptScreen.showAM()
                else:
                    PromptScreen.showPM()
                
                AppController.current_state = AppController.PROMPT
            return
                
    #On the prompt screen
        if AppController.current_state == AppController.PROMPT:
            if ButtonManager.button_pressed():

                if session == "AM":
                    EncouragementScreen.showAM()
                else:
                    EncouragementScreen.showPM()

                AppController.current_state = AppController.ENCOURAGEMENT
                AppController.encouragement_start_time = time.time()
            return
        
    #On the encouragement screen
        if AppController.current_state == AppController.ENCOURAGEMENT:
            time_elapsed = time.time() - AppController.encouragement_start_time

            if time_elapsed >= 15:
                AppController. current_state = AppController.SLEEP
                AppController.encouragement_start_time = None
                #Need to add DisplayManager sleep mode and power down LEDs
            return
