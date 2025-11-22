import json
import time
from message_queue import get_connection, QUEUE_NAME
from database import SessionLocal, EnrollmentEvent

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Mensagem recebida: {message}")
    
    # Salvar evento no banco de dados
    db = SessionLocal()
    try:
        event = EnrollmentEvent(
            class_id=message['class_id'],
            student_id=message['student_id'],
            timestamp=message['timestamp']
        )
        db.add(event)
        db.commit()
        print(f"Evento de inscrição registrado: Aluno {message['student_id']} na Turma {message['class_id']}")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")
        db.rollback()
    finally:
        db.close()
    
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    print("Aguardando RabbitMQ...")
    time.sleep(10)
    
    connection = get_connection()
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    
    print(f"Consumidor aguardando mensagens na fila '{QUEUE_NAME}'...")
    channel.start_consuming()

if __name__ == '__main__':
    main()
