def solution():
    N = input().strip()
    answer = ""
    for i in range(0, len(N), 10):
        answer += N[i:i+10] + "\n"
    print(answer, end="")

solution()