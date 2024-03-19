import sys
input = sys.stdin.readline
def solution():
    N = int(input())

    dic = {}
    for _ in range(N):
        a = input().strip().split('.')[1]
        dic[a] = dic.get(a, 0) + 1

    for a in sorted(dic):
        print(a, dic[a])


solution()