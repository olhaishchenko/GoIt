from collections import UserDict


class AddressBook(UserDict):
    # адресна книга з контактами
    def add_record(self, name):
        self.data[name] = Record(name)

    # def __str__(self):
    #     return f'{self.data}'
    #
    # def __repr__(self):
    #     return f'{self.data}'


class Field:
    pass


class Record:
    # клас запис: видаляє, додає, змінює контакт
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_new):
        self.phones.append(Phone(phone_new))

    def change_phone(self, phone_old, phone_new):
        self.phones[self.phones.index(Phone(phone_old))] = Phone(phone_new)

    def del_phone(self, phone_old):
        for phone in self.phones:
            if phone_old == phone:
                self.phones.remove(Phone(phone_old))

    # def __str__(self):
    #     return f'{self.name}: {", ".join([str(phone) for phone in self.phones])}'
    #
    # def __repr__(self):
    #     return f'{self.name}: {", ".join([str(phone) for phone in self.phones])}'


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