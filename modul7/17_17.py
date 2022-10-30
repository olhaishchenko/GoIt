# Повернемося до попереднього завдання та виконаємо зворотне.
# Напишіть рекурсивну функцію encode для кодування списку або рядка.
# Як аргумент функція приймає список ( наприклад
# ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ])
# або рядок (наприклад, "XXXZZXXYYYZZ"). Функція повинна повернути закодований
# список елементів (наприклад ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).


def encode(data):
    encode_data = []
    if not data:
        return encode_data
    i = 1
    if len(data) > 1:
        while i < len(data) and data[i-1] == data[i]:
            i += 1
            print(i)
        encode_data.append(data[0])
        encode_data.extend([i])
        print('i= ', i)
        encode_data.extend(encode(data[i:]))
        return encode_data
    else:
        encode_data.append(data[0])
        encode_data.append(1)
        return encode_data

print(encode(["X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z" ]))