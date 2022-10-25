# Дуже часто люди у своїх повідомленнях не ставлять великі літери,
# особливо це стало масовим явищем в еру мобільних. пристроїв.
# Розробіть функцію capital_text, яка прийматиме на вхід рядок з текстом
#  і повертатиме рядок з відновленими великими літерами.

# Функція повинна:

# зробити великою першу літеру в рядку, попри прогалини
# зробити великою першу літеру після точки, попри прогалини
# зробити великою першу літеру після знака оклику, попри прогалини
# зробити великою першу літеру після знака питання, попри прогалини

import re
def capital_text(s):
    # s=re.search(r'\.|\?|\! ', s)
    # print (s)
    # for item in s:
    #     item=item.strip(' ')
    #     item=item.capitalize()
    #     l=l+item
    #     print(item)
    # print(l)
    senteces=[]
    start = 0
    new_text = ''
    for m in re.finditer(r'\.|\?|\! *\b', s):
        end=m.start()+1
        senteces.append(s[start:end])
        start = end+1
    if end!=len(s):
        senteces.append(s[start:len(s)+1])
    
    for element in senteces:
        element = str(element).strip(' ')
        element = str(element).capitalize()
        new_text = new_text + ' ' + element
    new_text = new_text.lstrip(' ')
    return new_text
        # k=re.search(r'\w', s[m.start():])
        # s[m.start()+k.span(0)[0]].upper

        # print(k,s[m.start()+k.span(0)[0]].upper)


    # return s,k
print(capital_text("зробити великою першу літеру в рядку, попри прогалини.  зробити великою першу літеру після точки, попри прогалини.   зробити великою першу літеру після знака оклику, попри прогалини!  зробити великою першу літеру після знака питання, попри прогалини"))
