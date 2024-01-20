import sys
from heapq import *

N = int(input())

heap = []
heapify(heap)

for _ in range(N):
    d, w = map(int, input().split())
    heappush(heap, (-w, -d))

date = [0] * (N + 1)
date[0] = 1

total = 0
count = N
while heap and count:
    w, d = heappop(heap)
    index = N if -d > N else -d
    while index != 0:
        if date[index] == 0:
            date[index] = 1
            total += -w
            count -= 1
            break
        index -= 1
print(total)