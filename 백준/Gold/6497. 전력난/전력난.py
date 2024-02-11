import sys
input = sys.stdin.readline

def solution(m: int, n: int):     # m: 정점의 수, n: 간선의 수

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

    # 부모 테이블 생성
    parent = [-1] * m

    # 간선정보를 배열에 저장하고 오름차순으로 정렬
    edges = [list(map(int, input().split())) for _ in range(n)]
    edges.sort(key=lambda x: x[2])

    total_cost = 0      # 모든 길의 거리 비용
    minimum_cost = 0    # 최소 거리 비용

    # 간선정보를 담은 배열을 순회
    for edge in edges:
        n1, n2, weight = edge
        total_cost += weight

        x1, y1 = find_parent(n1), find_parent(n2)
        if x1 != y1:
            union_parent(x1, y1)
            minimum_cost += weight

    print(total_cost - minimum_cost)


while True:
    M, N = map(int, input().split())    # M: 정점의 수, N: 간선의 수
    if M == N == 0:
        break
    solution(M, N)