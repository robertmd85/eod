from confluent_kafka import Producer
from os import getenv
from dotenv import load_dotenv
load_dotenv()


kafka_password = getenv("KAFKA_PASSWORD")
kafka_username = getenv("KAFKA_USERNAME")
produce_config = {
    'bootstrap.servers': 'pkc-ldvj1.ap-southeast-2.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': kafka_username,
    'sasl.password': kafka_password
    }

producer = Producer(produce_config)


def produce(topic: str, message: str) -> None:
    producer.produce(topic, message)
    producer.flush()
    print(f"Produced message: {message}")
