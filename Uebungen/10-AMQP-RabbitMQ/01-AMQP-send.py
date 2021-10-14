# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
# start RabbitMQ with docker:
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
# python package for RabbitMQ
import pika

# connect to RabbitMQ-Broker on localhost
connection=pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel=connection.channel()

# create a queue to which the message will be delivered
# the name of the queue is idempotent; if the queue exists, nothing happens
channel.queue_declare(queue='hello')

# publish the message (body) to the queue (routing_key)
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
# close the connection
connection.close()
