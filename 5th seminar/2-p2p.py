# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"
import random


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        print("Вы ввели не число!")
        return False


def is_integer(number):
    try:
        int(number)
        return True
    except ValueError:
        print("Вы ввели дробное число!")
        return False


def is_positive(number):
    if number >= 0:
        return True
    else:
        return False


def random_player(player_one, player_two):
    players = [player_one, player_two]
    first_one = random.choice(players)
    players.remove(first_one)
    second_one = players[0]
    return first_one, second_one


# Решил немного вспомнить ООП :)
class Player:
    def __init__(self, name):
        self.name = name
        self._condition = None

    # Не уверен, насколько правильно в данном случае реализовывать по сути весь процесс игры через один метод класса.
    # Если размышлять с точки зрения ООП, кажется, что класс (пусть даже через метод) не должен знать правила игры,
    # а должен только что-то делать, а сама программа уже отвечает за ведение игры.
    # С другой стороны, это позволяет в "теле" программы не использовать никаких доп. условий.
    # Если вам не сложно, прошу дать комментарии по этому поводу
    def take(self, items):
        print(f'На столе конфет: {items} шт.')
        print("Сколько конфет вы хотите забрать?")
        print("(введите целое число меньше 28)")
        print()
        print(f'Ходит {self.name}')
        number = input()
        if is_number(number) and is_integer(number):
            number = int(number)
            while number <= 28 and is_positive(number) and number <= items:
                items -= number
                if items <= 0:
                    self._condition = 'проиграл'
                    print(f'{self.name} {self._condition}')
                    quit()
                print()
                return items
            else:
                print()
                print("Вы не можете столько взять!")
                items = self.take(items)
                return items
        else:
            print()
            print("Ошибка ввода!")
            items = self.take(items)
            return items


player1 = Player("Андрей")
player2 = Player("Юля")
candies = 2021
first_player, second_player = random_player(player1, player2)

while True:
    candies = first_player.take(candies)
    candies = second_player.take(candies)
