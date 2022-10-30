# При роботі веб-сервісів спілкування, за протоколом HTTP,
# найчастіше відбувається в форматі JSON. І надсилання даних на
# сервер при запиті POST - це необхідність використовувати словник,
# оскільки структура формату JSON ідентична словнику Python.
#
# Реалізуйте допоміжну функцію, яка формуватиме запит на сервер у
# вигляді словника. Дана функція make_request(keys, values) приймає
# два параметри у вигляді списків. Функція повинна створити словник із
# ключами з списку keys та значеннями зі списку values.
#
# Порядок відповідності збігається з індексами списків keys та values.
# Якщо довжина keys та values не збігаються, поверніть порожній словник.
def make_request(keys, values):
    server_dict = {}
    if len(keys) != len(values):
        return server_dict
    # for i in range(len(keys)):
    #     server_dict[keys[i]] = values[i]
    for key, value in zip(keys, values):
        server_dict[key] = value
    return server_dict


print(make_request([1, 2, 3, 4], [6, 2, 4, 3]))
