import os, time, pika

user = os.getenv("RABBITMQ_DEFAULT_USER")
pwd = os.getenv("RABBITMQ_DEFAULT_PASS")

def callback(ch, method, props, body):
    print(f"Body: {body.decode('utf-8')}")
    time.sleep(3)

def consume(host):
    for attempt in range(10):
        try:
            print(f"Connecting to RabbitMQ at {host} ... (try {attempt})")
            creds = pika.PlainCredentials(user, pwd)
            conn = pika.BlockingConnection(
                pika.ConnectionParameters(host=host, credentials=creds)
            )
            break
        except Exception as e:
            print(f"Failed: {e}")
            time.sleep(5)
    else:
        print("Failed to connect after 10 attempts, exiting.")
        exit(1)
    
    ch = conn.channel()
    ch.queue_declare(queue="router_jobs")
    ch.basic_qos(prefetch_count=1)
    ch.basic_consume(queue="router_jobs", on_message_callback=callback, auto_ack=True)
    ch.start_consuming()

if __name__ == "__main__":
    consume("localhost")  # Replace with your RabbitMQ host if needed