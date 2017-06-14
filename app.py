import argparse
from kafka import KafkaConsumer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--servers', help='the kafka brokers')
    parser.add_argument('--topic', help='the kafka topic to read')
    args = parser.parse_args()

    consumer = KafkaConsumer(args.topic, bootstrap_servers=args.servers)
    for msg in consumer:
        print(msg)


if __name__ == '__main__':
    main()
