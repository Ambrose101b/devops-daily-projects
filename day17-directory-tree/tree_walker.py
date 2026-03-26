import subprocess

TARGET_DIR = "/app/scandir"

try:
    print(f"🌲 Directory Tree for: {TARGET_DIR}\n")

    # Show tree structure
    subprocess.run(["tree", TARGET_DIR])

    # Count files
    files = subprocess.check_output(
        ["bash", "-c", f"find {TARGET_DIR} -type f | wc -l"],
        text=True
    ).strip()

    # Count directories
    dirs = subprocess.check_output(
        ["bash", "-c", f"find {TARGET_DIR} -type d | wc -l"],
        text=True
    ).strip()

    print("\n--------------------------------------")
    print(f"✅ Found {int(dirs)-1} folders and {files} files")

except Exception as e:
    print(f"❌ Error: {e}")