import os
from consumer import consume


def worker():
    host = os.getenv("RABBITMQ_HOST", "localhost")
    consume(host)


if __name__ == '__main__':
    worker()
