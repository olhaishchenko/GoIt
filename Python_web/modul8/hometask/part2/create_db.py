from faker import Faker

from random import randint

from models import Contact


def generate_contacts(contact_count: int):
    Contact.drop_collection()
    faker = Faker()
    generated_contacts = []
    for _ in range(contact_count):
        new_contact = Contact(fullname=faker.name())
        new_contact.age = randint(16, 80)
        new_contact.email = faker.email()
        new_contact.phoneNumber = faker.phone_number()
        new_contact.country = faker.country()
        new_contact.save()
        generated_contacts.append(new_contact)
    return generated_contacts


def get_contact_ids(contacts: list[Contact]):
    return [contact.id for contact in contacts]