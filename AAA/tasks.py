from celery import shared_task
import pika

from AAA.serializers import CustomUserSerializer

@shared_task
def send_registration_message(userId):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='registration_queue')
    

    channel.basic_publish(exchange='', routing_key='registration_queue', body=f'{userId}')
    connection.close()
