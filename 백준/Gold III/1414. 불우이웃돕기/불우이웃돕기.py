import sys
input = sys.stdin.readline

def solution():

    def find_parent(x):
        if parent[x] < 0:
            return x
        parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(x, y):
        if parent[x] > parent[y]:
            parent[x] = y
        else:
            if parent[x] == parent[y]:
                parent[x] -= 1
            parent[y] = x

    dic = {'0': 0}
    for val in range(1, 27):
        dic[chr(val + 96)] = val
        dic[chr(val + 64)] = val + 26

    N = int(input())
    parent = [-1] * N

    arr = [list(input().strip()) for _ in range(N)]

    total_length = 0    # 랜선 총 길이
    edges = []
    for i in range(N):                      # i == j인 경우
        total_length += dic[arr[i][i]]

    for i in range(N - 1):                  # i != j 인 경우
        for j in range(i + 1, N):
            v1, v2 = dic[arr[i][j]], dic[arr[j][i]]
            total_length += v1 + v2
            if v1 and v2: edges.append((i, j, min(v1, v2)))
            elif v1: edges.append((i, j, v1))
            elif v2: edges.append((i, j, v2))

    edges.sort(key=lambda x: x[2])

    minimum_length = 0
    for edge in edges:
        i, j, length = edge

        x, y = find_parent(i), find_parent(j)
        if x != y:
            union_parent(x, y)
            minimum_length += length

    cnt = 0
    for i in parent:
        if i < 0:
            cnt += 1
            if cnt > 1:
                return -1
    return total_length - minimum_length


print(solution())