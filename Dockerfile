# Use official Python image
FROM python:3.11-slim


# Set environment variables

# Create app directory
WORKDIR /

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./app /app
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

# Expose API port
EXPOSE 5000

# Start the server
# CMD ["python", "main.py"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
