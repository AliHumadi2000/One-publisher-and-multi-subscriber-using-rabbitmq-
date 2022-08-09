from email import message
import queue
import pika

#create connection
connection=pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
#create channe from the connection
channel=connection.channel()

#declare the name of the queue
channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):
    print("Recieved %r "%body)
channel.basic_consume(
    queue='hello',on_message_callback=callback,auto_ack=True
)
print("Waitng for message clik CTRL+C to exit")
channel.start_consuming()