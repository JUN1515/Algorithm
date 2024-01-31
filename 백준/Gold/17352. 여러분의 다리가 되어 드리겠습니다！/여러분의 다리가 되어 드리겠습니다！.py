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


N = int(input())
parent = [-1] * (N + 1)

for _ in range(N - 2):
    a, b = map(int, input().split())
    x, y = find_parent(a), find_parent(b)
    union_parent(x, y)

ans = []
for i in range(1, N + 1):
    if parent[i] < 0:
        ans.append(i)
        if len(ans) == 2:
            break
print(*ans)