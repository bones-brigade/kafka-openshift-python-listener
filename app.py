import os
from kafka import KafkaConsumer


def main():
    topic = os.environ['TOPIC']
    servers = os.environ['SERVERS']
    consumer = KafkaConsumer(topic, bootstrap_servers=servers)
    for msg in consumer:
        print(str(msg.value, 'utf-8'))


if __name__ == '__main__':
    main()
