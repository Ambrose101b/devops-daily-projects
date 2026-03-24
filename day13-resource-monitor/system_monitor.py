import psutil
import sys

cpu_usage = psutil.cpu_percent(interval=1)
ram_usage = psutil.virtual_memory().percent

print(f"📊 Current CPU Usage: {cpu_usage}%")
print(f"📊 Current RAM Usage: {ram_usage}%")

# Fail the pipeline if either is above 80%
if cpu_usage > 80 or ram_usage > 80:
    print("❌ CRITICAL: System resources are dangerously high!")
    sys.exit(1)
else:
    print("✅ System resources are healthy.")
    sys.exit(0)