import sys
from heapq import *

input = sys.stdin.readline

n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapify(heap)

for i in range(m):
    x = heappop(heap)
    y = heappop(heap)
    z = x + y
    heappush(heap, z)
    heappush(heap, z)
print(sum(heap))