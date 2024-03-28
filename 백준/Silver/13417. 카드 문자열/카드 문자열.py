import sys
from collections import deque
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    arr = list(input().split())
    Q = deque([arr[0]])
    for i in range(1, N):
        if Q[0] >= arr[i]:
            Q.appendleft(arr[i])
        else:
            Q.append(arr[i])
    print("".join(Q))


T = int(input().strip())
for _ in range(T):
    solution()