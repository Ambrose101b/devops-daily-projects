FROM python:3.9-slim
WORKDIR /app
# Copy the HTML file into the container
COPY index.html .
# Start a simple Python web server on port 8000
CMD ["python", "-m", "http.server", "8000"]