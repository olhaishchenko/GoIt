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
    def add_record(self):
        self.data[Record.name.value] =self.Record
        pass

class Record:
    def __init__(self, name, record = []):
        self.name = name

    def add_record(self):
        pass
    def del_record(self):
        pass
    def change_record(self):
        pass

class Field:
    pass
class Name:
    def __init__(self, name):
        self.name = name

class Phone:
    pass