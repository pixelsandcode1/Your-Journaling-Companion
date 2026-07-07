from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
import os

espressodolce = XglcdFont('EspressoDolce18x24.c', 18, 24)

#display.clear(0xF800)
#DisplayManager.display.draw_text8x8(130,130,"Hello World", color565(255,0,0), rotate = 90)
DisplayManager.display.draw_text(100, 200, "Hello World", espressodolce, color565(255,0,0), landscape = True, rotate_180 = True)
#print(os.listdir())