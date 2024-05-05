import pika

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='hello')

# Publish a message to the queue
channel.basic_publish(exchange='', routing_key='hello', body='Hello, RabbitMQ!')

print("Message sent to RabbitMQ")

# Close the connection
connection.close()

