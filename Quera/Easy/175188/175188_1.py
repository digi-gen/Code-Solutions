# https://quera.org/problemset/175188

n = int(input())
list_of_all_processes = []
for _ in range(n):
    line = input()
    number_of_process_to_up_cards = 0
    for i in range(len(line)):
        if line[i] == '0':
            try:
                if line[i + 1] == '1':
                    number_of_process_to_up_cards += 1
            except IndexError:
                # that means end of line
                number_of_process_to_up_cards += 1

    list_of_all_processes.append(number_of_process_to_up_cards)

print(*list_of_all_processes, sep='\n')

