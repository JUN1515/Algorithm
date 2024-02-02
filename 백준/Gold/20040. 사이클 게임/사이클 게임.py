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


n, m = map(int, input().split())    # 점의 개수, 진행된 차례의 수
parent = [-1] * n                   # 해당 인덱스가 음의 값을 가지면 루트 노드에 해당

ans = 0
for i in range(1, m + 1):
    a, b = map(int, input().split())

    if ans: continue                # 중간에 사이클을 완성하여도 입력은 모두 받아야하기에
    x, y = find_parent(a), find_parent(b)
    if x == y:  # cycle이 발생한 경우
        ans = i
    else:
        union_parent(x, y)
print(ans)
