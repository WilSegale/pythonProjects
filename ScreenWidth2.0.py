import pyautogui
from screeninfo import get_monitors

def get_screen_width():
    # Get the current screen resolution
    screen_width, _ = pyautogui.size()

    # Get all the monitors
    monitors = get_monitors()

    for monitor in monitors:
        # Check if the current screen width matches the monitor width
        if monitor.x <= screen_width < monitor.x + monitor.width:
            return monitor.width
 
    # If no matching monitor found, return the width of the primary monitor
    return monitors[0].width

# Usage
width = get_screen_width()
height = get_monitors()[0].height
print(f"Screen width and height: {width} x {height}".format(width=width, height=height))
