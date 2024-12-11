# Use Python base image
FROM python:3.12-slim

# Set environment variables for Python optimization
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy only the requirements.txt first to take advantage of Docker caching
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose port 8080 (default for Cloud Run)
EXPOSE 8080

# Default command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
