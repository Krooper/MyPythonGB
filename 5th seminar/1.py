# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"


letters = 'абв'
text = 'абвгдейка - это передача'

# Понимаю, что можно сделать и по-другому, но пытаюсь лишний раз потренироваться в использовании новых для меня функций
text_list = text.split(' ')
filtered_words_list = list(filter(lambda word: False if letters in word else True, text_list))
text = ' '
text += (' '.join(filtered_words_list))
print(text)
