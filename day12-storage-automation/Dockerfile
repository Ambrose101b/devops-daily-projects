FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN chmod +x cleanup.sh
CMD ["python3", "disk_check.py"]
