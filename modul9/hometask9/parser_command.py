def hello():
    text_output = "How can I help you?"
    return text_output


kontakt_number = {}


def add_phone(name_phone: list):
    number_phone = int(name_phone[1])
    name = name_phone[0].capitalize()

    kontakt_number[name] = number_phone
    text_output = "Number added"
    return text_output


def change(name_phone: list):
    number_phone = int(name_phone[1])
    name = name_phone[0].capitalize()
    kontakt_number[name]  # перевірка існування ім'я
    for char in filter(lambda value: value == name, kontakt_number.keys()):
        kontakt_number[name] = number_phone
    text_output = "Numer changed"
    return text_output


def phone(text: str):
    name = text[0].capitalize()
    kontakt_number[name]  # перевірка існування ім'я
    return kontakt_number[name]


def show_all(text: list):
    if text[0] == 'all' and len(text) == 1:
        return kontakt_number
    else:
        kontakt_number[1] # штучна помилка


def good_bye(text: list):
    if text[0] == 'bye':
        exit("Good bye")
    else:
        kontakt_number[1] # штучна помилка


def bye():
    exit("Good bye")


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
            print("Give me name and phone please splitted by space")
        except KeyError:
            print("Enter right user's name or user's number or command")
        except ValueError:
            print("Enter: add (name phone), change (name phone), \
phone (name), show all, good bye, close, exit to continue")
        except TypeError:
            print("Enter: add (name phone), change (name phone), \
phone (name), show all, good bye, close, exit to continue")

    return wrapper


@input_error
def call_handler(text: str):
    list_text = text.split(' ')
    if len(list_text) == 1:
        return INPUT_HANDLER[list_text[0]]()
    else:
        return INPUT_HANDLER[list_text[0]](list_text[1:])


def main():
    while True:
        text = input("Hello, input command: ").lower()
        print(call_handler(text))


if __name__ == "__main__":
    main()
