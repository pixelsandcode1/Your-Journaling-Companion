from drivers.ili9341 import Display, color565
from machine import Pin, SPI
from drivers.xglcd_font import XglcdFont

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
