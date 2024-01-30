import sys
sys.setrecursionlimit(1000000)

def find_parent(x):
    global parent
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 부모 테이블에서, 부모를 자기 자신으로 초기화

for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 1:  # 합집합 확인 연산
        print("YES") if find_parent(a) == find_parent(b) else print("NO")

    else:       # 합집합 연산
        union_parent(a, b)