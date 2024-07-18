# https://quera.org/problemset/211018

n = int(input())
h = map(int, input().split())
h = sorted(h, reverse=True)


shortest_path = 0
for hi in h:

    if abs(shortest_path + hi) < abs(shortest_path):
        shortest_path += hi
    else:
        shortest_path -= hi

print(abs(shortest_path))
