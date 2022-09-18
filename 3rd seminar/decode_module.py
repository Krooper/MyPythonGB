#  Функция для восстановления
def decoder(encoded_text):
    decoded_text = ''
    i = 0
    while i < len(encoded_text):
        counter = ''
        if encoded_text[i].isdigit():
            while encoded_text[i].isdigit():
                counter += str(encoded_text[i])
                i += 1
            counter = int(counter)
            for j in range(counter):
                decoded_text += encoded_text[i]
            i += 1
        else:
            decoded_text += encoded_text[i]
            i += 1
    return decoded_text
