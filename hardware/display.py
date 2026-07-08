#Display.py contains methods for text centering, text wrapping, header display, and sets the configurations for the control pins.

from drivers.ili9341 import Display, color565
from machine import Pin, SPI
from drivers.xglcd_font import XglcdFont
from hardware.time_mgmt import TimeManager
import time

#configures SPI and display to dedicated control pins

class DisplayManager:
    spi = SPI(0,
              baudrate = 40000000,
                sck = Pin(18),
                mosi = Pin(19),
                miso = Pin(16)
        )
    
    display = Display(spi, 
            dc = Pin(20),
            cs = Pin(17),
            rst = Pin(21),
            width = 240,
            height = 320
    )

    #wrap_text checks if the line length of the 8x8 words are 30 chars long. 
    #It also makes sure whole words stay together and do not get split by line.
    @staticmethod
    def wrap_text(text, width = 30):
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + (1 if current_line else 0) <= width:
                if current_line:
                    current_line += " "
                current_line += word
            
            else:
                # Current line is full
                lines.append(current_line)
                current_line = word

        # Add the final line
        if current_line:
            lines.append(current_line)

        return lines
    
    #centers each message on their individual line
    def center_text(self,text):
        
        for line in text:
            y_coordinate = (320 - len(text) * 8) // 2
        return y_coordinate

    _last_minute = None
    _header_x_coordinate = 0
    _header_y_coordinate = 0

    @staticmethod
    def draw_right_aligned_text(x_coordinate,text):
        right_align = DisplayManager.display
        screen_width = 300 #gave the screen some additional padding
        text_width = len(text) * 8

        y_coordinate = screen_width - text_width
        right_align.draw_text8x8(x_coordinate,y_coordinate,text, color565(245,240,240), rotate = 90)

    @staticmethod
    def draw_header():

        draw = DisplayManager.display
        date = TimeManager.get_date()
        current_time = TimeManager.get_time()

        DisplayManager.draw_right_aligned_text(200, date)
        DisplayManager.draw_right_aligned_text(180, current_time)

    @staticmethod
    def update_header():
        now = time.localtime()

        #if the minute has changed, update the minute
        if now[4] != DisplayManager._last_minute:
            DisplayManager._last_minute = now[4]

            DisplayManager.draw_header()

    @staticmethod
    def clear_header():
        clear = DisplayManager.display
        clear.fill_rectangle(200, 180, 30, 5, 0x0000)
        clear.fill_rectangle(180, 250, 30, 5, 0x0000)


#add a sleep function to clear display, tunr off LEDs, maybe reduce power