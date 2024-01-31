import sys
input = sys.stdin.readline

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


for tc in range(1, int(input()) + 1):
    n = int(input())    # 유저의 수
    parent = [-1] * n

    k = int(input())    # 친구 관계의 수
    for _ in range(k):
        a, b = map(int, input().split())
        x, y = find_parent(a), find_parent(b)
        if x != y:
            union_parent(x, y)

    ans = f'Scenario {tc}:\n'
    m = int(input())
    result = [0] * m
    for _ in range(m):
        u, v = map(int, input().split())
        x, y = find_parent(u), find_parent(v)
        ans += "1\n" if x == y else "0\n"
    print(ans)