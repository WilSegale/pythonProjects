import matplotlib.pyplot as plt
import plotly.graph_objects as go
import shutil
from sys import platform

# Bar graph data
import string
if platform == "win32":
    from ctypes import windll

    def get_drives():
        drives = []
        bitmask = windll.kernel32.GetLogicalDrives()
        for letter in string.ascii_uppercase:
            if bitmask & 1:
                drives.append(letter)
            bitmask >>= 1

        return drives

    if __name__ == '__main__':
        print (get_drives())    # On my PC, this prints ['A', 'C', 'D', 'F', 'H']
        
    print("Input the name of the drive you want to the amount of space remaning on")
    drives = input(">>> ")

    total,used,free = shutil.disk_usage(drives+":/")
    total // (2 ** 30)
    free // (2 ** 30)
    used // (2 ** 30) 
    labels = ['total','Used', 'Free']
    values = [total,used,free]
    fig = go.Figure(data=[go.Bar(x=labels, y=values, marker=dict(opacity=0.5))])
    fig.show()
    fig, ax = plt.subplots()

    # Create bar graph
    ax.bar(labels, values)

    # Add shadow effect to bars
    for patch in ax.patches:
        patch.set_alpha(0.5)
else:
    print('wrong os')