#!/bin/bash

docker rm -f my-jenkins

docker run -d -p 8081:8080 -p 50000:50000 --name my-jenkins jenkins/jenkins:lts-jdk17

echo "Jenkins is starting up..."
echo "Wait 30 seconds and run: docker logs my-jenkins to get the admin password."