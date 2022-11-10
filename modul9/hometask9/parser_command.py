def hello(text):
    return "How can I help you?"


kontakt_number = {}


def add_phone(name_phone: list):
    number_phone = name_phone[1]
    name = name_phone[0]
    kontakt_number[name] = number_phone
    return "Number added"


def change(name_phone: list):
    number_phone = name_phone[1]
    name = name_phone[0]
    l = kontakt_number[name]  # перевірка існування ім'я
    for char in filter(lambda value: value == name, kontakt_number.keys()):
        kontakt_number[name] = number_phone
    return "Numer changed"


def phone(text: str):
    name = text[0]
    l = kontakt_number[name]  # перевірка існування ім'я
    return kontakt_number[name]


def show_all(text: str):
    return kontakt_number


def good_bye(text: str):
    return "Good bye"
    exit(0)


INPUT_HANDLER = {
    "hello": hello,
    "add": add_phone,
    "change": change,
    "phone": phone,
    "show": show_all,
    "good": good_bye,
    "close": good_bye,
    "exit": good_bye
}


def input_error(func):
    def wrapper(text):
        try:
            func(text)
        except IndexError:
            print("Give me name and phone please splitted by space")
        except KeyError:
            print("Enter: add_name_phone, change_name_phone, phone_name, show all, good bye, close, exit to continue")
        except ValueError:
            print("Enter right user name")
    return wrapper


@input_error
def call_handler(text: str):
    list_text = text.split(' ')
    if list_text[0] in INPUT_HANDLER:
        INPUT_HANDLER[list_text[0]](list_text[1:])


def main():
    while True:
        text = input("Hello, input command: ").lower()
        print(call_handler(text))



if __name__ == "__main__":
    main()
