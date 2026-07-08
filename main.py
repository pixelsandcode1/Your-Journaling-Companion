from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
from hardware.rtc_wifi import RTCWifi
from screen_states import welcome
import time

"""
Main will be used to determine scheduling logic. It will check if the time is between 7 - 10AM & 7 - 10PM to turn on the welcome screen

Logic Tree:
---- Is it between 7 and 10AM or 7 and 10PM?
> If yes : show welcome screen & wait for button push
> If no : sleep


Boot.
Connect to Wi-Fi.
Synchronize the clock with NTP.
Disconnect Wi-Fi (optional, to save power).
Use the local clock for everything else.
"""

RTCWifi.init()
welcome.WelcomeScreen.show()

DisplayManager.update_header()
"""while True:
    DisplayManager.update_header()
    time.sleep(1)"""