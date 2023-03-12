from faker import Faker


from modul7.modul7_2.src.db import session
from modul7.modul7_2.src.models import Student

fake = Faker()


def create_students():
    for _ in range(10):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(student)
    session.commit()


if __name__ == '__main__':
    create_students()