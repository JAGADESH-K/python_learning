import psutil
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    print("\n🧐 System Monitor 🧐\n")
    print(f"CPU: {cpu}% used")
    print(f"RAM: {ram.percent}% ({round(ram.used / 1e9 / 2)} GB used of {round(ram.total / 1e9 / 2)} GB)")
    print(f"DISK: {disk.percent}% ({round(disk.used / 1e9 / 2)} GB used of {round(disk.total / 1e9 / 2)} GB)")

if __name__ == "__main__":
    try:
        while True:
            clear_screen()
            show_stats()
            time.sleep(3)
    except KeyboardInterrupt:
        print("Monitor stopped.")
