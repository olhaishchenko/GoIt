from AdressBook_Record import AddressBook

new_book = AddressBook()


def hello():# функція привітання
    return f"How can I help you?\nEnter: \n'add name phones' (додаємо ім'я та номери телефонів)\n\
    'change name phone_old phone_new' (міняє старий номер телефона на новий)\n\
    phone (name), show to continue;\n\
     good bye, close, exit to exit"


def add_phone_func(text):# функція додає номер або номери телефонів
    name, phones = create_data(text)
    for phone in phones:
        new_book[name].add_phone(phone)
    return f"Number added"


def change_phone_func(name_phone: list):# функція змінює номер телефону
    number_phone_old = int(name_phone[1])
    number_phone_new = int(name_phone[2])
    name = name_phone[0]
    new_book[name]  # перевірка існування ім'я, штучна помилка
    for char in filter(lambda value: value == name, new_book.keys()):
        new_book[name].change_phone(number_phone_old, number_phone_new)
    return f"Number changed"


def get_phone(text: str):# функція видає номер телефону за імям
    name = text[0].capitalize()
    number_phone = int(text[1])
    new_book[name]  # перевірка існування ім'я, штучна помилка
    return new_book[name]


def show_all(text: list):# функція видає весь список телефонів
    if text[0] == 'all' and len(text) == 1:
        return new_book.data.items()
    # штучна помилка
    raise KeyError


# функції прощавання)
def bye():
    exit("Good bye")

# словник функцій
INPUT_HANDLER = {
    "hello": hello,
    "add": add_phone_func,
    "change": change_phone_func,
    "del_phone": get_phone,
    "show": show_all,
    "close": bye,
    "exit": bye
}


def input_error(func):
    def wrapper(text):
        try:
            return func(text)
        except IndexError:
            result = "Give me name and phone please splitted by space"
        except KeyError:
            result = "Enter right user's name or user's number or command"
        except ValueError:
            result = "Enter: add (name phone), change (name phone), \
phone (name), show all to continue; good bye, close, exit to exit"
        except TypeError:
            result = "Enter: add (name phone), change (name phone), \
phone (name), show all, good bye, close, exit to continue"
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
            break
    if list_text:
        return INPUT_HANDLER[new_text](list_text)#визиваємо функції з аргументами
    else:
        return INPUT_HANDLER[new_text]()#визиваємо функції без аргументів


def create_data(text):
    """
    Розділяє вхідні дані на дві частини - номер і телефон.
    Також ці данні проходять валідацію.
    Для подальшої роботи з ними.
    :param data: Строка з номером і ім'ям.
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
    hello()
    while True:
        text = input("Hello, input command: ")
        print(call_handler(text))


new_book = AddressBook()
if __name__ == "__main__":
    main()
