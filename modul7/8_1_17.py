import re
def symbol(s):
    # list_symbol = []
    dict_symbol = {}
    for m in re.finditer(r'\+|\-|\\|\*|\(|\)', s):
        end_index = m.start()
        # list_symbol.append(s[end_index])
        dict_symbol[end_index] = s[end_index]
    return dict_symbol

def number_str(s):
    # list_s=[]
    start_index = 0
    dict_number = {}
    for m in re.finditer(r'\d+', s):
        start_index = int(m.span(0)[0])
        end_index = int(m.span(0)[1])
        new_element = s[start_index:end_index]
        # list_s.append(new_element)
        dict_number[start_index] = new_element
    return dict_number
def dict_string(s):
    dict_symbol = symbol(s)
    dict_number = number_str(s)
    dict_symbol.update(dict_number)
    return dict_symbol

def token_parser(s):
    s=s.strip()
    list_example = []
    dict_s = dict_string(s)
    if len(s)==0:
        return list_example
    for i in range(len(s)):
        if i in dict_s.keys():
            list_example.append(dict_s[i])
    return list_example
print(token_parser('2+ (3 -  5) *4 - 5 * 3'))