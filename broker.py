import subprocess
import sys
import os

try:    
    subprocess.run(["mosquitto"])
except FileNotFoundError:
    print("Mosquitto isn't installed. The script will install it now")
    subprocess.check_call(["sudo", "apt-add-repository", "-y", "ppa:mosquitto-dev/mosquitto-ppa"])
    subprocess.check_call(["sudo", "apt", "install", "-y", "mosquitto"])
    subprocess.run(["mosquitto"])
