import pika

from time import sleep

from models import Contact


def main():

    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='send_message')

    print(' [*] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        contacts = Contact.objects()
        contact_id = body.decode()
        contact_email = contacts(id=contact_id)[0].email
        sleep(1)
        print(f" [x] Sent message to contact's email: '{contact_email}' with id: {contact_id}")
        contacts(id=contact_id)[0].update(result=True)

    channel.basic_consume(queue='send_message', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    main()