list_buttons = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_letters = ['.,?!:', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ',' ']
dict_sequence = {}
for button, letters in zip(list_buttons, list_letters):
    dict_sequence[button] = letters




def sequence_buttons(string):
    answ = ''
    string = str(string).upper()
    for char in string:
        for i in dict_sequence:
            print(i)
            if char in dict_sequence[i]:
                print(char)
                answ += str(i)*(dict_sequence[i].index(char)+1)
    return answ

print(sequence_buttons("Hello, World!"))
