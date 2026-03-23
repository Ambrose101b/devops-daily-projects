# Day 6: Jenkins Containerization

Today I successfully deployed **Jenkins**, a premier Open Source Automation Server, using Docker.

### 📘 Concepts Learned:
* **Automated Pulls:** Docker automatically fetches official images from Docker Hub if not found locally.
* **Multi-Port Mapping:** Mapping 8081 for the UI and 50000 for build agents.
* **LTS (Long Term Support):** Using stable versions of software for production reliability.

### 💻 Setup Instructions:
1. Run the script: `bash install_jenkins.sh`
2. Access Jenkins at: `http://localhost:8081`
3. Retrieve the initial password: `docker logs my-jenkins`