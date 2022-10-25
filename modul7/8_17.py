# "2+ 34-5 * 3" => ['2', '+', '34', '-', '5', '*', '3']
# З метою спрощення вважаємо, що числа можуть бути тільки цілими,
#  і вхідний рядок завжди міститиме математичний вираз, що складається з дужок, чисел та операторів.

# Зверніть увагу, що лексеми можуть відокремлюватися один від 
# одного різною кількістю прогалин, а можуть і не відокремлюватися зовсім.
#  Прогалини не є лексемами та до підсумкового списку потрапити не повинні.
import re
def symbol(s):
    list_symbol = []
    for m in re.finditer(r'\+|\-|\\|\*|\(|\)', s):
        end_index = m.start()
        list_symbol.append(s[end_index])
    return list_symbol
def number(s):
    list_s=[]
    start_index = 0
    for m in re.finditer(r'\d+', s):
        start_index = m.span(0)[0]
        end_index = m.span(0)[1]
        new_element = s[start_index:end_index]
        list_s.append(new_element)
    return list_s

def token_parser(s):
    list_example = []
    if len(s.strip())==0:
        return list_example
    list_symbol = symbol(s)
    list_number = number(s)
    i = 0
    while i < len(list_number)-1:
        list_example.append(list_number[i])
        list_example.append(list_symbol[i])
        i=i+1
    list_example.append(list_number[-1])
    return list_example
print(token_parser("2+ 34-5 * 32"))
print(token_parser("   "))
print(token_parser('(2+ 3) *4 - 5 * 3'))
print(token_parser('2+ (3 -  5) *4 - 5 * 3'))
