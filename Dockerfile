# Use an official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Install system dependencies for Pillow (libjpeg, zlib)
RUN apt-get update && apt-get install -y libjpeg-dev zlib1g-dev

# Copy project files into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 8000

# Run the Flask app
CMD ["python", "app.py"]
