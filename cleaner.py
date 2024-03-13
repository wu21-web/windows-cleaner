import os
import platform
import easygui
import time

is_windows = None
# Using os.name
os_name = os.name

# More detailed, using platform
platform_system = platform.system()
print(f"platform.system(): {platform_system}")

if os_name == 'posix':
    is_windows = False
elif os_name == 'nt':
    is_windows = True
# platform.system() gives a more readable format
if platform_system == 'Linux':
    print("Windows Cleaner 1.1 built on Linux")
    print("Application Not Avaliable")
    exit(1)
elif platform_system == 'Darwin':
    print("Windows Cleaner 1.1 built on Mac OS X Vertura")
    print("Application Not Avaliable")
    exit(1)
elif platform_system == 'Windows':
    print("Windows Cleaner 1.1 built on Windows")
run = False
answer = easygui.buttonbox(msg="Are you going to start? Better close other applications.", title="Confirm", choices=("Yes", "Not Now"), default_choice = "Yes", image=None, images=None)
if answer == "Yes":
    run = True
elif answer == "No":
    exit(0)
else:
    print("Choice not known.")
    exit(1)
if os.path.exists(r"C:\Windows\temp"):
    print("Will start in three seconds ...")
    time.sleep(3)
else:
    print("Target Disappeared. No need to clean.")
    exit(0)

    