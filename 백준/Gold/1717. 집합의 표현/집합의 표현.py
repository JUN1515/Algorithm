import sys

def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    if parent[x] > parent[y]:   # 최대 깊이가 더 적은 부모를 루트 부모로 하기 위함
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


input = sys.stdin.readline
n, m = map(int, input().split())
parent = [-1] * (n + 1)

for _ in range(m):
    c, a, b = map(int, input().split())
    x, y = find_parent(a), find_parent(b)
    if c == 1:  # 합집합 확인 연산
        print("YES") if x == y else print("NO")
    else:       # 합집합 연산
        if x != y:
            union_parent(x, y)