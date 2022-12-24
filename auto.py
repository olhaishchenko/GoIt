# from prompt_toolkit import prompt
# from prompt_toolkit.completion import WordCompleter, merge_completers
# commands = {"help": "help_me",
#             "instruction": "instructions",
#             "create_contact": "book_create",
#             "show_contact_book": "book_show_all",
#             "show_contact": "book_show_one",
#             "show_contact_page": "book_show_page",
#             "clear_contact_book": "book_delete_all"}
# name = {"olga": "+380567458432",
#         "alex": "+380931345523"}
# name_completer = WordCompleter(name.keys())
#
# commands_completer = WordCompleter(commands.keys())
# completer = merge_completers([commands_completer, name_completer])
# text = prompt('Enter command: ', completer=completer)
# print(text)

from prompt_toolkit import prompt, PromptSession
from prompt_toolkit.completion import NestedCompleter



users = {"olga": None, "alex": None, "anna": None, "andrey": None}
goit_completer = NestedCompleter.from_nested_dict({
    'create': None,
    'add': users,
    'remove': users,
    'show': None,
    'search': None,
    'quit': None,
})
text = prompt('Enter: ', completer=goit_completer)
print('You said: %s' % text)

