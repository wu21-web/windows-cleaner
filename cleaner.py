import os
import platform
import easygui
is_windows = False
# Using os.name
os_name = os.name

# More detailed, using platform
platform_system = platform.system()
print(f"platform.system(): {platform_system}")

if os_name == 'posix':
    pass
elif os_name == 'nt':
    print("This is Windows")

# platform.system() gives a more readable format
if platform_system == 'Linux':
    print("This is Linux")
    exit(1)
elif platform_system == 'Darwin':
    print("This is MacOS")
    exit(1)
elif platform_system == 'Windows':
    print("This is Windows")
run = False
answer = easygui.buttonbox(msg="Are you going to start? Better close other applications.")