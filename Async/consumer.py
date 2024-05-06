import pika


QUEUE_NAME = "registration_queue"

# Establish connection to RabbitMQ server

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)
    

# Define a callback function to process incoming messages
def callback(ch, method, properties, body):
    print(f"Received message: {body}")
    

# Consume messages from the queue
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

print('Waiting for messages. To exit press CTRL+C')

# Start consuming messages
channel.start_consuming()
