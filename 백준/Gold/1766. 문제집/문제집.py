import sys
from heapq import *

input = sys.stdin.readline

# 정점의 수 입력 및 진입차수 배열 초기화
N, M = map(int, input().split())        # N: 문제의 수 (정점의 수, 1 ~ N), M: 정보의 개수 (간선의 수)
indegree = [0] * (N + 1)                # 진입차수 배열 초기화

# 방향 그래프의 간선 정보
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())    # A, B : A번 문제는 B번 문제보다 먼저 풀어야
    graph[A].append(B)
    indegree[B] += 1                    # 진입차수

# 진입 차수가 0인 정점을 모두 찾기
heap = [i for i in range(1, N + 1) if not indegree[i]]
result = []                     # 알고리즘 수행 결과를 담을 리스트

while heap:                     # heap이 빌때까지 반복문 수행
    v = heappop(heap)           # heap에서 원소 꺼내기 (가능한 쉬운 문제)
    result.append(v)            # 결과 리스트에 추가

    for w in graph[v]:
        indegree[w] -= 1        # 해당 정점과 연결된 모든 정점들의 진입 차수 빼기
        if indegree[w] == 0:
            heappush(heap, w)   # 새롭게 진입 차수가 0이 된 정점은 큐에 삽입

print(*result)