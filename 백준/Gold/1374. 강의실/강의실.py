import sys
input = sys.stdin.readline

N = int(input())

start = []
end = []

for _ in range(N):
    x, s, e = map(int, input().split())
    start.append(s)
    end.append(e)

start.sort()
end.sort()

room = N
index = 0
for s in start:
    if end[index] <= s:
        index += 1
        room -= 1
print(room)