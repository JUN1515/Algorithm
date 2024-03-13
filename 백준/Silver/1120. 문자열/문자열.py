import sys
input = sys.stdin.readline

def solution():
    A, B = input().strip().split()
    diff = 51
    for i in range(0, len(B) - len(A) + 1):
        temp_diff = 0
        for j in range(len(A)):
            if B[i + j] != A[j]:
                if temp_diff == diff:
                    break
                temp_diff += 1
        diff = temp_diff
    print(diff)


solution()