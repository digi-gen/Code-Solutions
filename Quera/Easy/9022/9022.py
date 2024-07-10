# https://quera.org/problemset/9022


# for n = 1 and n = 2 the last character will take (n)th chair
# and for other n the last character will seat on (n-1)th chair
n = int(input())
if n > 2:
    print(n - 1)
else:
    print(n)
