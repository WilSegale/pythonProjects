import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("You are running with administrative privileges.")
else:
    print("You are not running with administrative privileges.")
