from AdressBook_Record import AddressBook, Record

address_book = AddressBook()


def hello():  # функція привітання
    return f"How can I help you?\n\
Enter: \n'create name' (створюємо контакт)\n\
'add name phones' (додаємо ім'я та номери телефонів)\n\
'change name phone_old phone_new' (міняє старий номер телефона на новий)\n\
'del name phone' (видаляє номер телефону)\n\
'phone name' (видає номер телефону за іменем)\n\
'show' (показує всі контакти) to continue;\n\
'close or exit' to exit"


def create_new_contact(text):  # створюємо контакт
    name, phones = create_data(text)
    address_book.add_record(name)
    return f"created contact {name}"


def add_phone_func(text):  # функція додає номер або номери телефонів
    name, phones = create_data(text)
    address_book.check_record(name)
    if not phones:
        return f"No numbers added"
    for phone in phones:
        address_book[name].add_phone(phone)
    return f"Number added"


def change_phone_func(text):  # функція змінює номер телефону
    name, phones = create_data(text)
    if len(phones) < 2:
        raise IndexError(f"Please provide two phone numbers")
    number_phone_old = phones[0]
    number_phone_new = phones[1]
    address_book.check_record(name)
    address_book[name].change_phone(number_phone_old, number_phone_new)
    return f"Number changed"


def get_phone(text: str):  # функція видає номер телефону за імям
    name, phones = create_data(text)
    address_book.check_record(name)
    return address_book[name]


def del_phone(text):
    name, phones = create_data(text)
    address_book.check_record(name)
    if not phones:
        raise KeyError
    for phone in phones:
        address_book[name].del_phone(phone)
    return f"Number deleted"


def show_all():  # функція видає весь список телефонів
    return address_book.data.items()


# функції прощавання)
def bye():
    exit("Good bye")


# словник функцій
INPUT_HANDLER = {
    "hello": hello,
    "create": create_new_contact,
    "add": add_phone_func,
    "del": del_phone,
    "change": change_phone_func,
    "phone": get_phone,
    "show": show_all,
    "close": bye,
    "exit": bye
}


def input_error(func):
    def wrapper(text):
        try:
            return func(text)
        except IndexError as e:
            result = "Give me name and phone please splitted by space.\n" + str(e)
        except KeyError as e:
            result = "Enter right user's name or user's number or command.\n" + str(e)
        except ValueError as e:
            result = "Enter: add (name phone), change (name phone), \
phone (name), show all to continue; good bye, close, exit to exit.\n" + str(e)
        except TypeError as e:
            result = "Enter: add (name phone), change (name phone), \
phone (name), show all, good bye, close, exit to continue.\n" + str(e)
        return result

    return wrapper


@input_error
def call_handler(text: str):
    new_text = text
    list_text = ''
    for key in INPUT_HANDLER:
        if text.strip().lower().startswith(key):
            new_text = key
            list_text = text[len(key):]
            list_text = list_text.strip()
            break
    if list_text:
        return INPUT_HANDLER[new_text](list_text)  # визиваємо функції з аргументами
    else:
        return INPUT_HANDLER[new_text]()  # визиваємо функції без аргументів


def create_data(text):
    """
    Розділяє вхідні дані на дві частини - номер і телефон.
    Також ці данні проходять валідацію.
    Для подальшої роботи з ними.
    :param text: Строка з номером і ім'ям.
    :return: Вже розділені ім'я і номер
    """
    name, *phones = text.strip().split(' ')

    if name.isnumeric():
        raise ValueError('Wrong name.')
    for phone in phones:
        if not phone.isnumeric():
            raise ValueError('Wrong phones.')
    return name, phones


def main():
    print(hello())
    while True:
        text = input("Input command: ")
        print(call_handler(text))


if __name__ == "__main__":
    main()
