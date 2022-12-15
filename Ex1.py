# Создайте программу для игры в ""Крестики-нолики"".
from random import randint

field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

def draw_field():
    print(f'{field[0]} | {field[1]} | {field[2]}')
    print('_________')
    print(f'{field[3]} | {field[4]} | {field[5]}')
    print('_________')
    print(f'{field[6]} | {field[7]} | {field[8]}')

def take_input(player_token):
    while True:
        value = input('Ваш ход ' + player_token + ': ')
        if not (value in '123456789'):
            print('Вы ввели недопустимое значение, попробуйте еще раз')
            continue
        value = int(value)
        if str(field[value - 1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        field[value - 1] = player_token
        break


def check_winner():
    for each in win_combinations:
        if (field[each[0] - 1] == field[each[1] - 1] == field[each[2] - 1]):
            return field[each[1] - 1]
    else:
        return False


def game():
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_winner()
            if winner:
                draw_field()
                print(winner, 'выиграл!')
                break
        counter += 1
        if counter > 8:
            draw_field()
            print('Ничья!')
            break
game()

