# https://quera.org/problemset/605
from typing import List

# Dynamic Programming Approach
n = int(input())

fact_list: List[int] = [0 for _ in range(n + 1)]

def factorial(fact_list: List[int]) -> List[int]:
    for i in range(n + 1):
        if i == 0 or i == 1:
            fact_list[i] = 1
        else:
            fact_list[i] = (i * fact_list[i-1])

    return fact_list



if __name__ == '__main__':

    fact_list = factorial(fact_list)
    # print(fact_list)

    total_filling_ways = 0
    for i in range((n // 2) + 1):
        filling_ways_have_i_double_tiles = 0
        double_tiles_no = i
        single_tiles_no = n - (double_tiles_no * 2)
#       print(f'{double_tiles_no=} , {single_tiles_no=}')
        permutation_of_all_tiles = fact_list[double_tiles_no + single_tiles_no]
        permutation_of_repetitious_tiles = fact_list[double_tiles_no] * fact_list[single_tiles_no]
#       print(f'{permutation_of_all_tiles=}, {permutation_of_repetitious_tiles=}')
        filling_ways_have_i_double_tiles = permutation_of_all_tiles / permutation_of_repetitious_tiles
        total_filling_ways += filling_ways_have_i_double_tiles
#       print(f'{total_filling_ways=}')

    print(int(total_filling_ways))







