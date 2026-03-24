import shutil
import sys

total, used, free = shutil.disk_usage("/")
percent = (used / total) * 100

print(f"disk usage : {percent:.2f}%")

if percent > 80:
    print("Disk is too full")
    sys.exit(1)
else:
    print("Disk health is good")
    sys.exit(0)