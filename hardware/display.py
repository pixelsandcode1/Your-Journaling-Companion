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

"""
class DisplayManager:
        
        def __init__(self):
            self.spi = SPI(0, 
                baudrate = 40000000,
                sck = Pin(18),
                mosi = Pin(19),
                miso = Pin(16)
        )
            
            self.display = Display(
               self.spi, 
            dc = Pin(20),
            cs = Pin(17),
            rst = Pin(21),
            width = 240,
            height = 320
        )
            
        def clear(self,color = 0x0000):
              self.display.clear(color)
        
        def cleanup(self):
              self.display.cleanup()
"""
