"""Четыре в ряд"""

# импорт необходимых модулей
import os
import shutil
from numpy import diag

# создание списка значений игрового поля
list_board = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
]


# заполнение списка в правильном порядке
def list_board_reverse(list_: list) -> list:
    """Переворачивает массив на 90 градусов влево и возвращает список"""
    list_board_show = []
    for i in range((len(list_[0]) - 1), -1, -1):
        for j in range(len(list_)):
            list_board_show.append(list_[j][i])
    return list_board_show


def list_board_reverse_list(list_: list) -> list:
    """Переворачивает массив на 90 градусов влево и возвращает двумерный массив"""
    list_board_show = []
    for i in range((len(list_[0]) - 1), -1, -1):
        lists = []
        for j in range(len(list_)):
            lists.append(list_[j][i])
        list_board_show.append(lists)
    return list_board_show


# отображение игрового поля в консоли
def show_game(x: int):
    """Выводит игровое поле в консоль"""
    list_board_reverse(list_board)
    os.system('cls')
    print('{{:-^{}}}'.format(shutil.get_terminal_size().columns).format('Четыре в ряд'))
    print('\n {} | {} | {} | {} | {} | {} | {}\n '
          '\n {} | {} | {} | {} | {} | {} | {}\n '
          '\n {} | {} | {} | {} | {} | {} | {}\n '
          '\n {} | {} | {} | {} | {} | {} | {}\n '
          '\n {} | {} | {} | {} | {} | {} | {}\n '
          '\n {} | {} | {} | {} | {} | {} | {}'.format(*list_board_reverse(list_board)))
    print('\n\n 0 | 1 | 2 | 3 | 4 | 5 | 6\n ')
    print("\n Ход ■") if not x % 2 else print("\n Ход ○")


# проверка выйгрышных комбинаций
# проверка столбцов
def valid_columns(list_: list) -> str:
    """Проверяет столбцы игрового поля на наличии 4-х элементов подряд """
    for i in list_:
        column = ''.join([str(j) for j in i])
        if '○○○○' in column:
            return '○'
        elif '■■■■' in column:
            return '■'


# проверка строк
def valid_row(list_: list) -> str:
    """Переворачивает на 90 градусов влево и проверяет строки игрового поля на наличии 4-х элементов подряд """
    row_list = list_board_reverse_list(list_)
    for i in row_list:
        row = ''.join([str(j) for j in i])
        if '○○○○' in row:
            return '○'
        elif '■■■■' in row:
            return '■'


# проверка диагоналей
# проверяем диагонали слева-направо
def valid_diagonal_left(list_: list) -> str:
    """Проверяет диагонали игрового поля на наличиe 4-х элементов подряд"""
    diagonal_list = []
    for i in range(len(list_) * -1, len(list_[0])):
        diagonal_list.append(diag(list_board, i))
    for j in diagonal_list:
        diagonal_ = ''.join([str(k) for k in j])
        if '○○○○' in diagonal_:
            return '○'
        elif '■■■■' in diagonal_:
            return '■'


# проверяем диагонали справа-налево
def valid_diagonal_right(list_: list) -> str:
    """Переворачивает на 90 градусов влево и проверяет диагонали игрового поля на наличии 4-х элементов подряд"""
    reverse_list = list_board_reverse_list(list_)
    diagonal_list = []
    for i in range(len(reverse_list) * -1, len(reverse_list[0])):
        diagonal_list.append(diag(reverse_list, i))
    for j in diagonal_list:
        diagonal_ = ''.join([str(k) for k in j])
        if '○○○○' in diagonal_:
            return '○'
        elif '■■■■' in diagonal_:
            return '■'


# игровой процесс
# ход игрока
def make_a_move(player_symbol: str, move: str):
    """Выводит значение в ближайшую свободную ячейку в выбранном столбце"""
    if move.isdigit() and 0 <= int(move) <= 6 and len(move) == 1:
        if ' ' in list_board[int(move)]:
            move_index: int = list_board[int(move)].index(' ')
            list_board[int(move)][move_index] = player_symbol
    return False


# игра
def game():
    """Представляет игровой процесс путем объединения функций хода, проверок и вывода результата."""
    count = -1
    show_game(count)
    while True:
        move = input('\n Сделайте ход: ')
        count += 1 if move.isdigit() and 0 <= int(move) <= 6 and ' ' in list_board[int(move)] else 0
        make_a_move('○', move) if not count % 2 else make_a_move('■', move)
        show_game(count)
        if valid_row(list_board):
            print('\n Конец игры! Победили', valid_row(list_board))
            break
        elif valid_columns(list_board):
            print('\n Конец игры! Победили', valid_columns(list_board))
            break
        elif valid_diagonal_left(list_board):
            print('\n Конец игры! Победили', valid_diagonal_left(list_board))
            break
        elif valid_diagonal_right(list_board):
            print('\n Конец игры! Победили', valid_diagonal_right(list_board))
            break
        elif count == 42:
            print('\n Конец игры! Ничья!')
            break


if __name__ == '__main__':
    game()
