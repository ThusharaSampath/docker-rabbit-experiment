import pika
import os

username = os.getenv("USERNAME")
vhost = os.getenv("VHOST")
host = os.getenv("HOST")
password = os.getenv("PASSWORD")
queueName = "TestQueue"
exchange = 'choreo'

if (username != None and vhost != None and host != None and password != None):

    credentials = pika.PlainCredentials(username, password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host, port='5672', virtual_host=vhost, credentials=credentials, socket_timeout=5))

    channel = connection.channel()
    channel.exchange_declare('choreo', durable=True, exchange_type='topic')

    # create a queue in rabbitMQ
    channel.queue_declare(queue=queueName)

    # defining callback function to incoming queue messages
    def callbackFunctionForQueueA(ch, method, properties, body):
        print('Message is received from Queue {}. Message is : '.format(
            queueName), body)

    # attaching consumer callback function to the queue
    channel.basic_consume(
        queue=queueName, on_message_callback=callbackFunctionForQueueA, auto_ack=True)

    print("Starting consumer session..")

    # this will be command for starting the consumer session
    channel.start_consuming()
else:
    print("One or many environment variables was/were not set.")
