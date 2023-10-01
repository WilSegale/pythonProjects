import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin() == True:
    print("The script is running with administrative privileges.")
else:
    print("The script is NOT running with administrative privileges.")

