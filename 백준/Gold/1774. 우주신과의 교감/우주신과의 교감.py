import sys
input = sys.stdin.readline

def solution():

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(x, y):
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

    N, M = map(int, input().split())
    parent = [i for i in range(N)]

    coord = [tuple(map(int, input().split())) for _ in range(N)]    # 정점의 좌표

    edges = []  # 간선 정보
    for i in range(N - 1):
        for j in range(i + 1, N):
            x1, y1 = coord[i]
            x2, y2 = coord[j]
            dist_square = (x1 - x2)**2 + (y1 - y2)**2
            edges.append((i, j, dist_square))

    edges.sort(key=lambda x: x[2])

    # 이미 연결된 정점에 대해 합연산 해두기
    for _ in range(M):
        a, b = map(int, input().split())
        union_parent(find_parent(a - 1), find_parent(b - 1))

    result = 0
    for edge in edges:
        a, b, weight = edge
        x, y = find_parent(a), find_parent(b)

        if x != y:  # 집합에 포함되어 있지 않으면, 길이 추가
            union_parent(x, y)
            result += weight**(1/2)

    print("{:.2f}".format(result))


solution()