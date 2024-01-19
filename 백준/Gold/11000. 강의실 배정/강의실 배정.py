import sys
from heapq import *
input = sys.stdin.readline

N = int(input())

heap = []
heapify(heap)

for _ in range(N):
    s, t = map(int, input().split())
    heappush(heap, (s, t))


rooms = [heappop(heap)[1]]    # rooms의 요소는 각 방의 배열을 의미
heapify(rooms)

while heap:
    s, t = heappop(heap)
    min_room = heappop(rooms)   # 방들 중 가장 빨리 끝나는 방

    if min_room > s:                # 만약, 가장 일찍 끝나는 방보다 먼저 시작한다면
        heappush(rooms, min_room)   # 기존 강의실 다시 넣고, 새로운 강의실 추가
    heappush(rooms, t)              # 아니면 기존 강의실 시간 변경
print(len(rooms))