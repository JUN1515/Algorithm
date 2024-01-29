import sys
from collections import deque

def topology_sort():
    n = int(input())                                    # 팀의 수
    indegree = [0] * (n + 1)                            # 진입 차수
    last_year = [0] + list(map(int, input().split()))   # 작년 등수

    # 순위가 행 > 열 인 경우(행 -> 열), True
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            graph[last_year[i]][last_year[j]] = True
            indegree[last_year[j]] += 1

    m = int(input())        # 상대적인 등수가 바뀐 쌍의 수
    for _ in range(m):
        a, b = map(int, input().split())    # a의 순위 > b의 순위
        if graph[a][b]:
            graph[a][b] = False
            indegree[b] -= 1

            graph[b][a] = True
            indegree[a] += 1
        else:
            graph[a][b] = True
            indegree[b] += 1

            graph[b][a] = False
            indegree[a] -= 1

    Q = deque()     # 큐 정의
    rank = []       # 올해 순위 결과

    for i in range(1, n + 1):   # 진입 차수가 0 인 노드 찾기
        if indegree[i] == 0:
            Q.append(i)

    for _ in range(n):
        # 큐가 비어있다면 사이클이 발생했다는 의미 = 데이터에 일관성이 없어서 순위를 정할 수 없는 경우에 해당
        if not Q:
            return "IMPOSSIBLE"

        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러개라는 의미 = 확실한 순위를 찾을 수 없는 경우에 해당
        if len(Q) >= 2:
            return "?"

        v = Q.popleft()
        rank.append(str(v))

        for w in range(1, n + 1):
            if graph[v][w]:
                indegree[w] -= 1

                if indegree[w] == 0:
                    Q.append(w)

    return " ".join(rank)

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    answer = topology_sort()
    print(answer)