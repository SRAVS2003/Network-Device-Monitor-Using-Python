import os
import time
from datetime import datetime

def ping_device(ip):
    response = os.system(f"ping -n 1 {ip} > nul")  # Windows
    return "UP" if response == 0 else "DOWN"

print("Network Device Status Monitor\n")
with open("devices.txt", "r") as file:
    devices = [ip.strip() for ip in file.readlines()]

log_file = "network_log.txt"

while True:
    print("\nChecking devices...")
    with open(log_file, "a") as log:
        for ip in devices:
            status = ping_device(ip)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = f"[{current_time}] Device {ip} is {status}"
            print(result)
            log.write(result + "\n")
    time.sleep(5)
