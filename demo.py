#demo to record for my portfolio
from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont
from hardware.rtc_wifi import RTCWifi
from screen_states import welcome
from screen_states import prompts
from screen_states import encouragement
import time
from app_controller import AppController
from hardware.button import ButtonManager
from hardware.led_mgmt import LEDManager

RTCWifi.init()
print("Starting Journaling Companion Demo")

welcome.WelcomeScreen.show()

LEDManager.fill()

print("Waiting for button press...")

while not ButtonManager.button_pressed():
    time.sleep(0.05)

print("Button pressed!")

# Optional debounce
time.sleep(0.2)


prompts.PromptScreen.showAM()

LEDManager.timer_fill(10)

DisplayManager.display.clear(0x0000)

encouragement.EncouragementScreen.showAM()

time.sleep(5)

LEDManager.off()
DisplayManager.display.clear(0x0000)

print("Demo complete.")