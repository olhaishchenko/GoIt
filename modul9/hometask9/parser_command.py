def hello():
    text_output = "How can I help you?"
    return print(text_output)


kontakt_number = {}


def add_phone(name_phone: list):
    number_phone = name_phone[1]
    name = name_phone[0]
    kontakt_number[name] = number_phone
    text_output = "Number added"
    return print(text_output)


def change(name_phone: list):
    number_phone = name_phone[1]
    name = name_phone[0]
    l = kontakt_number[name]  # перевірка існування ім'я
    for char in filter(lambda value: value == name, kontakt_number.keys()):
        kontakt_number[name] = number_phone
    text_output = "Numer changed"
    return print(text_output)


def phone(text: str):
    name = text[0]
    l = kontakt_number[name]  # перевірка існування ім'я
    return print(kontakt_number[name])


def show_all():
    return print(kontakt_number)


def good_bye(text: str):
    if text[0] == 'bye':
        text_output = "Good bye"
        return text_output
    exit(0)


def bye():
    text_output = "Good bye"
    return text_output


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
            func(text)
        except IndexError:
            print("Give me name and phone please splitted by space")
        except KeyError:
            print("Enter: add (name phone), change (name phone), \
phone (name), show all, good bye, close, exit to continue")
        except ValueError:
            print("Enter right user name")
    return wrapper


@input_error
def call_handler(text: str):
    list_text = text.split(' ')
    if len(list_text) == 1:
        INPUT_HANDLER[list_text[0]]()
    else:
        INPUT_HANDLER[list_text[0]](list_text[1:])


def main():
    while True:
        text = input("Hello, input command: ").lower()
        call_handler(text)


if __name__ == "__main__":
    main()
