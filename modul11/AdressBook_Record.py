from collections import UserDict
from datetime import datetime


class AddressBook(UserDict):
    # адресна книга з контактами
    def add_record(self, name):
        self.data[name] = Record(name)

    def exist(self, name):
        return name in self.data

    def check_record(self, name):
        if not self.exist:
            raise ValueError(f"Contact {name} not exists. Create contact")

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Field:
    pass


class Record:
    # клас запис: видаляє, додає, змінює контакт
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = datetime(day=0, month=0, year=0000)

    def add_phone(self, phone_new):
        self.phones.append(Phone(phone_new))

    def change_phone(self, phone_old, phone_new):
        self.phones[self.phones.index(Phone(phone_old))] = Phone(phone_new)

    def del_phone(self, phone_old):
        self.phones.remove(Phone(phone_old))

    def __str__(self):
        return f'{self.name}: {", ".join([str(phone) for phone in self.phones])}'

    def __repr__(self):
        return f'{self.name}: {", ".join([str(phone) for phone in self.phones])}'


class Name(Field):
    def __init__(self, name):
        self.value = name

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone

    def __str__(self):
        return self.phone

    def __repr__(self):
        return self.phone

    def __eq__(self, other):
        return self.phone == other.phone
