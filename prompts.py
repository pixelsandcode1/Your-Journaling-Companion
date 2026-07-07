"""
This file contains the different prompts the screen can display. If it is over a certain length,
the prompt breaks into a new line.
"""

from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
import random
import time

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

#this line looks like a run-time error, but it runs in the Pico environment
chosen_prompt = random.choice(am_prompts) #type: str

welcome.draw_text8x8(200, 170, "Monday, July 6th", color565(245,240,240), rotate = 90)
welcome.draw_text8x8(180, 250, "9:45AM", color565(245,240,240), rotate = 90)

wrapped_prompt = DisplayManager.wrap_text(chosen_prompt, 30)

#once the string is parsed into a list of strings, put each new string on its own line, stacked & centered
x_coordinate = 120

for line in wrapped_prompt:
    line_width = len(line) * 8
    y_coordinate = (320 - line_width) // 2

    welcome.draw_text8x8(x_coordinate, y_coordinate, line, color565(245,240,240), rotate = 90)
    x_coordinate -= 15


