# https://quera.org/problemset/8901

n, pea_position = input().split()
n = int(n)

for i in range(n):
    position_1, position_2 = input().split()
    if pea_position == position_1:
        pea_position = position_2
    elif pea_position == position_2:
        pea_position = position_1

print(pea_position)
