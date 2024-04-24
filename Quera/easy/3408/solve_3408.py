# https://quera.org/problemset/3408

number_of_terms = int(input())
# splitting the terms with space and store them in 'terms'
terms = input().split(' ')
# print the terms from end to start
print(*terms[::-1])
