# https://quera.org/problemset/171788
from math import ceil, floor

number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    m, t, b = map(int, input().split())
    hunger_ratio = m / t
    h_prime = floor(hunger_ratio)
    pizzas = ceil((b * hunger_ratio) / 8)
    all_peaces = pizzas * 8
    maximum_peaces = (all_peaces - (b * h_prime)) + h_prime
    print(pizzas, maximum_peaces)
