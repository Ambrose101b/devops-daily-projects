#!/bin/bash

# This path is INSIDE the Jenkins container (the bridge)
PROJECT_PATH="/var/jenkins_home/my-projects/day2-system-monitor"

echo "------------------------------------------"
echo "Jenkins Automation Triggered: $(date)"
echo "------------------------------------------"

# Move to the project folder
cd $PROJECT_PATH || { echo "Folder not found!"; exit 1; }

echo "Verifying files in volume:"
ls -l

echo "Executing Monitor..."
# Note: This will fail until Day 8 installs Python in Jenkins
python3 monitor.py || echo "Wait for Day 8 to install Python in Jenkins!"

echo "------------------------------------------"
