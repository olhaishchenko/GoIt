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

    def iterator(self, count=2):
        records = []
        i = 0
        for record in self.data.values():
            records.append(record)
            i += 1
            if i == count:
                yield records
                records = []
                i = 0
       if len(self.data.values()) % count != 0

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

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.value}'


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
        return self.birthday.days_to_birthday()

    def __str__(self):
        return f'{self.name}: {", ".join([str(phone) for phone in self.phones])}, {self.birthday}'

    def __repr__(self):
        return f'{self.name}: {", ".join([str(phone) for phone in self.phones])}, {self.birthday}'


class Name(Field):
    pass


class Phone(Field):

    @Field.value.setter
    def value(self, value):
        if not value.isnumeric():
            raise ValueError('Wrong phones.')
        if len(value) != 12:
            raise ValueError("Phone must contains 12 symbols.")
        self._value = value

    def __eq__(self, other):
        return self.value == other.value


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        day_today = datetime.today()
        try:
            b_day = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Incorrect date format, should be `DD.MM.YYYY`")
        if b_day.date() > day_today.date():
            raise ValueError("Birthday can't be more than current year and date.")
        self._value = b_day

    def days_to_birthday(self):
        if not self._value:
            raise ValueError('Day of birthday not exists')
        day_today = datetime.today().date()
        next_b_day = datetime.strptime(self._value, "%d.%m.%Y").date()
        if day_today.month > next_b_day.month and day_today.day > next_b_day.day:
            next_b_day = next_b_day.replace(year=day_today.year + 1)
        else:
            next_b_day = next_b_day.replace(year=day_today.year)
        return (next_b_day.date()-day_today).days

    def __str__(self):
        return datetime.strftime(self.value, "%d.%m.%Y")

    def __repr__(self):
        return datetime.strftime(self.value, "%d.%m.%Y")
