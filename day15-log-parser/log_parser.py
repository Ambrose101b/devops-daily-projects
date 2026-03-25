import sys

log_file = "server.log"
error_count = 0
not_found_count = 0

print(f"🔍 Scanning {log_file}...")

try:
    # Open and read the file line by line
    with open(log_file, 'r') as file:
        for line in file:
            if "ERROR" in line:
                error_count += 1
            if "404" in line:
                not_found_count += 1

    # Print the final report
    print("-----------------------------------")
    print("📊 LOG ANALYSIS REPORT")
    print(f"❌ Critical ERRORs found: {error_count}")
    print(f"⚠️ 404 Not Found errors: {not_found_count}")
    print("-----------------------------------")

    # DevOps Logic: Fail the build if we have more than 2 critical errors
    if error_count > 2:
        print("🚨 THRESHOLD BREACHED: Too many critical errors! Failing pipeline.")
        sys.exit(1)
    else:
        print("✅ Log health is acceptable.")
        sys.exit(0)

except FileNotFoundError:
    print(f"❌ CRITICAL: {log_file} does not exist!")
    sys.exit(1)