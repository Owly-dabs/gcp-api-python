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

# Expose the port Cloud Run expects
EXPOSE 8080

# Run Uvicorn with production settings
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]