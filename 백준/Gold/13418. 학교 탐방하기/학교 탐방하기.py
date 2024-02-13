import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    if parent[x] > parent[y]:
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


def mst(arr1, arr2, parent):
    temp = arr1 + arr2
    result = 0
    for edge in temp:
        n1, n2, weight = edge
        x, y = find_parent(parent, n1), find_parent(parent, n2)
        if x != y:
            union_parent(parent, x, y)
            result += weight

    return result ** 2


def solution():
    N, M = map(int, input().split())    # 건물 N개 (1 ~ N, 입구 미포함)
    max_parent = [-1] * (N + 1)
    min_parent = [-1] * (N + 1)

    # A, B 건물 사이 길 C(오르막길: 0, 내릭막길: 1)
    uphills = []
    downhills = []
    for _ in range(M + 1):
        A, B, C = map(int, input().split())
        if C:   # 내리막길인 경우
            downhills.append((A, B, 0))
        else:   # 오르막길인 경우
            uphills.append((A, B, 1))

    max_val = mst(uphills, downhills, max_parent)
    min_val = mst(downhills, uphills, min_parent)
    print(max_val - min_val)


solution()