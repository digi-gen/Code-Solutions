# https://quera.org/problemset/9023
from collections import defaultdict

ch1 = 'karakter e komaki_1'
ch2 = 'karakter e komaki_2'


def calculate_distance_between_karakters(from_node: str, target_node: str, graph: defaultdict[str, set[str]]):
    """
    calculate number of edges between forom_node and target_node in graph recursively
    """

    neighbors = graph[from_node]
    if target_node in neighbors:
        return 1
    else:
        for neighbor in neighbors:
            neighbor_of_neighbors: set[str] = graph[neighbor]
            neighbor_of_neighbors.remove(from_node)
            if neighbor_of_neighbors:
                # this neighbor has other neighbors except from_node so is not a leaf
                distance = calculate_distance_between_karakters(neighbor, target_node, graph)
                if distance == 0:
                    # target_node not founded through this neighbor go ahead
                    continue
                else:
                    return 1 + distance
            else:
                # this neighbor is a leaf go ahead for other neighbors
                continue

        else:
            # when the target_node is not founded through any of neighbors
            # returns 0 as distance
            return 0


if __name__ == '__main__':

    # get data from console
    n = int(input())
    graph = defaultdict(set)
    for i in range(n - 1):
        node1, node2 = input().split()
        graph[node1].add(node2)
        graph[node2].add(node1)

    ch1_node, ch2_node = input().split()

    distance = calculate_distance_between_karakters(ch1_node, ch2_node, graph)
    # print(distance)

    if distance % 2 == 0:
        print(ch1)
    else:
        print(ch2)



