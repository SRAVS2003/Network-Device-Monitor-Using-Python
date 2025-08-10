# Network-Device-Monitor-Using-Python
Network Device Status Monitor
A Python-based tool for monitoring the connectivity of multiple network devices by sending periodic ping requests.
It displays real-time device status in the console and saves logs with timestamps for future reference, helping network administrators track uptime and troubleshoot issues effectively.

Table of Contents
Features

Installation

Usage

Configuration

Code Overview

Dependencies

Contributing

License

Features
Real-time Monitoring: Continuously checks the availability of multiple devices.

Device Status Tracking: Displays whether each device is UP or DOWN.

Logging: Saves connectivity results to a log file with timestamps.

Configurable Devices: Easily modify the list of devices to monitor.

Simple & Lightweight: Runs in any Python 3 environment without complex setup.

Installation
Clone the Repository


git clone https://github.com/your-username/network-device-status-monitor.git
cd network-device-status-monitor
Set Up a Virtual Environment (Optional but Recommended)


python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Required Libraries


pip install ping3
Usage
Edit the Device List
Open monitor.py and update the devices list:

python

devices = ["8.8.8.8", "1.1.1.1", "127.0.0.1"]
Run the Script


python monitor.py
Sample Output



Checking devices...
Device 8.8.8.8 is UP
Device 1.1.1.1 is UP
Device 127.0.0.1 is UP
Log File
All status checks are stored in network_log.txt:


2025-08-10 14:30:01 - Device 8.8.8.8 is UP
2025-08-10 14:30:01 - Device 1.1.1.1 is UP
Configuration
You can adjust:

Ping Interval: Change time.sleep(5) to set the check frequency.

Log File Name: Modify the filename in the open() function.

Code Overview
Main Components:

devices list: Contains IP addresses or hostnames to monitor.

Ping Function: Uses ping3 to check connectivity.

Logging: Writes results to both console and log file.

Dependencies
Python 3.x

ping3 (Install via pip install ping3)

Contributing
Contributions are welcome!

Fork this repository

Create a new branch (feature/your-feature)

Commit and push changes

Open a Pull Request


