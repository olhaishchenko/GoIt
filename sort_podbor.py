from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter, merge_completers
commands = {"help": "help_me",
            "instruction": "instructions",
            "create_contact": "book_create",
            "show_contact_book": "book_show_all",
            "show_contact": "book_show_one",
            "show_contact_page": "book_show_page",
            "clear_contact_book": "book_delete_all"}
name = {"olga": "+380567458432",
        "alex": "+380931345523"}
name_completer = WordCompleter(name.keys())

commands_completer = WordCompleter(commands.keys())
completer = merge_completers([commands_completer, name_completer])
text = prompt('Enter command: ', completer=completer)




# from prompt_toolkit import prompt, PromptSession
# from prompt_toolkit.completion import WordCompleter, NestedCompleter
# from prompt_toolkit.history import FileHistory
#
# session = PromptSession(history=FileHistory('~/.goit_history'))
# #
# # buf_name = WordCompleter(["olga", "alex", "anna", "andrey"])
# # buf_number = WordCompleter(["050444444444", "444444444444"])
# # html_completer = WordCompleter(['use', 'learn', 'copy', 'add', 'remove', 'move', 'delete'])
# # commands = {"help": "help_me",
# #             "instruction": "instructions",
# #             "create_contact": "book_create",
# #             "show_contact_book": "book_show_all",
# #             "show_contact": "book_show_one",
# #             "show_contact_page": "book_show_page",
# #             "clear_contact_book": "book_delete_all",
# #             "delete_contact": "book_delete_one",
# #             "add_to_contact": "book_add_values",
# #             "edit_contact": "book_edit_information",
# #             "edit_contact_name": "book_edit_name",
# #             "search_in_contacts": "book_search_in",
# #             "sort_contacts_by_tags": "sorted_by_tags",
# #             "show_birthdays": "book_show_nearest_birthdays",
# #             "days_to_birthday": "book_days_to_birthday",
# #             "show_all_birthdays": "book_days_to_birthday_for_all",
# #             "create_note": "notes_create",
# #             "show_note_book": "notes_show_all",
# #             "show_note": "notes_show_one",
# #             "show_note_page": "notes_show_page",
# #             "clear_note_book": "notes_delete_all",
# #             "delete_note": "notes_delete_one",
# #             "add_to_note": "notes_add_values",
# #             "edit_note": "notes_edit_information",
# #             "edit_note_name": "notes_edit_name",
# #             "search_in_notes": "notes_search_in",
# #             "sorted_notes_by_tags": "notes_sorted_by_tags",
# #             "file_sorter": "file_sorter",
# #             "exit": "good_bye"}
# # users_name = ["olga", "alex", "anna", "andrey"]
# users={"olga": None, "alex": None, "anna": None, "andrey": None}
# goit_completer = NestedCompleter.from_nested_dict({
#     'create': None,
#     'add': users,
#     'remove': users,
#     'show': None,
#     'search': None,
#     'quit': None,
# })
# text = session.prompt('Enter: ', completer=goit_completer)
# print('You said: %s' % text)
# # print(text)
#
#


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
