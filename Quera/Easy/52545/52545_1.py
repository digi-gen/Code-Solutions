# https://quera.org/problemset/52545
winner = 0
max_skill = 0
for i in range(4):
    skills_i = list(map(int, input().split()))
    if skills_i:
        max_skill_of_this_student = max(skills_i)
        if max_skill_of_this_student > max_skill:
            max_skill = max_skill_of_this_student
            winner = i


print(winner + 1)

