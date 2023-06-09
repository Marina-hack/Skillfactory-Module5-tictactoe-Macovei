instractions = """
Это будет наше игровое поле
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

   Инструкция:
   1. Введите номер ячейки от 1 до 9
   2. Вы должны заполнить все 9 ячеек
   3. Игрок N1 начинает первым
   """
sign_dict = []
for i in range(9):
    sign_dict.append(" ")

def print_board(sign_dict):
    board = f"""
 {sign_dict[0]} | {sign_dict[1]} | {sign_dict[2]}
---+---+---
 {sign_dict[3]} | {sign_dict[4]} | {sign_dict[5]}
---+---+---
 {sign_dict[6]} | {sign_dict[7]} | {sign_dict[8]}
"""
    print(board)

index_list = [ ]
def take_input(player_name):
    while True:
        x = int(input(f'{player_name}: '))
        x -= 1
        if 0 <= x < 10:
            if x in index_list:
                print(f'Ячейка {x+1} занята.')
                continue
            index_list.append(x)
            return x
        print('Пожалуйста введите число от 1 до 9')

def result_calculation(sign_dict, player_one, player_two):
    if any([sign_dict[0] == sign_dict[1] == sign_dict[2] == 'X' or sign_dict[1] == sign_dict[4] == sign_dict[7] == 'X' or\
           sign_dict[0] == sign_dict[4] == sign_dict[8] == 'X' or sign_dict[2] == sign_dict[5] == sign_dict[8] == 'X' or\
           sign_dict[3] == sign_dict[4] == sign_dict[5] == 'X' or sign_dict[2] == sign_dict[4] == sign_dict[6] == 'X' or\
           sign_dict[6] == sign_dict[7] == sign_dict[8] == 'X' or sign_dict[0] == sign_dict[3] == sign_dict[6] == 'X']):
        print(f'Поздравляю {player_one}. Вы выйграли!')
        quit('Спасибо вам за участие. Игра окончена.')
    elif any([sign_dict[0] == sign_dict[1] == sign_dict[2] == 'O' or sign_dict[1] == sign_dict[4] == sign_dict[7] == 'O' or \
           sign_dict[0] == sign_dict[4] == sign_dict[8] == 'O' or sign_dict[2] == sign_dict[5] == sign_dict[8] == 'O' or \
           sign_dict[3] == sign_dict[4] == sign_dict[5] == 'O' or sign_dict[2] == sign_dict[4] == sign_dict[6] == 'O' or \
           sign_dict[6] == sign_dict[7] == sign_dict[8] == 'O' or sign_dict[0] == sign_dict[3] == sign_dict[6] == 'O']):
        print(f'Поздравляю {player_two}. Вы выйграли!')
        quit('Спасибо вам за участие. Игра окончена.')
    else:
        return


def general():
    print("Игра крестики-нолики")
    player_one = input("Напишите имя первого игрока: ")
    player_two = input("Напишите имя второго игрока: ")
    print(f"{player_one} и {player_two}, добро пожаловать в игру!")
    print(instractions)
    print(f"{player_one} - значок Х")
    print(f"{player_two} - значок 0")

    print_board(sign_dict)
    for i in range(0, 9):
        if i % 2 == 0:
            index = take_input(player_one)
            sign_dict[index] = 'X'
        else:
            index = take_input(player_two)
            sign_dict[index] = 'O'

        print_board(sign_dict)
        result_calculation(sign_dict, player_one, player_two)

    print("Победила дружба. Сыграйте еще раз.")

general()

