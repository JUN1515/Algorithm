import sys

def solution():
    input = sys.stdin.readline
    N, S = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    l = 0
    min_length = N + 1

    for r in range(1, N + 1):
        arr[r] += arr[r - 1]        # 누적 합

        if min_length < r - l:      # 만일 현재 부분합의 길이가 최소 길이가 아닌 경우
            l = r - min_length      # 최소길이가 되게끔 l을 조정

        while arr[r] - arr[l] >= S: # l + 1 부터 r 까지의 부분합이 S보다 크다면
            min_length = r - l      # 최소 길이 저장
            l += 1                  # l을 오른쪽으로 이동

        if min_length == 1:         # 만일 중간에 최소 길이가 1인 경우가 나오면 리턴
            return 1

    if min_length == N + 1:         # 최소 길이가 변하지 않았던 경우
        return 0                    # 불가능한 경우이기에 0을 리턴
    else:
        return min_length


print(solution())