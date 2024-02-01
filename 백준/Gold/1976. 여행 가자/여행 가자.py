import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_find(x, y):
    if parent[x] > parent[y]:
        parent[x] = y
    else:
        if parent[x] == parent[y]:
            parent[x] -= 1
        parent[y] = x


N = int(input())    # 도시의 수
parent = [-1] * (N + 1)

M = int(input())    # 여행 계획에 속한 도시들
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i + 1, N):
        if arr[i][j] == 0: continue

        x, y = find_parent(i + 1), find_parent(j + 1)
        if x != y:
            union_find(x, y)

plan = list(set(map(int, input().split())))
r_node = find_parent(plan[0])

ans = "YES"
for node in plan:
    if r_node != find_parent(node):
        ans = "NO"
        break
print(ans)