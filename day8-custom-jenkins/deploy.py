import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True)

print("🚀 Deploying Super-Jenkins...")

# 1. Build Custom Image
run("docker build -t ambroser/jenkins-with-python:v1 .")

# 2. Stop old container
run("docker rm -f my-jenkins")

# 3. Run with TWO Volumes (Projects + Data)
# Note: ~/jenkins_data ensures your password and jobs STAY SAVED
run("""
docker run -d \
  -p 8081:8080 \
  --name my-jenkins \
  -v /home/ambrose/devops-daily-projects:/var/jenkins_home/my-projects \
  -v /home/ambrose/jenkins_data:/var/jenkins_home \
  ambroser/jenkins-with-python:v1
""")

print("✅ Done! Check http://localhost:8081 in 30 seconds.")