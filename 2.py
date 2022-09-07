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


digits_sum()
factorial_list()