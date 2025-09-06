FROM python

WORKDIR /app

# Copy code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Automatically read environment variables
ENV PYTHONUNBUFFERED=1

# Start the scheduler
CMD ["python", "scheduler.py"]
