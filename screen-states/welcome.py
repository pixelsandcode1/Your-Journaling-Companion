"""
The welcome screen is the first screen that users see. 
It greets them & asks if they are ready to start journaling.
It also reflects the date & time.
"""

from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
import time

welcome = DisplayManager.display 

espressodolce = XglcdFont('EspressoDolce18x24.c', 18, 24)

welcome.clear(0x0000)

welcome.draw_text8x8(200, 170, "Monday, July 6th", color565(245,240,240), rotate = 90)
welcome.draw_text8x8(180, 250, "9:45AM", color565(245,240,240), rotate = 90)

welcome.draw_text(110, 300, "Your Journaling Companion", espressodolce, color565(242,181,247), landscape = True, rotate_180 = True)

#welcome.draw_text8x8(100, 60, "Ready to start journaling?", color565(245,240,240), rotate = 90)
#welcome.draw_text(85, 310, "Ready to start journaling?", espressodolce, color565(245,240,240), landscape = True, rotate_180 = True)


welcome.draw_text8x8(45, 55, "Press the button to begin", color565(245,240,240), rotate = 90)
welcome.draw_text8x8(25, 150, " :)", color565(245,240,240), rotate = 90)
welcome.draw_text8x8(10, 50, "Everyday, 2x, for 10 minutes", color565(242, 181,247), rotate = 90)
#welcome.draw_text(50, 310, "Press the button to begin :)", espressodolce, color565(242,181,247), landscape = True, rotate_180 = True)

#time.sleep(5)
#welcome.clear(0x0000)