# 1. Start with the official Jenkins image
FROM jenkins/jenkins:lts-jdk17

# 2. Switch to 'root' (Administrator) to install software
USER root

# 3. Update the package list and install Python 3
RUN apt-get update && apt-get install -y python3 python3-pip

# 4. Switch back to the 'jenkins' user for safety
USER jenkins