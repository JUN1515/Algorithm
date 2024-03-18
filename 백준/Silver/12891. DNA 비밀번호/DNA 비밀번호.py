import sys
input = sys.stdin.readline

def check_func(arr):
    for i in range(4):
        if arr[i] > 0:
            return 0
    return 1

def solution():

    dic = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    S, P = map(int, input().strip().split())
    dna = input().strip()

    arr = list(map(int, input().strip().split()))

    for i in range(P):
        arr[dic[dna[i]]] -= 1
    answer = check_func(arr)

    for i in range(1, S - P + 1):
        arr[dic[dna[i + P - 1]]] -= 1
        arr[dic[dna[i - 1]]] += 1
        answer += check_func(arr)
    print(answer)


solution()