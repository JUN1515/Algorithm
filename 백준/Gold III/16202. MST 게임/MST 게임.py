import sys
input = sys.stdin.readline

def solution():

    def find_parent(x, parent):
        if parent[x] < 0:
            return x
        parent[x] = find_parent(parent[x], parent)
        return parent[x]

    def union_parent(x, y, parent):
        if parent[x] > parent[y]:
            parent[x] = y
        else:
            if parent[x] == parent[y]:
                parent[x] -= 1
            parent[y] = x

    def mst(arr):
        parent = [-1] * (N + 1)

        total = 0
        cnt = 0
        for lst in arr:
            a, b, w = lst
            x, y = find_parent(a, parent), find_parent(b, parent)
            if x != y:
                union_parent(x, y, parent)
                total += w
                cnt += 1
        if cnt == N - 1:
            return total
        else:
            return 0


    N, M, K = map(int, input().split())

    edges = []
    for w in range(1, M + 1):
        a, b = map(int, input().split())
        edges.append((a, b, w))

    result = [0] * K
    for i in range(K):
        val = mst(edges[i:])
        result[i] = val
        if val == 0:
            break
    print(*result)


solution()
