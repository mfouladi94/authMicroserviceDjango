from celery import shared_task
import pika

@shared_task
def send_registration_message(username):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='registration_queue')
    channel.basic_publish(exchange='', routing_key='registration_queue', body=f'New user registered: {username}')
    connection.close()
