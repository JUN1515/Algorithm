import sys
from heapq import *

input = sys.stdin.readline
N = int(input())

l_heap = [-int(input())]      # 중간 값과 같거나 작은 수, 최대힙
r_heap = []             # 중간 값보다 큰 수, 최소힙

balance = 0    # l_heap이 많으면 0, 같으면 1

print(-l_heap[0])
if N > 1:
    for i in range(N-1):
        num = int(input())
        if -l_heap[0] >= num:   # 중간 값보다 같거나 작은 숫자인 경우,

            heappush(l_heap, -num)
            if not balance:
                heappush(r_heap, -heappop(l_heap))
                balance = 1
            else:
                balance = 0
            print(-l_heap[0])

        elif -l_heap[0] < num:    # 중간 값보다 더 큰 숫자인 경우

            heappush(r_heap, num)
            if balance:
                heappush(l_heap, -heappop(r_heap))
                balance = 0
            else:
                balance = 1
            print(-l_heap[0])