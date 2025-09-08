FROM python:3.12-slim

WORKDIR /app

# System deps for netmiko/paramiko (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ssh-client \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir pika pymongo netmiko ntc-templates

# Copy application code
COPY . .

# Default command runs the worker entrypoint
CMD ["python", "worker.py"]
