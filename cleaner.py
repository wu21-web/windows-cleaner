import os
import platform
import easygui
import time

is_windows = None
os_name = os.name
platform_system = platform.system()
print(f"platform.system(): {platform_system}")

if os_name == 'posix':
    is_windows = False
elif os_name == 'nt':
    is_windows = True
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
    pass
elif answer == "No":
    exit(0)
else:
    print("Choice not known.")
    exit(1)
if os.path.exists("C:\\Windows\\Temp"):
    print("Will start in three seconds ...")
    time.sleep(3)
else:
    print("Target Disappeared. No need to clean.")
    exit(0)
run = True

# The path to the folder
folder_path = "C:\\Windows\Temp"

if run and is_windows:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                os.remove(file_path) 
                print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

folder_path = 'C:\\Windows\\Temp'
folder_size = get_folder_size(folder_path)
print(f"Total size of files in the folder: {folder_size} bytes.")
