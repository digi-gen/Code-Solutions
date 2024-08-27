# https://quera.org/problemset/226378

table = [[0] * 8 for _ in range(2)]

road_map = input()

i, j = 1, 0
table[i][j] = 1
for char in road_map:
    if char == 'R':
        i += 1
        j += 1
        if i > 1:
            print("DEATH")
            break
        table[i][j] = 1
    if char == 'L':
        i -= 1
        j += 1

        if i < 0:
            print("DEATH")
            break

        table[i][j] = 1

    if char == 'F':
        j += 1
        table[i][j] = 1
else:
    for row in table:
        print(*row, sep='')
