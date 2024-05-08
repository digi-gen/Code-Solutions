# https://quera.org/problemset/2794

x_main, y_main = -1, -1

x_ls = []
y_ls = []

for i in range(3):
    x, y = map(int, input().split())
    x_ls.append(x)
    y_ls.append(y)


# the result is some x that is come just one time among input x list
# and the same for y
for i in range(3):
    if x_ls.count(x_ls[i]) == 1:
        x_main = x_ls[i]
    if y_ls.count(y_ls[i]) == 1:
        y_main = y_ls[i]


print(x_main, y_main)
