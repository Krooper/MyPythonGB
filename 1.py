def day_of_week():
    def is_number(number):
        if number.isdigit():
            return True
        else:
            print("Неправильный ввод!")
            return False

    def in_range(number):
        if 1 <= number <= 7:
            return True
        else:
            print("Нет такого дня недели!")

    def day_off(number):
        if 6 <= number <= 7:
            print("Да")
        else:
            print("Нет")

    input_number = input()
    if is_number(input_number):
        week_day = int(input_number)
    if in_range(week_day):
        day_off(week_day)


def quarter():
    def is_number(number):
        try:
            float(number)
            return True
        except ValueError:
            print("Вы ввели не число!")
            return False

    def zero_check(number):
        if number == 0:
            print("Вы ввели число равное нулю!")
            return False
        else:
            return True

    def quarter_find(x, y):
        if x > 0 and y > 0:
            print("1-я четверть")
        elif x < 0 < y:
            print("2-я четверть")
        elif x < 0 > y:
            print("3-я четверть")
        else:
            print("4-я четверть")

    x = input()
    y = input()
    if is_number(x) and is_number(y):
        num_x = int(x)
        num_y = int(y)
        if zero_check(num_x) and zero_check(num_y):
            quarter_find(num_x, num_y)


day_of_week()
quarter()
