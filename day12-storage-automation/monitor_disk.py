import shutil
import sys

def check_storage():
    total, used, free = shutil.disk_usage("/")
    usage_percent = (used / total) * 100

    print(f"current disk usage: {usage_percent:.2f}%")

    if usage_percent > 80:
        print("🔴 ALERT: Disk usage is critical!")
        sys.exit(1) # This tells Jenkins the build FAILED
    else:
        print("🟢 SUCCESS: Disk usage is within safe limits.")
        sys.exit(0)

check_storage()