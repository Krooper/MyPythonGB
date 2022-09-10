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


def positive(number):
    if number[0] == '-':
        print("Отрицательное число преобразовано в положительное.")
        return number[1:]
    else:
        return number


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


def binarizator():
    def dec_to_bin(decimal_number):
        decimal_number = int(decimal_number)
        binary_number = ''
        while decimal_number > 0:
            binary_number = str(decimal_number % 2) + binary_number
            decimal_number = decimal_number // 2
        return binary_number

    print("Введите целое число:")
    number = input()
    if is_number(number):
        number = positive(number)
        if is_integer(number):
            print(f"Ваше число: {number}")
            print(f"Ваше число в двоичной системе счисления: {dec_to_bin(number)}")


def fibonacci_printer():
    def fibonacci_list(number):
        number = int(number)
        positive_fib_list = []
        fib1 = fib2 = 1
        positive_fib_list.append(fib1)
        positive_fib_list.append(fib2)
        for i in range(2, number):
            fib1, fib2 = fib2, fib1 + fib2
            positive_fib_list.append(fib2)

        negative_fib_list = []
        for i in range(len(positive_fib_list)):
            if i % 2 == 0:
                negative_fib_list.append(positive_fib_list[i])
            else:
                negative_fib_list.append(-positive_fib_list[i])

        fib_list = []
        i = len(negative_fib_list) - 1
        while i >= 0:
            fib_list.append(negative_fib_list[i])
            i -= 1
        fib_list.append(0)
        for i in range(len(positive_fib_list)):
            fib_list.append(positive_fib_list[i])
        return fib_list

    print("Введите номер элемента ряда Фибоначчи:")
    number = input()
    if is_number(number):
        number = positive(number)
        if is_integer(number):
            print(f"Ряд Фибоначчи: {fibonacci_list(number)}")


# odd_num_sum()
# pair_multiplication()
# fractional_diff()
# binarizator()
fibonacci_printer()
