def solution():
    check = False
    S = input().strip()
    N = len(S)
    arr = [0] * 26  # arr[0]: A, arr[25]: Z
    answer = [""] * (N + 1)

    for i in range(N):
        arr[ord(S[i]) - 65] += 1

    even = 0
    odd = [0, -1]
    for i in range(26):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd[0] += 1
            odd[1] = i

    if N % 2 and odd[0] == 1:
        check = True
    else:
        if odd[0] == 0:
            check = True

    if check:
        if odd[0] == 1:
            answer[N//2 + 1] = chr(odd[1] + 65)
            arr[odd[1]] -= 1

        top = 1
        for i in range(26):
            if arr[i] != 0:
                while arr[i] != 0:
                    answer[top] = chr(i + 65)
                    answer[-top] = chr(i + 65)
                    arr[i] -= 2
                    top += 1
        print("".join(answer))

    else:
        print("I'm Sorry Hansoo")


solution()