# Day 9: Declarative Jenkins Pipelines

## 🚀 The Mission
Move away from "Freestyle" jobs and implement **Pipeline as Code** using a `Jenkinsfile`.

## 🛠️ What I Built
* **Automated Workflow:** A 3-stage pipeline (Checkout -> Test -> Execute).
* **Code Validation:** Added a "Lint" stage that checks Python syntax before running the app.
* **Cross-Folder Execution:** Used Groovy's `dir()` command to target scripts in other project folders.

## 📋 How to Setup this Pipeline
1. Create a new **Pipeline** job in Jenkins named `Day9-System-Pipeline`.
2. Under **Pipeline Definition**, select `Pipeline script from SCM`.
3. Set SCM to **Git** and paste my repo URL.
4. Set **Branch Specifier** to `*/main`.
5. Set **Script Path** to `day9-jenkins-pipeline/Jenkinsfile`.

## 🧠 Lessons Learned
I learned that DevOps isn't just about running scripts; it's about building a **repeatable process**. If I break the Python code in Day 2, this Pipeline will catch it in the "Test" stage and stop the "Execute" stage from running!