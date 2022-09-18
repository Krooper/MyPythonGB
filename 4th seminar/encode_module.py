#  Функция для сжатия
def encoder(text):
    encoded_text = ''
    i = 0
    while i < len(text):
        counter = 1
        while i + 1 < len(text) and text[i] == text[i + 1]:
            counter += 1
            i += 1
        if counter == 1:
            encoded_text +=  text[i]
        else:
            encoded_text += str(counter) + text[i]
        i += 1
    return encoded_text
