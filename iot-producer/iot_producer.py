# iot_producer.py

from confluent_kafka import Producer
import json
import time
import random

# Kafka Producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker address
    'client.id': 'iot-producer'
}

# Create Kafka Producer instance
producer = Producer(conf)

# Function to generate simulated IoT data
def generate_iot_data():
    temperature = random.uniform(20.0, 30.0)  # Simulate temperature data
    humidity = random.uniform(30.0, 60.0)  # Simulate humidity data
    device_id = random.randint(1, 5)  # Random IoT device ID

    return {
        'device_id': device_id,
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': time.time()
    }

# Callback function for delivery reports
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Function to send data to Kafka
def produce_data():
    while True:
        data = generate_iot_data()  # Generate data
        print(f"Sending data: {data}")  # Log data
        # Send data to Kafka topic 'iot-data'
        producer.produce('iot-data', key=str(data['device_id']), value=json.dumps(data), callback=delivery_report)
        producer.flush()  # Ensure data is delivered
        time.sleep(5)  # Simulate data every 5 seconds

if __name__ == "__main__":
    produce_data()  # Start producing data
