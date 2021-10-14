# https://www.rabbitmq.com/tutorials/tutorial-three-python.html
# start RabbitMQ with docker:
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
# python package for RabbitMQ
import pika
import sys

connection=pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel=connection.channel()

# message are sent to an exchange of type fanout, which broadcasts the message to all known queues
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message=' '.join(sys.argv[1:]) or "info: Hello World!"
# publish to named exchange
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()
