import sys
input = sys.stdin.readline

def solution():
    N = int(input().strip())
    arr = [input().strip() for _ in range(N)]
    arr.sort(reverse=True)
    answer = N
    for i in range(1, N):
        for j in range(i - 1, -1, -1):
            if arr[i][0] != arr[j][0]:
                break

            if len(arr[i]) > len(arr[j]):
                break

            if arr[i] == arr[j][:len(arr[i])]:
                answer -= 1
                break
    print(answer)


solution()