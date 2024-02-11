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

    N, M = map(int, input().split())
    parent = [-1] * (N + 1)

    s, e = map(int, input().split())
    parent[s] = -100001                 # 시작점 s가 무조건 루트 정점이 되게끔

    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort(key=lambda x: -x[2])     # 내림차순 정렬

    for edge in edges:
        a, b, weight = edge         # weight는 현재 지날 수 있는 다리의 무게 제한
        x1, y1 = find_parent(a), find_parent(b)

        if x1 != y1:                # 두 지점의 루트 노드가 다를 경우
            union_parent(x1, y1)    # 합집합 연산

        if find_parent(e) == s:     # 만일, 도착점의 루트노다가 시작점이라면 리턴
            return weight
    return 0


print(solution())