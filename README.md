# confluent-kafka-python
a Python project for IoT streaming using Kafka in KRaft mode (Kafka Raft mode) and the confluent-kafka-python library

Step-by-Step Guide:
Step 1: Install Kafka with KRaft Mode
  (Ensure you are using a Kafka version that supports KRaft mode. This feature was introduced in Kafka 2.8.0, but is fully stabilized in later versions like 3.x.x.)
  1.1 Download Kafka
  
      wget https://downloads.apache.org/kafka/3.9.0/kafka_2.13-3.9.0.tgz
      tar -xzf kafka_2.13-3.9.0.tgz
      cd kafka_2.13-3.9.0
  1.2 Start Kafka in KRaft Mode
      In KRaft mode, Kafka runs without Zookeeper. To enable KRaft mode, modify the server.properties file to configure KRaft.
      [NOTE: I have coied my working tested version of server.properties file in this Repo under config/server.properties]
        1. Open the config/server.properties file and set the following properties:
        
          process.roles=broker,controller
          node.id=1
          listeners=PLAINTEXT://localhost:9092
          log.dirs=/tmp/kafka-logs
          metadata.log.dir=/tmp/kafka-metadata-logs
          # Kafka controller's settings
          controller.quorum.voters=1@localhost:9093
  1.3  Start the Kafka broker in KRaft mode:
  
          bin/kafka-server-start.sh config/server.properties 
  
  1.4  Create a Kafka topic where IoT data will be sent:
  
          bin/kafka-topics.sh --create --topic iot-data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Step 2: Set Up Python Project:
  2.1 Create a New Python Virtual Environment to isolate the project dependencies.
  
          # Create a virtual environment
          python3 -m venv iot-kafka-env
          # Activate the virtual environment
          source iot-kafka-env/bin/activate
  2.2 Install the Required Python Libraries
      We will need the confluent-kafka library to interact with Kafka.
      
          pip install confluent-kafka requests

Step 3: Write the IoT Data Producer
  The producer will simulate IoT devices sending temperature and humidity data to the Kafka topic.
  3.1 Create the Producer Script (iot_producer.py) from this repository.
  3.2 Explanation:
      confluent_kafka.Producer: This class allows you to produce messages to Kafka.
      generate_iot_data(): This function generates random IoT data (temperature, humidity, device ID, timestamp).
      producer.produce(): Sends the generated data to the iot-data topic.
      delivery_report(): Callback function to confirm that the data was delivered to Kafka.

Step 4: Write the IoT Data Consumer
  The consumer will listen to the iot-data topic and process the data received from the producer.
  4.1 Create the Consumer Script (iot_consumer.py) from this repository.
  4.2 Explanation:
      confluent_kafka.Consumer: Connects to Kafka and consumes messages from a topic.
      consumer.subscribe(): Subscribes to the iot-data topic.
      consumer.poll(): Polls for new messages from Kafka.
      The messages are deserialized and printed out.

Step 5: Run the Producer and Consumer
  5.1 Start the Kafka Producer
    In one terminal, run the producer to start sending simulated IoT data to the Kafka topic:
    
      python3 iot_producer.py
  5.2 Start the Kafka Consumer
    In another terminal, run the consumer to start receiving and processing data from the iot-data Kafka topic:
    
      python3 iot_consumer.py


You will see the producer sending random IoT data every 5 seconds, and the consumer printing it to the console.
    

