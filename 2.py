import datetime


def digits_sum():
    def is_number(number):
        try:
            float(number)
            return True
        except ValueError:
            print("Вы ввели не число!")
            return False

    def positive(number):
        if number[0] == '-':
            print("Отрицательное число преобразовано в положительное.")
            return number[1:]
        else:
            return number

    def is_integer(number):
        if number.isdigit():
            return True
        else:
            print("Вы ввели дробное число!")
            return False

    def sum_of_digits(number):
        sum = 0
        for i in str(number):
            sum += int(i)
        return sum

    print("Введите целое число:")
    number = input()
    if is_number(number):
        number = positive(number)
        if is_integer(number):
            print(f"Сумма цифр введенного числа: {sum_of_digits(number)}")


def factorial_list():
    def is_number(number):
        try:
            float(number)
            return True
        except ValueError:
            print("Вы ввели не число!")
            return False

    def positive(number):
        if number[0] == '-':
            print("Отрицательное число преобразовано в положительное.")
            return number[1:]
        else:
            return number

    def is_integer(number):
        if number.isdigit():
            return True
        else:
            print("Вы ввели дробное число!")
            return False

    def factorial(number):
        fact_list = []
        for i in range(int(number)+1):
            if i == 0:
                continue
            elif i == 1:
                fact_list.append(i)
            else:
                fact_list.append(i * (fact_list[i-2]))
        return fact_list

    print("Введите целое число:")
    number = input()
    if is_number(number):
        number = positive(number)
        if is_integer(number):
            print(f"Набор произведений: {factorial(number)}")


def number_palindrome():
    def is_number(number):
        try:
            float(number)
            return True
        except ValueError:
            print("Вы ввели не число!")
            return False

    def positive(number):
        if number[0] == '-':
            print("Отрицательное число преобразовано в положительное.")
            return number[1:]
        else:
            return number

    def is_integer(number):
        if number.isdigit():
            return True
        else:
            print("Вы ввели дробное число!")
            return False

    def get_palindrome(number):
        reversed_number = []
        iterator = 0
        for _ in range(len(number)):
            reversed_number.append(number[iterator-1])
            iterator -= 1
        return ''.join(reversed_number)

    def palindrome_check(number, reversed_number):
        while number != reversed_number:
            number = str(int(number) + int(reversed_number))
            reversed_number = get_palindrome(number)
        return number

    print("Введите целое число:")
    number = input()
    if is_number(number):
        number = positive(number)
        if is_integer(number):
            print(f"Найден палиндром: {palindrome_check(number, get_palindrome(number))}")


def random_number():
    def is_number(number):
        try:
            float(number)
            return True
        except ValueError:
            print("Вы ввели не число!")
            return False

    def positive(number):
        if number[0] == '-':
            print("Отрицательное число преобразовано в положительное.")
            return number[1:]
        else:
            return number

    def is_integer(number):
        if number.isdigit():
            return True
        else:
            print("Вы ввели дробное число!")
            return False

    print("Введите верхнюю границу диапазона (целое число):")
    number = input()
    if is_number(number):
        number = positive(number)
        if is_integer(number):
            random_num = int(round(datetime.datetime.now().microsecond))
            while random_num > int(number):
                random_num /= 10
            print(f"Случайное число: {int(random_num)}")


digits_sum()
factorial_list()
number_palindrome()
random_number()
