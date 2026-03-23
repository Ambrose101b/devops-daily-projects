import subprocess
import datetime

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

disk = subprocess.check_output(["df", "-h", "/"], text=True)
mem = subprocess.check_output(["free", "-m"], text=True)

report = f"--- Report: {now} ---\nDisk:\n{disk}\nMemory:\n{mem}\n"

print(report)

with open("system_health.log", "a") as f:
    f.write(report + "\n")