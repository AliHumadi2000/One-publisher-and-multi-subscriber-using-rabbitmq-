from email import message
import queue
import pika

# create connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
# create channe from the connection
channel = connection.channel()

# declare the name of the queue
channel.queue_declare(queue='hello')
message = 'hello world!'
channel.basic_publish(exchange='', routing_key='hello', body=message)
print("[x] Sent 'hello world'")
connection.close()
