import os
from kafka import KafkaConsumer


def main():
    topic = os.environ['KAFKA_TOPIC']
    servers = os.environ['KAFKA_SERVERS']
    consumer = KafkaConsumer(topic, bootstrap_servers=servers)
    for msg in consumer:
        print(msg)


if __name__ == '__main__':
    main()
