kontakt_number = {}


def hello():# функція привітання
    text_output = "How can I help you?"
    return text_output


def add_phone(name_phone: list):# функція додає номер телефону
    number_phone = int(name_phone[1])
    name = name_phone[0].capitalize()
    kontakt_number[name] = number_phone
    text_output = "Number added"
    return text_output


def change(name_phone: list):# функція змінює номер телефону
    number_phone = int(name_phone[1])
    name = name_phone[0].capitalize()
    kontakt_number[name]  # перевірка існування ім'я, штучна помилка
    for char in filter(lambda value: value == name, kontakt_number.keys()):
        kontakt_number[name] = number_phone
    text_output = "Numer changed"
    return text_output


def phone(text: str):# функція видає номер телефону за імям
    name = text[0].capitalize()
    kontakt_number[name]  # перевірка існування ім'я, штучна помилка
    return kontakt_number[name]


def show_all(text: list):# функція видає весь список телефонів
    if text[0] == 'all' and len(text) == 1:
        return kontakt_number
    # штучна помилка
    raise KeyError


# функції прощавання)
def good_bye(text: list):
    if text[0] == 'bye':
        exit("Good bye")
    # штучна помилка
    raise KeyError


def bye():
    exit("Good bye")

# словник функцій
INPUT_HANDLER = {
    "hello": hello,
    "add": add_phone,
    "change": change,
    "phone": phone,
    "show": show_all,
    "good": good_bye,
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
phone (name), show all, good bye, close, exit to continue"
        except TypeError:
            result = "Enter: add (name phone), change (name phone), \
phone (name), show all, good bye, close, exit to continue"
        return result
    return wrapper


@input_error
def call_handler(text: str):
    list_text = text.split(' ') #розбиваємо текст
    if len(list_text) == 1:
        return INPUT_HANDLER[list_text[0]]()#визиваємо функції без аргументів
    else:
        return INPUT_HANDLER[list_text[0]](list_text[1:])##визиваємо функції з аргументами


def main():
    while True:
        text = input("Hello, input command: ").lower()
        print(call_handler(text))


if __name__ == "__main__":
    main()
