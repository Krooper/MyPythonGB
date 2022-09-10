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
    for i in range(int(list_length)):
        print(f"Введите {i + 1}-й элемент массива")
        num_list.append(input())
        while not is_number(num_list[i]):
            print("Повторите ввод!")
            num_list[i] = input()
        num_list[i] = float(num_list[i])
    return num_list


def odd_num_sum():
    def odd_sum(numbers):
        i = 1
        num_sum = 0
        while i < len(numbers):
            num_sum += numbers[i]
            i += 2
        return num_sum

    numbers_list = list_input()
    print(f"Получившийся массив: {numbers_list}")
    print(f"Сумма нечетных элементов: {odd_sum(numbers_list)}")


def pair_multiplication():
    def multi(numbers):
        multi_list = []
        i = 0
        j = len(numbers) - 1
        while i <= j:
            multi_list.append(numbers[i]*numbers[j])
            i += 1
            j -= 1
        return multi_list

    numbers_list = list_input()
    print(f"Получившийся массив: {numbers_list}")
    print(f"Произведение пар: {multi(numbers_list)}")


def fractional_diff():
    def fract_min_max(numbers):
        min_fract = numbers[0] - int(numbers[0])
        max_fract = 0
        for i in range(len(numbers)):
            fract_part = numbers[i] - int(numbers[i])
            if fract_part < min_fract:
                min_fract = fract_part
            if fract_part > max_fract:
                max_fract = fract_part
        return max_fract - min_fract

    numbers_list = list_input()
    print(f"Получившийся массив: {numbers_list}")
    print(f"Наибольшая разница дробных частей: {round(fract_min_max(numbers_list), 2)}")


# odd_num_sum()
# pair_multiplication()
fractional_diff()
