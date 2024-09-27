# https://quera.org/problemset/104589

n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        print(n // i)
        break
