import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='registration_queue')
channel.basic_publish(exchange='', routing_key='registration_queue', body=f'New user registered: user')
connection.close()