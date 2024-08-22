# https://quera.org/problemset/279
fact_list = [1, 1]


def calculate_fact_from(from_index, value_from, to_index):
    """
    calculate factorials of i wich i in range(from_index + 1, to_index + 1) and return them in a list.

    >>> calculate_fact_from(2, 2, 5)
    [6, 24, 120]
    :param from_index: starting number that you have the factorial of it
    :param value_from: the factorial of from index
    :param to_index: last number that you want to calculate the factorial of it
    :return: list of factorials of i in range(from_index + 1, to_index + 1)
    """
    result_fact_list = []
    fact = value_from
    for i in range(from_index + 1, to_index + 1):
        fact *= i
        result_fact_list.append(fact)
    return result_fact_list


def factorial(n):
    """
    return the factorial if exist in global fact_list,
    else find it by calculate_fact_from function and return it.
    """
    global fact_list
    try:
        return fact_list[n]
    except IndexError:
        last_index = len(fact_list) - 1

        fact_list += (calculate_fact_from(last_index, fact_list[-1], n))
        return fact_list[-1]


if __name__ == '__main__':

    x, a, n = map(int, input().split())
    result = 0
    for k in range(n + 1):
        composition = (factorial(n) / (factorial(k) * factorial(n - k)))
        result += (composition * (x ** k) * (a ** (n - k)))

    print(f'{result:.0f}')
