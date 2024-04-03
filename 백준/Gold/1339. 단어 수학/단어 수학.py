import sys
input = sys.stdin.readline

def solution():
    dic = {}

    N = int(input().strip())
    arr = []
    for _ in range(N):
        arr.append(input().strip())

    for i in range(N):
        w = arr[i]
        w_length = len(w)
        for j in range(w_length):
            dic[w[j]] = dic.get(w[j], 0) + 10**(w_length - j - 1)

    lst = [(val, key) for key, val in dic.items()]
    lst.sort(reverse=True)

    alphaToNumber = {}
    num = 9
    for val, key in lst:
        alphaToNumber[key] = num
        num -= 1

    answer = 0
    for i in range(N):
        w = arr[i]
        w_length = len(w)
        for j in range(w_length):
            answer += alphaToNumber[w[j]] * 10**(w_length - j - 1)
    print(answer)


solution()