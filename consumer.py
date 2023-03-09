import pika
import os

credentials = pika.PlainCredentials('cgsqdwsf','vFm4y8aPT7I0y0wGA2W3N31yBfhI4aoe')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='dingo.rmq.cloudamqp.com', port='5672', virtual_host="cgsqdwsf",credentials= credentials,socket_timeout=5))

channel = connection.channel()
channel.exchange_declare('test', durable=True, exchange_type='topic')

#defining callback functions responding to corresponding queue callbacks
def callbackFunctionForQueueA(ch,method,properties,body):
 print('Got a message from Queue A: ', body)

#Attaching consumer callback functions to respective queues that we wrote above
channel.basic_consume(queue='A', on_message_callback=callbackFunctionForQueueA, auto_ack=True)

#this will be command for starting the consumer session
print("Starting consumer session..")
print(os.getenv("USERNAME"))
channel.start_consuming()
