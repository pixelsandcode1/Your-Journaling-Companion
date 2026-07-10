<h1 align= "center">Your Journaling Companion: A Raspberry Pi Project </h1>

- [About](#about)
- [File Structure](#file-structure)
- [Hardware Stack](#hardware-stack)
- [Software Architcture](#software-architecture)
- [Set Up Guidelines](#set-up-guidelines)

## About
Your Journaling Companion is a Raspberry Pi-powered embedded device designed to encourage consistent daily journaling through a calm and low-friction interaction model. The device quietly becomes a part of a users environment to create dedicated moments for gratitude and reflection journaling. Twice a day, it wakes up during predefined morning and evening journaling windows. A warm ambient glow signals that it is time to start a session, if they are ready to. When the user is ready, they press a single button which begins a ten-minute prompted writing session timed by LED animation. Upon completion, the user receives a brief encouraging message before the device goes to sleep. 

** 95 % done with this logic, need to fully update the led management to reflect the states (outside of the demo)

## File Structure

```text
journaling-companion/
│
├── main.py                  # Main application entry point
├── demo.py                  # Demo of the complete journaling flow
├── app_controller.py        # will be relocated, holds state machine logic
├── button_test.py           # used to verify button presses work
├── led_test.py              # used to verify the leds work
├── EspressoDolce18x24.py    # Pico very specific if this one is in the font folder, will relocate
│
├── hardware/
│   ├── display.py           # DisplayManager for rendering the UI
│   ├── button.py            # Button input handling
│   ├── led_mgmt.py          # LED animations and timer progress
│   └── time_mgmt.py         # Date and time utilities
│
├── screen_states/
│   ├── welcome.py           # Welcome screen
│   ├── prompt.py            # Random journaling prompt screen for AM and PM
│   └── encouragement.py     # Closing encouragement screen
│
│
├── drivers/                 # Third-party display/font drivers
├── fonts/                   # Bitmap font files
│
└── README.md
```

### Directory Overview

- **main.py** – Coordinates the application flow and transitions between screen states.
- **hardware/** – Contains reusable hardware interfaces for the display, button, LEDs, and time management.
- **screen_states/** – Defines each screen shown during the journaling experience.
- **prompts/** – Stores the journaling prompt library.
- **drivers/** – Contains third-party display and font drivers.
- **fonts/** – Stores bitmap font files used by the display.

## Hardware Stack
|Component| Hardware / Software Used| Reason|
| --- | --- | --- |
MCU | Raspberry Pi Pico 2 W | Had one on hand, instant boot, low power, great for embedded systems
Display | DIANN 2.8" SPI ILI9341 | Large enough for prompts while keeping the device compact and focused
LEDs | BTF-Lighting WS2812B ECO | Frames the display, customizable, and creates a more immersive ambient experience
Button | Tactile Switch | Physical touch & fun user interaction, simple implementation
Language | MicroPython | Identical syntax to Python, primary target is microcontrollers & no OS needed = direct pin control
IDE | VS Code + Raspberry Pi Extension | Preferred environment for development & comes with Raspberry Pi Pico extension available

## Software Architecture
The application was organized as a state machine with four primary states:

- **WELCOME:** Display the invitation, keep LEDs at a warm dim glow, monitor the button and the time window.
- **PROMPT:** Run the 10-minute countdown and animate the LEDs.
- **ENCOURAGEMENT:** Show an encouraging message, LED at a warm dim glow, then go to sleep.
- **SLEEP:** Turn off the display and LEDs, waking only when the next journaling window begins.

Separating functionality into independent modules for scheduling, display rendering, LED control, timing, and user input made the project significantly easier to extend as additional features were added.

## Set Up Guidelines

- Connect wires to ILI9341 using online documentation and AI assistance. I used a mixture of this youtube video from a Boston College professor, PythonTutorials Mastering the ILI9341 Display with MicroPython, and ChatGPT for additional support. Make sure the display turns on before continuing.
- Initialize ILI9341 library to test the display. To do this, you have to download a ili9341 driver. There are a few to choose from so pick one that meets your project specifications or use cases better. I used rdagger/micropython-ili9341 as it is well documented. I asked ChatGPT which files I would need that meet my project specs and it recommend the display control, an x-glcd file for formatting typography legibly, and a font file of my choice.
    - X-GLCD: It was originally created by MikroElektronika and arranges font pixel data into columns rather than rows to match hardware memory mapping
- Configure SPI and display & make sure to click “upload project to Pico.” After successfully testing some methods to display colors and text, I was ready to move on.
- Designed screens (pen & paper) and then prototyped+programmed them one by one.
    - You’ll go back in later and replace the prototypes with function calls to methods you’ve written.
- Planned order of design interaction:
    - Display and Software Flow = what the user sees
    - Scheduling and RTC (ensuring the screen is on between set windows of time)
    - Power management (making sure the screen powers down at set times)
    - User input (button) programming
    - Visual Feedback (putting LEDs on a timer)
- Connect to wifi to set RTC clock and date 
- Connected buttons, tested, and then connected LEDS and tested
    - The LED part was a little harder for me as I wanted many LEDs lit, while the Pico is not designed to support so many LEDs. After a few youtube tutorials and a little assistance from my embedded SWE husband, I got the lights connected and learned how to animate them in the desired sequence. It requires a 5V power system and has to be plugged in externally.
- Assemble a structure for displaying the screen and hide all the wires. It is only a prototype after all so it does not need to be super pretty at this point.

Constant code refactoring was required as the project grew, as expected! Taking the approach like an embedded systems software engineer meant breaking down each system requirement and programming that logic before moving on to the next piece and connecting them. The architecture continued to be refined as I went.