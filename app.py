import argparse
import logging
import os

from kafka import KafkaConsumer


def get_arg(env, default):
    return os.getenv(env) if os.getenv(env, '') is not '' else default


def parse_args(parser):
    args = parser.parse_args()
    args.brokers = get_arg('KAFKA_BROKERS', args.brokers)
    args.topic = get_arg('KAFKA_TOPIC', args.topic)
    return args


def main(args):
    consumer = KafkaConsumer(args.topic, bootstrap_servers=args.brokers)
    for msg in consumer:
        out = msg.value if msg.value is not None else ""
        logging.info('received: ' + str(msg.value, 'utf-8'))
    logging.info('exiting')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info('starting kafka-python-listener')
    parser = argparse.ArgumentParser(
            description='listen for some stuff on kafka')
    parser.add_argument(
            '--brokers',
            help='The bootstrap servers, env variable KAFKA_BROKERS',
            default='localhost:9092')
    parser.add_argument(
            '--topic',
            help='Topic to publish to, env variable KAFKA_TOPIC',
            default='bones-brigade')
    args = parse_args(parser)
    main(args)
