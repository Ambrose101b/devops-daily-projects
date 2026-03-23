# Day 9: Declarative Jenkins Pipelines

## 🚀 The Mission
Transition from manual "Freestyle" jobs to **Pipeline as Code** using a `Jenkinsfile`.

## 🛠️ What I Built
* **Three-Stage Pipeline:** Automated the workflow into Checkout, Test, and Execute phases.
* **Code Validation:** Implemented a "Lint" stage using `py_compile` to catch errors before the app runs.
* **Workspace Management:** Used the Groovy `dir()` command to target files in the `day2-system-monitor` directory.

## 📋 Setup Instructions
1. Open Jenkins at `localhost:8081`.
2. Create a new **Pipeline** job named `System-Monitor-Pipeline`.
3. Set Definition to **Pipeline script from SCM**.
4. SCM: **Git** | URL: `https://github.com/Ambrose101b/devops-daily-projects.git`
5. Branch: `*/main`
6. Script Path: `day9-jenkins-pipeline/Jenkinsfile`
