import sys
input = sys.stdin.readline

N = int(input())

X = [0] * N
Y = [0] * N

for i in range(N):
    x, y = map(float, input().split())
    X[i] = x
    Y[i] = y

result = 0
for i in range(0, N - 1):
    result += (X[i] * Y[i + 1]) - (Y[i] * X[i + 1])
result += (X[N - 1] * Y[0]) - (Y[N - 1] * X[0])
result = round(abs(result) / 2, 1)
print(result)