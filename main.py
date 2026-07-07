from hardware.display import DisplayManager, color565
from drivers.xglcd_font import XglcdFont


"""
Main will be used to determine scheduling logic. It will check if the time is between 7 - 10AM & 7 - 10PM to turn on the welcome screen

Logic Tree:
---- Is it between 7 and 10AM or 7 and 10PM?
> If yes : show welcome screen & wait for button push
> If no : sleep
"""