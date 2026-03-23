import os

folders = ["scripts", "config", "logs"]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Created directory: {folder}")
    else:
        print(f"Directory {folder} already exists")

with open("logs/setup.logs", "w") as log_file:
    log_file.write("workspace setup completed successfully.\n")

print("Setup complete!")