# https://www.rabbitmq.com/tutorials/tutorial-two-python.html
# start RabbitMQ with docker:
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
# decrease default acknowledgement timeout (30 min) in docker image:
# connect to docker image (start a bash):
## docker container exec -it rabbitmq /bin/bash
# in order to decrease the timeout to 30 s, we add the following line to the rabbitmq configuration file:
## echo consumer_timeout=30000 >> /etc/rabbitmq/conf.d/10-default-guest-user.conf
# restart the docker image
## docker restart rabbitmq
# python package for RabbitMQ
from random import random
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

# every dot "." stands for one second of computation time for the worker
# send lots of messages to the server
print('Producing messages')
for i in range(1000):
    message="Message {}".format(i)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
connection.close()
print('Done producing messages')