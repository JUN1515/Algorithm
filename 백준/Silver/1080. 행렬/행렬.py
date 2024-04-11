import sys
input = sys.stdin.readline
def change_operator(i, j, arr):
    for r in range(i, i + 3):
        for c in range(j, j + 3):
            arr[r][c] = 0 if arr[r][c] else 1
def validation(n, m, arr):
    for r in range(n):
        for c in range(m):
            if arr[r][c]:
                return False
    return True

def solution():
    answer = 0
    N, M = map(int, input().split())
    arr1 = [list(input().strip()) for _ in range(N)]
    arr2 = [list(input().strip()) for _ in range(N)]

    diff = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr1[r][c] != arr2[r][c]:
                diff[r][c] = 1

    if N >= 3 and M >= 3:
        for r in range(N - 2):
            for c in range(M - 2):
                if diff[r][c]:
                    change_operator(r, c, diff)
                    answer += 1

    if not validation(N, M, diff):
        answer = -1
    print(answer)


solution()