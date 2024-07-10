# https://quera.org/problemset/228669

m = int(input())
n = int(input())

if m == 1 or n == 1:
    print(m * n)
else:
    # four homes that are in corners are common between sides and shouldn't be duplicated
    right_and_left_sides = 2 * (m - 2)
    up_and_bottom_sides = 2 * n
    print(right_and_left_sides + up_and_bottom_sides)
