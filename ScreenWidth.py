from screeninfo import get_monitors

def get_screen_width():
    # Get the primary monitor
    monitor = get_monitors()[0]
    return monitor.width

# Usage
width = get_screen_width()
height = get_monitors()[0].height


print(f"Screen width and height: {width} x {height}".format(width=width, height=height))
