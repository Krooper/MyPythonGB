# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное
# количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст,
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


# Функция, принимающая текст и сдвиг для шифровки
# и записывающая зашифрованный текст в файл (если файла нет, она его создает - режим w+)
def encryptor(text, shift):
    encrypted_text = ''
    with open('encrypted_message.txt', 'w+', encoding='utf-8') as encrypted_message:
        for letter in text:
            encrypted_letter = chr(ord(letter) + shift)
            encrypted_text += encrypted_letter
        encrypted_message.write(encrypted_text)


# Функция, принимающая файл с защифрованным текстом и сдвиг для дешифровки
# и записывающая дешифрованный текст в новый файл (если файла нет, она его создает - режим w+)
def decryptor(file, shift):
    decrypted_text = ''
    with open('decrypted_message.txt', 'w+', encoding='utf-8') as decrypted_message:
        with open(file, 'r', encoding='utf-8') as encrypted_message:
            for line in encrypted_message:
                for letter in line:
                    decrypted_letter = chr(ord(letter) - shift)
                    decrypted_text += decrypted_letter
        decrypted_message.write(decrypted_text)


encryptor('абба', -2)
decryptor('encrypted_message.txt', -2)
