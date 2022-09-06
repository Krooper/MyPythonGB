# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_number (number):
    if number.isdigit():
        return True
    else:
        print("Неправильный ввод!")
        return False


def in_range (number):
    if 1 <= number <= 7:
        return True
    else:
        print("Нет такого дня недели!")


def day_off (number):
    if 6 <= number <= 7:
        print("Да")
    else:
        print("Нет")


input_number = input()
if is_number(input_number):
    week_day = int(input_number)
    if in_range(week_day):
        day_off(week_day)




