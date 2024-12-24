import os

def get_cpu_temp():
    temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    celsius = float(temp) / 1000  # Convert from millidegrees to degrees
    fahrenheit = (celsius * 9 / 5) + 32
    return celsius, fahrenheit

celsius, fahrenheit = get_cpu_temp()
print(f"CPU Temperature: {celsius:.2f}°C / {fahrenheit:.2f}°F")
