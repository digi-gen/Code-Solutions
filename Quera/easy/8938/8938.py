# https://quera.org/problemset/8938

n, m = map(int, input().split())

costs = [[0] * n for _ in range(n)]

for i in range(n):
    costs[i] = list(map(int, input().split()))

total_cost = 0
for _ in range(m):
    i, j = map(int, input().split())
    total_cost += costs[i - 1][j - 1]

print(total_cost)

