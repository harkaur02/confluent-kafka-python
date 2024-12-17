# Dockerfile for IoT Producer

FROM python:3.12.3

# Set the working directory
WORKDIR /app

# Copy the Python project files into the container
COPY . .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the producer
CMD ["python", "iot_producer.py"]
