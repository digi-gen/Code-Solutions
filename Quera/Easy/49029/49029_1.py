# https://quera.org/problemset/49029
from typing import Tuple


def check_bottom_left(x, y):
    global wall
    is_good_window = True
    bottom_row, left_column = (x + 1, y - 1)
    try:
        if wall[bottom_row][left_column] == glass_sign:
            if is_one_glass_one_block((wall[bottom_row][y], wall[x][left_column])):
                is_good_window = False
    except IndexError:
        is_good_window = True

    return is_good_window


def check_bottom_right(x, y):
    global wall
    is_good_window = True
    bottom_row, right_column = (x + 1, y + 1)
    try:
        if wall[bottom_row][right_column] == glass_sign:
            if is_one_glass_one_block((wall[x][right_column], wall[bottom_row][y])):
                is_good_window = False
    except IndexError:
        is_good_window = True

    return is_good_window


def is_one_glass_one_block(two_not_diagonal_cells: Tuple[str, str]) -> bool:
    glass_no = two_not_diagonal_cells.count(glass_sign)
    block_no = two_not_diagonal_cells.count(block_sign)
    return glass_no == block_no == 1


def is_good_wall():
    global wall
    flag = True
    for i in range(n):
        for j in range(m):
            if wall[i][j] == glass_sign:
                check_window_funcs = ( check_bottom_left, check_bottom_right)
                if all(func(i, j) for func in check_window_funcs):
                    flag = True
                else:
                    flag = False
                    
            if not flag:
                return flag

    return flag


if __name__ == '__main__':
    n, m = map(int, input().split())
    wall = [list(input()) for _ in range(n)]

    glass_sign = '+'
    block_sign = '*'

    if is_good_wall():
        print('good wall')
    else:
        print('bad wall')
