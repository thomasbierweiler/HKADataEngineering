# https://www.rabbitmq.com/tutorials/tutorial-two-python.html
# start RabbitMQ with docker:
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
# python package for RabbitMQ
import pika
import time
import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] {} Received {}".format(datetime.datetime.now(),body.decode()))
    time.sleep(body.count(b'.'))
    print(" [x] {} Done".format(datetime.datetime.now()))
    # acknowledge the message; make sure that the message is delivered and processed by a worker
    ch.basic_ack(delivery_tag=method.delivery_tag)

# give one message to a worker at a time, i.e. don't dispatch a new message to a worker until it has processed and acknowledged the previous one
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()
