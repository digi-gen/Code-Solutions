# https://quera.org/problemset/177663

n, *divisors = (number for number in map(int, input().split()))

result = sum(1 for i in range(1, n + 1) if any(i % divisor == 0 for divisor in divisors))

print(result)
