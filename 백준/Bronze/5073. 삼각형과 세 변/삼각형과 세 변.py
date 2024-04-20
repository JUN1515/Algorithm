import sys
input = sys.stdin.readline

def solution():
    while True:
        answer = "Invalid"

        A, B, C = map(int, input().strip().split())

        total = A + B + C
        if total == 0:
            break
        max_val = max(A, B, C)

        if max_val < total - max_val:
            if A == B == C:
                answer = "Equilateral"
            elif A == B or A == C or B == C:
                answer = "Isosceles"
            else:
                answer = "Scalene"
        print(answer)


solution()