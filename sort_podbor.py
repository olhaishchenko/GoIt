# # fh = ['use', 'learn', 'copy', 'add', 'remove', 'move', 'delete']
# # data = input('input command')
# # if type(data) is str:
# #     i=0
# #     for command in fh:
# #         if len(command)>= len(data):
# #             for i in range(len(data)):
# #                 if data[i] == command[i]
# #

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


buf_name = WordCompleter(["olga", "alex", "anna", "andrey"])
buf_number = WordCompleter(["050444444444", "444444444444"])
html_completer = WordCompleter(['use', 'learn', 'copy', 'add', 'remove', 'move', 'delete'])
text = prompt('Enter: ', completer=html_completer)
print('You said: %s' % text)
print(text)
# my_completer = WordCompleter(["add", "birthday", "close", "change", "create", "del", "exit", "hello", "next_birthday",
#                               "phone", "show", "search"])

# text = prompt('Enter HTML: ', completer=my_completer,
#               complete_while_typing=True)
# print('You said: %s' % text)


# import asyncio
#
# from prompt_toolkit.input import create_input
# from prompt_toolkit.keys import Keys
#
#
# async def main() -> None:
#     done = asyncio.Event()
#     input = create_input()
#
#     def keys_ready():
#         for key_press in input.read_keys():
#             print(key_press)
#
#             if key_press.key == Keys.ControlC:
#                 done.set()
#
#     with input.raw_mode():
#         with input.attach(keys_ready):
#             await done.wait()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
