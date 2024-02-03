import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())    # 섬의 수, 다리의 수

    graph = [{} for _ in range(N + 1)]
    for _ in range(M):
        A, B, C = map(int, input().split()) # A - B 섬 사이 중량제한 C
        if B in graph[A]:
            if graph[A][B] < -C: continue

        graph[A][B] = -C
        graph[B][A] = -C

    # 공장 위치
    p1, p2 = map(int, input().split())

    Q = deque([p1])
    visited = [0] * (N + 1)
    visited[p1] = -int(1e10)

    while Q:
        v = Q.popleft()
        if visited[v] >= visited[p2]:   # 현재 이동중인 중량 무게가, 최종 중량 무게보다 적다면
            continue

        for w, weight in graph[v].items():
            possible_weight = max(visited[v], weight)
            if not visited[w]:                          # 방문한 적이 없는 경우
                # 이전 이동중인 중량과 현재 다리의 중량 제한과 비교하여 더 작은 것을 선택
                visited[w] = possible_weight
                Q.append(w)

            else:                                       # 방문한 적이 있는 경우
                if visited[w] > possible_weight:        # 만일 현재 이동 가능한 중량이 더 큰 경우,
                    visited[w] = possible_weight
                    Q.append(w)

    return -visited[p2]

print(solution())