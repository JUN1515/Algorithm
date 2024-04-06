import sys
from heapq import *
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    heap = list(map(int, input().strip().split()))
    heapify(heap)

    answer = 0
    f1 = heappop(heap)
    while heap:
        f2 = heappop(heap)
        temp = f1 + f2
        answer += temp

        f1 = heappushpop(heap, temp)
    print(answer)


T = int(input().strip())
for _ in range(T):
    solution()