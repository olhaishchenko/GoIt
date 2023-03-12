import pika
from models import Contact
from create_db import generate_contacts, get_contact_ids


def main(contacts: list[Contact]):
    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue="send_message")
    for nd in get_contact_ids(contacts):
        channel.basic_publish(exchange='', routing_key='send_message', body=str(nd))
        print(f" [x] Sent id: {nd}")
    connection.close()


if __name__ == '__main__':
    contacts = generate_contacts(5)
    main(contacts)