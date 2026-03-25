import os
import time
import sys

# We point this to where Docker will mount the folder
DIR_NAME = "/app/server_backups"
DAYS_THRESHOLD = 7
SECONDS_IN_A_DAY = 86400

print("-----------------------------------")
print(f"🧹 Scanning '{DIR_NAME}' for files older than {DAYS_THRESHOLD} days...")
print("-----------------------------------\n")

now = time.time()
deleted_count = 0

# Check if the directory exists before scanning
if os.path.exists(DIR_NAME) and os.path.isdir(DIR_NAME):
    # Loop through just the names of the files in the directory
    for filename in os.listdir(DIR_NAME):
        # We MUST combine the folder path and the file name to work with it
        filepath = os.path.join(DIR_NAME, filename)
        
        # Make sure it is actually a file and not a sub-folder
        if os.path.isfile(filepath):
            # Check if file is older than the threshold
            if now - os.path.getmtime(filepath) > (DAYS_THRESHOLD * SECONDS_IN_A_DAY):
                os.remove(filepath) # Deletes the file
                print(f"🗑️ DELETED: {filename}")
                deleted_count += 1
            else:
                print(f"✅ KEPT: {filename} (Fresh)")
else:
    print(f"❌ ERROR: Directory {DIR_NAME} not found!")
    sys.exit(1) # Fail the Jenkins pipeline if the folder is missing

print("\n-----------------------------------")
print(f"🎉 Cleanup complete. Removed {deleted_count} old file(s).")