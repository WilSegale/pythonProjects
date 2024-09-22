from screeninfo import get_monitors

# Get the primary monitor
primary_monitor = get_monitors()[0]

# Get the resolution of the primary monitor
width, height = primary_monitor.width, primary_monitor.height

print("Resolution of primary monitor:")
print(f"Width: {width}px, Height: {height}px")
