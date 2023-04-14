# python script showing battery details
import psutil

battery = psutil.sensors_battery()
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
if battery:
   battery = psutil.sensors_battery()
   print("Battery percentage : ", battery.percent)
   print("Power plugged in : ", battery.power_plugged)
   print("Battery left : ", convertTime(battery.secsleft))

else:
    print("No battery found.")