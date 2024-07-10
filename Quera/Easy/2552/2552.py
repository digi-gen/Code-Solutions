# https://quera.org/problemset/2552
from typing import List, Tuple

size, number_of_objects = map(int, input().split())
table: List[List[bool]] = [[False] * size for _ in range(size)]

for _ in range(number_of_objects):
    x, y = map(int, input().split())
    table[x - 1][y - 1] = True   # there is an object in this position on table


"""
find possible rectangles can be made by objects
It's like finding divisors of size which multiply of them is equal to number of objects.
"""
possible_rectangles: List[Tuple[int, int]] = []
for i in range(1, size + 1):
    if (possible_rect_size := number_of_objects / i).is_integer():
        possible_rectangles.append((i, int(possible_rect_size)))


min_movements = number_of_objects  # possible maximum movements_of_current_sub_table of objects

"""
creating a sub-table with size of possible_rectangles from table and count the number of False in it,
which shows there is no object in this position 
and a movement should be performed to bring an object from another position to this one. 
"""
for rect_width, rect_height in possible_rectangles:
    for i in range(size - rect_width + 1):
        for j in range(size - rect_height + 1):
            sub_table = [row[j:j + rect_height] for row in table[i:i + rect_width]]
            movements_of_current_sub_table = 0
            for row in sub_table:
                movements_of_current_sub_table += row.count(False)

            if movements_of_current_sub_table < min_movements:
                min_movements = movements_of_current_sub_table

print(min_movements)
