FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY uptime_check.py .

CMD ["python3", "uptime_check.py"]

