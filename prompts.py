"""
This file contains the different prompts the screen can display. If it is over a certain length,
the prompt breaks into a new line.
"""

from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
import random

welcome = DisplayManager.display 

espressodolce = XglcdFont('EspressoDolce18x24.c', 18, 24)

am_prompts = [
    "Describe your ideal morning.",
    "What are you looking forward to today?",
    "How do you handle a bad day?",
    "What would make today great?",
    "Share one positive affirmation for today and its meaning.",
    "What does a good day look like?",
    "Write a letter to someone you love.",
    "Who do you feel supported by in your life?",
    "Write a letter of encouragement to yourself.",
    "Write an appreciation letter to yourself.",
    "Make a list of 10 things you are grateful for.",
    "Describe an ideal day. What would you do?",
    "What do you like best about yourself?"
    "How are you doing, really?"

]

pm_prompts = [
    "What made you smile today?",
    "What was the best part of your day?",
    "Write a list of 10 things that make you smile.",
    "What was your favorite childhood book?",
    "What have you been reading recently?",
    "Try sensory journaling. What can you see, hear, etc?",
    "When was a time you felt very content?", 
    "List your goals for this month.",
    "List your goals for this week.",
    "What has been stressing you lately?",
    "What keeps you up at night?",
    "What emotions were most present today?",
    "What felt heavy in your mind today?",
    "What helps you feel grounded?",
    "What does self care mean to you?"
]


chosen_prompt = random.choice(am_prompts) #type: str

welcome.clear(0x0000)

welcome.draw_text8x8(200, 170, "Monday, July 6th", color565(245,240,240), rotate = 90)
welcome.draw_text8x8(180, 250, "9:45AM", color565(245,240,240), rotate = 90)

str_length = len(chosen_prompt)
print("this is the string length: ", str_length)

if str_length < 32:

    welcome.draw_text8x8(110, 35, chosen_prompt, color565(245,240,240), rotate = 90)
    print("Hit this one")

else:
   print("I started to wrap the text.")
   wrap_length = 30

   first_half = chosen_prompt[:wrap_length] 
   second_half = chosen_prompt[wrap_length:]
   print("This is the first half:", first_half)
   print("This is the second half: ", second_half)

   welcome.draw_text8x8(120, 35, first_half, color565(245,240,240), rotate = 90)
   welcome.draw_text8x8(110, 35, second_half, color565(245,240,240), rotate = 90)

   print("I wrapped the text.")
   