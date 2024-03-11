def solution():
    S = input()
    N = len(S)
    answer = set()


    for i in range(N):
        for j in range(i, N):
            answer.add(S[i : j + 1])

    print(len(answer))


solution()