import psutil
from datetime import datetime
import csv
import os
import time

def get_system_info():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get CPU, memory, and disk usage using psutil
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    return [now, cpu, memory, disk]

def write_log(data):
    file_exists = os.path.isfile("log.csv")
    with open("log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "CPU", "Memory", "Disk"])
        writer.writerow(data)

if __name__ == "__main__":
    # Repeat the log process 5 times with 10-second intervals
    for _ in range(5):
        system_info = get_system_info()
        write_log(system_info)
        if _ < 4:  # Don't sleep after the last iteration
            time.sleep(10)
