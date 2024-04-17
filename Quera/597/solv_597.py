
# problem link : https://quera.org/problemset/597

number = int(input())
i, j = 0, 0

if number % 2 == 0:
    if number % 4 == 0:
        i, j = -1, 1
        coefficient = number / 4
        i *= coefficient
        j *= coefficient

    elif number % 4 == 2:
        i, j = 1, 0
        coefficient = (number - 2) / 4
        i += coefficient
        j += (- coefficient)

else:
    if number % 4 == 3:
        i, j = 1, 1
        coefficient = (number + 1) / 4
        i *= coefficient
        j *= coefficient

    else:
        i, j = 0, 0
        coefficient = (number - 1) / 4
        i -= coefficient
        j -= coefficient

print(int(i), int(j))



