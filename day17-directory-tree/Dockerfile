FROM python:3.9-slim
WORKDIR /app

RUN apt-get update && apt-get install -y tree

COPY tree_walker.py .

CMD ["python", "tree_walker.py"]
