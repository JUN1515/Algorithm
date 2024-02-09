import sys
input = sys.stdin.readline

def solution():
    A = input().strip()
    B = input().strip()

    a_length = len(A)
    b_length = len(B)

    dp = [""] * max(a_length, b_length)

    for a in A:
        current_length, current_str = 0, ""

        for i, b in enumerate(B):
            if current_length < (length := len(dp[i])):
                current_length = length
                current_str = dp[i]

            elif a == b:
                dp[i] = current_str + b

    answer = ""
    for s in dp:
        if len(answer) < len(s):
            answer = s

    print(len(answer))
    if answer:
        print(answer)


solution()