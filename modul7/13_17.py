# Створіть функцію get_employees_by_profession(path, profession).
# Функція повинна у файлі (параметр path) знайти всіх співробітників зазначеної професії (параметр profession)
#
# Вимоги:
#
# відкрийте файл за допомогою with для читання
# отримайте рядки з файлу за допомогою методу readlines()
# за допомогою методу find знайдіть усі рядки у файлі, де є вказана profession, та помістіть записи до списку
# об'єднайте всі ці рядки в списку в один рядок за допомогою методу join
# (пам'ятайте про переклад рядків '\n' та зайві прогалини, які треба прибрати)
# приберіть значення змінної 'profession' (замініть на порожній рядок "" методом replace)
# поверніть отриманий рядок із файлу
def get_employees_by_profession(path, profession):
    new_list = ''
    with open(path, 'r') as fh:
        s = fh.readlines()
        for i in range(len(s)):
            if s[i].find(profession) != -1:
                s[i] = s[i].rstrip('\n')
                s[i] = s[i].replace(profession, '')
                new_list += s[i]
    new_list = new_list[:-1]
    return new_list




