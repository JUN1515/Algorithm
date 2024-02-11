import sys
input = sys.stdin.readline

def solution():

    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union_parent(x, y):
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

    N = int(input())                    # 정점: 1 ~ N
    parent = [i for i in range(N + 1)]  # 부모 테이블 생성

    # mat[i][j] 는 i와 j 사이의 플로우 관리 비용이다.
    mat = [list(map(int, input().split())) for _ in range(N)]

    # 간선 정보 저장
    edges = []
    for i in range(N):
        for j in range(i + 1, N + 1):
            edges.append((i, j, mat[i - 1][j - 1])) # 행성 1와 j사이 설치 비용 mat[i][j]

    # 간선을 가중치 순으로 정렬 (오름차순)
    edges.sort(key=lambda x: x[2])

    # 최소 비용
    total = 0

    # 간선을 하나씩 확인
    for edge in edges:
        p1, p2, cost = edge

        x1 = find_parent(p1)
        y1 = find_parent(p2)
        # 사이클이 발생하지 않는 경우 (두 노드의 부모가 동일하지 않는 경우)에만 집합에 포함
        if x1 != y1:
            union_parent(x1, y1)
            total += cost

    print(total)


solution()