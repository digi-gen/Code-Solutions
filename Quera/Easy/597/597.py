
# problem link : https://quera.org/problemset/597

number = int(input())
i, j = 0, 0
coefficient = 0

# determining the raising or falling line
if number % 2 == 0:
    # Up-left line
    if number % 4 == 0:
        # base term of this line
        i, j = -1, 1
        # number of the terms in this line are moduls of 4
        # So we can determine the coefficient of terms dividing by 4
        coefficient = number / 4
        i *= coefficient
        j *= coefficient

    # bottem-right line
    elif number % 4 == 2:
        i, j = 1, 0
        # (number -2 ) because of making the number modul of 4
        coefficient = (number - 2) / 4
        i += coefficient
        j += (- coefficient)

else:
    # Up-right line
    if number % 4 == 3:
        i, j = 1, 1
        coefficient = (number + 1) / 4
        i *= coefficient
        j *= coefficient
    # bottem-left line
    else:
        i, j = 0, 0
        coefficient = (number - 1) / 4
        i -= coefficient
        j -= coefficient

print(int(i), int(j))



