# https://quera.org/problemset/52550
from collections import defaultdict

if __name__ == '__main__':
    n = int(input())
    colorized_socks: dict[int, list] = defaultdict(list)

    for number_of_sock, color_of_sock in zip(range(1, n+1), map(int, input().split(' '))):
        colorized_socks[color_of_sock].append(number_of_sock)

    # print(colorized_socks)

    paired_socks: list[tuple[int, int]] = []

    for _, same_color_socks in colorized_socks.items():

        for i in range(1, len(same_color_socks), 2):
            # start iterator from 1 and pass index with i-1 and i to avoid out of range exception
            paired_socks.append((same_color_socks[i-1], same_color_socks[i]))

    paired_socks.sort(key=lambda x: x[0])

    print(len(paired_socks))
    for sock1, sock2 in paired_socks:
        print(sock1, sock2)
