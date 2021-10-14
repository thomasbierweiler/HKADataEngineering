# https://www.rabbitmq.com/tutorials/tutorial-three-python.html
# start RabbitMQ with docker:
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
# python package for RabbitMQ
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

# message are sent to an exchange of type fanout, which broadcasts the message to all known queues
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# exclusive=True: delete the queue if the consumer connection is closed
result=channel.queue_declare(queue='', exclusive=True)
queue_name=result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
