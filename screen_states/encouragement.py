"""
This file contains the different encoruagement messages the pre-sleep screen can display. 
If it is over a certain length, the prompt and messaging breaks into a new line.
"""

from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
import random

class EncouragementScreen:

    encouragement_prompts = [
        "Great job!",
        "You did amazing!",
        "Nice work.",
        "Way to be consistent!",
        "Keep it up!",
        "Wahoo, you did that!"
    ]

    middle_prompts = [
        "Every reflection adds up.",
        "Trust the process.",
        "Another prompt completed.",
        "How did that feel?",
        "Keep at it.",
        "Thats the power of consistency.",
        "Remember to grant yourself grace.",
        "Thank you for showing up.",
        "Keep going.",
        "You showed up."
    ]

    goodbye_prompts = [
    "See you later.",
    "See you tomorrow."
    ]

    @staticmethod
    def showAM():
        encg = DisplayManager()
        
        encg.display.clear(0x0000)
        DisplayManager.draw_header()

        Eprompt = random.choice(EncouragementScreen.encouragement_prompts) #type: str
        Mprompt = random.choice(EncouragementScreen.middle_prompts) #type:str
        Gprompt = EncouragementScreen.goodbye_prompts[0] #type: str

        screen_width = 320
        char_width = 8

        # to display the centered lines in the encouragement/pre-sleep screen
        encg.display.draw_text8x8(120, encg.center_text(Eprompt), Eprompt, color565(242,181,247), rotate = 90)
        encg.display.draw_text8x8(100, encg.center_text(Mprompt), Mprompt, color565(245,240,240), rotate = 90)
        encg.display.draw_text8x8(80, encg.center_text(Gprompt), Gprompt, color565(245,240,240), rotate = 90)
        encg.display.draw_text8x8(60, encg.center_text(":)"), ":)", color565(242,181,247), rotate = 90)

    @staticmethod
    def showPM():
        encg = DisplayManager()
        
        encg.display.clear(0x0000)
        DisplayManager.draw_header()

        Eprompt = random.choice(EncouragementScreen.encouragement_prompts) #type: str
        Mprompt = random.choice(EncouragementScreen.middle_prompts) #type:str
        Gprompt = EncouragementScreen.goodbye_prompts[1] #type: str

        screen_width = 320
        char_width = 8

        # to display the centered lines in the encouragement/pre-sleep screen
        encg.display.draw_text8x8(120, encg.center_text(Eprompt), Eprompt, color565(242,181,247), rotate = 90)
        encg.display.draw_text8x8(100, encg.center_text(Mprompt), Mprompt, color565(245,240,240), rotate = 90)
        encg.display.draw_text8x8(80, encg.center_text(Gprompt), Gprompt, color565(245,240,240), rotate = 90)
        encg.display.draw_text8x8(60, encg.center_text(":)"), ":)", color565(242,181,247), rotate = 90)