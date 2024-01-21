import sys
from heapq import *

input = sys.stdin.readline
N = int(input())

heap = list(map(int, input().split()))
heapify(heap)

for _ in range(N-1):
    lst = map(int, input().split())
    for elm in lst:
        heappush(heap, elm)
        heappop(heap)
print(heappop(heap))