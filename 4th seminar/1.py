# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

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


def prime_factors(number):
    primes_list = [2, 3, 5, 7]
    factors_list = []
    if is_number(number):
        number = positive(number)
        if is_integer(number):
            number = int(number)
            for i in primes_list:
                if number % i == 0:
                    factors_list.append(i)
    return factors_list


print(prime_factors(input()))
