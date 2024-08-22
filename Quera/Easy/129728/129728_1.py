# https://quera.org/problemset/129728

print(' '.join(sorted([(char if (ord(char) % 2 != 0) else char.upper()) for char in input()], reverse=True)))

# input_string = str(input())
# array = []
# for i in range(len(input_string)):
#     if (ord(input_string[i]) - 97) % 2 == 0:
#         array.append(input_string[i])
#     else:
#         array.append(input_string[i].upper())
# array.sort(reverse=True)
# answer = ' '.join(array)
# print(answer)
