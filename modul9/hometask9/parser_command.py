import re


def hello(text: str):
    print("How can I help you?")


kontakt_number = {}


def add_phone(name_phone: list):
    number_phone = name_phone[1]
    name = name_phone[0]
    kontakt_number[name] = number_phone


def change(text: str):
    number_phone = re.findall(r"\d+", text)
    name = re.findall(r"\w+", text)
    kontakt_number[name] = number_phone


def phone(text: str):
    name = re.findall(r"\w+", text)
    print(kontakt_number[name])


def show_all(text: str):
    print(kontakt_number)


def good_bye(text: str):
    print("Good bye")
    exit(0)


INPUT_HANDLER = {
    "hello": hello,
    "add": add_phone,
    "change": change,
    "phone": phone,
    "show_all": show_all,
    "good bye": good_bye,
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
            print("Enter user name")
    return wrapper


@input_error
def call_handler(text: str):
    list_text = text.split(' ')
    if list_text[0] in INPUT_HANDLER:
        INPUT_HANDLER[list_text[0]](list_text[1:])


def main():
    while True:
        text = input("Hello, input command: ").lower()
        call_handler(text)
        print(kontakt_number)


if __name__ == "__main__":
    main()
