# https://quera.org/problemset/76278
def calculator(n, m, li):
    group_flag = m
    grouped_list = []
    while group_flag < n:
        grouped_list.append(sum(li[(group_flag - m): group_flag]))
        group_flag += m

    grouped_list.append(sum(li[group_flag - m:]))

    result = 0
    for i in range(len(grouped_list)):
        result += (grouped_list[i] * ((-1) ** i))

    return result

