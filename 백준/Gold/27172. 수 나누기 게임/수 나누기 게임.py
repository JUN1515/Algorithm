import sys

def solution():
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    max_num = max(arr) + 1

    has_card = [False] * max_num
    numbers = [0] * max_num

    for i in arr:
        has_card[i] = True

    for i in arr:
        for j in range(2 * i, max_num, i):      # j % i == 0 -> j는 승리
            if has_card[j]:
                numbers[j] -= 1
                numbers[i] += 1

    result = [0] * n
    for i in range(n):
        result[i] = numbers[arr[i]]
    print(*result)


solution()