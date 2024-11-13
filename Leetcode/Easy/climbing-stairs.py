# https://leetcode.com/problems/climbing-stairs/
import math


class Solution:

    # dynamic programming approach
    '''
    def climbStairs(self, n: int) -> int:
        results = [0] * 46
        for i in range(1, n + 1):
            if i == 1 or i == 2:
                results[i] = i
            else:
                results[i] = results[i - 1] + results[i - 2]

        result = results[n]

        return result
    '''

    def climbStairs(self, n: int) -> int:
        """
            solution using Binet's formula for fibonacci(n) equation
            fib(n + 1) == solution of this question
        """

        # Constants for Binet's formula
        phi = (1 + math.sqrt(5)) / 2
        psi = (1 - math.sqrt(5)) / 2
        # Apply Binet's formula for a[n] = F_(n+1)
        a_n_value = (phi ** (n + 1) - psi ** (n + 1)) / math.sqrt(5)
        return round(a_n_value)  # Round to handle floating-point precision issues


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(6))






