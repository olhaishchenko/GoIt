#В цій домашній роботі ви повинні реалізувати такі класи:
# Клас AddressBook, який успадковується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу.
# Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів
# та зберігання обов'язкового поля Name.
# Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку загальну для всіх полів.
# Клас Name, обов'язкове поле з ім'ям.
# Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.

# Критерії прийому
# Реалізовано всі класи із завдання.
# Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується
# значення Record.name.value.
# Record зберігає об'єкт Name в окремому атрибуті.
# Record зберігає список об'єктів Phone в окремому атрибуті.
# Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
# AddressBook реалізує метод add_record, який додає Record у self.data.

from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = self.record


class Field:
    pass


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def del_phone(self, phone):
        self.phones.remove(Phone(phone))

    def change_phone(self, phone_old, phone_new):
        self.phones[self.phones.index(Phone(phone_old))] = Phone(phone_new)


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
