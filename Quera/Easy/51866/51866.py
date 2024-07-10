# https://quera.org/problemset/51866

n, k = map(int, input().split())
costs = list(map(int, input().split()))

if k >= 3:
    print(min(costs))
elif k == 1:
    print(max(costs))
else:
    minimum_possible_cost = max(costs)
    for i in range(2, n - 1):
        first_part_maximum = max(costs[:i])
        second_part_maximum = max(costs[i:])
        minimum_possible_cost = min(minimum_possible_cost, second_part_maximum)

    print(minimum_possible_cost)
