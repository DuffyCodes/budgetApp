# Use official Python image
FROM python:3.11-slim


# Set environment variables

# Create app directory
WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

# Expose API port
EXPOSE 5000

WORKDIR /app

# Start the server
CMD ["python", "main.py"]