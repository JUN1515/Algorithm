import sys
input = sys.stdin.readline

def solution():

    def find_parent(x):
        if parent[x] < 0:
            return x
        parent[x] = find_parent(parent[x])
        return parent[x]

    def uinon_parent(x, y):
        if parent[x] > parent[y]:
            parent[x] = y
        else:
            parent[y] = x

    N, M, K = map(int, input().split())
    parent = [-1] * (N + 1)

    for i in map(int,  input().split()):
        parent[i] = -1001

    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x:x[2])

    result = 0
    for edge in edges:
        a, b, w = edge
        x, y = find_parent(a), find_parent(b)

        if parent[x] == parent[y] == -1001:
            continue

        if x != y:
            uinon_parent(x, y)
            result += w

    print(result)


solution()