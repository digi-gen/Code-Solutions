# https://quera.org/problemset/9021
n = int(input())

keys = tuple(map(int, input().split()))
off_on_s = tuple(map(int, input().split()))
keys_to_turn = sorted((key for key, off_on in zip(keys, off_on_s) if off_on == 1))
print(*keys_to_turn)
