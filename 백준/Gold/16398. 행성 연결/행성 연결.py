### ref : https://www.acmicpc.net/source/69406767

import sys
from heapq import *
input = sys.stdin.readline

def solution():
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    cost = [int(1e12) + 1] * N

    visited = [False] * N
    heap = [(0, 0)]
    cost[0] = 0

    result = 0   # 최소 비용

    while heap:
        current_cost, v = heappop(heap)
        if visited[v]: continue

        visited[v] = True
        result += current_cost

        for w in range(N):
            if visited[w]: continue
            if cost[w] > mat[v][w]:
                heappush(heap, (mat[v][w], w))
                cost[w] = mat[v][w]

    print(result)


solution()