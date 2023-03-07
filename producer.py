#producer
import pika
#declaring the credentials needed for connection like host, port, username, password, exchange etc

credentials = pika.PlainCredentials('cgsqdwsf','vFm4y8aPT7I0y0wGA2W3N31yBfhI4aoe')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='dingo.rmq.cloudamqp.com', port='5672', virtual_host="cgsqdwsf",credentials= credentials,socket_timeout=5))

# credentials = pika.PlainCredentials('guest','guest')
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port='5672', virtual_host="/",credentials= credentials))

channel= connection.channel()
channel.exchange_declare('test', durable=True, exchange_type='topic')
channel.queue_declare(queue= 'A')
channel.queue_bind(exchange='test', queue='SalesOrderQueue', routing_key='A')
# channel.queue_declare(queue= 'B')
# channel.queue_bind(exchange='test', queue='B', routing_key='B')
# channel.queue_declare(queue= 'C')
# channel.queue_bind(exchange='test', queue='C', routing_key='C')
#messaging to queue named C
message= 'hello consumer!!!!!'
channel.basic_publish(exchange='test', routing_key='A', body= message)
channel.close()