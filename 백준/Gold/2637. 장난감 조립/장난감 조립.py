import sys
from collections import deque

input = sys.stdin.readline
N = int(input())    # 완제품 번호
M = int(input())

indegree = [0] * (N + 1)

graph = [{} for _ in range(N + 1)]
for _ in range(M):
    # 중간 부품이나 완제품 X를 만드는데 중간 부품 혹은 기본 부품 Y가 K개 필요하다"는 뜻, Y --(K)--> X
    X, Y, K = map(int, input().split())
    if Y in graph[X]:           # 완제품의 진입노드가 0이 되도록 하기 위함.
        if graph[X][Y] < K:
            continue
    else:
        indegree[Y] += 1
    graph[X][Y] = K

Q = deque([N])
result = [0] * (N + 1)
result[N] = 1

for _ in range(N):
    v = Q.popleft()

    if not graph[v]: continue   # 기본부품인 경우 넘어가기

    for w in graph[v]:
        result[w] += graph[v][w] * result[v]    # v를 n개 만들기 위해서는 w가 n * k 개 필요함
        indegree[w] -= 1
        if indegree[w] == 0:
            Q.append(w)

    result[v] = 0   # v의 기본 또는 중간부품이 몇갠지 저장했으면, v의 개수는 0으로 초기화

for i in range(1, N):
    if result[i]:
        print(i, result[i])