import os
import json
import pika
import time

RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
QUEUE_NAME = 'enrollment_queue'

def get_connection():
    try:
        params = pika.ConnectionParameters(
            host=RABBITMQ_HOST,
            connection_attempts=1,
            socket_timeout=2
        )
        connection = pika.BlockingConnection(params)
        return connection
    except Exception as e:
        raise e

def publish_enrollment(class_id, student_id):
    try:
        connection = get_connection()
        channel = connection.channel()
        channel.queue_declare(queue=QUEUE_NAME, durable=True)
        
        message = {
            'class_id': class_id,
            'student_id': student_id,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        channel.basic_publish(
            exchange='',
            routing_key=QUEUE_NAME,
            body=json.dumps(message),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        
        connection.close()
        print(f"Mensagem publicada: {message}")
    except Exception as e:
        print(f"Erro ao publicar mensagem: {e}")
