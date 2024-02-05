import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

l, r = 0, N - 1
left, right = arr[l], arr[r]
min_val = left + right
while l != r:
    val = arr[l] + arr[r]

    if abs(min_val) > abs(val):
        left, right = arr[l], arr[r]
        min_val = val

    if val < 0:     # 두 용액의 합이 음수이면,
        l += 1      # l을 오른쪽으로 이동 (음의 값이 줄어듬)

    else:           # 두 용액의 합이 양수이면,
        r -= 1      # r을 왼쪽으로 이동 (양의 값이 줄어듬)
print(left, right)