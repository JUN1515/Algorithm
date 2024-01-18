import sys
from heapq import *
input = sys.stdin.readline

# 연산의 개수
N = int(input())

heap = []
heapify(heap)

for _ in range(N):
    num = int(input())
    if num == 0:
        print(-heappop(heap)) if heap else print(0)
    else:
        heappush(heap, -num)