#  Функция для восстановления
def decoder(text):
    decoded_text = ''
    words_list = text.split()
    for word in words_list:
        decoded_word = ''


    # i = 0
    # while i < len(text):
    #     counter = 1
    #     while i + 1 < len(text) and text[i] == text[i + 1]:
    #         counter += 1
    #         i += 1
    #     decoded_text += str(counter) + text[i]
    #     i += 1
    # return decoded_text
