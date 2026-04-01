import shutil
import psutil
import sys

DISK_THRESHOLD = 80
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80

print("---------------------------------------------------")
print("🩺 Starting Server Health Check...")
print("---------------------------------------------------\n")

total, used, free = shutil.disk_usage("/")
disk_percent = (used / total) * 100

cpu_percent = psutil.cpu_percent(interval=1)

ram = psutil.virtual_memory()
ram_percent = ram.percent

print(f"💾 Disk Usage: {disk_percent:.2f}%")
print(f"🧠 CPU Usage:  {cpu_percent}%")
print(f"⚙️ RAM Usage:  {ram_percent}%\n")

if disk_percent > DISK_THRESHOLD or cpu_percent > CPU_THRESHOLD or ram_percent > RAM_THRESHOLD:
    print("CRITICAL WARNING: System resoureces have exceeded safe limits!")
    sys.exit(1)
else:
    print("✅ System health is NORMAL. All resources are within safe limits.")
    sys.exit(0)