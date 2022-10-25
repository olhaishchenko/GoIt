# Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) 
# для знаходження слова, що шукається в рядку ребуса.

# Параметри функції:

# riddle - рядок із зашифрованим словом.
# word_length – довжина зашифрованого слова.
# start_letter - літера, з якої починається слово (мається на увазі, що до початк
# у слова літера не зустрічається в рядку).
# reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому.
#  Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' 
# зашифроване слово 'power'.
# Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок.


def solve_riddle(riddle, word_length, start_letter, reverse=False):
    
    start = str(riddle).find(start_letter)
    if start == -1:
        word=''
    elif not reverse:
        word = riddle[start:start+word_length]
    else:
        word = riddle[start:start-word_length:-1]       
    return word
# ('aaatttrrr', 5, 'p', True) поверне наступну строку '' 
print(solve_riddle('aaatttrrr', 5, 'p', True))   
  