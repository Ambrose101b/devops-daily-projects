# Day 4: Docker Web Server

Today I moved beyond scripts and deployed a functional web server using Docker.

### Key Skills:
- **Port Mapping:** Learned how to link Host Port 8080 to Container Port 8000.
- **Detached Mode:** Running containers in the background using `-d`.
- **Base Images:** Using Python's built-in HTTP module to serve static content.

### Access the App:
Run `docker run -p 8080:8000 devops-webserver` and visit `localhost:8080`.