# https://quera.org/problemset/218361


l1 = map(int, input().split())
l2 = map(int, input().split())

chesh_to_chesh = 0

for l1_i, l2_i in zip(l1, l2):
    if l1_i == l2_i == 1:
        chesh_to_chesh += 1

print(chesh_to_chesh)
