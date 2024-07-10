# https://quera.org/problemset/2637

number_of_lines = int(input())
# the maximized parts in square can be made by drawing half of lines horizontally and other half vertically
horizontal_lines = number_of_lines // 2
vertical_lines = number_of_lines - horizontal_lines
# and the number of made parts in a dimension is one more than separator lines
# so total parts are multiply of each dimension parts
print((horizontal_lines + 1) * (vertical_lines + 1))
