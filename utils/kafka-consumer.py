from confluent_kafka import Consumer
from os import getenv
from dotenv import load_dotenv
load_dotenv()

kafka_password = getenv("KAFKA_PASSWORD")
kafka_username = getenv("KAFKA_USERNAME")

consumer_config = {
    'bootstrap.servers': 'pkc-ldvj1.ap-southeast-2.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'group.id': 'stock_prices',
    'auto.offset.reset': 'earliest',
    'sasl.username': kafka_username,
    'sasl.password': kafka_password,
    'auto.offset.reset': 'latest',
    'enable.auto.commit': True,
}

consumer = Consumer(consumer_config)


async def consume(topic: str) -> None:
    consumer.subscribe([topic])
    try:
        while True:
            print("Waiting for message...")
            msg = await consumer.poll(1.0)
            if msg is None:
                continue
            elif msg.error():
                print(f'Consumer error: {msg.error()}')
                continue
            else:
                print(f'Consumed message: {msg.value().decode("utf-8")}')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await consumer.close()
        print("Consumer closed.")


consume("stock_prices")
