# 느낌상 다익스트라 알고리즘 쓰면 될듯?
# 일단 1번 부터 시작해서 최단 경로 탐색
# 가지치고 조건으로 배달 가능 시간 이상인 부분 제외
# distance 배열에서 INF값을 가진 원소를 제외한 나머지 개수 세면 될듯

from heapq import *

def solution(N, road, K):
    answer = 0
    
    INF = 10000 * 50 + 1
    distance = [INF] * (N + 1)
    
    graph = [{} for _ in range(N + 1)]
    for a, b, c in road:
        if b in graph[a]:           # 두 마을을 연결하는 도로는 여러 개 있을 수 있음
            if graph[a][b] < c:
                continue
                
        graph[a][b] = c             # 양방향
        graph[b][a] = c
        
    heap = [(0, 1)]     # 현재 이동 거리, 노드 정보
    distance[1] = 0
    
    while heap:
        current_dist, v = heappop(heap)
        
        if distance[v] < current_dist: continue
        
        for w, dist in graph[v].items():
            next_dist = current_dist + dist
            if K < next_dist: continue
            if distance[w] > next_dist:
                distance[w] = next_dist
                heappush(heap, (next_dist, w))
    
    for i in range(1, N + 1):
        if distance[i] != INF:
            answer += 1
        
    return answer