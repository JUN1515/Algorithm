import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
max_val = max(arr)

numbers = [[False, 0] for i in range(max_val + 1)]
for i in arr:
    numbers[i][0] = True

for i in arr:
    for j in range(2 * i, max_val + 1, i):      # j % i == 0 -> j는 승리
        if numbers[j][0]:
            numbers[j][1] -= 1
            numbers[i][1] += 1

result = [0] * n
for i in range(n):
    result[i] = numbers[arr[i]][1]
print(*result)