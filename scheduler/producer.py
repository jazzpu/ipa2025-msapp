import os
import pika


def produce(host, body):
    user = os.environ.get("RABBITMQ_USER", "guest")
    pwd = os.environ.get("RABBITMQ_PASS", "guest")
    credentials = pika.PlainCredentials(user, pwd)
    params = pika.ConnectionParameters(host=host, credentials=credentials)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.exchange_declare(exchange="jobs", exchange_type="direct")
    channel.queue_declare(queue="router_jobs")
    channel.queue_bind(queue="router_jobs", exchange="jobs", routing_key="check_interfaces")

    channel.basic_publish(exchange="jobs", routing_key="check_interfaces", body=body)

    connection.close()

if __name__ == "__main__":
    produce("rabbitmq", b"test-message")
