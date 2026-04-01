FROM python:3.9-slim
WORKDIR /app
RUN pip install psutil
COPY health_check.py .
CMD ["python", "health_check.py"]
