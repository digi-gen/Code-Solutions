# https://quera.org/problemset/7612
from collections import deque


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def is_bipartite(n, edges, disjoint_set: UnionFind):
    graph = [[] for _ in range(n)]
    movable = [True for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n  # -1 means unvisited, 0 and 1 are two colors

    for start in range(n):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            while queue:

                node = queue.popleft()
                parent_id = disjoint_set.find(node)

                if not movable[parent_id]:
                    continue

                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        movable[parent_id] = False  # Not bipartite

    return color, movable


def main():
    n, m, q = map(int, input().split())
    edges = []
    uf = UnionFind(n)

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        uf.union(u, v)

    colors, moveable = is_bipartite(n, edges, uf)

    queries = [tuple(map(int, input().split())) for _ in range(q)]

    for a, b in queries:
        a -= 1
        b -= 1
        parent_a = uf.find(a)
        if not moveable[parent_a]:
            print("impossible")
            continue
        if parent_a != uf.find(b):
            print("independent")
        elif colors[a] == colors[b]:
            print("cw")
        else:
            print("ccw")


if __name__ == "__main__":
    main()
