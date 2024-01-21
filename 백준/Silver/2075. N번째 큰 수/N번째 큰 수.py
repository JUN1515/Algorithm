import sys
from heapq import *

input = sys.stdin.readline
N = int(input())

heap = list(map(int, input().split()))
heapify(heap)

for _ in range(N-1):
    for num in map(int, input().split()):
        if heap[0] < num:
            heapreplace(heap, num)
print(heappop(heap))