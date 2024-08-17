# https://quera.org/problemset/9109
from heapq import heappush, heappop, heapify

n = int(input())
colors = tuple(map(int, input().split()))
color_quantity = {}

for color in colors:
        if quantity := color_quantity.get(color):
            color_quantity[color] += 1
        else:
            color_quantity[color] = 1

minimum_color = min((tuple((value, key)) for key, value in color_quantity.items()))
print(minimum_color[1])

