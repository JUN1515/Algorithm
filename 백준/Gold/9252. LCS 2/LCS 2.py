import sys
input = sys.stdin.readline

def solution():
    A = "A" + input().strip()
    B = "A" + input().strip()

    c_cnt = len(A)
    r_cnt = len(B)

    LCS = [[""] * c_cnt for _ in range(r_cnt)]

    for r in range(1, r_cnt):
        for c in range(1, c_cnt):
            if A[c] == B[r]:
                LCS[r][c] = LCS[r - 1][c - 1] + A[c]
            else:
                if len(LCS[r - 1][c]) >= len(LCS[r][c - 1]):
                    LCS[r][c] = LCS[r - 1][c]
                else:
                    LCS[r][c] = LCS[r][c - 1]

    answer = LCS[r_cnt - 1][c_cnt - 1]
    print(len(answer))
    print(answer)


solution()