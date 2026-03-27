import subprocess
import sys
from pathlib import Path

# We point this to where Docker will mount the volume
LOG_DIR = Path("/app/logs")
LOG_FILE = LOG_DIR / "app.log"
ROTATED_FILE = LOG_DIR / "app.log.1"

print("---------------------------------------------------")
print(f"🔄 Starting Log Rotation for: {LOG_FILE}")
print("---------------------------------------------------\n")

if not LOG_FILE.exists():
    print(f"❌ ERROR: {LOG_FILE} does not exist. Check volume mapping!")
    sys.exit(1)

try:
    # 1. Rename app.log to app.log.1 using Linux 'mv' command
    print(f"📄 Renaming active log: {LOG_FILE.name} -> {ROTATED_FILE.name}")
    subprocess.run(["mv", str(LOG_FILE), str(ROTATED_FILE)], check=True)

    # 2. Compress app.log.1 using Linux 'gzip' command
    # Note: gzip automatically adds '.gz' and deletes the original uncompressed file!
    print(f"🗜️ Compressing log file: {ROTATED_FILE.name} -> {ROTATED_FILE.name}.gz")
    subprocess.run(["gzip", "-f", str(ROTATED_FILE)], check=True)

    # 3. Create a fresh, empty app.log using Linux 'touch' command
    print(f"✨ Creating fresh log file: {LOG_FILE.name}")
    subprocess.run(["touch", str(LOG_FILE)], check=True)

    print("\n---------------------------------------------------")
    print("✅ Log rotation and compression complete!")

except subprocess.CalledProcessError as e:
    # If any of the Linux commands fail, this catches the error and stops the script
    print(f"❌ ERROR: A system command failed: {e}")
    sys.exit(1)