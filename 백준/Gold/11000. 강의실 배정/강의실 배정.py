import sys
input = sys.stdin.readline

N = int(input())

start, end = [], []

for _ in range(N):
    s, t = map(int, input().split())
    start.append(s)
    end.append(t)

start.sort()
end.sort()

rooms = N
index = 0

for s in start:
    if end[index] <= s: # 종료 시간 <= 시작 시간이라면
        index += 1
        rooms -= 1
print(rooms)