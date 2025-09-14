# Use official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Use the port provided by Cloud Run ($PORT environment variable)
# Default to 8080 for local development
ENV PORT=8080

# Expose the port (mostly for documentation, Cloud Run ignores this)
EXPOSE $PORT

# Run Uvicorn with production settings
CMD uvicorn api:app --host 0.0.0.0 --port $PORT