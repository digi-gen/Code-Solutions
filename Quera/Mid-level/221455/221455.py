# https://quera.org/problemset/221455

n, m = map(int, input().split())

base_row_size = n - 1
size_of_neighbour_matrix = int(base_row_size * ((base_row_size + 1) / 2))
neighbour_matrix = [False] * size_of_neighbour_matrix


def give_row_flag(i: int, base=base_row_size):
    result = 0
    if i == 0:
        return result
    else:
        base_row_size_copy = base
        for x in range(i):
            result += base_row_size_copy
            base_row_size_copy -= 1
        return result


def give_position_in_neighbour_matrix(i, j):
    flag_row_i_plus = give_row_flag(i + 1)
    position_in_neighbour_matrix = flag_row_i_plus - (base_row_size - j)
    return position_in_neighbour_matrix


for i in range(m):
    a, b = map(int, input().split())
    u, v = (a, b) if (a < b) else (b, a)
    del a, b

    # make u and v zero based
    u -= 1
    v -= 2

    neighbour_matrix[give_position_in_neighbour_matrix(u, v)] = True


total_operations = 0

for j in range(base_row_size):
    upper_edges_of_vertex_i = 0
    for i in range(j + 1):
        upper_edges_of_vertex_i += 1 if neighbour_matrix[give_position_in_neighbour_matrix(i, j)] else 0

    if upper_edges_of_vertex_i == 0:
        total_operations += 1
    elif upper_edges_of_vertex_i > 1:
        total_operations += (upper_edges_of_vertex_i - 1)


print(total_operations)


