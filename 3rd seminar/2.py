# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        print("Вы ввели не число!")
        return False


def is_integer(number):
    if number.isdigit():
        return True
    else:
        print("Вы ввели дробное число!")
        return False


def list_input():
    num_list = []
    print("Введите длину массива")
    list_length = input()
    while not is_number(list_length) or not is_integer(list_length):
        print("Повторите ввод!")
        list_length = input()
    i = 0
    while i < int(list_length):
        print(f"Введите {i + 1}-й элемент массива")
        num_list.append(input())
        while not is_number(num_list[i]):
            print("Повторите ввод!")
            num_list[i] = input()
        if is_integer(num_list[i]):
            num_list[i] = int(num_list[i])
            i += 1
        else:
            num_list.remove(num_list[i])
    return num_list


def unique_num_list (num_list):
    unique_list = []
    for i in range(len(num_list)):
        if num_list[i] != num_list[i-1]:
            unique_list.append(int(num_list[i]))
    return unique_list


print(unique_num_list(list_input()))
