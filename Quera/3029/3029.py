# https://quera.org/problemset/3029

x, y = map(int, input().split())
x1, y1 = map(int, input().split())

# Just determining is the x of point of his friend is more or less than his x.
if x > x1:
    print('Left')
else:
    print('Right')

