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
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Record:
    # клас запис: видаляє, додає, змінює контакт
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_new):
        self.phones.append(Phone(phone_new))

    def change_phone(self, phone_old, phone_new):
        self.phones[self.phones.index(Phone(phone_old))] = Phone(phone_new)

    def del_phone(self, phone_old):
        self.phones.remove(Phone(phone_old))

    def add_birthday(self, b_day):
        self.birthday = Birthday(b_day)

    def days_to_birthday(self):
        if not self.birthday:
            raise ValueError('Day of birthday not exists')
        day_today = datetime.today().date()
        next_b_day = datetime(self.birthday).date()
        # if day_today.month > next_b_day.month and day_today.day > next_b_day.day:
        if day_today > next_b_day:
            next_b_day.year = day_today.year + 1
        else:
            next_b_day.year = day_today.year
        return (next_b_day-day_today).days

    def __str__(self):
        return f'{self.name}: {", ".join([str(phone) for phone in self.phones])}, {self.birthday}'

    def __repr__(self):
        return f'{self.name}: {", ".join([str(phone) for phone in self.phones])}, {self.birthday.__str__()}'


class Name(Field):
    def __init__(self, name):
        self._value = None
        self.value = name

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Phone(Field):
    def __init__(self, phone):
        self._value = None
        self.value = phone

    @Field.value.setter
    def value(self, value):
        if not value.isnumeric():
            raise ValueError('Wrong phones.')
        if len(value) != 12:
            raise ValueError("Phone must contains 12 symbols.")
        self._value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        return self.value == other.value


class Birthday(Field):
    def __init__(self, birthday):
        self._value = None
        self.value = birthday

    @Field.value.setter
    def value(self, value):
        day_today = datetime.today().date()
        b_day = datetime.strptime(str(value), "%d.%m.%Y").date()
        if b_day > day_today:
            raise ValueError("Birthday can't be more than current year and date.")
        self._value = value

    # def __gt__(self, other):
    #     first_day = datetime.strptime(str(self.value), "%d.%m.%Y").date()
    #     second_day = datetime.strptime(str(other), "%d.%m.%Y").date()
    #     return first_day.month > second_day.month and first_day.day > second_day.day

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value
