# Напишіть функцію to_indexed(start_file, end_file),
# яка зчитуватиме вміст файлу, додаватиме до прочитаних рядків порядковий
# номер і зберігати їх у такому вигляді у новому файлі.
#
# Кожний рядок у створеному файлі повинен починатися з його номера,
# двокрапки та пробілу, після чого має йти текст рядка з вхідного файлу.
#
# Нумерація рядків іде від 0

def to_indexed(source_file, output_file):
    new_str = ''
    with open(source_file, 'r') as sf:
        s = sf.readlines()
        for i in range(len(s)):
            new_str += str(i) + ': ' + s[i]
    with open(output_file, 'w') as of:
        of.write(new_str)





