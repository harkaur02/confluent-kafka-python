# iot_consumer.py

from confluent_kafka import Consumer, KafkaException, KafkaError
import json

# Kafka Consumer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'iot-group',
    'auto.offset.reset': 'earliest'  # Start reading from the earliest message
}

# Create Kafka Consumer instance
consumer = Consumer(conf)

# Function to consume messages from Kafka
def consume_data():
    # Subscribe to the 'iot-data' topic
    consumer.subscribe(['iot-data'])

    try:
        while True:
            # Poll for new messages
            msg = consumer.poll(timeout=1.0)  # Wait for 1 second
            if msg is None:
                continue  # No message, continue polling
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition reached
                    print(f"End of partition reached {msg.partition()} at offset {msg.offset()}")
                else:
                    # Error
                    raise KafkaException(msg.error())
            else:
                # Successfully received message
                data = json.loads(msg.value().decode('utf-8'))  # Deserialize message
                print(f"Received data: {data}")

    finally:
        # Close the consumer
        consumer.close()

if __name__ == "__main__":
    consume_data()  # Start consuming data
