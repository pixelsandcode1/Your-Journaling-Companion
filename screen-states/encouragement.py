"""
This file contains the different encoruagement messages the pre-sleep screen can display. 
If it is over a certain length, the prompt and messaging breaks into a new line.
"""

from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
import random
import time

welcome = DisplayManager()

encouragement_prompts = [
    "Great job!",
    "You did amazing!",
    "Nice work.",
    "Way to be consistent!",
    "Keep it up!",
    "Wahoo, you did that!"
]

middle_prompt = [
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

welcome.display.clear(0x0000)

welcome.display.draw_text8x8(200, 170, "Monday, July 6th", color565(245,240,240), rotate = 90)
welcome.display.draw_text8x8(180, 250, "9:45AM", color565(245,240,240), rotate = 90)

Eprompt = random.choice(encouragement_prompts) #type: str
Mprompt = random.choice(middle_prompt) #type:str

#time logic to determine pre-sleep screen message 
time = 7

if time < 10:
    Gprompt = goodbye_prompts[0]
else:
   Gprompt = goodbye_prompts[1]

screen_width = 320
char_width = 8

# to display the centered lines in the encouragement/pre-sleep screen
welcome.display.draw_text8x8(120, welcome.center_text(Eprompt), Eprompt, color565(242,181,247), rotate = 90)
welcome.display.draw_text8x8(100, welcome.center_text(Mprompt), Mprompt, color565(245,240,240), rotate = 90)
welcome.display.draw_text8x8(80, welcome.center_text(Gprompt), Gprompt, color565(245,240,240), rotate = 90)
welcome.display.draw_text8x8(60, welcome.center_text(":)"), ":)", color565(245,240,240), rotate = 90)