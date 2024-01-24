import sys
from collections import deque

input = sys.stdin.readline

# 과목 수, 선수 조건의 수
N, M = map(int, input().split())
indegree = [0] * (N + 1)

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  # A -> B
    indegree[B] += 1    # 진입차수


Q = deque()             # 큐 정의
answer = [0] * (N + 1)  # 결과 저장 배열

for i in range(1, N + 1):
    if indegree[i] == 0:
        Q.append(i)
        answer[i] += 1         # 진입 차수가 0인것은 모두 1학기에 가능

while Q:    # Q가 빌 때까지
    v = Q.popleft()

    for w in graph[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            Q.append(w)
            answer[w] = answer[v] + 1

print(*answer[1:])