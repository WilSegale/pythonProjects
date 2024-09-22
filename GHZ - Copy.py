import psutil

def get_cpu_frequency():
    freq = psutil.cpu_freq()
    if freq is not None:
        return freq.current / 1000  # Convert to GHz
    else:
        return "N/A"

print("CPU Frequency: {} GHz".format(get_cpu_frequency()))
if get_cpu_frequency() <= float(3.0):
    print("your computer is slow")
else:
    print("your computer is fast")