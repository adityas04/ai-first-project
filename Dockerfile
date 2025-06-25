# Start from official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project files into the container
COPY . /app/

# (Optional) Expose a port if your main.py starts a web server
# EXPOSE 8000

# Run the main script
CMD ["python", "main.py"]
