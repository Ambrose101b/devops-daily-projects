# Step 1: Use a tiny version of Python as our base
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Install the 'free' command (procps package)
# We use -y to auto-confirm and then clean up to keep the image small
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*
# Step 3: Copy our script into the container

COPY monitor.py .

# Step 4: Run the script when the container starts
CMD ["python", "monitor.py"]