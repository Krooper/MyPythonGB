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


def expression_check():
    print("X \tY \tZ \tnot(x or y or z) \tnot x and not y and not z \tFUNC")
    print("-- \t-- \t-- \t\t-- \t\t\t-- \t\t\t--")
    for x in True, False:
        for y in True, False:
            for z in True, False:
                first_half = not(x or y or z)
                second_half = not x and not y and not z
                if first_half == second_half:
                    print(f"{x} \t{y} \t{z} \t\t{first_half} \t\t\t{second_half} \t\t\tTrue")
                else:
                    print(f"{x} \t{y} \t{z} \t\t{first_half} \t\t\t{second_half} \t\t\tFalse")


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


def quarter_numbers():
    def is_number(number):
        if number.isdigit():
            return True
        else:
            print("Неправильный ввод!")
            return False

    def in_range(number):
        if 1 <= number <= 4:
            return True
        else:
            print("Нет такой четверти на плоскости!")

    quarter_inp = input()
    if is_number(quarter_inp):
        quarter_num = int(quarter_inp)
        if in_range(quarter_num):
            if quarter_num == 1:
                print("X = [1;+inf], Y = [1;+inf]")
            elif quarter_num == 2:
                print("X = [-inf1;-1], Y = [1;+inf]")
            elif quarter_num == 3:
                print("X = [-inf1;-1], Y = [-inf1;-1]")
            else:
                print("X = [1;+inf], Y = [-inf1;-1]")


def distance():
    def is_number(number):
        try:
            float(number)
            return True
        except ValueError:
            print("Вы ввели не число!")
            return False

    def distance_find(x1, x2, y1, y2):
        return round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 4)

    x1 = input()
    x2 = input()
    y1 = input()
    y2 = input()

    if is_number(x1) and is_number(x2) and is_number(y1) and is_number(y2):
        x1_num = int(x1)
        x2_num = int(x2)
        y1_num = int(y1)
        y2_num = int(y2)
        print(f"Расстояние между точками равно {distance_find(x1_num, x2_num, y1_num, y2_num)}")


day_of_week()
expression_check()
quarter()
quarter_numbers()
distance()
