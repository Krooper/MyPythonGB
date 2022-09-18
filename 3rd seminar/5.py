# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.
import encode_module
import decode_module


# Функция для считывания текста из файла, его шифровки и записи шифрованного сообщения в другой файл
def encoded_writer(file):
    encrypted_text = ''
    with open('encrypted_message.txt', 'w+', encoding='utf-8') as encrypted_message:
        with open(file, 'r', encoding='utf-8') as initial_text:
            for line in initial_text:
                encrypted_text = encode_module.encoder(line)
        encrypted_message.write(encrypted_text)


# Функция для считывания зашифрованного текста из файла, его дешифровки и записи дешифрованного сообщения в другой файл
def decoded_writer(file):
    decrypted_text = ''
    with open('decrypted_message.txt', 'w+', encoding='utf-8') as decrypted_message:
        with open(file, 'r', encoding='utf-8') as encrypted_message:
            for line in encrypted_message:
                decrypted_text = decode_module.decoder(line)
        decrypted_message.write(decrypted_text)


encoded_writer('initial text.txt')
