from collections import UserDict


class AddressBook(UserDict):
    # адресна книга з контактами
    def add_record(self, name):
        self.data[name] = Record(name)

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

    def add_phone(self, phone_new):
        self.phones.append(Phone(phone_new))

    def change_phone(self, phone_old, phone_new):
        self.phones[self.phones.index(Phone(phone_old))] = Phone(phone_new)

    def del_phone(self, phone_old):
        self.phones.remove(Phone(phone_old))

    # def get_phone(text: str):  # функція видає номер телефону за імям
    #     name = text[0].capitalize()
    #     kontakt_number[name]  # перевірка існування ім'я, штучна помилка
    #     return kontakt_number[name]
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

# build CLI bot to work with AddressBook
# The bot should ask for the input and work in infinite loop
# on "create" it should create a new record in the AddressBool
# on "list" it should print all the records in the AddressBook
# on "find" it should ask for the name and print the record
# on "exit" it should exit the program
# on "help" it should print the list of commands
# on "add" it should ask for the name and phone and add the phone to the record
# on "change" it should ask for the name and phone and change the phone in the record
# on "delete" it should ask for the name and phone and delete the phone from the record

# CLIAddressBook is a class that implements the same functionality as the main function via CLI
# The class should have a method run that starts the CLI
class CLIAddressBook:
    def __init__(self):
        self.book = AddressBook()

    def run(self):
        print('Hello to the AddressBook CLI tool\n')
        while True:
            command = input('Enter command: ')
            # create name - if command start with prefix `create` then create a new record in the AddressBook with "name" value
            if command.startswith('create'):
                name = command.split(' ')[1]
                self.handler_create(name)
            elif command.startswith('list'):
                self.handler_list()
            elif command.startswith('find'):
                name = command.split(' ')[1]
                self.handler_find(name)
            elif command == 'exit':
                print('Bye!')
                exit(0)
            elif command == 'help':
                self.print_help()
            elif command.startswith('add'):
                name, phone = command.split(' ')[1:]
                self.handler_add(name, phone)
            elif command.startswith('change'):
                name, phone_old, phone_new = command.split(' ')[1:]
                self.handler_change(name, phone_old, phone_new)
            elif command.startswith('delete'):
                name, phone = command.split(' ')[1:]
                self.handler_delete(name, phone)
            else:
                print('Unknown command')

    def print_help(self):
        print('create, list, find, exit, help, add, change, delete')

    def handler_create(self, name):
        self.book.add_record(name)

    def handler_list(self):
        print(self.book)

    def handler_find(self, name):
        print(self.book[name])

    def handler_add(self, name, phone):
        self.book[name].add_phone(phone)

    def handler_change(self, name, phone_old, phone_new):
        self.book[name].change_phone(phone_old, phone_new)

    def handler_delete(self, name, phone):
        self.book[name].del_phone(phone)


def main():
    cli = CLIAddressBook()
    cli.run()

if __name__ == "__main__":
    main()
