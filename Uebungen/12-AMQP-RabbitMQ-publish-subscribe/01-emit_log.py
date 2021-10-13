# https://www.rabbitmq.com/tutorials/tutorial-three-python.html
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
