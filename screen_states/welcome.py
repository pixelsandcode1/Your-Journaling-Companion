"""
The welcome screen is the first screen that users see. 
It greets them & asks if they are ready to start journaling.
It also reflects the date & time.
"""

from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
from hardware.time_mgmt import TimeManager

class WelcomeScreen:

    @staticmethod
    def show():
        welcome = DisplayManager.display
        espressodolce = XglcdFont('EspressoDolce18x24.c', 18, 24)
        date = TimeManager.get_date()
        time = TimeManager.get_time()

        welcome.clear(0x0000)
        print("I hit checkpoint 1.")

        welcome.draw_text8x8(200, 180, date, color565(245,240,240), rotate = 90)
        welcome.draw_text8x8(180, 250, time, color565(245,240,240), rotate = 90)
        welcome.draw_text(110, 300, "Your Journaling Companion", espressodolce, color565(242,181,247), landscape = True, rotate_180 = True)
        welcome.draw_text8x8(45, 55, "Press the button to begin", color565(245,240,240), rotate = 90)
        welcome.draw_text8x8(25, 150, " :)", color565(245,240,240), rotate = 90)
        welcome.draw_text8x8(10, 50, "Everyday, 2x, for 10 minutes", color565(242, 181,247), rotate = 90)
        print("I hit the final checkpoint.")
