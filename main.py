from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
from hardware.rtc_wifi import RTCWifi
from screen_states import welcome
from screen_states import prompts
from screen_states import encouragement
import time
from app_controller import AppController
from hardware.button import ButtonManager

"""
Main will be used to determine scheduling logic. It will check if the time is between 7 - 10AM 
& 7 - 10PM to turn on the welcome screen.

Logic Tree:
---- Is it between 7 and 10AM or 7 and 10PM?
> If yes : show welcome screen & wait for button push
> If no : sleep

"""

RTCWifi.init()
welcome.WelcomeScreen.show()

DisplayManager.update_header()
prompts.PromptScreen.showAM()
time.sleep(10)
DisplayManager.update_header()
encouragement.EncouragementScreen.showAM()
time.sleep(5)
DisplayManager.display.clear(0x0000)


print("No button? shutting down now.")

"""while True:
    
    AppController.update()
    DisplayManager.update_header()
    time.sleep(0.05)
    """