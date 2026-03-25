FROM python:3.9-slim
WORKDIR /app
COPY log_parser.py .
COPY server.log .
CMD ["python3", "log_parser.py"]
