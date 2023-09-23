from DontEdit import *


if platform != "win32":
    def MacOrLinux():
        if os.geteuid() == 0:
            print(f"{BRIGHT}{RED}WARNING:{RESET} It's recommended not to run this program with sudo.")
            print(f"Running the program with sudo privileges might have unintended consequences.")
            print(f"Consider running the program without sudo.")
            exit(1)
        else:
            battery = psutil.sensors_battery()

            def convertTime(seconds):
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                return "%d:%02d:%02d" % (hours, minutes, seconds)

            if battery:
                battery = psutil.sensors_battery()
                if battery.power_plugged == 0:
                    print(f"{BRIGHT}{YELLOW}Battery percentage: {GREEN}{battery.percent}%")
                    print(f"{YELLOW}Power plugged in: {RED}{battery.power_plugged}")
                    print(f"{YELLOW}Battery left: {GREEN}{convertTime(battery.secsleft)}{RESET}")
                else:
                    print(f"{BRIGHT}{YELLOW}Battery percentage: {GREEN}{battery.percent}%")
                    print(f"{YELLOW}Power plugged in: {GREEN}{battery.power_plugged}")
                    print(f"{YELLOW}Battery left: {RED}{convertTime(battery.secsleft)}{RESET}")
            else:
                print(f"{RED}{BRIGHT}[-] No battery found.{RESET}")
    MacOrLinux()
else:
    def Windows():
        # Check if the script is running with administrative privileges
        def is_admin():
            try:
                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False

        if is_admin():
            print(f"WARNING: It's recommended not to run this program with administrative privileges.")
            print(f"Running the program with admin privileges might have unintended consequences.")
            print(f"Consider running the program without admin privileges.")
        else:
            battery = psutil.sensors_battery()

            def convertTime(seconds):
                minutes, seconds = divmod(seconds, 60)
                hours, minutes = divmod(minutes, 60)
                return "%d:%02d:%02d" % (hours, minutes, seconds)

            if battery:
                if battery.power_plugged == 0:
                    print(f"Battery percentage: {battery.percent}%")
                    print(f"Power plugged in: {battery.power_plugged}")
                    print(f"Battery left: {convertTime(battery.secsleft)}")
                else:
                    print(f"Battery percentage: {battery.percent}%")
                    print(f"Power plugged in: {battery.power_plugged}")
                    print(f"Battery left: {convertTime(battery.secsleft)}{RESET}")
            else:
                print(f"{BRIGHT}{RED}[-]{RESET} No battery found.")
    Windows()