# Use a slim Python image to keep it fast
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the monitor and cleanup scripts into the container
COPY monitor_disk.py .
COPY clean_logs.sh .

# Give execute permissions to the Bash script
RUN chmod +x clean_logs.sh

# Default command: Run the Python Disk Monitor first
CMD ["python3", "monitor_disk.py"]
