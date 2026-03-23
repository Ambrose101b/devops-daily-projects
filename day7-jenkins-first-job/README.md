# Day 7: Scripted Automation with Jenkins

Today I moved my automation logic out of the Jenkins UI and into a version-controlled shell script.

### Key Concepts:
- **Separation of Concerns:** Jenkins manages the *schedule*, but the Shell Script manages the *logic*.
- **Volume Mapping:** Jenkins accesses my local Ubuntu files via the `/var/jenkins_home/my-projects` mount.
- **Cron Scheduling:** Configured the job to run every minute using `* * * * *`.

### How to use:
The Jenkins job `System-Health-Check` is configured to run `bash /var/jenkins_home/my-projects/day7-jenkins-first-job/run_health_check.sh`.